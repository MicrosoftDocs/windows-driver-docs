---
title: Updates for IddCx versions 1.10 and later
description: Version 1.10 updates to the Indirect Display Driver Class eXtension for console and remote indirect display drivers
ms.date: 10/20/2023
keywords:
- IddCx version 1.10
- Console and remote indirect display driver, IddCx versions 1.10 and later
- Console and remote IDD, IddCx versions 1.10 and later
- Console indirect display driver
- Console IDD
- Remote indirect display driver
- Remote IDD
- HDR support, IddCx
- SDR support, IddCx
---

# Updates for IddCx versions 1.10 and later

This page describes the changes made in IddCx version 1.10. A single indirect display driver (IDD) binary built against IddCx 1.10 can run on Windows 10, version 1803 and above using runtime checks to verify whether DDI changes in IddCx 1.10 are available on that system. For more information, see [Building a WDF driver for multiple versions of Windows](../wdf/building-a-wdf-driver-for-multiple-versions-of-windows.md).

The IddCx 1.10 changes fall into the following categories:

* Update the [**IddCxGetVersion**](/windows-hardware/drivers/ddi/iddcx/nf-iddcx-iddcxgetversion) version (console and remote). For a complete list of IddCx-related version information, see [IddCx versions](iddcx-versions.md).
* Add HDR10 (high dynamic range) and SDR (standard dynamic range) Wide Color Gamut (WCG) support to Indirect Displays.

## Updated IddCxGetVersion version

The value returned by [**IddCxGetVersion**](/windows-hardware/drivers/ddi/iddcx/nf-iddcx-iddcxgetversion) has been updated but differs depending on the OS:

* The Windows 11, version 22H2 September Update returns 0x1A00 (IDDCX_VERSION_SV3).
* The 2024 Windows platform release will return 0x1A80.

This versioning is significant for remote drivers where the behavior of the OS differs slightly.

## HDR and SDR wide color gamut support

For some introductory information about color on Windows, including SDR WCG, see [DirectX with advanced color on HDR and SDR displays](/windows/win32/direct3darticles/high-dynamic-range).

### Driver DDI and OS support

Where possible, existing DDIs were extended to allow a driver to report support for:

* HDR10
* SDR WCG
* Receiving data describing any HDR frames sent to an IDD

Newer variants of existing DDIs were added when existing DDIs couldn't be extended. In most cases, these changes are applicable to both console and remote drivers but a few details specific to remote drivers are also defined.

Version 1.10 and greater drivers that support HDR must use the newer DDI variants. Older drivers or drivers that don't support HDR can continue to use the existing functions. An overview of the changes is given in the sections following this one.

The following table lists the driver-implemented DDIs added in IddCx 1.10 and names the previous equivalent if there was one. The OS may call these functions if the driver reports them, even for adapters that aren't trying to support HDR.

| Driver functions that OS calls for HDR adapters | Previous equivalent function |
| ---------------------------------------- | ---------------------------- |
| [**EVT_IDD_CX_ADAPTER_QUERY_TARGET_INFO**](/windows-hardware/drivers/ddi/iddcx/nc-iddcx-evt_idd_cx_adapter_query_target_info) | N/A |
| [**EVT_IDD_CX_MONITOR_SET_DEFAULT_HDR_METADATA**](/windows-hardware/drivers/ddi/iddcx/nc-iddcx-evt_idd_cx_monitor_set_default_hdr_metadata)* | N/A |
| [**EVT_IDD_CX_PARSE_MONITOR_DESCRIPTION2**](/windows-hardware/drivers/ddi/iddcx/nc-iddcx-evt_idd_cx_parse_monitor_description2)** | [**EVT_IDD_CX_PARSE_MONITOR_DESCRIPTION**](/windows-hardware/drivers/ddi/iddcx/nc-iddcx-evt_idd_cx_parse_monitor_description) |
| [**EVT_IDD_CX_MONITOR_QUERY_TARGET_MODES2**](/windows-hardware/drivers/ddi/iddcx/nc-iddcx-evt_idd_cx_monitor_query_target_modes2) | [**EVT_IDD_CX_MONITOR_QUERY_TARGET_MODES**](/windows-hardware/drivers/ddi/iddcx/nc-iddcx-evt_idd_cx_monitor_query_target_modes) |
| [**EVT_IDD_CX_ADAPTER_COMMIT_MODES2**](/windows-hardware/drivers/ddi/iddcx/nc-iddcx-evt_idd_cx_adapter_commit_modes2) | [**EVT_IDD_CX_ADAPTER_COMMIT_MODES**](/windows-hardware/drivers/ddi/iddcx/nc-iddcx-evt_idd_cx_adapter_commit_modes) |

*\*: Function isn't called for remote drivers.*

*\*\*: Function might not be called for remote drivers depending on the [adapter flags](#reporting-adapter-hdr-support) set by the driver.*

The following table lists the OS-implemented functions added in IddCx 1.10 and names the previous equivalent(s) if there was one. A version 1.10 driver can call the newer variants if it has determined that these functions are available in the OS that the driver is running on.

| Newer functions a driver must call for HDR adapters | Previous equivalent |
| --------------------------------------------------- | ------------------- |
| [**IddCxSwapChainReleaseAndAcquireBuffer2**](/windows-hardware/drivers/ddi/iddcx/nf-iddcx-iddcxswapchainreleaseandacquirebuffer2) | [**IddCxSwapChainReleaseAndAcquireBuffer**](/windows-hardware/drivers/ddi/iddcx/nf-iddcx-iddcxswapchainreleaseandacquirebuffer)/[**IddCxSwapChainReleaseAndAcquireSystemBuffer**](/windows-hardware/drivers/ddi/iddcx/nf-iddcx-iddcxswapchainreleaseandacquiresystembuffer) |
| [**IddCxMonitorQueryHardwareCursor3**](/windows-hardware/drivers/ddi/iddcx/nf-iddcx-iddcxmonitorqueryhardwarecursor3) | [**IddCxMonitorQueryHardwareCursor2**](/windows-hardware/drivers/ddi/iddcx/nf-iddcx-iddcxmonitorqueryhardwarecursor2) or [**IddCxMonitorQueryHardwareCursor**](/windows-hardware/drivers/ddi/iddcx/nf-iddcx-iddcxmonitorqueryhardwarecursor) |
| [**IddCxAdapterDisplayConfigUpdate2**](/windows-hardware/drivers/ddi/iddcx/nf-iddcx-iddcxadapterdisplayconfigupdate2)* | [**IddCxAdapterDisplayConfigUpdate**](/windows-hardware/drivers/ddi/iddcx/nf-iddcx-iddcxadapterdisplayconfigupdate)* |
| [**IddCxMonitorUpdateModes2**](/windows-hardware/drivers/ddi/iddcx/nf-iddcx-iddcxmonitorupdatemodes2) | [**IddCxMonitorUpdateModes**](/windows-hardware/drivers/ddi/iddcx/nf-iddcx-iddcxmonitorupdatemodes) |

*\*: For use by remote drivers only.*

### Reporting adapter HDR support

Version 1.10 and above drivers should set the **IDDCX_ADAPTER_FLAGS_CAN_PROCESS_FP16** flag added to [**IDDCX_ADAPTER_FLAGS**](/windows-hardware/drivers/ddi/iddcx/ne-iddcx-iddcx_adapter_flags) to report support for FP16 surfaces. FP16 surfaces can be used for HDR10 or just SDR WCG. Setting this flag implies that a driver does everything required to enable HDR10 or SDR WCG, including:

* Report target capabilities via the introduced [**EVT_IDD_CX_ADAPTER_QUERY_TARGET_INFO**](/windows-hardware/drivers/ddi/iddcx/nc-iddcx-evt_idd_cx_adapter_query_target_info) function
* Report extended mode information via the following introduced functions:
  * [**EVT_IDD_CX_PARSE_MONITOR_DESCRIPTION2**](/windows-hardware/drivers/ddi/iddcx/nc-iddcx-evt_idd_cx_parse_monitor_description2)
  * [**EVT_IDD_CX_MONITOR_QUERY_TARGET_MODES2**](/windows-hardware/drivers/ddi/iddcx/nc-iddcx-evt_idd_cx_monitor_query_target_modes2)
* Only update target modes via [**IddCxMonitorUpdateModes2**](/windows-hardware/drivers/ddi/iddcx/nf-iddcx-iddcxmonitorupdatemodes2) and no longer call**IddCxMonitorUpdateModes**
* Only query cursor details via [**IddCxMonitorQueryHardwareCursor3**](/windows-hardware/drivers/ddi/iddcx/nf-iddcx-iddcxmonitorqueryhardwarecursor3) and no longer call **IddCxMonitorQueryHardwareCursor2** or **IddCxMonitorQueryHardwareCursor**
* Process FP16 desktop surfaces provided by [**IddCxSwapChainReleaseAndAcquireBuffer2**](/windows-hardware/drivers/ddi/iddcx/nf-iddcx-iddcxswapchainreleaseandacquirebuffer2)
* Use the HDR 3x4 matrix transform received by [**EVT_IDD_CX_MONITOR_SET_GAMMA_RAMP**](/windows-hardware/drivers/ddi/iddcx/nc-iddcx-evt_idd_cx_monitor_set_gamma_ramp)
* Send HDR metadata to the display. This metadata is sent either in [**EVT_IDD_CX_MONITOR_SET_DEFAULT_HDR_METADATA**](/windows-hardware/drivers/ddi/iddcx/nc-iddcx-evt_idd_cx_monitor_set_default_hdr_metadata) or [**IddCxSwapChainReleaseAndAcquireBuffer2**](/windows-hardware/drivers/ddi/iddcx/nf-iddcx-iddcxswapchainreleaseandacquirebuffer2)
* Apply SDR white level where appropriate; for example, to mouse cursors. The SDR white level is included in [**IddCxSwapChainReleaseAndAcquireBuffer2**](/windows-hardware/drivers/ddi/iddcx/nf-iddcx-iddcxswapchainreleaseandacquirebuffer2) and [**IddCxMonitorQueryHardwareCursor3**](/windows-hardware/drivers/ddi/iddcx/nf-iddcx-iddcxmonitorqueryhardwarecursor3)

### Reporting target HDR capabilities

If a driver wishes to enable HDR for an adapter, it must provide additional information about each target connector via its [**EVT_IDD_CX_ADAPTER_QUERY_TARGET_INFO**](/windows-hardware/drivers/ddi/iddcx/nc-iddcx-evt_idd_cx_adapter_query_target_info) function. Target connector-specific information is needed because only some of the available targets might support some aspects of HDR.

### HDR metadata

When the driver provides a monitor descriptor containing HDR metadata, the OS calls [**EVT_IDD_CX_MONITOR_SET_DEFAULT_HDR_METADATA**](/windows-hardware/drivers/ddi/iddcx/nc-iddcx-evt_idd_cx_monitor_set_default_hdr_metadata) to give the default HDR metadata to the driver. The driver must keep this default data and use it when sending HDR10 info frames (SMPTE ST.2086) to the monitor. When a driver calls [**IddCxSwapChainReleaseAndAcquireBuffer2**](/windows-hardware/drivers/ddi/iddcx/nf-iddcx-iddcxswapchainreleaseandacquirebuffer2), the OS also provides HDR metadata information. If this metadata indicates that the default should be used, it's the stored default data that is being referred to.

When an HDR mode is set, the OS sends HDR metadata state with every frame. This metadata tells the driver which HDR metadata to use via the introduced [**IDDCX_METADATA2**](/windows-hardware/drivers/ddi/iddcx/ns-iddcx-iddcx_metadata2) structure. The metadata is either a new metadata block or an indication that the driver should use either the default metadata the OS previously provided or the same metadata as the previous frame.

Note: HDR metadata isn't made available to remote drivers because any HDR10 metadata should come from the display subsystem on the client.

### Reporting HDR modes

When a display is connected to a target, the OS queries the driver for currently supported monitor and target modes. To correctly advertise HDR capabilities, extra information is needed for each of these modes, so an HDR driver must expose the following DDIs introduced in v1.10:

* [**EVT_IDD_CX_PARSE_MONITOR_DESCRIPTION2**](/windows-hardware/drivers/ddi/iddcx/nc-iddcx-evt_idd_cx_parse_monitor_description2) returns a list of [**IDDCX_MONITOR_MODE2**](/windows-hardware/drivers/ddi/iddcx/ns-iddcx-iddcx_monitor_mode2) structures.
* [**EVT_IDD_CX_MONITOR_QUERY_TARGET_MODES2**](/windows-hardware/drivers/ddi/iddcx/nc-iddcx-evt_idd_cx_monitor_query_target_modes2) returns a list of [**IDDCX_TARGET_MODE2**](/windows-hardware/drivers/ddi/iddcx/ns-iddcx-iddcx_monitor_mode2) structures.

These extended modes indicate the possible bit depths and surface formats that can be used. A driver can also update a target mode list by calling [**IddCxMonitorUpdateModes2**](/windows-hardware/drivers/ddi/iddcx/nf-iddcx-iddcxmonitorupdatemodes2).

The OS infers variations of modes for HDR and SDR WCG based on the information returned by the driver's [**EVT_IDD_CX_ADAPTER_QUERY_TARGET_INFO**](/windows-hardware/drivers/ddi/iddcx/nc-iddcx-evt_idd_cx_adapter_query_target_info) callback prior to any modes being reported.

The OS validates the modes to try to detect repeated modes that should be combined and reported as a single mode. For example, a target that supports 1080p at 60 Hz in both 8 bits and 10 bits per channel should be reported as a single mode. However if the target supports these modes but they require different amounts of bandwidth it's still OK for these modes to be reported separately.

### An added gamma type

The existing [**EVT_IDD_CX_MONITOR_SET_GAMMA_RAMP**](/windows-hardware/drivers/ddi/iddcx/nc-iddcx-evt_idd_cx_monitor_set_gamma_ramp) DDI has been extended so that the OS can provide the 3x4 matrix transform needed to support HDR displays to drivers that advertise HDR support.

### SDR white level

Mouse cursor pixel data is always SDR. When a monitor is set in an HDR mode, the SDR white level must be applied to mouse cursors. IddCx v.10 provides this capability in two places:

* It has been added to the per frame metadata received by a driver when calling [**IddCxSwapChainReleaseAndAcquireBuffer2**](/windows-hardware/drivers/ddi/iddcx/nf-iddcx-iddcxswapchainreleaseandacquirebuffer2).
* It's also part of the introduced [**IddCxMonitorQueryHardwareCursor3**](/windows-hardware/drivers/ddi/iddcx/nf-iddcx-iddcxmonitorqueryhardwarecursor3) function so that a driver can render cursor updates at the correct white level without needing to receive a new frame. The default SDR white level is 80 nits.

### Surface color space

Even though the driver reported color space as part of mode information, the OS reports the actual color space used by a specific frame in the introduced [**IDDCX_METADATA2**](/windows-hardware/drivers/ddi/iddcx/ns-iddcx-iddcx_metadata2) structure.

### HDR with remote drivers

Where possible, OS and driver behavior should be the same for a remote driver as with a console driver. The exceptions are:

* HDR metadata isn't provided to remote drivers. The client system is expected to provide this metadata based on the physically connected display. It's meaningless to use metadata determined by the server.
* The 3x4 color matrix transform is also not sent. Again, a remote driver is expected to use the equivalent data from the client system.
* Remote drivers can provide the colorimetry data and SDR white level to be used on the server.
* Monitor modes are also optional for remote drivers. If a remote driver sets the [**IDDCX_ADAPTER_FLAGS_ALL_TARGET_MODES_MONITOR_COMPATIBLE**](/windows-hardware/drivers/ddi/iddcx/ne-iddcx-iddcx_adapter_flags) adapter flag, the OS won't ask it for monitor modes and instead just uses the target modes. This capability allows a driver to specify unusual modes without needing to report the equivalent monitor mode; for example, based on a client window size rather than a monitor size.

### Supporting a 1.10 driver running down level

Version 1.10 drivers that run on older Windows releases need to take several steps to ensure compatibility. Specifically, drivers must:

* Continue to export all existing functions such as [**EVT_IDD_CX_PARSE_MONITOR_DESCRIPTION**](/windows-hardware/drivers/ddi/iddcx/nc-iddcx-evt_idd_cx_parse_monitor_description), [**EVT_IDD_CX_MONITOR_QUERY_TARGET_MODES**](/windows-hardware/drivers/ddi/iddcx/nc-iddcx-evt_idd_cx_monitor_query_target_modes), and [**EVT_IDD_CX_ADAPTER_COMMIT_MODES**](/windows-hardware/drivers/ddi/iddcx/nc-iddcx-evt_idd_cx_adapter_commit_modes).
* Use the [**IDD_CX_CLIENT_CONFIG_INIT**](/windows-hardware/drivers/ddi/iddcx/nf-iddcx-idd_cx_client_config_init) macro to set the size of the [**IDD_CX_CLIENT_CONFIG**](/windows-hardware/drivers/ddi/iddcx/ns-iddcx-idd_cx_client_config) structure.
* Not try to call any OS-implemented functions that aren't available in older releases. Use **IDD_IS_FUNCTION_AVAILABLE** to check for availability.
* None of the v1.10 functions can be exported. A driver can use the **IDD_IS_FIELD_AVAILABLE** macro to check whether it should write the **EvtIddCx*Xxx*** callback to the [**IDD_CX_CLIENT_CONFIG**](/windows-hardware/drivers/ddi/iddcx/ns-iddcx-idd_cx_client_config) structure.
* **IDD_IS_FIELD_AVAILABLE** can also help a driver determine if it's safe to set **IDDCX_ADAPTER_FLAGS_CAN_PROCESS_FP16** or **IDDCX_ADAPTER_FLAGS_ALL_TARGET_MODES_MONITOR_COMPATIBLE**. If one of the v1.10 DDIs isn't available, the driver shouldn't set the flag.

An example of how **IDD_IS_FIELD_AVAILABLE** can be used:

``` cpp
    if (IDD_IS_FIELD_AVAILABLE(IDD_CX_CLIENT_CONFIG, EvtIddCxParseMonitorDescription2))
    {
        IddCxClientConfig.EvtIddCxParseMonitorDescription2 = ParseMonitorDescription2;
    }
```

For more information, see [Building IddCx 1.4 drivers](building-iddcx1.4-drivers.md).
