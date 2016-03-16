---
title: State Machines in the Framework
description: State Machines in the Framework
ms.assetid: 5ef307c6-0310-4a83-a63f-3a6d96782013
keywords: ["PnP WDK KMDF state machines", "Plug and Play WDK KMDF state machines", "power management WDK KMDF state machines", "state machines WDK KMDF", "states WDK KMDF", "PnP state machines WDK KMDF", "power states WDK KMDF", "current state machine state WDK KMDF", "status information WDK KMDF state machines", "power policy WDK KMDF"]
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20State%20Machines%20in%20the%20Framework%20%20RELEASE:%20%283/16/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




