---
title: GDI Memory Services
description: GDI Memory Services
ms.assetid: 60b45f8f-766b-498c-a0c2-3e93ea4b43b9
keywords:
- GDI WDK Windows 2000 display , memory services
- graphics drivers WDK Windows 2000 display , memory services
- drawing WDK GDI , memory services
- memory WDK GDI
ms.date: 04/20/2017
ms.localizationpriority: medium
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
<td align="left"><p>[<strong>EngAllocMem</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564176)</p></td>
<td align="left"><p>Allocates a block of memory, and inserts a caller-supplied tag before the allocation.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>EngAllocPrivateUserMem</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564177)</p></td>
<td align="left"><p>Allocates a block of private user memory from the address space of a specified process, and inserts a caller-supplied tag before the allocation.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>EngAllocUserMem</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564178)</p></td>
<td align="left"><p>Allocates a block of memory from the address space of the current process, and inserts a caller-supplied tag before the allocation.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>EngFreeMem</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564895)</p></td>
<td align="left"><p>Deallocates a block of system memory allocated by [<strong>EngAllocMem</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564176).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>EngFreePrivateUserMem</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564907)</p></td>
<td align="left"><p>Deallocates a block of private user memory allocated by [<strong>EngAllocPrivateUserMem</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564177).</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>EngFreeUserMem</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564912)</p></td>
<td align="left"><p>Deallocates a block of user memory allocated by [<strong>EngAllocUserMem</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564178).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>EngSecureMem</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565011)</p></td>
<td align="left"><p>Locks down the specified address range in memory.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>EngUnsecureMem</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565454)</p></td>
<td align="left"><p>Unlocks a memory address range that is locked down.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>HeapVidMemAllocAligned</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567267)</p></td>
<td align="left"><p>Allocates [<em>off-screen memory</em>](https://msdn.microsoft.com/library/windows/hardware/ff556318#wdkgloss-off-screen-memory) for a display driver by using the DirectDraw video memory heap manager.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>VidMemFree</strong>](https://msdn.microsoft.com/library/windows/hardware/ff570554)</p></td>
<td align="left"><p>Frees off-screen memory allocated for a display driver by [<strong>HeapVidMemAllocAligned</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567267).</p></td>
</tr>
</tbody>
</table>

 

 

 





