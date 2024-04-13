---
title: Bug Check 0xDA SYSTEM_PTE_MISUSE
description: The SYSTEM_PTE_MISUSE bug check has a value of 0x000000DA. This indicates that a page table entry (PTE) routine has been used in an improper way.
keywords: ["Bug Check 0xDA SYSTEM_PTE_MISUSE", "SYSTEM_PTE_MISUSE"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- SYSTEM_PTE_MISUSE
api_type:
- NA
---

# Bug Check 0xDA: SYSTEM\_PTE\_MISUSE


The SYSTEM\_PTE\_MISUSE bug check has a value of 0x000000DA. This indicates that a page table entry (PTE) routine has been used in an improper way.

> [!IMPORTANT]
> This article is for programmers. If you're a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).


## SYSTEM\_PTE\_MISUSE Parameters


Parameter 1 indicates the type of violation. The meaning of the other parameters depends on the value of Parameter 1.

<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Parameter 1</th>
<th align="left">Parameter 2</th>
<th align="left">Parameter 3</th>
<th align="left">Parameter 4</th>
<th align="left">Cause of Error</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>0x01</p></td>
<td align="left"><p>The address of the internal lock tracking structure</p></td>
<td align="left"><p>The address of the memory descriptor list</p></td>
<td align="left"><p>The address of the duplicate internal lock tracking structure</p></td>
<td align="left"><p>The mapping being freed is a duplicate.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x02</p></td>
<td align="left"><p>The address of the internal lock tracking structure</p></td>
<td align="left"><p>The number of mappings that the system expects to free</p></td>
<td align="left"><p>The number of mappings that the driver is requesting to free</p></td>
<td align="left"><p>The number of mappings being freed is incorrect.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x03</p></td>
<td align="left"><p>The address of the first internal tracking structure found</p></td>
<td align="left"><p>The mapping address that the system expects to free</p></td>
<td align="left"><p>The mapping address that the driver is requesting to free</p></td>
<td align="left"><p>The mapping address being freed is incorrect.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x04</p></td>
<td align="left"><p>The address of the internal lock tracking structure</p></td>
<td align="left"><p>The page frame number that the system expects should be first in the MDL</p></td>
<td align="left"><p>The page frame number that is currently first in the MDL</p></td>
<td align="left"><p>The first page of the mapped MDL has changed since the MDL was mapped.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x05</p></td>
<td align="left"><p>The address of the first internal tracking structure found</p></td>
<td align="left"><p>The virtual address that the system expects to free</p></td>
<td align="left"><p>The virtual address that the driver is requesting to free</p></td>
<td align="left"><p>The start virtual address in the MDL being freed has changed since the MDL was mapped.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x06</p></td>
<td align="left"><p>The MDL specified by the driver</p></td>
<td align="left"><p>The virtual address specified by the driver</p></td>
<td align="left"><p>The number of mappings to free (specified by the driver)</p></td>
<td align="left"><p>The MDL being freed was never (or is currently not) mapped.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x07</p></td>
<td align="left"><p>The initial mapping</p></td>
<td align="left"><p>The number of mappings</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>(Windows 2000 only) The mapping range is being double-allocated.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x08</p></td>
<td align="left"><p>The initial mapping</p></td>
<td align="left"><p>The number of mappings the caller is freeing</p></td>
<td align="left"><p>The number of mappings the system thinks should be freed</p></td>
<td align="left"><p>(Windows 2000 only) The caller is asking to free an incorrect number of mappings.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x09</p></td>
<td align="left"><p>The initial mapping</p></td>
<td align="left"><p>The number of mappings that the caller is freeing</p></td>
<td align="left"><p>The mapping index that the system thinks is already free</p></td>
<td align="left"><p>(Windows 2000 only) The caller is asking to free several mappings, but at least one of them is not allocated.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x0A</p></td>
<td align="left"><p><strong>1:</strong> The driver requested "bug check on failure" in the MDL.</p>
<p><strong>0:</strong> The driver did not request "bug check on failure" in the MDL.</p></td>
<td align="left"><p>The number of mappings that the caller is allocating</p></td>
<td align="left"><p>The type of mapping pool requested</p></td>
<td align="left"><p>(Windows 2000 only) The caller is asking to allocate zero mappings.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x0B</p></td>
<td align="left"><p>The corrupt mapping</p></td>
<td align="left"><p>The number of mappings that the caller is allocating</p></td>
<td align="left"><p>The type of mapping pool requested</p></td>
<td align="left"><p>(Windows 2000 only) The mapping list was already corrupt at the time of this allocation. The corrupt mapping is located below the lowest possible mapping address.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x0C</p></td>
<td align="left"><p>The corrupt mapping</p></td>
<td align="left"><p>The number of mappings that the caller is allocating</p></td>
<td align="left"><p>The type of mapping pool requested</p></td>
<td align="left"><p>(Windows 2000 only) The mapping list was already corrupt at the time of this allocation. The corrupt mapping is located above the lowest possible mapping address.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x0D</p></td>
<td align="left"><p>The initial mapping</p></td>
<td align="left"><p>The number of mappings that the caller is freeing</p></td>
<td align="left"><p>The type of mapping pool</p></td>
<td align="left"><p>(Windows 2000 only) The caller is trying to free zero mappings.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x0E</p></td>
<td align="left"><p>The initial mapping</p></td>
<td align="left"><p>The number of mappings that the caller is freeing</p></td>
<td align="left"><p>The type of mapping pool</p></td>
<td align="left"><p>(Windows 2000 only) The caller is trying to free mappings, but the guard mapping has been overwritten.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x0F</p></td>
<td align="left"><p>The non-existent mapping</p></td>
<td align="left"><p>The number of mappings that the caller is trying to free</p></td>
<td align="left"><p>The type of mapping pool being freed</p></td>
<td align="left"><p>(Windows 2000 only) The caller is trying to free a non-existent mapping. The non-existent mapping is located below the lowest possible mapping address.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x10</p></td>
<td align="left"><p>The non-existent mapping</p></td>
<td align="left"><p>The number of mappings the caller is trying to free</p></td>
<td align="left"><p>The type of mapping pool being freed</p></td>
<td align="left"><p>(Windows 2000 only) The caller is trying to free a non-existent mapping. The non-existent mapping is located above the highest possible mapping address.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x11</p></td>
<td align="left"><p>The non-existent mapping</p></td>
<td align="left"><p>The number of mappings that the caller is trying to free</p></td>
<td align="left"><p>The type of mapping pool being freed</p></td>
<td align="left"><p>(Windows 2000 only) The caller is trying to free a non-existent mapping. The non-existent mapping is at the base of the mapping address space.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x100</p></td>
<td align="left"><p>The number of mappings being requested</p></td>
<td align="left"><p>The caller's identifying tag</p></td>
<td align="left"><p>The address of the routine that called the caller of this routine</p></td>
<td align="left"><p> The caller requested 0 mappings.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x101</p></td>
<td align="left"><p>The first mapping address</p></td>
<td align="left"><p>The caller's identifying tag</p></td>
<td align="left"><p>The owner's identifying tag</p></td>
<td align="left"><p> A caller is trying to free a mapping address range that it does not own.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x102</p></td>
<td align="left"><p>The first mapping address</p></td>
<td align="left"><p>The caller's identifying tag</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>The mapping address space that the caller is trying to free is apparently empty.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x103</p></td>
<td align="left"><p>The address of the invalid mapping</p></td>
<td align="left"><p>The caller's identifying tag</p></td>
<td align="left"><p>The number of mappings in the mapping address space</p></td>
<td align="left"><p>The mapping address space that the caller is trying to free is still reserved. <strong><a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-mmunmapreservedmapping" data-raw-source="[MmUnmapReservedMapping](/windows-hardware/drivers/ddi/wdm/nf-wdm-mmunmapreservedmapping)">MmUnmapReservedMapping</a></strong></p>
<p>must be called before <strong><a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-mmfreemappingaddress" data-raw-source="[MmFreeMappingAddress](/windows-hardware/drivers/ddi/wdm/nf-wdm-mmfreemappingaddress)">MmFreeMappingAddress</a></strong>.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x104</p></td>
<td align="left"><p>The first mapping address</p></td>
<td align="left"><p>The caller's identifying tag</p></td>
<td align="left"><p>The owner's identifying tag</p></td>
<td align="left"><p>The caller is attempting to map an MDL to a mapping address space that it does not own.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x105</p></td>
<td align="left"><p>The first mapping address</p></td>
<td align="left"><p>The caller's identifying tag</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>The caller is attempting to map an MDL to an invalid mapping address space. The caller has mostly likely specified an invalid address.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x107</p></td>
<td align="left"><p>The first mapping address</p></td>
<td align="left"><p>The address of the non-empty mapping</p></td>
<td align="left"><p>The last mapping address</p></td>
<td align="left"><p>The caller is attempting to map an MDL to a mapping address space that has not been properly reserved. The caller should have called <strong><a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-mmunmapreservedmapping" data-raw-source="[MmUnmapReservedMapping](/windows-hardware/drivers/ddi/wdm/nf-wdm-mmunmapreservedmapping)">MmUnmapReservedMapping</a></strong> prior to calling <strong><a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-mmmaplockedpageswithreservedmapping" data-raw-source="[MmMapLockedPagesWithReservedMapping](/windows-hardware/drivers/ddi/wdm/nf-wdm-mmmaplockedpageswithreservedmapping)">MmMapLockedPagesWithReservedMapping</a></strong></p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x108</p></td>
<td align="left"><p>The first mapping address</p></td>
<td align="left"><p>The caller's identifying tag</p></td>
<td align="left"><p>The owner's identifying tag</p></td>
<td align="left"><p>The caller is attempting to unmap a locked mapping address space that it does not own.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x109</p></td>
<td align="left"><p>The first mapping address</p></td>
<td align="left"><p>The caller's identifying tag</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>The caller is attempting to unmap a locked virtual address space that is apparently empty.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x10A</p></td>
<td align="left"><p>The first mapping address</p></td>
<td align="left"><p>The number of mappings in the locked mapping address space</p></td>
<td align="left"><p>The number of mappings to unmap</p></td>
<td align="left"><p>The caller is attempting to unmap more mappings than actually exist in the locked mapping address space.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x10B</p></td>
<td align="left"><p>The first mapping address</p></td>
<td align="left"><p>The caller's identifying tag</p></td>
<td align="left"><p>The number of mappings to unmap</p></td>
<td align="left"><p>The caller is attempting to unmap a portion of a locked virtual address space that is not currently mapped.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x10C</p></td>
<td align="left"><p>The first mapping address</p></td>
<td align="left"><p>The caller's identifying tag</p></td>
<td align="left"><p>The number of mappings to unmap</p></td>
<td align="left"><p>The caller is not unmapping the entirety of the locked mapping address space.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x200</p></td>
<td align="left"><p>The first mapping address</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>The caller is attempting to reserve a mapping address space that contains no mappings.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x201</p>
<p>0x202</p></td>
<td align="left"><p>The first mapping address to reserve</p></td>
<td align="left"><p>The address of the mapping that has already been reserved</p></td>
<td align="left"><p>The number of mappings to reserve</p></td>
<td align="left"><p>One of the mappings that the caller is attempting to reserve has already been reserved.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x300</p></td>
<td align="left"><p>The first mapping address to release</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>The caller is attempting to release a mapping address space that contains no mappings.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x301</p></td>
<td align="left"><p>The address of the mapping</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>The caller is attempting to release a mapping that it is not permitted to release.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x302</p></td>
<td align="left"><p>The address that the caller is trying to release.</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>The caller is attempting to release a system address that is not currently mapped.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x303</p></td>
<td align="left"><p>The first mapping address</p></td>
<td align="left"><p>The number of mappings to release</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>The caller is attempting to release a mapping address range that was not reserved.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x304</p></td>
<td align="left"><p>The first mapping address</p></td>
<td align="left"><p>The number of mappings to release</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>The caller is attempting to release a mapping address range that begins in the middle of a different allocation.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x305</p></td>
<td align="left"><p>The first mapping address</p></td>
<td align="left"><p>The number of mappings that the caller is trying to release</p></td>
<td align="left"><p>The number of mappings that should be released</p></td>
<td align="left"><p>The caller is attempting to release the wrong number of mappings.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x306</p></td>
<td align="left"><p>The first mapping address</p></td>
<td align="left"><p>The free mapping address</p></td>
<td align="left"><p>The number of mappings to release</p></td>
<td align="left"><p>One of the mappings that the caller is attempting to release is already free.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x400</p></td>
<td align="left"><p>The base address of the I/O space mapping</p></td>
<td align="left"><p>The number of pages to be freed</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>The caller is trying to free an I/O space mapping that the system is unaware of.</p></td>
</tr>
</tbody>
</table>

 

## Cause

The error is indicated by the value of Parameter 1.

A stack trace will identify the driver that caused the error.

