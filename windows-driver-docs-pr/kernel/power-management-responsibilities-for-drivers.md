---
title: Power Management Responsibilities for Drivers
author: windows-driver-content
description: Power Management Responsibilities for Drivers
MS-HAID:
- 'PwrMgmt\_c90fbeea-d906-4dcd-b1ea-b786f9a3beaf.xml'
- 'kernel.power\_management\_responsibilities\_for\_drivers'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: c42a5b95-76f3-4975-b452-4858bbbe532e
keywords: ["power management WDK kernel , driver responsibilities", "driver power responsibilities WDk kernel", "conserving power WDK kernel", "power management WDK kernel , power states", "power states WDK kernel", "states WDK power management", "system power states WDK kernel , power management", "device power states WDK kernel"]
---

# Power Management Responsibilities for Drivers


## <a href="" id="ddk-power-management-responsibilities-for-drivers-kg"></a>


Drivers that support power management are responsible for:

[Reporting device power capabilities](reporting-device-power-capabilities.md) during PnP enumeration.

[Setting device object flags for power management](setting-device-object-flags-for-power-management.md).

[Handling power IRPs](handling-power-irps.md) sent by the power manager or a driver.

[Powering up a device](powering-up-a-device.md) as soon as needed after system start-up or idle shutdown.

[Powering down a device](powering-down-a-device.md) at system shutdown time or putting it to sleep when idle.

[Enabling device wake-up](enabling-device-wake-up.md), if the device supports wake-up capabilities.

[Managing device performance states](managing-device-performance-states.md), if the device supports decreasing performance or features to reduce power consumption.

Not every driver in every device stack performs all of these tasks. Typically, the bus driver reports capabilities, sets flags, and manipulates the physical device, and the device power policy manager (usually the function driver) issues requests to put the device to sleep and to enable wake-up.

With few exceptions, drivers power on and power off their devices, and they enable devices for wake-up in response to power IRPs, that is, IRPs with the major code [**IRP\_MJ\_POWER**](https://msdn.microsoft.com/library/windows/hardware/ff550784). Power IRPs can be sent by the power manager and, in some cases, by a driver.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Power%20Management%20Responsibilities%20for%20Drivers%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


