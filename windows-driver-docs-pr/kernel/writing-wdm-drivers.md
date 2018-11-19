---
title: Writing WDM Drivers
description: Writing WDM Drivers
ms.assetid: 379305f0-3caa-4c8d-add5-17e8c83f2429
ms.localizationpriority: medium
ms.date: 10/17/2018
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

 

 

 




