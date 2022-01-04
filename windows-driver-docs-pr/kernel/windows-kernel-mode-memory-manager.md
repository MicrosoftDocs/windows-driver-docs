---
title: Windows Kernel-Mode Memory Manager
description: Windows Kernel-Mode Memory Manager
ms.date: 10/17/2018
---

# Windows Kernel-Mode Memory Manager


The Windows kernel-mode memory manager component manages physical memory for the operating system. This memory is primarily in the form of random access memory (RAM).

The memory manager manages memory by performing the following major tasks:

-   Managing the allocation and deallocation of memory virtually and dynamically.

-   Supporting the concepts of memory-mapped files, shared memory, and copy-on-write.

For more detailed information about memory management for drivers, see [Memory Management for Windows Drivers](managing-memory-for-drivers.md).

Routines that provide a direct interface to the memory manager are usually prefixed with the letters "**Mm**"; for example, **MmGetPhysicalAddress**. To find documentation on memory manager routines, navigate to [**MmAdvanceMdl**](/windows-hardware/drivers/ddi/wdm/nf-wdm-mmadvancemdl) and use the Table of Contents on the left to scroll through the Mm* routines.

For lists of memory manager routines sorted by functionality, see [Memory Allocation and Buffer Management](/windows-hardware/drivers/ddi/_kernel/#memory-allocation-and-buffer-management).

 

