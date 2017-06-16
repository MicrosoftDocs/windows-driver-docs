---
title: Making Drivers Pageable
author: windows-driver-content
description: Making Drivers Pageable
ms.assetid: 0b3c1e00-2416-4534-9934-bb05f91c7482
keywords: ["memory management WDK kernel , pageable drivers", "pageable drivers WDK kernel", "pageable drivers WDK kernel , about pageable drivers", "paged out drivers WDK kernel"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Making Drivers Pageable


## <a href="" id="ddk-making-drivers-pageable-kg"></a>


By default, the linker assigns names such as ".text" and ".data" to the code and data sections of a driver image file. When the driver is loaded, the I/O manager makes these sections nonpaged. A nonpaged section is always memory-resident.

A driver developer has the option to make designated parts of a driver pageable so that Windows can move these parts to the paging file when they are not in use. To make a code or data section pageable, the driver developer assigns a name that begins with "PAGE" to the section. The I/O manager checks the names of the sections when it loads a driver. If a section name begins with "PAGE", the I/O manager makes the section pageable.

Code that runs at IRQL &gt;= DISPATCH\_LEVEL must be memory-resident. That is, this code must be either in a nonpageable segment, or in a pageable segment that is locked in memory. If code that is running at IRQL &gt;= DISPATCH\_LEVEL causes a page fault, a bug check occurs. Drivers can use the [**PAGED\_CODE**](https://msdn.microsoft.com/library/windows/hardware/ff558773) macro to verify that pageable functions are called only at appropriate IRQLs.

If a code or data section is pageable, the driver can lock the section in memory by calling the [**MmLockPagableCodeSection**](https://msdn.microsoft.com/library/windows/hardware/ff554601) or [**MmLockPagableDataSection**](https://msdn.microsoft.com/library/windows/hardware/ff554607) routine. The section remains locked until the driver calls the [**MmUnlockPagableImageSection**](https://msdn.microsoft.com/library/windows/hardware/ff556377) routine to unlock it. While the pageable section is locked, it behaves the same as a nonpaged section.

For information about how to assign names to code and data sections, see [**MmLockPagableCodeSection**](https://msdn.microsoft.com/library/windows/hardware/ff554601) and [**MmLockPagableDataSection**](https://msdn.microsoft.com/library/windows/hardware/ff554607).

This section includes the following topics:

[When Should Code and Data Be Pageable?](when-should-code-and-data-be-pageable-.md)

[Making Driver Code or Data Pageable](making-driver-code-or-data-pageable.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Making%20Drivers%20Pageable%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


