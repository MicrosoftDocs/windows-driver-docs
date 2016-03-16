---
title: Introduction
description: Introduction
ms.assetid: 9f6249ab-e0c4-4bb4-8759-632c479cae46
keywords: ["PnP WDK KMDF about PnP in framework based drivers", "Plug and Play WDK KMDF about PnP in framework based drivers", "power management WDK KMDF about power management"]
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Introduction%20%20RELEASE:%20%283/16/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




