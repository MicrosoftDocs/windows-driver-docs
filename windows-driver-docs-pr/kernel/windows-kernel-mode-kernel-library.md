---
title: Windows Kernel-Mode Kernel Library
description: Windows kernel-mode kernel library
ms.date: 05/08/2025
ms.topic: concept-article
---

# Windows kernel-mode kernel library

The *kernel* of an operating system implements the core functionality that everything else in the operating system depends upon. The Microsoft Windows kernel provides basic low-level operations such as scheduling threads or routing hardware interrupts. It's the heart of the operating system and all tasks it performs must be fast and simple.

Routines that provide a direct interface to the kernel library are usually prefixed with "**Ke**", for example, **KeGetCurrentThread**. For a list of kernel library routines, see [Kernel Library Support Routines](/windows-hardware/drivers/ddi/_kernel/#core-kernel-library-support-routines).

>[!NOTE]
>The term *microkernel* doesn't apply to the current kernel used in the Windows operating system.
