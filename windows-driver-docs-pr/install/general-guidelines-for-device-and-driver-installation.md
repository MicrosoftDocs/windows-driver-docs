---
title: General Guidelines for Device and Driver Installation
description: General Guidelines for Device and Driver Installation
ms.assetid: E62906AB-CE32-4b07-B7DB-F523FFE4E6C2
keywords:
- device installations WDK , general guidelines
- driver installations WDK , general guidelines
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# General Guidelines for Device and Driver Installation


The fundamental goal for device and driver installation on Windows operating systems is to make the process as easy as possible for the user. Your installation procedures and the components of your [driver packages](driver-packages.md) should work seamlessly with the operating system's [device installation components](https://msdn.microsoft.com/library/windows/hardware/ff541277).

To provide the best possible user experience, use the following guidelines to design and implement your installation procedures:

-   Do not automatically restart the system or require the user to do so, unless it is absolutely necessary.

-   Always use [INF files](inf-files.md) for device installation. Make sure that all INF files are well formed and use correct syntax.

-   Leave your INF files on the system after installation; do not delete them. The INF file is used not only when the device or driver is first installed, but also when the user requests a driver update through Device Manager.

-   Use one of the [System-Defined Device Setup Classes](https://msdn.microsoft.com/library/windows/hardware/ff553419). Do not define your own setup class unless there is a compelling reason to do so.

-   Do not make assumptions about the location, format, or meaning of registry keys or values. For more information about registry keys and trees, see [Registry Trees and Keys for Devices and Drivers](registry-trees-and-keys.md).

 

 





