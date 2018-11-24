---
title: Porting PnP and Power Management
description: Porting PnP and Power Management
ms.assetid: 29ADD3CF-7CDE-4D97-8082-76B4F94DB6A2
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Porting PnP and Power Management


WDF implements intelligent defaults for Plug and Play (PnP) and power management, so simple drivers (including most filter drivers) do not require additional code to meet the basic requirements for PnP. The framework automatically creates and manages PnP, power management, and power policy state machines. By default:

-   The FDO owns power policy for the device.
-   Only the [*EvtDriverDeviceAdd*](https://msdn.microsoft.com/library/windows/hardware/ff541693) callback is required; all other PnP and power management callbacks are optional. A driver implements other callbacks to support device-specific features.
-   The framework implements power management for all WDFQUEUE objects, so that by default requests are dispatched from the queue to the driver’s I/O event callbacks only when the device hardware is available (that is, in the D0 state).

If the device does not support interrupts or map memory, or require initialization or deinitialization when power transitions occur, the WDF driver requires only the [*EvtDriverDeviceAdd*](https://msdn.microsoft.com/library/windows/hardware/ff541693) callback.
When a device is inserted or removed, the framework invokes PnP and power event callbacks in a defined order. The topics in this section describe the order, which varies slightly for PDOs, FDOs, and filter DOs:

-   [Power-Up Sequence for a Function or Filter Device Object](power-up-sequence-for-a-function-or-filter-driver.md)
-   [Power-Up Sequence for a Physical Device Object](power-up-sequence-for-a-bus-driver.md)
-   [Power-Down and Removal Sequence for a Function or Filter Device Object](power-down-and-removal-sequence-for-a-function-or-filter-driver.md)
-   [Power-Down and Removal Sequence for a Physical Device Object](power-down-and-removal-sequence-for-a-bus-driver.md)
-   [Surprise-Removal Sequence](surprise-removal-sequence.md)

For a complete list of the callbacks that correspond to each minor PnP and power IRP code, see [WDM IRPs and WDF Event Callback Functions](wdm-irps-and-kmdf-event-callback-functions.md).

For more information about supporting PnP and power management in a framework-based driver, see the following topics:

-   [Supporting PnP and Power Management in Your Driver](supporting-pnp-and-power-management-in-your-driver.md)
-   [Power Policy Ownership](power-policy-ownership.md)

 

 





