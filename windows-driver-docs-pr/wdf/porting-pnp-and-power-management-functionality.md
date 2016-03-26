---
title: Porting PnP and Power Management
description: Porting PnP and Power Management
ms.assetid: 29ADD3CF-7CDE-4D97-8082-76B4F94DB6A2
---

# Porting PnP and Power Management


WDF implements intelligent defaults for Plug and Play (PnP) and power management, so simple drivers (including most filter drivers) do not require additional code to meet the basic requirements for PnP. The framework automatically creates and manages PnP, power management, and power policy state machines. By default:

-   The FDO owns power policy for the device.
-   Only the [*EvtDriverDeviceAdd*](https://msdn.microsoft.com/library/windows/hardware/ff541693) callback is required; all other PnP and power management callbacks are optional. A driver implements other callbacks to support device-specific features.
-   The framework implements power management for all WDFQUEUE objects, so that by default requests are dispatched from the queue to the driver’s I/O event callbacks only when the device hardware is available (that is, in the D0 state).

If the device does not support interrupts or map memory, or require initialization or deinitialization when power transitions occur, the WDF driver requires only the [*EvtDriverDeviceAdd*](https://msdn.microsoft.com/library/windows/hardware/ff541693) callback.
When a device is inserted or removed, the framework invokes PnP and power event callbacks in a defined order. The topics in this section describe the order, which varies slightly for PDOs, FDOs, and filter DOs:

[Power-Up Sequence for a Function or Filter Device Object](power-up-sequence-for-a-function-or-filter-driver.md)
[Power-Up Sequence for a Physical Device Object](power-up-sequence-for-a-bus-driver.md)
[Power-Down and Removal Sequence for a Function or Filter Device Object](power-down-and-removal-sequence-for-a-function-or-filter-driver.md)
[Power-Down and Removal Sequence for a Physical Device Object](power-down-and-removal-sequence-for-a-bus-driver.md)
[Surprise-Removal Sequence](surprise-removal-sequence.md)
For a complete list of the callbacks that correspond to each minor PnP and power IRP code, see [WDM IRPs and WDF Event Callback Functions](wdm-irps-and-kmdf-event-callback-functions.md).

For more information about supporting PnP and power management in a framework-based driver, see the following topics:

[Supporting PnP and Power Management in Your Driver](supporting-pnp-and-power-management-in-your-driver.md)
[Power Policy Ownership](power-policy-ownership.md)
 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Porting%20PnP%20and%20Power%20Management%20%20RELEASE:%20%283/24/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




