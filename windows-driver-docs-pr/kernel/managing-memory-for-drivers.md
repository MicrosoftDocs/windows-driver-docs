---
title: Memory Management for Windows Drivers
description: Kernel-mode drivers allocate memory for purposes such as storing internal data, buffering data during I/O operations, and sharing memory with other kernel-mode and user-mode components.
ms.assetid: e030a37c-26ab-4177-9980-4336928975e1
keywords: ["memory management WDK kernel", "available space WDK kernel", "free space WDK kernel", "space WDK See memory WDK"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Memory Management for Windows Drivers


Kernel-mode drivers allocate memory for purposes such as storing internal data, buffering data during I/O operations, and sharing memory with other kernel-mode and user-mode components. Driver developers should understand memory management in Windows so that they use allocated memory correctly and efficiently. Windows manages virtual and physical memory, and divides memory into separate user and system address spaces. A driver can specify whether allocated memory supports capabilities such as demand paging, data caching, and instruction execution.




The *memory manager* is the kernel component that performs the memory management operations in Windows. For more information, see [Windows Kernel-Mode Memory Manager](windows-kernel-mode-memory-manager.md).

The memory manager implements a number of kernel-mode support routines that drivers call to allocate and manage memory. For more information, see [Memory Allocation and Buffer Management](https://msdn.microsoft.com/library/windows/hardware/ff554422).

The memory-management capabilities of kernel-mode drivers are different from those of user-mode applications. For more information about memory management for applications, see [Memory Management](https://msdn.microsoft.com/library/windows/desktop/aa366779).

## In this section


-   [Overview of Windows Memory Space](overview-of-windows-memory-space.md)
-   [Allocating System-Space Memory](allocating-system-space-memory.md)
-   [Map Registers](map-registers.md)
-   [Mapping Bus-Relative Addresses to Virtual Addresses](mapping-bus-relative-addresses-to-virtual-addresses.md)
-   [Using the Kernel Stack](using-the-kernel-stack.md)
-   [Using Lookaside Lists](using-lookaside-lists.md)
-   [Making Drivers Pageable](making-drivers-pageable.md)
-   [Accessing Read-Only System Memory](accessing-read-only-system-memory.md)
-   [Accessing User-Space Memory](accessing-user-space-memory.md)
-   [No-Execute (NX) Nonpaged Pool](no-execute-nonpaged-pool.md)
-   [Section Objects and Views](section-objects-and-views.md)
-   [Using MDLs](using-mdls.md)

 

 




