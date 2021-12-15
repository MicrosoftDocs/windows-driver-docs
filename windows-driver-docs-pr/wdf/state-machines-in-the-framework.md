---
title: State Machines in the Framework
description: State Machines in the Framework
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
---

# State Machines in the Framework


To keep track of each device's state, the framework uses a PnP state machine, a power state machine, and a power policy state machine. The framework creates an instance of each state machine for each device that is plugged into a system.

>[!NOTE]
>This functionality is for Microsoft-internal use only.

For drivers that do need to know this information, the framework provides two sets of interfaces:

-   A set of driver-supplied event callback functions.

    The driver can request that the framework call one of the following callback functions whenever one of the state machines enters or exits a particular state:

    -   [*EvtDevicePnpStateChange*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_pnp_state_change_notification), which the driver registers by calling [**WdfDeviceInitRegisterPnpStateChangeCallback**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceinitregisterpnpstatechangecallback).
    -   [*EvtDevicePowerStateChange*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_power_state_change_notification), which the driver registers by calling [**WdfDeviceInitRegisterPowerStateChangeCallback**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceinitregisterpowerstatechangecallback).
    -   [*EvtDevicePowerPolicyStateChange*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_power_policy_state_change_notification), which the driver registers by calling [**WdfDeviceInitRegisterPowerPolicyStateChangeCallback**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceinitregisterpowerpolicystatechangecallback).
-   A set of methods that return the current state of the state machines.

    The driver can call one of the following methods to determine the current state of one of the state machines for a particular device:

    -   [**WdfDeviceGetDevicePnpState**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicegetdevicepnpstate)
    -   [**WdfDeviceGetDevicePowerState**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicegetdevicepowerstate)
    -   [**WdfDeviceGetDevicePowerPolicyState**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicegetdevicepowerpolicystate)

 

