---
title: Windows Kernel-Mode Memory Manager
author: windows-driver-content
description: Windows Kernel-Mode Memory Manager
MS-HAID:
- 'memanager\_bd6f26d2-d0b4-464f-98e6-fc70e3e713d4.xml'
- 'kernel.windows\_kernel\_mode\_memory\_manager'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: ab464d5b-7bad-494e-80cd-e32ca9e9fa8d
---

# Windows Kernel-Mode Memory Manager


The Windows kernel-mode memory manager component manages physical memory for the operating system. This memory is primarily in the form of random access memory (RAM).

The memory manager manages memory by performing the following major tasks:

-   Managing the allocation and deallocation of memory virtually and dynamically.

-   Supporting the concepts of memory-mapped files, shared memory, and copy-on-write.

For more detailed information about memory management for drivers, see [Memory Management for Windows Drivers](managing-memory-for-drivers.md).

Routines that provide a direct interface to the memory manager are usually prefixed with the letters "**Mm**"; for example, **MmGetPhysicalAddress**. For a list of memory manager routines, see [Memory Manager Routines](https://msdn.microsoft.com/library/windows/hardware/ff554435).

For lists of memory manager routines sorted by functionality, see [Memory Allocation and Buffer Management](https://msdn.microsoft.com/library/windows/hardware/ff554422).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Windows%20Kernel-Mode%20Memory%20Manager%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


