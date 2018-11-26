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

Very few drivers need to be aware of the state of a device's state machines. However, for the drivers that do need to know this information, the framework provides two sets of interfaces:

-   A set of driver-supplied event callback functions.

    The driver can request that the framework call one of the following callback functions whenever one of the state machines enters or exits a particular state:

    -   [*EvtDevicePnpStateChange*](https://msdn.microsoft.com/library/windows/hardware/ff540874), which the driver registers by calling [**WdfDeviceInitRegisterPnpStateChangeCallback**](https://msdn.microsoft.com/library/windows/hardware/ff546057).
    -   [*EvtDevicePowerStateChange*](https://msdn.microsoft.com/library/windows/hardware/ff540878), which the driver registers by calling [**WdfDeviceInitRegisterPowerStateChangeCallback**](https://msdn.microsoft.com/library/windows/hardware/ff546071).
    -   [*EvtDevicePowerPolicyStateChange*](https://msdn.microsoft.com/library/windows/hardware/ff540876), which the driver registers by calling [**WdfDeviceInitRegisterPowerPolicyStateChangeCallback**](https://msdn.microsoft.com/library/windows/hardware/ff546066).
-   A set of methods that return the current state of the state machines.

    The driver can call one of the following methods to determine the current state of one of the state machines for a particular device:

    -   [**WdfDeviceGetDevicePnpState**](https://msdn.microsoft.com/library/windows/hardware/ff545969)
    -   [**WdfDeviceGetDevicePowerState**](https://msdn.microsoft.com/library/windows/hardware/ff545985)
    -   [**WdfDeviceGetDevicePowerPolicyState**](https://msdn.microsoft.com/library/windows/hardware/ff545974)

 

 





