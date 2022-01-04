---
title: GDI Driver-Related Services
description: GDI Driver-Related Services
keywords:
- GDI WDK Windows 2000 display , driver-related services
- graphics drivers WDK Windows 2000 display , driver-related services
- drawing WDK GDI , driver-related services
ms.date: 04/20/2017
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
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-engcreatedriverobj" data-raw-source="[&lt;strong&gt;EngCreateDriverObj&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-engcreatedriverobj)"><strong>EngCreateDriverObj</strong></a></p></td>
<td align="left"><p>Creates a <a href="/windows/win32/api/winddi/ns-winddi-driverobj" data-raw-source="[&lt;strong&gt;DRIVEROBJ&lt;/strong&gt;](/windows/win32/api/winddi/ns-winddi-_driverobj)"><strong>DRIVEROBJ</strong></a> structure. This structure is used to track a device-managed resource that must be released if the resource-allocating process terminates without first cleaning it up.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-engdeletedriverobj" data-raw-source="[&lt;strong&gt;EngDeleteDriverObj&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-engdeletedriverobj)"><strong>EngDeleteDriverObj</strong></a></p></td>
<td align="left"><p>Frees the handle used for tracking a device-managed resource.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-enggetdrivername" data-raw-source="[&lt;strong&gt;EngGetDriverName&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-enggetdrivername)"><strong>EngGetDriverName</strong></a></p></td>
<td align="left"><p>Returns the name of the driver's DLL.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-englockdriverobj" data-raw-source="[&lt;strong&gt;EngLockDriverObj&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-englockdriverobj)"><strong>EngLockDriverObj</strong></a></p></td>
<td align="left"><p>Creates an exclusive lock on a driver object for the calling thread.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-engunlockdriverobj" data-raw-source="[&lt;strong&gt;EngUnlockDriverObj&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-engunlockdriverobj)"><strong>EngUnlockDriverObj</strong></a></p></td>
<td align="left"><p>Unlocks the driver object.</p></td>
</tr>
</tbody>
</table>

 

