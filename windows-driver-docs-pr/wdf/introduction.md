---
title: Introduction
author: windows-driver-content
description: Introduction
ms.assetid: 9f6249ab-e0c4-4bb4-8759-632c479cae46
keywords: ["PnP WDK KMDF , about PnP in framework-based drivers", "Plug and Play WDK KMDF , about PnP in framework-based drivers", "power management WDK KMDF , about power management"]
---

# Introduction


Plug and Play (PnP) and power management operations must be performed individually for each device, so the kernel-mode Windows Driver Framework implements all PnP and power management interfaces in the framework device object.

When the system's PnP manager determines that a device is connected to the system, the framework calls your driver's [*EvtDriverDeviceAdd*](https://msdn.microsoft.com/library/windows/hardware/ff541693) callback function. This callback function must create a framework device object for the device.

To support PnP and power management, the framework device object defines:

-   A set of event callback functions that allow the driver to react to events, such as device removal or the device's transition in and out of its [working (D0) state](https://msdn.microsoft.com/library/windows/hardware/ff543210).

-   A set of object methods that allow the driver to report device-specific capabilities, such as the device's ability to enter a [low-power (sleeping) state](https://msdn.microsoft.com/library/windows/hardware/ff543186) when idle or the device's ability to wake itself, or the entire system, from a low-power state when an external event occurs.

The framework handles many PnP and power activities for you, so your driver does not have to contain the code to support them. For example, when the system is about to enter a low-power state, the framework handles the I/O requests that must travel through the driver stack to set the system's devices to low power. Your driver never sees these requests and you do not have to write any code to handle them.

If you have written Microsoft Windows Driver Model (WDM) drivers in the past, you will probably find that there is little obvious correlation between the interfaces that framework-based drivers use and those that WDM drivers use. The interfaces differ because the framework hides and simplifies most of the PnP and power management interfaces that WDM defines.

This documentation does not discuss similarities between the driver interfaces of Windows Driver Framework and the underlying WDM interfaces because you should be able to write a framework-based driver without understanding the WDM activity that occurs inside Windows Driver Framework.

 

 





