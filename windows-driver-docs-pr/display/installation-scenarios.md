---
title: WDDM 1.2 installation scenarios
description: The Windows 8 installation graphics driver behavior is designed to ensure that, whenever possible, our customers get a graphics driver that has been tested and certified for Windows 8.
ms.assetid: AC4C214A-63C6-48C8-BA57-6DAE9E93BED9
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# WDDM 1.2 installation scenarios


The Windows 8 installation graphics driver behavior is designed to ensure that, whenever possible, our customers get a graphics driver that has been tested and certified for Windows 8. This behavior is defined by the rules that are described in this section.

## <span id="in_this_section"></span>In this section


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Topic</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>[Windows 8 in-box graphics driver preferred](windows-8-in-box-graphics-driver-preferred-.md)</p></td>
<td align="left"><p>In this scenario, Windows 8 in-box graphics driver are preferred over Windows 7 or older graphics drivers.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[Windows 8 in-box graphics drivers treated as generic drivers](windows-8-in-box-graphics-drivers-treated-as-generic-drivers-.md)</p></td>
<td align="left"><p>In this scenario, Windows 8 in-box graphics drivers, including the MS Basic Display Driver (MSBDD), are all treated like generic drivers by Windows and Windows Update.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[WDDM graphics driver migrated to Windows 8](wddm-graphics-driver-migrated-to-windows-8.md)</p></td>
<td align="left"><p>When there is no Window 8 in-box coverage for the graphics hardware in a Windows 8 upgrade installation, a WDDM 1.1 or WDDM 1.0 graphics driver that was used by the previous version of Windows will be migrated to Windows 8.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[XDDM drivers not supported for Windows 8](xddm-drivers--not-supported-for-windows-8-.md)</p></td>
<td align="left"><p>XDDM drivers are not supported for Windows 8 and will not install or run on Windows 8.</p></td>
</tr>
</tbody>
</table>

 

 

 





