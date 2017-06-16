---
title: Writing WDM Drivers
author: windows-driver-content
description: Writing WDM Drivers
ms.assetid: 379305f0-3caa-4c8d-add5-17e8c83f2429
---

# Writing WDM Drivers


This section discusses the Microsoft Windows Driver Model (WDM) architecture. This architecture started in Windows 2000 as an enhancement to previous Windows NT device drivers.

**Note**  Drivers for versions of Windows NT-based operating systems before Windows 2000 are not supported, and you should update these drivers. The WDM architecture does not support drivers for non-Windows NT-based operating systems (such as Windows 98), and you should rewrite such drivers.

 

This section is divided into three parts:

-   [Windows Driver Model](windows-driver-model.md) describes the Windows Driver Model (WDM), including types of WDM drivers, device configuration, and WDM versioning.

-   [Device Objects and Device Stacks](device-objects-and-device-stacks.md) describes device objects and device stacks. The section includes information about physical device objects (PDOs), functional device objects (FDOs), and filter device objects (filter DOs). Drivers are often built from a set of device objects that work together. This set of device objects is called a *stack*. Stacks can help you understand the flow of information to and from a driver and how different parts of the driver communicate internally.

-   [Kernel-Mode Driver Components](kernel-mode-driver-components.md) describes which routines you must implement to have a functional driver and which routines are optional.

    A *device driver* is a set of software code that must integrate into the operating system. To complete this integration, you must write a set of handler routines in your driver that process calls from the operating system. These routines can be simple function calls, but many of them implement the processing of *I/O request packets* (IRPs), which facilitate communication between drivers and the operating system.

**Note**  WDM drivers can also use the Windows Driver Frameworks (WDF) library to make some parts of a device driver easier to write. Specifically, kernel-mode drivers can use the Kernel-Mode Driver Framework (KMDF), which is part of WDF. For more information about KMDF for kernel-mode drivers, see [Kernel-Mode Driver Framework Overview](https://msdn.microsoft.com/library/windows/hardware/ff544296). Note that KMDF does not replace WDM. You must still understand many parts of WDM to write a KMDF driver.

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Writing%20WDM%20Drivers%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


