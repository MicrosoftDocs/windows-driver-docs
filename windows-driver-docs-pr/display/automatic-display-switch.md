---
title: Automatic Display Switch (ADS)
description: Describes the Automatic Display Switch (ADS) feature.
keywords:
- WDDM , automatic display switch , GPU
- WDDM , ADS , GPU
- WDDM , mux device , GPU switching
ms.date: 02/06/2025
---

# Automatic display switch

> [!IMPORTANT]
> Some information relates to a prerelease product that might be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.

This article describes the automatic display switch (ADS) feature that provides support for a laptop's internal panel to be seamlessly switched between an integrated GPU (iGPU) and discrete GPU (dGPU). ADS is an optional WDDM feature, supported starting in Windows 11, version 24H2 update 2025.01D (WDDM 3.2).

In this article:

* GPU0 refers to the GPU that the integrated panel is currently connected to.
* GPU1 refers to the GPU that the panel is to be switched to.

## Overview

Some released laptops have a multiplexer (mux) device that allows the internal panel to be switched between the integrated GPU (iGPU) and discrete GPU (dGPU). The graphics driver currently triggers and performs the switch in these laptops without any OS knowledge, which leads to some undesired user experiences.

ADS allows the OS to control the use of a mux device in the system to switch between the iGPU and dGPU when scanning out to the internal panel. Hence, the OS can provide a better user experience.

The initial version of ADS only supports switching the internal panel between the iGPU and dGPU. In the future, this feature might be expanded to support muxing of external connectors in laptops as well.

## High level design

In general, the system has to ensure the internal panel's content is displayed without any flickers/glitch while the switch is in progress. The OS doesn't restrict this functionality to any particular display protocol. This article focuses on how to implement ADS with eDP, but there are more industry standards that can be used (for example, MIPI or DSI). A platform design is free to use another display connection protocol if they can achieve the same experience without any other OS changes.

The subsections within this section identify design aspects of the feature and detail the high level approach for each aspect.

### Control of the mux device

To reduce dependencies between the iGPU and dGPU graphics drivers, the mux is exposed as a separate device that the OS can control independent of the graphics drivers. The advantages of this approach are:

1. It reduces the complexity of the graphics driver because the driver doesn't need to know how to control every different mux that an OEM might use.
1. It reduces or eliminates dependencies between graphics drivers, which reduce driver updates and makes it easier for OEMs to select GPUs and muxes.
1. The OS can switch the mux when a graphics driver isn't available.

#### Exposing the mux device

Because this solution is for muxing between internal iGPU and dGPU, it makes sense to expose the mux via ACPI.

#### Functionality of the mux driver

The mux driver must meet the following high level functional requirements:

1. It must provide the status of the mux, which target is currently controlling the internal panel, and any capability caps.
2. It must provide a way to trigger a switch and report the status of the switch.

For more information on the mux ACPI device and its methods, see [ACPI](#mux-acpi-device).

In order to perform a seamless switch, the mux device requires the following conditions at all times during the GPU switch:

1. Panel power. At any time, the mux needs panel power to be provided by either of the GPUs. It's OK to have both GPUs provide the panel power at the same time.
1. Brightness-enabled control signals from both GPUs when switching.
1. Brightness level (pulse-width modulated) from both GPUs when switching.

The mux switches the following information between the two GPUs and the panel:

1. Brightness-enabled control signal
1. Brightness level (pulse-width modulated)
1. DisplayPort (DP) Aux line
1. Hot plug detection (HPD) line
1. DP data line

The mux must have the ability to switch when the panel isn't active. At least for internal panel switching the mux shouldn't trigger any HPD signals to the GPU when switching.

The GPU driver should never call the mux ACPI methods.

### Automatic display switch DDI

Several DDIs are added to satisfy the mux requirements. There are five different points that the OS calls a driver's DDIs during a mux switch, using the following functions. The various calls depend on the stage of the switch and whether the driver is controlling the GPU that currently has control of the display.

|       **DDI**      | **Description** |
|--------------------|-----------------|
| [**DxgkDdiDisplayMuxPreSwitchAway**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_displaymux_pre_switch_away)  | Call to the driver currently connected to the display. This call informs the driver that the system is planning to switch away the display to another GPU (from GPU0 to GPU1). |
| [**DxgkDdiDisplayMuxPreSwitchAwayGetPrivateData**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_displaymux_pre_switch_away_get_private_data) | Call to collect any private switch data from the driver currently connected to the panel (from GPU0). |
| [**DxgkDdiDisplayMuxPreSwitchTo**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_displaymux_pre_switch_to) | Call to the driver currently not connected to the display. This call informs the driver that the OS is planning to switch the display to this GPU (to GPU1). |
| [**DxgkDdiDisplayMuxSwitchCanceled**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_displaymux_switch_canceled) | Call to the driver to indicate the switch sequence was canceled before the switch was completed. |
| [**DxgkDdiDisplayMuxPostSwitchAway**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_displaymux_post_switch_away)  | The mux switch is complete and GPU0's driver is no longer connected to the display. |
| [**DxgkDdiDisplayMuxPostSwitchToPhase1**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_displaymux_post_switch_to_phase1) | The mux switch is complete and GPU1's driver is now connected to the display. This driver should now perform phase 1 tasks. |
| [**DxgkDdiDisplayMuxPostSwitchToPhase2**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_displaymux_post_switch_to_phase2) | The mux switch is complete and the GPU1's driver is now connected to the display. This driver should now perform phase 2 tasks. |
| [**DxgkDdiDisplayMuxUpdateState**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_displaymux_update_state) | Called at adapter start and return to the D0 power state to let the driver know the current mux state. |

There are explicit actions the driver needs to complete at each stage. These actions are described later in this article.

For a complete list of ADS-related DDI updates, see [WDDM DDI changes for automatic display switching](#wddm-ddi-changes-for-automatic-display-switching).

### Sharing data between GPU0 and GPU1

There might be cases where a better user experience can be built when:

* GPU0 and GPU1 are from the same IHV.
* GPU0 can pass information to GPU1 regarding the display configuration that is opaque to the OS.

A data blob is described by a GUID that GPU1's driver can quickly identify if it understands the data blob. At a high level, the OS calls GPU0 to obtain the blob GUID and data before the switch and passes it to GPU1 before it's asked to HPD in the display.

GPU1's driver is responsible for:

* Checking that it understands the GUID of the blob.
* Validating each element of data in the blob to avoid any harmful effects from malformed data in the blob.

### Driver interoperability

If a WDDM driver supports ADS, it needs to support ADS no matter which OEM system it's running on or what the other GPU on the system is.

### The switch sequence

Although it might be technically possible to switch away from a GPU when that GPU's driver is stopped, this scenario isn't currently supported. Therefore, the switch is only performed when both GPUs have drivers loaded that support the switching DDI.

The following sequence is a high level view of the whole switch sequence when the panel is active, where GPU0 and GPU1 represent the iGPU and dGPU, respectively. GPU0 is currently connected to the internal panel via the mux and we want to switch to GPU1 scanning out to the panel.

1. A switch call is made at the API level.
1. The OS collects attributes of the current internal panel state (HDR, mode, refresh rate, and so forth) and checks for temporary display mode.
1. The OS disables performing any display topology due to HPDs from any GPU in the system.
1. The OS calls GPU1 driver's [**DxgkDdiDisplayMuxPreSwitchTo**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_displaymux_pre_switch_to), passing the current brightness level. The driver should do the following only if the lid is open:
    * Turn on power to the panel.
    * Set the brightness enabled signal.
    * Set the brightness level that the OS passed.
1. The OS disables calling [**DxgkDdiQueryConnectionChange**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_queryconnectionchange) on GPU0 to ensure that lid HPD away can't be processed until after the mux switch.
1. The OS calls GPU0 driver's [**DxgkDdiDisplayMuxPreSwitchAway**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_displaymux_pre_switch_away) DDI. The driver should:
    * If the lid is active, enable PSR1 (panel self refresh 1) on the panel and ensure it isn't disabled until the OS requests disablement later in the sequence.
    * Add a packet to its connection change list with [**DXGK_CONNECTION_CHANGE**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_connection_change)'s **ConnectionStatus** set to **MonitorStatusDisconnected** and **MonitorConnect.MonitorConnectFlags.DisplayMuxConnectionChange** set to 1.
    * GPU0 can't add any connection change packets for the lid target into its queue. The OS bug checks if it does so.
    * Return the size of any private ADS data blob (GUID and data) to the OS.
   If the GPU0 driver fails this call, it needs to ensure any ADS connection status packets it placed into the queue are removed before returning.
1. If GPU0's driver returned a nonzero private data size, the OS allocates that size and passes it to GPU0's [**DxgkDdiDisplayMuxPreSwitchAwayGetPrivateData**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_displaymux_pre_switch_away_get_private_data) callback to get the private switch data.
1. The OS calls the mux's ACPI method to switch from GPU0 to GPU1.
1. The OS enables GPU0's [**DxgkDdiQueryConnectionChange**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_queryconnectionchange) to be called again.
1. The OS calls GPU0's **DxgkDdiQueryConnectionChanges** to process the [**MonitorStatusDisconnected**](/windows-hardware/drivers/ddi/d3dkmddi/ne-d3dkmddi-_dxgk_connection_status) connection packet with **DisplayMuxConnectionChange** set to 1.
1. The OS calls GPU0's [**DxgkddiSettimingsfromvidpn**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_settimingsfromvidpn) to inactivate the path of the display that is being switched from. GPU0's driver should:
    * Turn panel power off.
    * Disable the brightness signal.
    * Stop sending brightness level to mux.
1. The OS processes the display departure. It doesn't trigger a topology change to avoid unnecessary topology changes.
1. The OS calls GPU1's [**DxgkDdiDisplayMuxPostSwitchToPhase1**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_displaymux_post_switch_to_phase1) callback, passing any ADS private blob it obtained from GPU0. The driver should:
    * Determine if the lid is open or closed.
    * Add the packet to its connection change list with [**DXGK_CONNECTION_CHANGE**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_connection_change)'s:
      * **MonitorConnect.MonitorConnectFlags.DisplayMuxConnectionChange** bit set.
      * **ConnectionStatus** set to **MonitorStatusConnected** if the lid is open or **MonitorStatusDisconnected** if the lid is closed.
    * If lid is closed, turn off power and the brightness enabled signal to the panel.
1. If the OS hasn't yet called [**DxgkDdiQueryAdapterInfo**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_queryadapterinfo) with [**DXGKQAITYPE_INTEGRATED_DISPLAY_DESCRIPTOR2**](/windows-hardware/drivers/ddi/d3dkmddi/ne-d3dkmddi-_dxgk_queryadapterinfotype) for GPU1's internal target, it does so. As a result of this call, the OS calls [**DxgkDdiQueryDeviceDescriptor**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_query_device_descriptor) as well.
1. The OS calls GPU1's [**DxgkDdiQueryConnectionChange**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_queryconnectionchange) to process the event in its connection change list. This call results in [**DxgkDdiQueryDeviceDescriptor**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_query_device_descriptor) being called for the new monitor being HPD'ed in.
1. The OS enables display topology changes due to HPDs.
1. The OS will asynchronously process the connection packets from GPU0 and GPU1 with **DisplayMuxConnectionChange** set to 1.
1. If GPU1 queued **MonitorStatusConnected**:
    * The OS calls GPU1's DWM functions to enumerate modes.
    * [**DxgkddiSettimingsfromvidpn**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_settimingsfromvidpn) is called on GPU1 to activate the display path.
    * DWM renders and presents the frame to the display path on GPU1.
    * The OS waits for the first frame to be made visible.
1. The OS calls GPU1's [**DxgkDdiDisplayMuxPostSwitchToPhase2**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_displaymux_post_switch_to_phase2) callback, where the driver should turn off PSR1 for the display if **MonitorStatusConnected** was queued by GPU1; otherwise, it should do nothing.
1. The OS calls GPU0's [**DxgkDdiDisplayMuxPreSwitchAway**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_displaymux_pre_switch_away). While there are no expected actions from the driver, this call is useful for any driver cleanup or bookkeeping related to switching.
1. The OS collects the attributes of the current internal panel state. If the panel state differs from what was previously saved, the OS triggers telemetry.

This switch sequence is the same for iGPU->dGPU and dGPU->iGPU. There might be cases to switch the mux when the panel is inactive. In that case, this sequence isn't needed and the OS can just call ACPI methods on the mux to switch.

Most of the OS doesn't know the driver is in PSR mode. As a result, the driver still needs to generate Vsync syncs, report flips as completed, and so forth, even though the user doesn't see these happenings.

#### Recovery process

If a failure happens during any stage of the switch sequence, the following cleanup is performed:

1. The OS calls GPU0's [**DxgkDdiDisplayMuxSwitchCanceled**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_displaymux_switch_canceled) if GPU0's [**DxgkDdiDisplayMuxPreSwitchAway**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_displaymux_pre_switch_away) was successfully called but its[**DxgkDdiDisplayMuxPostSwitchAway**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_displaymux_post_switch_away) hasn't been called.
1. The OS calls GPU1's **DxgkDdiDisplayMuxSwitchCanceled** if GPU1's [**DxgkDdiDisplayMuxPreSwitchTo**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_displaymux_pre_switch_to) was successfully called but its [**DxgkDdiDisplayMuxPostSwitchToPhase2**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_displaymux_post_switch_to_phase2) hasn't been called.
1. The OS re-enables display topology changes if they're disabled.
1. The OS re-enables calling [**DxgkDdiQueryConnectionChange**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_queryconnectionchange) on GPU0 if disabled.
1. The OS polls for lid connectivity on the GPU that the lid is connected to.
1. The OS triggers a set display configuration (SDC) Reset. The driver that has the panel connected to it through the mux (returned from **DxgkDdiDisplayMuxSwitchCanceled**) needs to ensure that PSR is disabled.

#### Unusual events that can happen during the switch

* User external plugs or unplugs a monitor

  As part of the switch sequence, we disable the OS's processing of HPD events. In this way, any HPD is queued up and processed along with the lid arrive in one atomic operation.

* Another app calls SDC during the switch

  While the switch is in progress, calls to SDC are blocked and will be executed after the switch is processed.

* Driver gets disabled during switch  

  When a driver is stopped, the calls in the switch sequence fail and the recovery sequence is activated. The [PnPStop section](#pnp-stopping-the-adapter-that-is-scanning-out-to-a-target) also details how it ensures the screen is always visible.

#### Lid close scenarios

The driver generally could use any of the following approaches to detect lid open/close events:

* Track lid state from [**DxgkDdiNotifyAcpiEvent**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_notify_acpi_event)([**DxgkPowerStateEvent**](/windows-hardware/drivers/ddi/dispmprt/ne-dispmprt-_dxgk_event_type), PO_CB_LID_SWITCH_STATE)
* Track lid state from the [**PoRegisterPowerSettingCallback**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-poregisterpowersettingcallback)(GUID_LIDSWITCH_STATE_CHANGE) callback.
* A different, platform-dependent way.

However, for WDDM in general, drivers have to use the **DxgkDdiNotifyAcpiEvent** approach because it allows *Dxgkrnl* state and driver state to be in sync. Given that both iGPU and dGPU can be GPU1 in a switch sequence, it makes sense for all ADS drivers to track the lid state even when lid is switched away from it.

Once the OS processes the **DisplayMuxConnectionChange** event from GPU0, it considers that GPU0 doesn't own the lid state anymore and therefore GPU0 can't report any more connection status packets for that target until the lid is switched back. If GPU0 does so, the OS will bug check. Once the OS processes the [**DisplayMuxConnectionChange**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_connection_change) from GPU1, it considers GPU1 to be the owner of the lid state. Any lid open or close events can be ignored between those two events as GPU1 is expected to know the lid state and report the correct **DisplayMuxConnectionChange** packet.

#### When the OS considers that the driver owns the panel

The following table describes the sequence stages at which the OS considers a GPU to own the panel. The owning GPU can report connective changes using the switch sequence. The step numbers are from the previously described switch sequence.

| **Stage from** | **Stage to** | **Which GPU controls the panel** |
|----------------|--------------|----------------------------------|
| Before switch  | Step 5       | GPU0                             |
| Step 6         | Step 12      | No GPU                           |
| Step 13        | After switch | GPU1                             |

The OS bug checks if it sees a connection change packet in the driver's queue for a mux'ed target when the GPU doesn't control the panel.

### Controlling panel self refresh (PSR)

The ADS feature uses PSR to avoid glitches during the transition. Specifically, PSR1 (full screen update mode) is used so that GPU0 and GPU1 don't need to negotiate which PSR mode to use.

Even within PSR1, there are optional features that panel needs to support:

| **Sink capability** | **Details** | **Sink exposed via** |
|---------------------|-------------|----------------------|
| DPCD & eDP version | Expose eDP v1.3 or greater. | DPCD |
| PSR Capability and Version | Sink shall support version 1. | DPCD 00070h bit 7:0 |
| Support VSC SDP to convey PSR state | For PSR only; sink shall support at least revision 2 with up to 8 valid bytes to convey PSR state and CRC value. | DPCD 170 |
| Sink shall properly report PSR related state | Sink shall expose state; for example, link CRC error, RFB storage error, sink device self refresh status, max resync frame count, last actual sync latency in sink, and last received PSR SDP. | DPCD 2008h, 2009h, 200Ah shall reflect correct state of the sink. |

When GPU1 performs link training as part of a [**DxgkddiSettimingsfromvidpn**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_settimingsfromvidpn) call from the OS, the driver doesn't know the DP lane and bandwidth setting used by GPU0 so has to perform a full link training sequence rather than fast link training. The OS isn't going to negotiate any PSR policies between the GPUs, so the panel needs to support all the PSR versions and features that the GPUs will use. For example, the panel has to support a scenario where GPU0 might use PSR2 with some set features, then PSR1 will be used for the switch, then GPU1 might use PSR2 with a different set of features.

#### Ensuring the panel stays in PSR during the switch

When GPU1 sets a mode on the panel, there's no guarantee that the link attributes set by GPU1 while panel is in PSR will match the PSR entry mode. For example, the refresh rate or active size might change. Today DP or other industry standards don't have a way for the panel to report that it can keep the panel in PSR while link attributes are changed. Long term, we want to work to get this capability added to the DP specification. Until that happens, for an ADS-enabled system, the OEM has to pick a TCon/panel/Mux combination that can stay in PSR while the link attributes (for example, refresh rate, active size) change between any two combinations exposed in the EDID. This approach ensures that PSR can be kept active during the switch.

In order for the ADS HLK test to verify that PSR is maintained during the switch process we would like a way for the OS to know if the PSR wasn't active after GPU1 test the mode. A challenge is that it's not defined how a panel will react if it can't support PSR across the link training.  

As part of [**DxgkDdiDisplayMuxPostSwitchToPhase2**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_displaymux_post_switch_to_phase2), the driver returns a Boolean value in **pWasPanelInPSR** to inform the OS whether it detected that the panel wasn't in PSR.

### EDID of the internal panel

For the OS to provide the expected behavior when selecting display modes and topologies with different monitors connected, both GPUs are required to report the EDID/DisplayId for the internal display. This requirement ensures that the CCD database that stores display modes and topologies will pick those same settings regardless of which GPU is controlling the internal display.

The EDID that the drivers report to the OS should be the EDID that is queried from the panel using aux command without any modification.

Currently the OS will call [**DxgkDdiQueryAdapterInfo**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_queryadapterinfo)(DXGKQAITYPE_INTEGRATED_DISPLAY_DESCRIPTOR2) when starting a driver that reports an internal panel. If the mux is switched way from that integrated target, the driver can't communicate with the panel to collect the required information. The solution is that when a driver is started and the mux is switched away from its internal target, the OS delays calling **DxgkDdiQueryAdapterInfo**(DXGKQAITYPE_INTEGRATED_DISPLAY_DESCRIPTOR2) until the mux is first switched to the internal target.

### How the OS decides if ADS feature is enabled on a system and switch is allowed

The OS performs the following list of checks to determine if ADS is available on a system. All checks have to be true for ADS to be supported.

1. There's a GPU that is marked as integrated hybrid ([**DXGK_DRIVERCAPS.HybridIntegrated**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_drivercaps)) that:
   * Its driver implements the [**DXGK_DISPLAYMUX_INTERFACE**](/windows-hardware/drivers/ddi/dispmprt/ns-dispmprt-dxgk_displaymux_interface_2) interface.
   * Checks the ADS support level returned from [**DxgkDdiDisplayMuxGetDriverSupportLevel**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_displaymux_get_driver_support_level).
   * Checks the runtime ADS status from [**DxgkDdiDisplayMuxGetRuntimeStatus**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_displaymux_get_runtime_status).
   * Driver has to support the following DDIs:
       * [**DxgkddiSettimingsfromvidpn**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_settimingsfromvidpn)
       * [**DxgkDdiSetVidPnSourceAddressWithMultiPlaneOverlay3**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_setvidpnsourceaddresswithmultiplaneoverlay3)
       * [**DxgkDdiDisplayDetectControl**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_displaydetectcontrol)
       * [**DxgkDdiQueryConnectionChange**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_queryconnectionchange)
       * [**DxgkDdiNotifyAcpiEvent**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_notify_acpi_event)
   * Exposes a target for internal monitor with [**DXGK_CHILD_CAPABILITIES.HpdAwareness**](/windows-hardware/drivers/ddi/dispmprt/ns-dispmprt-_dxgk_child_capabilities) set to **HpdAwarenessInterruptible** and [**DXGK_CHILD_DESCRIPTOR.ChildDeviceType**](/windows-hardware/drivers/ddi/dispmprt/ns-dispmprt-_dxgk_child_descriptor) set to **TypeIntegratedDisplay**.
   * Under the ACPI namespace for the internal monitor, there's a DMID method that successfully returns an ACPI name of the mux.
   * GPU ACPI device has a '_DEP' ACPI method that returns the correct mux ACPI name as a dependency.
2. There's a GPU that is marked as discrete hybrid ([**DXGK_DRIVERCAPS.HybridDiscrete**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_drivercaps)) that:
   * Its driver implements the [**DXGK_DISPLAYMUX_INTERFACE**](/windows-hardware/drivers/ddi/dispmprt/ns-dispmprt-dxgk_displaymux_interface_2) interface.
   * Checks the ADS support level returned from [**DxgkDdiDisplayMuxGetDriverSupportLevel**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_displaymux_get_driver_support_level).
   * Driver has to support the following DDIs:
       * [**DxgkddiSettimingsfromvidpn**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_settimingsfromvidpn)
       * [**DxgkDdiSetVidPnSourceAddressWithMultiPlaneOverlay3**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_setvidpnsourceaddresswithmultiplaneoverlay3)
       * [**DxgkDdiDisplayDetectControl**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_displaydetectcontrol)
       * [**DxgkDdiQueryConnectionChange**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_queryconnectionchange)
       * [**DxgkDdiNotifyAcpiEvent**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_notify_acpi_event)
   * Exposes a target for internal monitor with [**DXGK_CHILD_CAPABILITIES.HpdAwareness**](/windows-hardware/drivers/ddi/dispmprt/ns-dispmprt-_dxgk_child_capabilities) set to **HpdAwarenessInterruptible** and [**DXGK_CHILD_DESCRIPTOR.ChildDeviceType**](/windows-hardware/drivers/ddi/dispmprt/ns-dispmprt-_dxgk_child_descriptor) set to **TypeIntegratedDisplay**.
   * Under the ACPI namespace for the internal monitor, there's a DMID method that successfully returns an ACPI name of the mux.
   * GPU ACPI device has a '_DEP' ACPI method that returns the correct mux ACPI name as a dependency.
3. The mux ACPI name returned from ACPI DMID method from steps 1 and 2 match.
4. The ACPI mux device has ACPI DMQU, DMCF, and DMSL methods.
5. The mux ACPI DMQU method returned the ACPI name of the internal panel target from one of the GPUs.
6. ADS currently only supports systems with a single internal panel.
7. Either:
   1. GPU0, GPU1, and Mux ACPI all report full ADS support.
   2. GPU0, GPU1, and Mux ACPI all report either experimental or full ADS support and the EnableMDMExperimentalFeature registry key is set.

Conditions 1 and 2 imply that both adapters have to be started in order for the mux to be switched.

#### Controlling the quality of ADS feature rollout

For ADS to provide a good user experience, all of the following components have to work together flawlessly:

1. The OS display mux functionality.
2. The platform ACPI methods for mux switching.
3. The display mux switching functionality in the iGPU and dGPU drivers.

To help IHV/OEMs have nonship quality code in releases, they can expose any of the following levels of ADS support:

* No support: the driver doesn't support any ADS functionality.
* Development support: the driver supports ADS but the driver's implementation is still under development and shouldn't be used beyond this purpose.
* Experimental support: The driver supports ADS but isn't at ship quality yet. The OS won't enable ADS by default but can be configured to enable it.
* Full support: The driver supports ADS at ship quality. The OS considers that the driver supports ADS.

### Display attributes that should remain the same after a display switch

A display switch shouldn't change any of the following display attributes:

1. Desktop resolution
2. VidPn path (including VidPn source mode, target mode, scaling, and so forth)
3. DPI
4. Night light setting
5. Gamma
6. Display topology
7. HDR on/off
8. SDR white level
9. Color profile
10. OPM target type of the monitor
11. Display brightness

### Matching GPU caps for seamless switch experience

To give the user a seamless switching experience, the display should be configured the same after the switch as it was before the switch. There are certain GPU features that both GPUs need the same support to achieve this behavior. For example, if one GPU supports HDR and the other doesn't, then a switch while HDR is enabled on one GPU wouldn't be seamless.

The following table lists GPU display functionality and features, and describes the alignment requirements between the two GPUs.

|  **Feature**          | **GPUs required to have seamless support** |
| --------------------- | ------------------------------------------ |
| HDR                   | If the panel supports HDR, then both GPUs either have to support fp16 HDR or not support HDR. |
| Hw cursor             | No. The OS adapts to different cursor features without visible disruption to the user. |
| MPO                   | No. The OS adapts to different MPO features without visible disruption to the user. |
| PSR                   | Both GPUs need to support this feature. |
| EDID/DisplayID        | Both GPUs have to expose the same EDID/DisplayId. |
| Brightness caps       | Both GPUs have to support the same brightness interface and brightness caps. |
| Brightness levels     | Both GPUs need to expose the same brightness levels and intervals. |
| Resolution            | Both GPUs need to support the same source modes and target resolution. |
| Refresh rates         | See *Issue if GPU1 doesn't support the refresh rate that GPU0 is running the panel at* for details. |
| Dynamic Refresh Rate  | No. The OS adapts to different virtual refresh rate support. |
| Variable Refresh Rate | See *Issue if GPU1 doesn't support the refresh rate that GPU0 is running the panel at* for details. |

#### Issue if GPU1 doesn't support the refresh rate that GPU0 is running the panel at

If GPU1 doesn't support the same mode as GPU0, then the reduced mode will likely be stored in the display topology database. Then, when the system switches back to GPU0, the reduced mode will be set. For example, if GPU0 support 120Hz but GPU1 only supports 60Hz then the following sequence could happen:

1) System is configured so GPU0 is controlling the display and the mode is 120Hz.
2) User manually switches to GPU1.
3) Display topology database has 120Hz stored for the display but GPU1 doesn't support it so OS picks 60Hz.
4) 60Hz is set and stored in the display topology database.
5) User manually switches back to GPU0.
6) Display topology database reads 60Hz from the database.

To provide the best experience, an OEM should select an iGPU and dGPU that both support the maximum refresh rate of the internal panel. If that's not possible and one GPU can't support the panel's max refresh rate, then the GPU that does support the panel's refresh rate must support the Windows Dynamic Refresh Rate (DRR) feature with ranges that include:

* The highest refresh rate of the other GPU.
* The highest refresh rate of the internal panel.

For example, if the panel can support 300Hz and iGPU can only support 60Hz then the dGPU has to support VRR with a range of at least 60Hz to 300Hz.

To summarize, the ADS requirement for refresh rate is either:

1. iGPU and dGPU support the maximum refresh rate of the internal panel.
2. The GPU that supports the maximum refresh rate of the internal panel has to support DRR with a range from highest refresh rate the other GPU can support to the maximum refresh rate of the internal panel.

### HDR and Dolby Vision

The OS sets the same HDR/Dolby vision state on the internal panel on GPU1 after the switch as was set on internal panel on GPU0 before the switch. The user shouldn't notice any changes.

### Nightlight

Nightlight is implemented via WDDM gamma or color matrix DDIs. In both of these cases, the OS sets the same nightlight levels through GPU1 after the switch as it did with GPU0 before the switch.

### Color profile

The OS applies the same color profile to the panel after the switch as was applied before the switch.

### Displaying bug check screen

Currently the OS supports displaying the bug check screen on non-POST devices. When a bug check occurs the OS:

* Doesn't switch the mux.
* Uses the current OS support for displaying the bug check screen.

When evaluating potential targets to display the bug check on, the OS skips any targets connected to a mux that is switched to a different target.

There's a small period of time when the HPD away from GPU0 was processed but the HPD in from GPU1 isn't yet fully processed. If a bug check occurs during this period, the user won't see the bug check. If a bug check occurs in the small period of time when PSR is still enabled, the driver controlling the display should ensure the panel isn't in PSR mode when the OS calls [**DxgkDdiSystemDisplayEnable**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_system_display_enable).

### Content Adaptive brightness algorithm

In an ideal world, the content adaptive algorithm used by both GPUs should produce the same effect. However, the same effect likely won't be the case and the user might notice a difference when the internal panel is switched.

### Brightness data

To ensure the user doesn't notice a brightness change due to the switch, all the brightness attributes exposed by GPU0 and GPU1 need to be identical. This requirement ensures that any brightness level before the switch on GPU0 will be supported on GPU1 after the switch.

To do so, the drivers for GPU0 and GPU1 have to:

1. Use the same brightness interface, either [**DXGK_BRIGHTNESS_INTERFACE_2**](/windows-hardware/drivers/ddi/dispmprt/ns-dispmprt-dxgk_brightness_interface_2) or [**DXGK_BRIGHTNESS_INTERFACE_3**](/windows-hardware/drivers/ddi/dispmprt/ns-dispmprt-dxgk_brightness_interface_3), where version 3 is highly recommended.
2. For brightness v3 interface, both drivers have to expose either nits-based or uncalibrated brightness.
3. For brightness v2 interface, both drivers have to return exactly the same possible brightness levels from **GetPossibleBrightness**.
4. For brightness v3 interface, both drivers have to return the exact same ranges; that is, each driver should return identical [**DXGK_BRIGHTNESS_GET_NIT_RANGES_OUT**](/windows-hardware/drivers/ddi/d3dkmdt/ns-d3dkmdt-_dxgk_brightness_get_nit_ranges_out) structures from **GetNitRanges**.
5. The internal tables the driver uses to convert OS supplied brightness levels to panel-specific settings must be the same.

In most laptops, the GPU driver gets some or all of this brightness level data from the platform in a nonstandard way. We expect this platform-to-GPU data exchange might have to be expanded to achieve these requirements.

Although the brightness interface is queried at adapter start time, the OS won't call any of the brightness interface's DDIs until the internal panel is HPD'ed. HPD occurs after the mux is switched to the GPU so the driver has access to the EDID of the internal panel at that time.

We understand that there are IHV-specific ways for the driver to set the panel brightness for panels that don't support PWM. However, this method adds complication for the TCon as it might have to support getting the brightness in a different IHV-specific way depending on which GPU is connected via the mux.

### Boot configuration of the mux

The system firmware controls which GPU is connected to the internal panel at system start time. The OS stores which GPU was last in control of the panel. Then, during the boot sequence, the OS switches the mux if necessary so the correct GPU is controlling the panel.

To preserve any boot image when a mux switch is necessary, the switch is performed only when:

* Both GPUs are powered up.
* The OS has transitioned from boot graphics controlling the output to DWM/shell controlling the output.

Thus, the switch occurs after the [**DxgkddiSettimingsfromvidpn**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_settimingsfromvidpn) call on the GPU that controls the internal panel and the user will experience a frozen screen while the panel is in PSR during the switch.

### Providing mux information to the driver

This feature is intentionally designed to have the OS call the driver to provide the information rather than providing a callback that the driver can call at any time. This method avoids the driver getting confused if it queries the OS state during a switch sequence.

The OS calls the driver's [**DxgkDdiDisplayMuxUpdateState**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_displaymux_update_state) DDI to provide the driver with the current mux state in the following cases:

1. At driver start, which allows the driver to avoid timely polling sequences when the panel isn't connected.
2. On return to D0 from D*x*. When returning from some power states (for example, hibernate), the firmware might have to reset the mux; hence the driver doesn't know the state.

These cases along with the normal DDIs involved in the switch sequence ensure that the driver can determine which way a mux is switched at any time the GPU is active.

In the first version of this feature, there are no plans to switch the mux when the internal panel isn't active, so all switches will go through the same sequence.

#### Adapter start time

When a driver starts, it needs to respond to polling requests from the OS. The driver could attempt to discover if the mux is switched to them by attempting to communicate but that could be time consuming or unreliable. As part of the GPU start sequence, the OS calls the [**DxgkDdiDisplayMuxUpdateState**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_displaymux_update_state) DDI for each target that is connected to a mux and indicates whether it's switched to that target.

When a driver starts, it needs to respond to polling requests from the OS. The driver could attempt to discover if the mux is switched to their GPU by communicating with the OS, but that could be time consuming or unreliable.

Instead, as part of the GPU start sequence, the OS calls [**DxgkDdiDisplayMuxUpdateState**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_displaymux_update_state) for each target that is connected to a mux and indicates whether the mux is switched to that target. The OS reports to the driver whether the mux is switched to the driver's GPU before it calls any polling DDIs.

The ADS driver continues to report the internal panel to the OS the same way, with the OS calling [**DxgkDdiQueryAdapterInfo**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_queryadapterinfo)(**DXGKQAITYPE_INTEGRATED_DISPLAY_DESCRIPTOR2**) to query the internal panel details. The driver needs to ensure that [**DXGK_CHILD_CAPABILITIES.HpdAwareness**](/windows-hardware/drivers/ddi/dispmprt/ns-dispmprt-_dxgk_child_capabilities) is set to **HpdAwarenessInterruptible** for any target connected to a mux.

#### D0 transition

Whenever a GPU with a connected mux is returned to powered-on state from a low power state, the OS calls [**DxgkDdiDisplayMuxUpdateState**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_displaymux_update_state) to tell the driver whether the mux is connected to its target or switched away to the other GPU.

#### Boot sequence

The following boot sequence highlights ADS-specific aspects. In this sequence, the system boots with:

* The iGPU connected to the mux.
* The user's last configuration before reboot was that the mux was connected to the dGPU.

The boot sequence is asynchronous in nature, so this sequence is for example's purpose only.

1. The system powers on and the iGPU is connected to the panel through the mux.
2. The iGPU displays the boot screen on the panel.
3. Windows loads and displays the boot animation on the internal lid.
4. Due to _DEP on both the iGPU and dGPU, the OS's mux driver is started before either GPU driver. The mux driver uses ACPI calls to ensure the mux is configured correctly. The mux driver verifies that the ACPI mux implementation meets ADS requirements.
5. *Dxgkrnl* calls [**DxgkDdiAddDevice**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_add_device) for the iGPU.
6. *Dxgkrnl* calls [**DxgkDdiQueryInterface**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_query_interface)([**DXGK_DISPLAYMUX_INTERFACE**](/windows-hardware/drivers/ddi/dispmprt/ns-dispmprt-dxgk_displaymux_interface_2)) for the iGPU. Even if the current system doesn't support ADS, the driver returns its interface if it does support ADS.
7. *Dxgkrnl* calls [**DxgkDdiDisplayMuxGetDriverSupportLevel**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_displaymux_get_driver_support_level) to get the driver's ADS support level.
8. *Dxgkrnl* calls [**DxgkDdiDisplayMuxReportPresence**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_displaymux_report_presence)(TRUE) to let the iGPU know that the system has a functioning ADS mux in it.
9. *Dxgkrnl* calls [**DxgkDdiStartDevice**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_start_device). The iGPU driver returns the number of children including the VidPn target for the internal panel.
10. *Dxgkrnl* calls [**DxgkDdiDisplayMuxGetRuntimeStatus**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_displaymux_get_runtime_status) to check whether the iGPU supports ADS and if the driver got all required information from the system.
11. *Dxgkrnl* calls [**DxgkDdiQueryChildStatus**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_query_child_status) for each child that the iGPU exposes.
12. Once *Dxgkrnl* finds the iGPU-reported child that is connected to the mux, it calls [**DxgkDdiDisplayMuxUpdateState**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_displaymux_update_state) to inform the iGPU that the mux is connected to that target.
13. Because the iGPU exposed a connected internal monitor, *Dxgkrnl* sets a mode on the iGPU using [**DxgkddiSettimingsfromvidpn**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_settimingsfromvidpn).
14. *Dxgkrnl* starts the dGPU driver, then repeats steps 5-12 for the dGPU.
15. *Dxgkrnl* detects that the iGPU, dGPU, and mux are all configured correctly, so it creates a mux pair and the PnP Device Interface properties for the mux pair.
16. *Dxgkrnl* reads the last mux configuration from the registry. Because the last configuration was dGPU, *Dxgkrnl* now starts the mux switch sequence previously described to switch the mux to the dGPU.

### Panel drivers

Monitor panel drivers are loaded based on the PnP hardware ID generated from the EDID. Given that the EDID stays the same, the panel driver is loaded when either GPU is controlling the internal panel. Both drivers will expose the same brightness functionality. Thus, loading shouldn't cause any issue and the panel driver won't need to know which GPU is in control of the mux.

### Identify the targets a mux controls

When the OS starts the driver, it calls the driver's [**DxgkDdiQueryChildRelations**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_query_child_relations) to query information about the reported children. The driver fills in the [**DXGK_CHILD_DESCRIPTOR**](/windows-hardware/drivers/ddi/dispmprt/ns-dispmprt-_dxgk_child_descriptor) structure for each child. The **AcpiUid** member is defined to be the value returned by the _ADR method under that child in the ACPI namespace, which allows the OS to find the ACPI name for that child.  

For ADS, we define an ACPI DMID method that needs to be under the child ACPI namespace for the target. This DMID method returns the ACPI name of the mux device. It allows the OS to find the mux ACPI name for the target.

### PnP stopping the adapter that is scanning out to a target

The OS won't switch the mux when the GPU that is scanning out to the internal panel is stopped. The following scenarios go through the different cases when a GPU is stopped.

1. GPU0 is the post. It's connected to the internal panel and is stopped.

   In this case, the Basic Display Driver (BDD) takes over the currently active mode on GPU0 and continues updating the screen.

2. GPU0 is the post but GPU1 is connected to the internal panel. GPU0 is stopped.

   Due to the current OS design, BDD is started on GPU0, which causes a ghost monitor to be reported and appear in the display CPL.

3. GPU1 isn't the post and is connected to the internal panel. GPU1 is stopped.

   Due to the current OS design, BDD isn't started on GPU1 and hence the user won't be able to see the panel.

4. GPU1 isn't the post. GPU0 is connected to internal panel and GPU1 is stopped.

   No switch occurs and nothing happens. GPU0 continues to display on the panel.

Scenarios 2 and 3 create a bad experience for the user. The ADS feature changes the behavior to fix these two cases.

### Plugin/external GPUs aren't supported

We don't believe there's any use case for this feature with plugin GPUs.

### ADS is limited to single internal panels only

The first version of ADS only supports single internal panels. However, the feature is engineered in a way that allows it to support muxing external and multiple internal displays (when supported by OS) in the future with minimal driver changes.

### Current POST adapter policy changes

The OS previously had some policies regarding the POST adapter. For example, the POST adapter was the only adapter that could expose internal targets. These types of restrictions are removed from the OS with the introduction of ADS.  

### Disable monitor arrival visual effects

When a monitor is connected in Windows 11, the shell/DWM have an animation sequence. This animation is disabled in display switch scenarios.

### Disable PnP bonk

When a monitor is added or removed, the PnP system plays a 'bonk' sound to notify the user. This 'bonk" is disabled in display switch scenarios.

### Application notifications

When a display switch occurs, the system goes through the regular HPD removal and HPD arrival code paths. Hence all the normal application notifications trigger as normal; for example, the PnP notification for the HPD out and the HPD in and the WM_DISPLAYCHANGE window messages.

### API to trigger switch

The plan is to have a public API so the OS and IHV control panel can trigger the switch.

### Display related APIs and Win+P behavior

Given that the internal panel is only ever connected to a single GPU, display APIs work as expected along with Win+P functionality.

### HLK test

If a GPU driver or ACPI firmware reports full ADS support, it needs to pass the ADS HLK tests on an ADS-enabled system.

### GPU HPDing internal panel when the mux is switched away from that GPU

The OS triggers a bug check when an internal panel is reported as connected from a driver when that mux is currently switched away from that driver.

### AC/DC transition

For the first version of the ADS feature, the OS won't store an AC vs DC mux setting and won't trigger a mux switch on an AC <-> DC transition.

### System power transitions

The main concern with power transitions is when the firmware resets the mux state (for example, hibernate), and on resume from power the mux isn't switched to the panel it was before the power transition.

The initial approach was to switch the mux back to the dGPU after powering on both the iGPU and dGPU. The issue with this approach is that, depending on different asynchronous events, the result might be multiple mode changes.

The updated approach to help streamline the user experience is for the system to switch the mux back to the expected target while both the iGPU and dGPU are asleep, thus avoiding multiple mode changes.

#### Power transition sequence

The following example describes a hibernate power transition on an ADS system.

1. System is configured with mux connected to the dGPU.
2. System enters hibernation.
3. Both the iGPU and dGPU are transitioned to D3 power.
4. System powers off.
5. User powers on the system.
6. Firmware configures the mux to iGPU and iGPU display boot sequence on the internal panel.
7. *Dxgkrnl* reads the last mux configuration (dGPU in this case), and compares it to the current mux position using ACPI (iGPU in this case). *Dxgkrnl* then calls ACPI to switch the mux to the dGPU.
8. *Dxgkrnl* transitions iGPU to D0, then calls iGPU's[**DxgkDdiDisplayMuxUpdateState**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_displaymux_update_state) to inform the driver that the mux isn't connected to it.
9. *Dxgkrnl* transitions the dGPU to D0, then calls dGPU's [**DxgkDdiDisplayMuxUpdateState**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_displaymux_update_state) to inform the driver that the mux is connected to it.
10. *Dxgkrnl* sets a mode on the dGPU.

### All In One systems (AIO)

Any AIO system that wants to support ADS must have the internal panel exposed as an internal target type on both GPUs.

## Mux ACPI device

The OEM is responsible for adding the mux device in the ACPI namespace and providing the required methods to operate the mux.
  
The GPU driver should never call the mux's ACPI methods because the mux device could be located anywhere in the ACPI tree. The recommendation is to locate the mux under the closest shared ancestor of both GPUs.

Current mux devices only support two inputs and we don't expect future muxes to support more than that, so the design can assume two inputs and a single output to each mux.

The mux device can never be stopped while the system is running. It's a hidden system device.

### Mux device ACPI methods

Only the driver stack for an ACPI device can call to evaluate ACPI methods on the device. Therefore, in order to call mux device methods to switch the mux, the OS needs to have a driver loaded for the mux device. For this reason, the OS now provides a display mux driver as the driver for all display switch muxes.

A mux device is required to have the following methods:

* _HID identifies the mux device by hardware ID. We've reserved 'MSFT0005' for the ACPI display mux.
* DMQU (Display Mux Query) returns the current state of the mux.
* DMCF (Display Mux Configure) configures the mux.

#### Method _HID (Hardware ID)

**Arguments:**

None

**Returns:**

An ASCII string containing the hardware ID, which is 'MSFT0005'.

#### Method DMQU (Display Mux Query)

In a future release, we expect to add additional information to query. To enable additional queries in the future, *Arg0* is used to indicated the query type. If the ```DMQU``` method doesn't understand a query type, it should fail the method as unsupported.

**Arguments:**

*Arg0*: An integer specifying the query type. The following table lists the query type values and their meanings.

| Query type value | Meaning |
| ---------------- | ------- |
| 1     | Query current switch state |
| 2     | Query the mux ADS support level |
| 3     | Query the first GPU child that the mux is connected to |
| 4     | Query the second GPU child that the mux is connected to |

**Returns:**

If the method understands the specified query type, it should return the appropriate data as outlined in the following table. If the method doesn't understand the specified query type, it should return an empty string.

| Query type value | Return data |
| ---------------- | ----------- |
| 1    | ASCII string that contains the ACPI name of the GPU child device that the mux is currently switched to. |
| 2    | Integer representing the ADS support level. See the next table for details. |
| 3    | ASCII string that contains the ACPI name of the first GPU child device that the mux connected to. |
| 4    | ASCII string that contains the ACPI name of the second GPU child device that the mux connected to. |

The following table lists the ADS support level values and their meanings when the query type is 2.

| Returned data | Meaning |
| ------------- | ------- |
| 0    | No support |
| 1    | Development support. Systems can ship with this setting without passing any of the HLK tests as ADS will be disabled by default on customer systems. |
| 2    | Experimental support. Systems can ship with this setting without passing any of the HLK tests as ADS will be disabled by default on customer systems. |
| 3    | Full support. ADS will be enabled by default on this system if it's paired with full supported graphics drivers. The system needs to pass ADS HLK tests to ship. |

#### Method DMCF (Display Mux Configure)

**Arguments:**

*Arg0*: ASCII name of the ACPI GPU child device that the mux should switch to.

**Returns:**

Integer 0 means success; nonzero indicates failure. The OEM can define the nonzero value for better diagnostics.

### GPU device ACPI methods

Before a graphics driver for a GPU is started, the system needs to know if the mux ACPI device is working and what its current state is. In order to do so, the ACPI mux device's driver must already be started. The system uses the ACPI ```_DEP``` method under each GPU's ACPI namespace to guarantee the device relationship.

If a GPU already has a ```_DEP``` method, it should add the ACPI name of the mux device to the returned dependence list. If the GPU doesn't already have a ```_DEP``` method, it should add one.

In order for the ACPI firmware to only declare a GPU's dependency on the mux if the OS supports ADS, an ACPI ```_OSI``` query is added. The ACPI firmware can use this query to check for ADS support. OS versions that support ADS will report support by returning true to the ```_OSI(“DisplayMux”)``` ACPI command.

### GPU child device ACPI methods

For each target connected to a mux, that child's ACPI device exposes an ACPI method that returns the ACPI name of the mux device that it's connected to. For details, see [*Identify the targets a mux controls*](#identify-the-targets-a-mux-controls).

#### Method DMID (Display Mux Identifier)

**Arguments:**

None

**Returns:**

ASCII string that contains the ACPI name of the ACPI mux device that this output is connected to

### Example

The following example demonstrates how a system with two GPUs (GPU0 and GPU1) and a mux is set up and managed within the ACPI framework.

* The mux device's ACPI name is 'SB.MUX1'.

* For GPU0:
  * GPU0's ACPI name is 'SB.PCI0.GFX0'.
  * It exposes VidPn target 0x40f04, which reports a [**DXGK_CHILD_DESCRIPTOR.AcpiUid**](/windows-hardware/drivers/ddi/dispmprt/ns-dispmprt-_dxgk_child_descriptor) value of 0x400.
  * The ACPI child device name corresponding to the target connected to the mux is 'SB.PCI0.GFX0.DD1F'.
  * The ACPI method _ADR under 'SB.PCI0.GFX0.DD1F' returns 0x400. This return value is how the OS knows this ACPI device corresponds to VidPn target 0x40f04.
  * The ACPI method DMID under 'SB.PCI0.GFX0.DD1F' returns 'SB.MUX1'.

* For GPU1:
  * GPU1's ACPI name is 'SB.PCI0.PEG0.PEGP'.
  * It exposes VidPn target 0x1103, which reports a **DXGK_CHILD_DESCRIPTOR.AcpiUid** value of 0x100.
  * The ACPI child device name corresponding to the target connected to the mux is 'SB.PCI0.PEG0.PEGP.EDP1'.
  * The ACPI method _ADR under 'SB.PCI0.PEG0.PEGP.EDP1' returns 0x100. This return value is how the OS knows this ACPI device corresponds to VidPn target 0x1103.
  * The ACPI method DMID under 'SB.PCI0.PEG0.PEGP.EDP1' returns 'SB.MUX1'.

* The OS knows that GPU0 target 0x40f04 and GPU1 target 0x1103 are connected to the same mux with ACPI name 'SB.MUX1'.

* If GPU1 is currently connected to the panel, the OS can switch the mux to GPU0 by calling the DMCF method on 'SB.MUX1' passing 'SB.PCI0.GFX0.DD1F'

The following ACPI machine language code is for the relevant parts of the example. Pseudocode for platform logic is surrounded by <>.

```aml

DefinitionBlock
{
    Device (MUX1) // This is _SB_.MUX1
    {
        Name (_HID, "MSFT0007")  // _HID: Hardware ID

        Method (DMQU, 1, Serialized)  // DMQU: Display Mux Query
        {
            Switch (ToInteger(Arg0))
            {
                Case (1)
                {
                    If (<Mux is in error>)
                    {
                        Return ("")
                    }
                    If (<Mux switched to GPU0>)
                    {
                        Return ("_SB_.PCI0.GFX0.DD1F")
                    }
                    Else
                    {
                        Return ("_SB_.PCI0.PEG0.PEGP.EDP1")
                    }
                }
                Case (2) 
                {
                    Return (1)  // Mux only has developmental support
                }
                Case (3)
                {
                    If (<Mux is in error>)
                    {
                        Return ("")
                    }
                    Return ("_SB_.PCI0.GFX0.DD1F")
                }
                Case (4)
                {
                    If (<Mux is in error>)
                    {
                        Return ("")
                    }
                    Return ("_SB_.PCI0.PEG0.PEGP.EDP1")
                }

            }
            // Unknown type
            Return ("")
        }

        Method (DMCF, 1, Serialized)  // DMCF: Display Mux Configure
        {
            If (<Arg0 does not match either of the GPU children this mux is connected to>)
            {
                Return (1) // Failure, use 1 to indicate this particular failure
            }

            // Switch the mux

            If (<Mux switch was successful>)
            {
                Return (0) // Success
            }
            Else
            {
                Return (2) // Failure, use 2 to indicate this particular failure
            }
        }
    }

    Scope (_SB_.PCI0.GFX0) // ACPI Device for GPU0
    {
        Method (_DEP, 0, NotSerialized)  // _DEP: Dependency on Mux device
        {
            If (_OSI(“DisplayMux”))
            {
                Return (Package {"_SB_.MUX1"})
            }
            Else
            {
                Return (Package (0x00){})
            }
        }

        Device (DD1F) // SB.PCI0.GFX0.DD1F which is child of GPU that is connected to the Mux
        {
            Name (_ADR, 0x400)  // _ADR: Matches the AcpiUid driver reports for the target connected to mux
            Method (DMID, 0, NotSerialized)  // DMID: ACPI name of the mux this target is connected to
            {
                Return ("_SB_.MUX1")
            }
        }
    }

    Scope (_SB_.PCI0.PEG0.PEGP) // ACPI Device for GPU1
    {
        Method (_DEP, 0, NotSerialized)  // _DEP: Dependency on Mux device
        {
            If (_OSI(“DisplayMux”))
            {
                Return (Package {"_SB_.MUX1"})
            }
            Else
            {
                Return (Package (0x00){})
            }
        }

        Device (EDP1) // SB.PCI0.PEG0.PEGP.EDP1 which is child of GPU that is connected to the Mux
        {
            Name (_ADR, 0x100)  // _ADR: Matches the AcpiUid driver reports for the target connected to mux
            Method (DMID, 0, NotSerialized)  // DMID: ACPI name of the mux this target is connected to
            {
                Return ("_SB_.MUX1")
            }
        }
    }
}
```

## API changes

The ADS feature adds the following public API functionality:

1. Enumerate the mux devices in the system.
2. Query information about the mux; for example, which targets is it connected to and which target is it currently switched to.
3. Trigger a mux switch.
4. How to detect when the mux has been switched.

### Enumerate the mux devices in the system

Applications can use general plug and play APIs to find device interfaces that represent a functioning display mux. User-mode components can use
[Windows.Devices.Enumeration.DeviceInformation](/uwp/api/windows.devices.enumeration.deviceinformation?view=winrt-22000). Either C# or C++ can be used with these APIs to enumerate mux devices.

```cpp
// Display Mux device interface
// {93c33929-3180-46d3-8aab-008c84ad1e6e}
DEFINE_GUID(GUID_DEVINTERFACE_DISPLAYMUX, 0x93c33929, 0x3180, 0x46d3, 0x8a, 0xab, 0x00, 0x8c, 0x84, 0xad, 0x1e, 0x6e);
```

### IDisplayMuxDevice interface

The **IDisplayMuxDevice** interface is added to represent the mux device.

The following code demonstrates how to enumerate display mux devices, query their states, switch the active display target, and react to state changes using the Windows Runtime APIs.

``` winrt
#include <winrt/Windows.Foundation.h>
#include <winrt/Windows.Devices.Enumeration.h>
#include <winrt/Windows.Foundation.Collections.h>
#include <winrt/Windows.Devices.Display.Core.h>

#include <string>
#include <sstream>
#include <iomanip>
#include <windows.h>

namespace winrt
{
using namespace winrt::Windows::Foundation;
using namespace winrt::Windows::Foundation::Collections;
using namespace winrt::Windows::Devices::Enumeration;
using namespace winrt::Windows::Devices::Display;
using namespace winrt::Windows::Devices::Display::Core;
} // namespace winrt

void SwitchDisplayMuxTarget()
{
    // PnP device interface search string for Mux device interface
    std::wstring muxDeviceSelector = L"System.Devices.InterfaceClassGuid:=\"{93c33929-3180-46d3-8aab-008c84ad1e6e}\" AND System.Devices.InterfaceEnabled:=System.StructuredQueryType.Boolean#True";

    // Execute the device interface query
    winrt::DeviceInformationCollection deviceInformations = winrt::DeviceInformation::FindAllAsync(muxDeviceSelector, nullptr).get();
    if (deviceInformations.Size() == 0)
    {
        printf("No DisplayMux devices\n");
        return;
    }
    printf("%ld display mux devices found\n\n", deviceInformations.Size());

    // Only one mux in first release but here is generic code for multiple
    for (unsigned int i = 0; i < deviceInformations.Size(); i++)
    {
        printf("Display Mux device %ld :\n", i);

        // Get the device interface so we can query the info
        winrt::DeviceInformation deviceInfo = deviceInformations.GetAt(i);

        // Get the device id
        std::wstring deviceId = deviceInfo.Id().c_str();
        printf("    Device ID string : %S \n", deviceId.c_str());

        // Create the DisplayMuxDevice object
        auto displayMuxDevice = winrt::DisplayMuxDevice::FromIdAsync(deviceId).get();
        if (!displayMuxDevice)
        {
            printf("Failed to create DisplayMuxDevice object");
            continue;
        }

        // Check if DisplayMux is active
        auto displayMuxActive = displayMuxDevice.IsActive();
        printf("    DisplayMux state : %s \n", displayMuxActive ? "Active" : "Inactive");
        if (!displayMuxActive)
        {
            continue;
        }

        // Register for call back when the state of the DisplayMux changes
        UINT changeCount = 0;
        auto token = displayMuxDevice.Changed([&changeCount](auto, auto Args) -> HRESULT {
            changeCount++;
            return S_OK;
        });

        // Find targets connected to the DisplayMux and the current target
        auto targetsList = displayMuxDevice.GetAvailableMuxTargets();
        winrt::DisplayTarget currentTarget = displayMuxDevice.CurrentTarget();

        // Switch the display mux to the other target
        // NOTE SetPreferredTarget() is a sync method so use .get() to wait for the operation to complete
        printf("\n");
        if (currentTarget == targetsList.GetAt(0))
        {
            printf("DisplayMux currently connected to first target\n");
            displayMuxDevice.SetPreferredTarget(targetsList.GetAt(1)).get();
            printf("Calling SetPreferredTarget to switch DisplayMux to second target\n");
        }
        else if (currentTarget == targetsList.GetAt(1))
        {
            printf("DisplayMux currently connected to second target\n");
            displayMuxDevice.SetPreferredTarget(targetsList.GetAt(0)).get();
            printf("Calling SetPreferredTarget to switch DisplayMux to first target\n");
        }
        else
        {
            printf("Could not find current target in target list\n");
        }

        // Now read the current position
        currentTarget = displayMuxDevice.CurrentTarget();
        targetsList = displayMuxDevice.GetAvailableMuxTargets();
        if (currentTarget == targetsList.GetAt(0))
        {
            printf("DisplayMux is now currently connected to first target\n");
        }
        else if (currentTarget == targetsList.GetAt(1))
        {
            printf("DisplayMux is now currently connected to second target\n");
        }
        else
        {
            printf("Could not find current target in target list\n");
        }

        // Now unregister for change callback and display the
        displayMuxDevice.Changed(token);
        printf("DisplayMux state change callback was called %ld times\n\n", changeCount);
    }
}
```

## WDDM DDI changes for automatic display switching

This section describes the additions and changes made to the WDDM DDI to support ADS. These changes are available starting with Windows 11, version 24H2 update 2025.01D (WDDM 3.2).

### Querying KMD's ADS support interface

The [**DXGK_DISPLAYMUX_INTERFACE_2**](/windows-hardware/drivers/ddi/dispmprt/ns-dispmprt-dxgk_displaymux_interface_2) interface structure is added. It contains the OS-to-driver calls needed to support ADS version 2. The OS [queries for the driver's supported ADS interface](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_query_interface) at driver start, with [**InterfaceType**](/windows-hardware/drivers/ddi/video/ns-video-_query_interface) set to GUID_WDDM_INTERFACE_DISPLAYMUX_2.

([**DXGK_DISPLAYMUX_INTERFACE**](/windows-hardware/drivers/ddi/dispmprt/ns-dispmprt-dxgk_displaymux_interface) contains the OS-to-driver calls needed to support Version 1 of the ADS feature. This version was used during the prerelease of ADS.)

### KMD functions to support ADS

KMD implements the following functions to support ADS. *Dxgkrnl* obtains KMD's ADS functional interface through a call to KMD's [**DxgkddiQueryInterface**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_query_interface).


### Driver reporting ADS capability

The driver reports its level of ADS support when the OS calls its [**DxgkDdiDisplayMuxGetDriverSupportLevel**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_displaymux_get_driver_support_level) DDI. If the driver doesn't implement the [**DXGK_DISPLAYMUX_INTERFACE**](/windows-hardware/drivers/ddi/dispmprt/ns-dispmprt-dxgk_displaymux_interface_2) interface, the OS considers the support level to be DXGK_DISPLAYMUX_SUUPORT_LEVEL_NONE.

The driver should report its ADS support level no matter which system it's running on. The support level reported by the driver should only be based on the driver. The driver shouldn't take into account any of the following criteria when reporting its ADS support level:

1. The system OEM.
2. Any other GPU in the system.
3. The presence or not of the ACPI mux device.
4. The presence or not of the ACPI entries under the GPU's ACPI node.

### Update for reporting targets at start adapter time

When the adapter starts, it reports all its child devices via the [**DxgkDdiQueryChildRelations**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_query_child_relations) DDI. The report includes any internal targets connected to a mux. An internal target includes the [**DXGK_CHILD_CAPABILITIES.Type.IntegratedDisplayChild.DescriptorLength**](/windows-hardware/drivers/ddi/dispmprt/ns-dispmprt-_dxgk_integrated_display_child) field.

A problem arises if the mux is switched to the other GPU when the adapter starts. In this situation, the driver can't communicate with the internal panel to query the EDID/DisplayId size. Thus, a driver that exposes the GUID_WDDM_INTERFACE_DISPLAYMUX_2 interface must set **DXGK_CHILD_CAPABILITIES.Type.IntegratedDisplayChild.DescriptorLength** to zero at adapter start if the mux isn't currently switched to the driver's GPU. Otherwise, the OS fails the adapter start.

The OS updates its internal information about the size of the internal descriptor on the first mux switch operation.

### Update for connection change

As previously mentioned, there's an ADS-specific way to report the internal panel state during an automatic display switch sequence. To indicate that a connection change packet is part of an ADS switch sequence, the **DisplayMuxConnectionChange** flag is added to [**DXGK_CONNECTION_MONITOR_CONNECT_FLAGS**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-dxgk_connection_monitor_connect_flags). When **DisplayMuxConnectionChange** is set, it indicates that the **MonitorStatusConnected** or **MonitorStatusDisconnected** [connection status](/windows-hardware/drivers/ddi/d3dkmddi/ne-d3dkmddi-_dxgk_connection_status) is related to an automatic display switch.

**DisplayMuxConnectionChange** should only be used during an ADS switch and shouldn't be used for any other purpose. It should be used in the following ADS occasions:

* While the driver is processing [**DxgkDdiDisplayMuxPreSwitchAway**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_displaymux_pre_switch_away).

  If the internal panel is connected, the driver should add a [**DXGK_CONNECTION_CHANGE**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_connection_change) packet to its connection change list with **DXGK_CONNECTION_CHANGE.ConnectionStatus** set to **MonitorStatusDisconnected** and **DXGK_CONNECTION_CHANGE.MonitorConnect.MonitorConnectFlags.DisplayMuxConnectionChange** set to 1.  These settings indicate to the OS that the driver has released control of the internal panel.

* While the driver is processing [**DxgkDdiDisplayMuxPostSwitchToPhase1**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_displaymux_post_switch_to_phase1).

  * The driver should first determine if the internal panel is connected.
  * If panel is connected, the driver should add a [**DXGK_CONNECTION_CHANGE**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_connection_change) packet to its connection change list with **DXGK_CONNECTION_CHANGE.ConnectionStatus** set to **MonitorStatusConnected** and **DXGK_CONNECTION_CHANGE.MonitorConnect.MonitorConnectFlags.DisplayMuxConnectionChange** set to 1.
  * If the panel isn't connected, the driver should add a **DXGK_CONNECTION_CHANGE** packet to its connection change list with **DXGK_CONNECTION_CHANGE.ConnectionStatus** set to **MonitorStatusDisconnected** and **DXGK_CONNECTION_CHANGE.MonitorConnect.MonitorConnectFlags.DisplayMuxConnectionChange** set to 1.

* While the driver is processing [**DxgkDdiDisplayMuxSwitchCanceled**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_displaymux_switch_canceled).

  * All change packets added by driver in **DxgkDdiDisplayMuxSwitchCanceled** need to have [**DXGK_CONNECTION_CHANGE.MonitorConnect.MonitorConnectFlags.DisplayMuxConnectionChange**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_connection_change) set to 1.

* *n the event a target polling request comes in during a switch, **DisplayMuxConnectionChange** should only be set for connection change packets that are added from [**DxgkDdiDisplayMuxPreSwitchAway**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_displaymux_pre_switch_away), [**DxgkDdiDisplayMuxPostSwitchToPhase1**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_displaymux_post_switch_to_phase1), or [**DxgkDdiDisplayMuxSwitchCanceled**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_displaymux_switch_canceled).

### Updated guidance for DxgkDdiSystemDisplayEnable

When an ADS driver's **DxgkDdiSystemDisplayEnable**(/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_system_display_enable) DDI is called, the driver has to ensure that PSR is disabled at end of its **DxgkDdiSystemDisplayEnable** DDI call.

## OEM guidance

There are several aspects of the ADS feature that are below the level that the OS controls in the platform. It's essential that OEMs ensure it works properly. The following list summarizes some of the key points that OEMs need to consider:

* Both the hybrid integrated and hybrid discrete driver have to support ADS.
* The mux selected for the platform is able to be controlled via ACPI.
* The _HID, DMQU and DMCF methods under the mux device and the GPU child ACPI devices for the internal targets are implemented and have the DMID ACPI method.
* Both GPUs' ACPI devices must have _DEP to mark their dependence to the mux ACPI device.
* The brightness interface/caps/ranges exposed by both GPUs match exactly.
* As detailed in the [Brightness data](#brightness-data) section, the brightness v3 interface is highly recommended over the brightness V2 interface.
* If a monitor panel driver is used, the code should be GPU-independent; that is, the same logic can be used when either GPU is in control of the panel.
* At least for an internal mux, the act of switching the mux shouldn't generate an HPD event.
* If the OEM wanted to disable the mux in a system, the DMQU ACPI method should return 0 when called with Arg0 set to 2.
* The mux must be able to switch between GPUs even when the drivers are in low power. In this case, PSR won't be used.
* When the mux switches from one GPU to another, the brightness of the panel should be maintained without any brightness glitches. There are multiple ways to do so, including the following ways. The OEM is responsible for ensuring the system maintains the brightness across switches.
  * Use DisplayPort Aux Nits based brightness control.
  * Use a Tcon with PWM reconstruction to avoid any brightness glitch.
* The panel and Tcon used can stay in self-refresh (PSR1 for eDP) when the pre-switch and post-switch link configuration are exposed by the EDID and supported by both iGPU and dGPU. This includes but isn't limited to:
  * Refresh rate
  * Active size
  * Number of eDP lanes used and lane bandwidth
  * eDP DSC setting
  * eDP VSC SDP version used
  * PSR version and features used for non-switch scenarios
