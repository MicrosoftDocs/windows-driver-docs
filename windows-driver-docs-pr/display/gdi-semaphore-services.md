---
title: GDI Semaphore Services
description: GDI Semaphore Services
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
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-engacquiresemaphore" data-raw-source="[&lt;strong&gt;EngAcquireSemaphore&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-engacquiresemaphore)"><strong>EngAcquireSemaphore</strong></a></p></td>
<td align="left"><p>Acquires the resource associated with the semaphore for exclusive access by the calling thread.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-engcreatesemaphore" data-raw-source="[&lt;strong&gt;EngCreateSemaphore&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-engcreatesemaphore)"><strong>EngCreateSemaphore</strong></a></p></td>
<td align="left"><p>Creates a semaphore object.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-engdeletesafesemaphore" data-raw-source="[&lt;strong&gt;EngDeleteSafeSemaphore&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-engdeletesafesemaphore)"><strong>EngDeleteSafeSemaphore</strong></a></p></td>
<td align="left"><p>Removes a reference to the specified safe semaphore.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-engdeletesemaphore" data-raw-source="[&lt;strong&gt;EngDeleteSemaphore&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-engdeletesemaphore)"><strong>EngDeleteSemaphore</strong></a></p></td>
<td align="left"><p>Deletes a semaphore object from the system's resource list.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-enginitializesafesemaphore" data-raw-source="[&lt;strong&gt;EngInitializeSafeSemaphore&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-enginitializesafesemaphore)"><strong>EngInitializeSafeSemaphore</strong></a></p></td>
<td align="left"><p>Initializes the specified safe semaphore.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-engissemaphoreowned" data-raw-source="[&lt;strong&gt;EngIsSemaphoreOwned&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-engissemaphoreowned)"><strong>EngIsSemaphoreOwned</strong></a></p></td>
<td align="left"><p>Determines whether any thread holds the specified semaphore.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-engissemaphoreownedbycurrentthread" data-raw-source="[&lt;strong&gt;EngIsSemaphoreOwnedByCurrentThread&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-engissemaphoreownedbycurrentthread)"><strong>EngIsSemaphoreOwnedByCurrentThread</strong></a></p></td>
<td align="left"><p>Determines whether the currently executing thread holds the specified semaphore.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-engreleasesemaphore" data-raw-source="[&lt;strong&gt;EngReleaseSemaphore&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-engreleasesemaphore)"><strong>EngReleaseSemaphore</strong></a></p></td>
<td align="left"><p>Releases the specified semaphore.</p></td>
</tr>
</tbody>
</table>

 

