---
title: General Guidelines for Device and Driver Installation
description: General Guidelines for Device and Driver Installation
ms.assetid: E62906AB-CE32-4b07-B7DB-F523FFE4E6C2
keywords: ["device installations WDK , general guidelines", "driver installations WDK , general guidelines"]
---

# General Guidelines for Device and Driver Installation


The fundamental goal for device and driver installation on Windows operating systems is to make the process as easy as possible for the user. Your installation procedures and the components of your [driver packages](driver-packages.md) should work seamlessly with the operating system's [device installation components](https://msdn.microsoft.com/library/windows/hardware/ff541277).

To provide the best possible user experience, use the following guidelines to design and implement your installation procedures:

-   Do not automatically restart the system or require the user to do so, unless it is absolutely necessary.

-   Always use [INF files](inf-files.md) for device installation. Make sure that all INF files are well formed and use correct syntax.

-   Leave your INF files on the system after installation; do not delete them. The INF file is used not only when the device or driver is first installed, but also when the user requests a driver update through Device Manager.

-   Use one of the [System-Defined Device Setup Classes](https://msdn.microsoft.com/library/windows/hardware/ff553419). Do not define your own setup class unless there is a compelling reason to do so.

-   Do not make assumptions about the location, format, or meaning of registry keys or values. For more information about registry keys and trees, see [Registry Trees and Keys for Devices and Drivers](registry-trees-and-keys.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20General%20Guidelines%20for%20Device%20and%20Driver%20Installation%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




