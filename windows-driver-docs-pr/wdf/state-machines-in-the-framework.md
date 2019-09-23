---
title: State Machines in the Framework
description: State Machines in the Framework
ms.assetid: 5ef307c6-0310-4a83-a63f-3a6d96782013
keywords:
- PnP WDK KMDF , state machines
- Plug and Play WDK KMDF , state machines
- power management WDK KMDF , state machines
- state machines WDK KMDF
- states WDK KMDF
- PnP state machines WDK KMDF
- power states WDK KMDF
- current state machine state WDK KMDF
- status information WDK KMDF , state machines
- power policy WDK KMDF
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# State Machines in the Framework


To keep track of each device's state, the framework uses a PnP state machine, a power state machine, and a power policy state machine. The framework creates an instance of each state machine for each device that is plugged into a system.

>[!NOTE]
>This functionality is for Microsoft-internal use only.

For drivers that do need to know this information, the framework provides two sets of interfaces:

-   A set of driver-supplied event callback functions.

    The driver can request that the framework call one of the following callback functions whenever one of the state machines enters or exits a particular state:

    -   [*EvtDevicePnpStateChange*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfdevice/nc-wdfdevice-evt_wdf_device_pnp_state_change_notification), which the driver registers by calling [**WdfDeviceInitRegisterPnpStateChangeCallback**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfdevice/nf-wdfdevice-wdfdeviceinitregisterpnpstatechangecallback).
    -   [*EvtDevicePowerStateChange*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfdevice/nc-wdfdevice-evt_wdf_device_power_state_change_notification), which the driver registers by calling [**WdfDeviceInitRegisterPowerStateChangeCallback**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfdevice/nf-wdfdevice-wdfdeviceinitregisterpowerstatechangecallback).
    -   [*EvtDevicePowerPolicyStateChange*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfdevice/nc-wdfdevice-evt_wdf_device_power_policy_state_change_notification), which the driver registers by calling [**WdfDeviceInitRegisterPowerPolicyStateChangeCallback**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfdevice/nf-wdfdevice-wdfdeviceinitregisterpowerpolicystatechangecallback).
-   A set of methods that return the current state of the state machines.

    The driver can call one of the following methods to determine the current state of one of the state machines for a particular device:

    -   [**WdfDeviceGetDevicePnpState**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfdevice/nf-wdfdevice-wdfdevicegetdevicepnpstate)
    -   [**WdfDeviceGetDevicePowerState**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfdevice/nf-wdfdevice-wdfdevicegetdevicepowerstate)
    -   [**WdfDeviceGetDevicePowerPolicyState**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfdevice/nf-wdfdevice-wdfdevicegetdevicepowerpolicystate)

 

 





