---
title: GDI Memory Services
description: GDI Memory Services
keywords:
- GDI WDK Windows 2000 display , memory services
- graphics drivers WDK Windows 2000 display , memory services
- drawing WDK GDI , memory services
- memory WDK GDI
ms.date: 04/20/2017
---

# GDI Memory Services


## <span id="ddk_gdi_memory_services_gg"></span><span id="DDK_GDI_MEMORY_SERVICES_GG"></span>


GDI provides several memory-related services to driver writers, including the ability to allocate and deallocate system memory, user memory, private user memory, and video memory, as well as the ability to lock and unlock a range of memory. The following table lists the GDI memory services.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Function</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-engallocmem" data-raw-source="[&lt;strong&gt;EngAllocMem&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-engallocmem)"><strong>EngAllocMem</strong></a></p></td>
<td align="left"><p>Allocates a block of memory, and inserts a caller-supplied tag before the allocation.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-engallocprivateusermem" data-raw-source="[&lt;strong&gt;EngAllocPrivateUserMem&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-engallocprivateusermem)"><strong>EngAllocPrivateUserMem</strong></a></p></td>
<td align="left"><p>Allocates a block of private user memory from the address space of a specified process, and inserts a caller-supplied tag before the allocation.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-engallocusermem" data-raw-source="[&lt;strong&gt;EngAllocUserMem&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-engallocusermem)"><strong>EngAllocUserMem</strong></a></p></td>
<td align="left"><p>Allocates a block of memory from the address space of the current process, and inserts a caller-supplied tag before the allocation.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-engfreemem" data-raw-source="[&lt;strong&gt;EngFreeMem&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-engfreemem)"><strong>EngFreeMem</strong></a></p></td>
<td align="left"><p>Deallocates a block of system memory allocated by <a href="/windows/win32/api/winddi/nf-winddi-engallocmem" data-raw-source="[&lt;strong&gt;EngAllocMem&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-engallocmem)"><strong>EngAllocMem</strong></a>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-engfreeprivateusermem" data-raw-source="[&lt;strong&gt;EngFreePrivateUserMem&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-engfreeprivateusermem)"><strong>EngFreePrivateUserMem</strong></a></p></td>
<td align="left"><p>Deallocates a block of private user memory allocated by <a href="/windows/win32/api/winddi/nf-winddi-engallocprivateusermem" data-raw-source="[&lt;strong&gt;EngAllocPrivateUserMem&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-engallocprivateusermem)"><strong>EngAllocPrivateUserMem</strong></a>.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-engfreeusermem" data-raw-source="[&lt;strong&gt;EngFreeUserMem&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-engfreeusermem)"><strong>EngFreeUserMem</strong></a></p></td>
<td align="left"><p>Deallocates a block of user memory allocated by <a href="/windows/win32/api/winddi/nf-winddi-engallocusermem" data-raw-source="[&lt;strong&gt;EngAllocUserMem&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-engallocusermem)"><strong>EngAllocUserMem</strong></a>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-engsecuremem" data-raw-source="[&lt;strong&gt;EngSecureMem&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-engsecuremem)"><strong>EngSecureMem</strong></a></p></td>
<td align="left"><p>Locks down the specified address range in memory.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-engunsecuremem" data-raw-source="[&lt;strong&gt;EngUnsecureMem&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-engunsecuremem)"><strong>EngUnsecureMem</strong></a></p></td>
<td align="left"><p>Unlocks a memory address range that is locked down.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/dmemmgr/nf-dmemmgr-heapvidmemallocaligned" data-raw-source="[&lt;strong&gt;HeapVidMemAllocAligned&lt;/strong&gt;](/windows/win32/api/dmemmgr/nf-dmemmgr-heapvidmemallocaligned)"><strong>HeapVidMemAllocAligned</strong></a></p></td>
<td align="left"><p>Allocates <em>off-screen memory</em> for a display driver by using the DirectDraw video memory heap manager.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/dmemmgr/nf-dmemmgr-vidmemfree" data-raw-source="[&lt;strong&gt;VidMemFree&lt;/strong&gt;](/windows/win32/api/dmemmgr/nf-dmemmgr-vidmemfree)"><strong>VidMemFree</strong></a></p></td>
<td align="left"><p>Frees off-screen memory allocated for a display driver by <a href="/windows/win32/api/dmemmgr/nf-dmemmgr-heapvidmemallocaligned" data-raw-source="[&lt;strong&gt;HeapVidMemAllocAligned&lt;/strong&gt;](/windows/win32/api/dmemmgr/nf-dmemmgr-heapvidmemallocaligned)"><strong>HeapVidMemAllocAligned</strong></a>.</p></td>
</tr>
</tbody>
</table>

 

