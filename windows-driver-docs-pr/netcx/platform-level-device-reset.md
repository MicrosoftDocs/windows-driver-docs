---
title: Recovering an unresponsive NIC with platform-level device reset
description: Recovering an unresponsive NIC with platform-level device reset
ms.assetid: 
keywords:
- Recovering mechanism, device reset, collecting diagnostics
ms.date: 07/02/2020
ms.localizationpriority: medium
ms.custom: Fe
---

# Recovering an unresponsive NIC with platform-level device reset

NetAdapterCx provides an effective way to reset and recover malfunctioning network devices through platform-level device reset (PLDR). Without rebooting the entire Windows system, the PLDR operation tears down the stack of affected network devices ensuring their hardware and drivers restart from a blank state. NetAdapterCx also enables client drivers to [collect diagnostics](#register-the-optional-diagnostics-collection-callback) from failed devices before they are platform-level reset.

PLDR is triggered by either:

* The operating system (OS). The OS side can trigger PLDR if it detects abnormal device behavior. For example, when an in-transmit packet is stuck in the driver for too long.

* Independent hardware vendor (IHV) client drivers. Client drivers can request NetAdapterCx to trigger PLDR. For example, when a driver detects that their device is unresponsive to its control command.

<!-- 
PLDR can be triggered by either the operating system (OS) or the independent hardware vendor (IHV)'s client drivers.
OS side can trigger PLDR if it detects abnormal device behaviors, such like a in-transmit packet is stuck in the driver for too long.

Client driver can also request NetAdapterCx to perform a reset if, for example, IHV's client driver detects its device becomes unresponsive to its control command.
-->

In order to provide user-friendly device failure and recovery, we recommend that IHVs and original equipment manufacturers (OEMs) support PLDR for their network devices. For more information on PLDR, see [Resetting and recovering a device](../kernel/resetting-and-recovering-a-device.md).

## Register the optional diagnostics collection callback

NetAdapterCx offers IHV client drivers the option to collect unique, device-specific diagnostics from failed devices.

As part of the NetAdapterCx reset and recovery process the client driver can collect diagnostics from the failed device before the device is platform-level reset. IHVs and Microsoft can use this data in post-failure analysis to improve the quality of their products.

<!-- 
As part of the reset and recovery process initiated by NetAdapterCx, NetAdapterCx gives the client driver an opportunity to collect their own specific diagnostic from the failed device, before the device is being PLDR.
These data will be helpful in post-failure analysis for both Microsoft and IHVs in order to further improve the quality of the product.
-->

### Register NET_DEVICE_RESET_DIAGNOSTICS_CAPABILITIES

Client drivers need to initialize and register the [**NET_DEVICE_RESET_DIAGNOSTICS_CAPABILITIES**](/windows-hardware/drivers/ddi/netdevice/ns-netdevice-net_device_reset_diagnostics_capabilities) structure in their [**EVT_WDF_DRIVER_DEVICE_ADD**](/windows-hardware/drivers/ddi/wdfdriver/nc-wdfdriver-evt_wdf_driver_device_add) callback function in order to collect device-specific diagnostics.

[**NET_DEVICE_RESET_DIAGNOSTICS_CAPABILITIES**](/windows-hardware/drivers/ddi/netdevice/ns-netdevice-net_device_reset_diagnostics_capabilities) contains:

* A unique GUID. The IHV specifies this GUID and uses it later to identify and retrieve the reset diagnostics from a memory dump. For example, the [.enumtag](../debugger/-enumtag--enumerate-secondary-callback-data-.md) command can be used to retrieve the diagnostics.

* An [**EVT_NET_DEVICE_COLLECT_RESET_DIAGNOSTICS**](/windows-hardware/drivers/ddi/netdevice/nc-netdevice-evt_net_device_collect_reset_diagnostics) event callback function. NetAdapterCx invokes this callback to collect diagnostics. If the client driver provides an **EVT_NET_DEVICE_COLLECT_RESET_DIAGNOSTICS** callback, NetAdapterCx invokes it on the client driver using a *dedicated* thread.

The following example shows how to register **NET_DEVICE_RESET_DIAGNOSTICS_CAPABILITIES** to NetAdapterCx:

```cpp
EVT_WDF_DRIVER_DEVICE_ADD EvtWdfDriverDeviceAdd;

NTSTATUS EvtWdfDriverDeviceAdd(
    WDFDRIVER Driver,
    PWDFDEVICE_INIT DeviceInit
)
{
    ...

    NET_DEVICE_RESET_DIAGNOSTICS_CAPABILITIES resetResetDiagnosticsCapabilities;
    NET_DEVICE_RESET_DIAGNOSTICS_CAPABILITIES_INIT(
        &resetResetDiagnosticsCapabilities,
        DUMMY_GUID,
        EvtDeviceCollectResetDiagnostics);
    NetDeviceInitSetResetDiagnosticsCapabilities(DeviceInit, &resetResetDiagnosticsCapabilities);

    ...
}
```

See [**NET_DEVICE_RESET_DIAGNOSTICS_CAPABILITIES_INIT**](/windows-hardware/drivers/ddi/nf-netdevice-net_device_reset_diagnostics_capabilities_init) on how to initialize the **NET_DEVICE_RESET_DIAGNOSTICS_CAPABILITIES** structure. 

See [**NetDeviceInitSetResetDiagnosticsCapabilitites**](/windows-hardware/drivers/ddi/nf-netdevice-netdeviceinitsetresetdiagnosticscapabilitites) on how to advertise the **NET_DEVICE_RESET_DIAGNOSTICS_CAPABILITIES** structure to NetAdapterCx.

### Implement EVT_NET_DEVICE_COLLECT_RESET_DIAGNOSTICS

The reset and recovery sequence can happen at any given time. Therefore, the client driver's [**EVT_NET_DEVICE_COLLECT_RESET_DIAGNOSTICS**](/windows-hardware/drivers/ddi/netdevice/nc-netdevice-evt_net_device_collect_reset_diagnostics) callback implementation must consider the following:

* NetAdapterCx synchronizes the **EVT_NET_DEVICE_COLLECT_RESET_DIAGNOSTICS** callback with other callbacks that might occur during the [power-down sequence](power-down-sequence-for-a-netadaptercx-client-driver.md). The client driver can assume NetAdapterCx won't invoke callbacks like packet queue cancel/stop, hardware release, and device object deletion until **EVT_NET_DEVICE_COLLECT_RESET_DIAGNOSTICS** returns.

* The client driver must use extra caution when handling diagnostics collection to avoid dead lock. It must take into account that the hardware may already be in a failed state.

* It's critical for **EVT_NET_DEVICE_COLLECT_RESET_DIAGNOSTICS** to complete as soon as possible so the rest of the PLDR process can proceed. **EVT_NET_DEVICE_COLLECT_RESET_DIAGNOSTICS** must be reliable and must return within 3 seconds.

<!--
Therefore, the client driver's [**EVT_NET_DEVICE_COLLECT_RESET_DIAGNOSTICS**](/windows-hardware/drivers/ddi/netdevice/nc-netdevice-evt_net_device_collect_reset_diagnostics) callback implementation should take this into consideration.

NetAdapterCx synchronizes the **EVT_NET_DEVICE_COLLECT_RESET_DIAGNOSTICS** callback with other callbacks that might occur during [power-down sequence](power-down-sequence-for-a-netadaptercx-client-driver.md).
Therefore in handling **EVT_NET_DEVICE_COLLECT_RESET_DIAGNOSTICS**, the client driver can assume callbacks like packet queue cancel/stop, releasing hardware, and deleting the device object will not happen until **EVT_NET_DEVICE_COLLECT_RESET_DIAGNOSTICS** returns.
The client driver must use extra caution when handling the diagnostics collecting to avoid dead lock, and keep in mind the hardware may already be in failed state.

It's critical for **EVT_NET_DEVICE_COLLECT_RESET_DIAGNOSTICS** to complete as soon as possible, so the rest of PLDR process can proceed.
This callback must be reliable and must return within 3 seconds.
-->

In the **EVT_NET_DEVICE_COLLECT_RESET_DIAGNOSTICS** callback, the client driver should submit diagnostics as a flat data buffer to NetAdapterCx by calling the [**NetDeviceStoreResetDiagnostics**](/windows-hardware/drivers/ddi/nf-netdevice-netdevicestoreresetdiagnostics) API.
Once **NetDeviceStoreResetDiagnostics** returns it is safe for the client driver to free its reset diagnostics data buffer.

NetAdapterCx always invokes the **EVT_NET_DEVICE_COLLECT_RESET_DIAGNOSTICS** callback at PASSIVE_LEVEL.
The client driver must call the **NetDeviceStoreResetDiagnostics** API at PASSIVE_LEVEL.
The flat buffer the client driver uses to collect reset diagnostics can come from either paged or non-paged pool.

> [!IMPORTANT]
> The [**NetDeviceStoreResetDiagnostics**](/windows-hardware/drivers/ddi/nf-netdevice-netdevicestoreresetdiagnostics) API must only be called in the [**EVT_NET_DEVICE_COLLECT_RESET_DIAGNOSTICS**](/windows-hardware/drivers/ddi/netdevice/nc-netdevice-evt_net_device_collect_reset_diagnostics) callback.
> It cannot be used to re-submit diagnostics data after previous **NetDeviceStoreResetDiagnostics** returns.
> Violating either of these cases will result in a bugcheck.

> [!IMPORTANT]
> The size limitation for reset diagnostics is 1 MBytes.

## NetAdapterCx reset and recover sequence

The following sequence occurs from the client driver's perspective when PLDR is triggered by either the OS or the client driver:

1. NetAdapterCx invokes the client driver's [**EVT_NET_DEVICE_COLLECT_RESET_DIAGNOSTICS**](/windows-hardware/drivers/ddi/netdevice/nc-netdevice-evt_net_device_collect_reset_diagnostics) callback to collect diagnostics from the failed device. For example, the driver may collect a snapshot of the device firmware. This step is optional and only occurs if the client driver has registered the [**NET_DEVICE_RESET_DIAGNOSTICS_CAPABILITIES**](/windows-hardware/drivers/ddi/netdevice/ns-netdevice-net_device_reset_diagnostics_capabilities) structure. Otherwise, NetAdapterCx will skip this step.

2. NetAdapterCx performs the platform-level device reset operation. NetAdapterCx power recycles the hardware and tears down the software device stack.

Steps 1 and 2 in the diagram below correspond to the description of the NetAdapterCx reset and recover sequence:

<img src=images/pldr_flowchart.png alt="Illustration of the NetAdapterCx reset and recover sequence outlined above" width="600"/>

## How a client driver requests PLDR

A client driver triggers PLDR using the NetAdapterCx [**NetDeviceRequestReset**](/windows-hardware/drivers/ddi/nf-netdevice-netdevicerequestreset.md) API when it detects device failure. **NetDeviceRequestReset** returns immediately to the client driver.
The reset and recovery sequence described in [NetAdapterCx reset and recover sequence](#netadaptercx-reset-and-recover-sequence) is triggered and is asynchronous to the **NetDeviceRequestReset** call.

Only one PLDR operation can happen at any given time. Therefore, subsequent calls of **NetDeviceRequestReset** have no effect when a reset and recovery operation is already in-flight.

Calling **NetDeviceRequestReset** also has no effect if the [power-down sequence](power-down-sequence-for-a-netadaptercx-client-driver.md) has already been initiated.
