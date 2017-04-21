---
title: GDI Driver-Related Services
description: GDI Driver-Related Services
ms.assetid: bb46ae7a-9ade-4e23-b9fe-489f83445ff3
keywords:
- GDI WDK Windows 2000 display , driver-related services
- graphics drivers WDK Windows 2000 display , driver-related services
- drawing WDK GDI , driver-related services
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20GDI%20Driver-Related%20Services%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




