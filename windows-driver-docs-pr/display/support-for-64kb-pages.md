---
title: Support for 64KB pages
description: WDDM 2.0+ support for 64 KB pages
ms.date: 03/15/2023
---

# Support for 64KB pages

Starting with WDDM 2.0 (Windows Display Driver Model), WDDM provides two types of leaf page tables to support 64KB pages:

- A leaf page table that supports 4 KB page table entries (PTEs).
- A leaf page table that supports 64 PTEs.

Both PTE sizes cover the same virtual address range, so a page table for 4KB pages has 16 times the number of entries as the 64 KB page table.

The size of a 64 KB page table is defined by [**DXGK_GPUMMUCAPS**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_gpummucaps)::**LeafPageTableSizeFor64KPagesInBytes**.

The [*UpdatePageTable*](dxgkddiupdatepagetable.md) operation has a **DXGK_UPDATEPAGETABLEFLAGS**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_updatepagetableflags)::**Use64KBPages** flag that indicates the type of the page table to be updated.

There are two modes of operations that are supported by WDDM 2.0+:

1. The PTEs of the level 1 page table point either to 4 KB page table or 64 KB page table.
2. The PTEs of the level 1 page table point to a 4 KB page table and a 64 KB page table at the same time. This is called "dual PTE" mode. Dual PTE support is expressed by the [**DXGK_GPUMMUCAPS**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_gpummucaps)::**DualPteSupported** cap.

The video memory manager chooses the page size based on the allocation alignment, graphics processing unit (GPU) memory segment properties, and the GPU memory segment type. It maps an allocation using 64 KB pages if its alignment and the size are a multiple of 64 KB and it is resident in a memory segment that supports 64 KB pages.

## Single PTE mode

In this mode the PTEs of the level 1 page table point either to a 4 KB page table or a 64 KB page table.

The [**DXGK_PTE**](/windows-hardware/drivers/ddi/d3dukmdt/ns-d3dukmdt-_dxgk_pte)::**PageTablePageSize** field is added to **DXGK_PTE**. It should be used only for PTEs of the level 1 page table (page directory in the old terminology). This field tells the kernel-mode driver the type of the corresponding page table (using 64KB or 4KB pages).

The video memory manager chooses to use a 64 KB page table for a virtual address range when:

- Only 64 KB aligned allocations are mapped to the range.
- The memory segments of all allocations mapped to the range support 64 KB pages.

When a virtual address range is mapped by 64 KB pages and the above conditions are no longer valid (for example, an allocation is committed to the system memory segment), the video memory manager switches from the 64 KB page table to the 4 KB page table.

When a page table has only 64 KB PTEs and a PTE needs to point to 4KB page (for example, an allocation is placed in system memory), the page table will be converted to use 4 KB PTEs.

The conversion is done as follows:

1. All contexts of the process are suspended.
2. Existing PTEs are updated to point to 4KB pages. The driver will get the [*UpdatePageTable*](./dxgkddiupdatepagetable.md) paging operation.
3. The level 1 PTE that points to the page table will be updated to reflect the new page size (**PageTablePageSize** = **DXGK_PTE_PAGE_TABLE_PAGE_4KB**). The driver will get the [*UpdatePageTable*](./dxgkddiupdatepagetable.md) paging operation.
4. All contexts of the process are resumed.

There is no conversion from a page table with 4KB PTEs to a page table with 64KB PTEs.

To prevent frequent switches between different page table sizes, the driver should pack small allocations together.

## Dual PTE mode

In this mode the PTEs of the level 1 page table might point to a 4 KB page table and a 64 KB page table at the same time.

Both pointers in the entries of the level 1 page table might have the **Valid** flag set, but the entries in the level 0 page table that cover the same 64 KB virtual address range can't be valid at the same time.

When an allocation that is covered by a 64 KB PTE is placed to a memory segment with 64 KB page size, the 64 KB PTE becomes invalid and the corresponding 4 KB PTEs become valid.

In the following diagram a 4 KB allocation and a 64 KB aligned allocation are in the same virtual address range covered by a level 0 page table and in a segment that supports 64 KB pages.

:::image type="content" source="images/support-for-64kb-pages.1.png" alt-text="Diagram showing dual PTE mode with 4KB and 64KB aligned allocations in the same virtual address range.":::
