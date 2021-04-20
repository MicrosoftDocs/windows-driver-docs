---
title: Windows Kernel-Mode Kernel Library
description: Windows Kernel-Mode Kernel Library
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# Windows Kernel-Mode Kernel Library

The *kernel* of an operating system implements the core functionality that everything else in the operating system depends upon. The Microsoft Windows kernel provides basic low-level operations such as scheduling threads or routing hardware interrupts. It is the heart of the operating system and all tasks it performs must be fast and simple.

Routines that provide a direct interface to the kernel library are usually prefixed with "**Ke**", for example, **KeGetCurrentThread**. For a list of kernel library routines, see [Kernel Library Support Routines](/windows-hardware/drivers/ddi/_kernel/#core-kernel-library-support-routines).

>[!NOTE]
>The term *microkernel* does not apply to the current kernel used in the Windows operating system.
