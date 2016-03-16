---
title: Enumerating the Devices on a Bus
description: Enumerating the Devices on a Bus
ms.assetid: 5731db82-2bc8-4a8d-98f1-3977845f572c
keywords: ["PnP WDK KMDF bus enumeration", "Plug and Play WDK KMDF bus enumeration", "bus enumeration WDK KMDF", "enumeration WDK KMDF", "child devices WDK KMDF", "listing child devices WDK KMDF"]
---

# Enumerating the Devices on a Bus


*Bus enumeration* is the act of determining which child devices are connected to a parent device. A parent device is typically a bus adapter, but it can also be a device that supports multiple functions, such as a sound card, for which each function requires a separate set of drivers.

Kernel-Mode Driver Framework (KMDF) supports two types of bus enumeration:

-   [Static enumeration](static-enumeration.md), which is easy to implement and is ideal if the number and type of child devices is not system-specific and does not change after the hardware has been plugged in.

-   [Dynamic enumeration](dynamic-enumeration.md), which should be used if the number or type of child devices changes from one computer to another.

A bus driver can use either or both types of bus enumeration.

For more information about writing a KMDF bus driver, see [Bus Driver Development Based on KMDF](http://msdn.microsoft.com/windows/hardware/gg463281).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Enumerating%20the%20Devices%20on%20a%20Bus%20%20RELEASE:%20%283/16/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




