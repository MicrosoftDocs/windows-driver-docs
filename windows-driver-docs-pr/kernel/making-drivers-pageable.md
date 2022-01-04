---
title: Making Drivers Pageable
description: Making Drivers Pageable
keywords: ["memory management WDK kernel , pageable drivers", "pageable drivers WDK kernel", "pageable drivers WDK kernel , about pageable drivers", "paged out drivers WDK kernel"]
ms.date: 06/16/2017
---

# Making Drivers Pageable





By default, the linker assigns names such as ".text" and ".data" to the code and data sections of a driver image file. When the driver is loaded, the I/O manager makes these sections nonpaged. A nonpaged section is always memory-resident.

A driver developer has the option to make designated parts of a driver pageable so that Windows can move these parts to the paging file when they are not in use. To make a code or data section pageable, the driver developer assigns a name that begins with "PAGE" to the section. The I/O manager checks the names of the sections when it loads a driver. If a section name begins with "PAGE", the I/O manager makes the section pageable.

Code that runs at IRQL &gt;= DISPATCH\_LEVEL must be memory-resident. That is, this code must be either in a nonpageable segment, or in a pageable segment that is locked in memory. If code that is running at IRQL &gt;= DISPATCH\_LEVEL causes a page fault, a bug check occurs. Drivers can use the [**PAGED_CODE**](./paged_code.md) macro to verify that pageable functions are called only at appropriate IRQLs.

If a code or data section is pageable, the driver can lock the section in memory by calling the [**MmLockPagableCodeSection**](/windows-hardware/drivers/ddi/wdm/nf-wdm-mmlockpagablecodesection) or [**MmLockPagableDataSection**](/windows-hardware/drivers/ddi/wdm/nf-wdm-mmlockpagabledatasection) routine. The section remains locked until the driver calls the [**MmUnlockPagableImageSection**](/windows-hardware/drivers/ddi/wdm/nf-wdm-mmunlockpagableimagesection) routine to unlock it. While the pageable section is locked, it behaves the same as a nonpaged section.

For information about how to assign names to code and data sections, see [**MmLockPagableCodeSection**](/windows-hardware/drivers/ddi/wdm/nf-wdm-mmlockpagablecodesection) and [**MmLockPagableDataSection**](/windows-hardware/drivers/ddi/wdm/nf-wdm-mmlockpagabledatasection).

This section includes the following topics:

[When Should Code and Data Be Pageable?](when-should-code-and-data-be-pageable-.md)

[Making Driver Code or Data Pageable](detecting-code-that-can-be-pageable.md)

