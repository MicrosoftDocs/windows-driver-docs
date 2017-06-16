---
title: Memory Management for Windows Drivers
author: windows-driver-content
description: Kernel-mode drivers allocate memory for purposes such as storing internal data, buffering data during I/O operations, and sharing memory with other kernel-mode and user-mode components.
ms.assetid: e030a37c-26ab-4177-9980-4336928975e1
keywords: ["memory management WDK kernel", "available space WDK kernel", "free space WDK kernel", "space WDK See memory WDK"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Memory Management for Windows Drivers


Kernel-mode drivers allocate memory for purposes such as storing internal data, buffering data during I/O operations, and sharing memory with other kernel-mode and user-mode components. Driver developers should understand memory management in Windows so that they use allocated memory correctly and efficiently. Windows manages virtual and physical memory, and divides memory into separate user and system address spaces. A driver can specify whether allocated memory supports capabilities such as demand paging, data caching, and instruction execution.

## <a href="" id="ddk-memory-management-kg"></a>


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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Memory%20Management%20for%20Windows%20Drivers%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


