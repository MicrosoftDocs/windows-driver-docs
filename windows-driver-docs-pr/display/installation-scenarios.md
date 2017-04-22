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

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20WDDM%201.2%20installation%20scenarios%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




