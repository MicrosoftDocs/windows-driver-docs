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
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564174" data-raw-source="[&lt;strong&gt;EngAcquireSemaphore&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564174)"><strong>EngAcquireSemaphore</strong></a></p></td>
<td align="left"><p>Acquires the resource associated with the semaphore for exclusive access by the calling thread.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564760" data-raw-source="[&lt;strong&gt;EngCreateSemaphore&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564760)"><strong>EngCreateSemaphore</strong></a></p></td>
<td align="left"><p>Creates a semaphore object.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564814" data-raw-source="[&lt;strong&gt;EngDeleteSafeSemaphore&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564814)"><strong>EngDeleteSafeSemaphore</strong></a></p></td>
<td align="left"><p>Removes a reference to the specified safe semaphore.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564819" data-raw-source="[&lt;strong&gt;EngDeleteSemaphore&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564819)"><strong>EngDeleteSemaphore</strong></a></p></td>
<td align="left"><p>Deletes a semaphore object from the system&#39;s resource list.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564959" data-raw-source="[&lt;strong&gt;EngInitializeSafeSemaphore&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564959)"><strong>EngInitializeSafeSemaphore</strong></a></p></td>
<td align="left"><p>Initializes the specified safe semaphore.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564960" data-raw-source="[&lt;strong&gt;EngIsSemaphoreOwned&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564960)"><strong>EngIsSemaphoreOwned</strong></a></p></td>
<td align="left"><p>Determines whether any thread holds the specified semaphore.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564961" data-raw-source="[&lt;strong&gt;EngIsSemaphoreOwnedByCurrentThread&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564961)"><strong>EngIsSemaphoreOwnedByCurrentThread</strong></a></p></td>
<td align="left"><p>Determines whether the currently executing thread holds the specified semaphore.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff565004" data-raw-source="[&lt;strong&gt;EngReleaseSemaphore&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff565004)"><strong>EngReleaseSemaphore</strong></a></p></td>
<td align="left"><p>Releases the specified semaphore.</p></td>
</tr>
</tbody>
</table>

 

 

 





