---
title: GDI Semaphore Services
description: GDI Semaphore Services
ms.assetid: b91211a7-19c3-4974-9222-f8eb64c29cc8
keywords:
- GDI WDK Windows 2000 display , semaphore services
- graphics drivers WDK Windows 2000 display , semaphore services
- drawing WDK GDI , semaphore services
- semaphore services WDK GDI
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# GDI Semaphore Services


## <span id="ddk_gdi_semaphore_services_gg"></span><span id="DDK_GDI_SEMAPHORE_SERVICES_GG"></span>


GDI provides a selection of services related to semaphores and safe semaphores. A driver can use these services to create or delete a semaphore, and acquire or release a semaphore.

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
<td align="left"><p>[<strong>EngAcquireSemaphore</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564174)</p></td>
<td align="left"><p>Acquires the resource associated with the semaphore for exclusive access by the calling thread.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>EngCreateSemaphore</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564760)</p></td>
<td align="left"><p>Creates a semaphore object.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>EngDeleteSafeSemaphore</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564814)</p></td>
<td align="left"><p>Removes a reference to the specified safe semaphore.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>EngDeleteSemaphore</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564819)</p></td>
<td align="left"><p>Deletes a semaphore object from the system's resource list.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>EngInitializeSafeSemaphore</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564959)</p></td>
<td align="left"><p>Initializes the specified safe semaphore.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>EngIsSemaphoreOwned</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564960)</p></td>
<td align="left"><p>Determines whether any thread holds the specified semaphore.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>EngIsSemaphoreOwnedByCurrentThread</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564961)</p></td>
<td align="left"><p>Determines whether the currently executing thread holds the specified semaphore.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>EngReleaseSemaphore</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565004)</p></td>
<td align="left"><p>Releases the specified semaphore.</p></td>
</tr>
</tbody>
</table>

 

 

 





