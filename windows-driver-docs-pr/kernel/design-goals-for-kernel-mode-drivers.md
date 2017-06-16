---
title: Design Goals for Kernel-Mode Drivers
author: windows-driver-content
description: Design Goals for Kernel-Mode Drivers
ms.assetid: 2799556e-0359-4388-acf3-74d90eb86a0f
keywords: ["kernel-mode drivers WDK , design goals"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Design Goals for Kernel-Mode Drivers


## <a href="" id="ddk-design-goals-for-kernel-mode-drivers-kg"></a>


Kernel-mode drivers share many of the design goals of the operating system, particularly those of the system I/O manager. Kernel-mode drivers are designed to be:

-   [Portable](portable.md) from one platform to another.

-   [Configurable](configurable.md) to various hardware and software platforms.

-   [Always preemptible and always interruptible](always-preemptible-and-always-interruptible.md).

-   [Multiprocessor-safe](multiprocessor-safe.md) on multiprocessor platforms.

-   [Object-based](object-based.md).

-   [Packet-driven I/O with reusable IRPs](packet-driven-i-o-with-reusable-irps.md).

-   Capable of [supporting asynchronous I/O](supporting-asynchronous-i-o.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Design%20Goals%20for%20Kernel-Mode%20Drivers%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


