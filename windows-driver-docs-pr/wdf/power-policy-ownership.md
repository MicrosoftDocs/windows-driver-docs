---
title: Power Policy Ownership
description: Power Policy Ownership
ms.assetid: 8e44eedd-6afe-45c6-bbe8-42cfb6f6a644
keywords: ["power management WDK KMDF , ownership", "ownership WDK KMDF", "ownership WDK KMDF , power policy", "power policy WDK KMDF", "wake-up capabilities WDK KMDF", "sleep power management WDK KMDF", "low-power states WDK KMDF", "device power states WDK KMDF", "working states WDK KMDF", "power states WDK KMDF"]
---

# Power Policy Ownership


For each device, one (and only one) of the device's drivers must be the device's *power policy owner*. The power policy owner determines the appropriate [device power state](https://msdn.microsoft.com/library/windows/hardware/ff543162) for a device and sends requests to the device's driver stack whenever the device's power state should change.

Framework-based drivers do not contain code that requests changes in a device's power state, because the framework provides that code. By default, whenever the system enters a [system sleeping state](https://msdn.microsoft.com/library/windows/hardware/ff564575), the framework asks the driver for your device's bus to lower the device power state to D3. (Your driver can change the default behavior so that the framework sets your device's sleep state to D1 or D2, if the device provides wake-up capabilities.) When the system power returns to its [working (S0) state](https://msdn.microsoft.com/library/windows/hardware/ff564591), the framework requests the bus driver to restore your device to its working (D0) state.

The power policy owner is also responsible for enabling and disabling the following device features:

-   Your device's ability to enter a [low-power (sleeping) state](https://msdn.microsoft.com/library/windows/hardware/ff543186) when it is idle and the system remains in its working (S0) state

-   Your device's ability to wake itself up from a sleeping state when it detects an external event

-   Your device's ability to wake up the entire system from a system sleeping state when it detects an external event

If your device supports these idle power-down and system wake-up capabilities, the power policy owner can also call [**WdfDeviceInitSetPowerPolicyEventCallbacks**](https://msdn.microsoft.com/library/windows/hardware/ff546774) to register a set of power policy event callback functions.

By default, for framework-based drivers, the device's function driver is the power policy owner. (If there is no function driver and the bus driver has called [**WdfPdoInitAssignRawDevice**](https://msdn.microsoft.com/library/windows/hardware/ff548802), the bus driver is the power policy owner). If you want to change the power policy owner for a driver stack, the default power policy owner must call [**WdfDeviceInitSetPowerPolicyOwnership**](https://msdn.microsoft.com/library/windows/hardware/ff546776) to disable ownership, and the driver that will be the power policy owner must call **WdfDeviceInitSetPowerPolicyOwnership** to enable ownership.

The framework does the following work for the power policy owner:

-   It handles all power policy communication between your driver and the rest of the driver stack. For example, your driver does not have to request the bus driver to change the device's power state, because the framework makes the request.

-   If your driver registers power policy event callback functions, the framework calls them when it is time to enable or disable the device's ability to wake itself from a low-power state.

-   If your driver allows users to modify idle and wake settings, the framework provides a user interface in the form of a property sheet page that Device Manager displays.

For more information about the power policy owner's responsibilities, see the following topics:

-   [Supporting Idle Power-Down](supporting-idle-power-down.md)
-   [Supporting System Wake-Up](supporting-system-wake-up.md)
-   [User Control of Device Idle and Wake Behavior](user-control-of-device-idle-and-wake-behavior.md)
-   [Supporting Functional Power States](supporting-functional-power-states.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Power%20Policy%20Ownership%20%20RELEASE:%20%283/25/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




