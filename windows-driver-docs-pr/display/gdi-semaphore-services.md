---
title: GDI Semaphore Services
description: GDI Semaphore Services
ms.assetid: b91211a7-19c3-4974-9222-f8eb64c29cc8
keywords: ["GDI WDK Windows 2000 display , semaphore services", "graphics drivers WDK Windows 2000 display , semaphore services", "drawing WDK GDI , semaphore services", "semaphore services WDK GDI"]
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

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20GDI%20Semaphore%20Services%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




