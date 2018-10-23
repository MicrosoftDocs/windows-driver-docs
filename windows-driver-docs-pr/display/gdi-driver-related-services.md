---
title: GDI Driver-Related Services
description: GDI Driver-Related Services
ms.assetid: bb46ae7a-9ade-4e23-b9fe-489f83445ff3
keywords:
- GDI WDK Windows 2000 display , driver-related services
- graphics drivers WDK Windows 2000 display , driver-related services
- drawing WDK GDI , driver-related services
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# GDI Driver-Related Services


## <span id="ddk_gdi_driver_related_services_gg"></span><span id="DDK_GDI_DRIVER_RELATED_SERVICES_GG"></span>


Driver writers can use the GDI driver-related services listed in the following table to create or delete driver objects, obtain the name of the driver's DLL, and lock or unlock a driver object.

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
<td align="left"><p>[<strong>EngCreateDriverObj</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564207)</p></td>
<td align="left"><p>Creates a [<strong>DRIVEROBJ</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556162) structure. This structure is used to track a device-managed resource that must be released if the resource-allocating process terminates without first cleaning it up.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>EngDeleteDriverObj</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564792)</p></td>
<td align="left"><p>Frees the handle used for tracking a device-managed resource.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>EngGetDriverName</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564927)</p></td>
<td align="left"><p>Returns the name of the driver's DLL.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>EngLockDriverObj</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564967)</p></td>
<td align="left"><p>Creates an exclusive lock on a driver object for the calling thread.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>EngUnlockDriverObj</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565044)</p></td>
<td align="left"><p>Unlocks the driver object.</p></td>
</tr>
</tbody>
</table>

 

 

 





