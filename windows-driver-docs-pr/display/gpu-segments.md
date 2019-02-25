---
title: GPU segments
description: graphics processing unit (GPU) access to physical memory is abstracted in the device driver interface (DDI) by a segmentation model.
ms.assetid: E6CAD808-73C0-48AB-BF95-76911D5C104A
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# GPU segments


graphics processing unit (GPU) access to physical memory is abstracted in the device driver interface (DDI) by a segmentation model. The kernel mode driver expresses the physical memory resources available to a GPU by enumerating a set of segments, which are then managed by the video memory manager.

There are three types of segments in Windows Display Driver Model (WDDM) v2:

<span id="Memory_Segment"></span><span id="memory_segment"></span><span id="MEMORY_SEGMENT"></span>Memory Segment  
A memory segment represents memory, dedicated to a GPU. This may be VRAM on a discrete GPU or firmware/driver reserved memory on an integrated GPU. There can be multiple memory segments enumerated.

New in WDDM v2, a memory segment is managed as a pool of physical pages which are either 4KB or 64KB in size. Surface data is copied into and out of a memory segment using *Fill*/*Transfer*/*Discard*/*FillVirtuall*/*TransferVirtual* paging operations.

The CPU may access the content of a memory segment in one of two ways. First, a memory segment may be visible in the physical address space of the CPU, in which case the video memory manager simply maps CPU virtual addresses directly to allocations within the segment. New in WDDM v2, the video memory manager also supports accessing the content of a memory segment through a programmable CPU host aperture associated with that segment.

<span id="Aperture__Segment"></span><span id="aperture__segment"></span><span id="APERTURE__SEGMENT"></span>Aperture Segment  
An aperture segment is a global page table used to make discontinuous system memory pages appears contiguous from the perspective of a GPU engine.

In WDDM v2, a single aperture segment must be reported.

<span id="System_Memory_Segment"></span><span id="system_memory_segment"></span><span id="SYSTEM_MEMORY_SEGMENT"></span>System Memory Segment  
The system memory segment is an implicit segment representing system memory references (i.e. a guest physical address). The system memory segment is not directly enumerated by the kernel mode driver. It is implicitly enumerated by the video memory manager and always gets assigned `SegmentId==0`. To place an allocation in the system memory segment, the kernel mode driver needs to use the aperture segment ID.

## <span id="Physical_memory_reference"></span><span id="physical_memory_reference"></span><span id="PHYSICAL_MEMORY_REFERENCE"></span>Physical memory reference


In the DDI, physical memory references always take the form of a segment ID-segment offset pair.

## <span id="Accessing_allocations_by_physical_address"></span><span id="accessing_allocations_by_physical_address"></span><span id="ACCESSING_ALLOCATIONS_BY_PHYSICAL_ADDRESS"></span>Accessing allocations by physical address


GPU engines, which don't support GPU virtual addressing, need to access allocations through their physical addresses. This has implication on how an allocation gets assigned resources from a segment. Physical references imply that an allocation must be allocated either contiguously in a memory segment or occupy a contiguous range in the aperture segment.

To avoid unnecessary and expensive contiguous allocations, the kernel mode driver must explicitly identify allocations, which require to be accessed physically by a rendering engine, by setting the new [**DXGK\_ALLOCATIONINFOFLAGS2**](https://msdn.microsoft.com/library/windows/hardware/ff560970)::**AccessedPhysically** flag during allocation creation.

Such allocations will be mapped to the aperture segment when resident in system memory. The allocations will be contiguous when resident in a memory segment. Allocations, created this way, may be referenced through the allocation list on engines, operating in the physical addressing mode.

Allocations, which do not have this flags set, will be allocated as a set of pages in a memory segment or a set of pages in system memory, either of which are accessed through GPU virtual addresses. Allocations created this way cannot be referenced through the allocation list. Any command buffer submission referencing the allocation that way will be rejected.

Primary surfaces are understood to be accessed physically by the display controller and will be allocated contiguously in a memory segment or mapped into the aperture segment when displayed. The kernel mode driver should only set the **AccessedPhysically** flags when a rendering engine will access the allocation physically. The distinction between the implicit physical access on primary surface and the explicit flags is when the allocation will be mapped into the aperture. When the **AccessedPhysically** flags is set, the allocation will be mapped into the aperture whenever it is resident. Primary surfaces, which do not have this flags set, will be mapped into the aperture only when being displayed. This helps to remove pressure on the aperture segment, as typically there are only a few primary surface actively being displayed, while there may be a very large number of them existing and being rendered to (i.e. all *FlipEx* swapchains are created as primary and potentially displayable surfaces in *dFlip*/*iFlip* scenarios).

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"></td>
<td align="left">AccessedPhysically==0</td>
<td align="left">AccessedPhysically==1</td>
<td align="left">Primary &amp;&amp; AccessedPhysically==0</td>
</tr>
<tr class="even">
<td align="left">Memory Segment</td>
<td align="left"><p><strong>Set of pages</strong></p>
<p>Only GPU virtual access is allowed.</p></td>
<td align="left"><p><strong>Contiguous</strong></p>
<p>GPU physical access is allowed</p></td>
<td align="left"><p><strong>Contiguous</strong></p>
<p>Only GPU virtual access is allowed by rendering engines.</p></td>
</tr>
<tr class="odd">
<td align="left">Aperture Segment</td>
<td align="left"><p><strong>Not mapped</strong></p>
<p>System memory pages, only mapped by GPU page tables, not to the aperture segment.</p>
<p>Only GPU virtual access is allowed.</p></td>
<td align="left"><p><strong>Mapped when resident</strong></p>
<p>GPU physical access is allowed.</p></td>
<td align="left"><p><strong>Mapped when displayed</strong></p>
<p>Only GPU virtual access is allowed by rendering engines.</p></td>
</tr>
</tbody>
</table>

 

 

 





