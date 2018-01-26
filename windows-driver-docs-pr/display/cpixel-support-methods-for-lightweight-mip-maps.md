---
title: CPixel Support Methods for Lightweight MIP Maps
description: CPixel Support Methods for Lightweight MIP Maps
ms.assetid: 79204a0c-c3a8-4059-a1be-9febf20a8cbd
keywords: ["CPixel interface, described"]
ms.author: windowsdriverdev
ms.date: 01/05/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# CPixel Support Methods for Lightweight MIP Maps


## <span id="ddk_cpixel_support_methods_for_lightweight_mip_maps_gg"></span><span id="DDK_CPIXEL_SUPPORT_METHODS_FOR_LIGHTWEIGHT_MIP_MAPS_GG"></span>


This section describes the methods defined for the **CPixel** class. These methods are used to recover the layout of lightweight system memory MIP-map textures. Method prototypes are defined in the *pixel.hpp* file. This file along with *pixel.cpp* and *pixlib.cpp* were originally included in the Microsoft Windows Driver Development Kit (DDK) and are used to build the *PixLib.lib* support library. (The DDK preceded the Windows Driver Kit \[WDK\].)

For more information about the *PixLib.lib* library, see the [PixLib](http://go.microsoft.com/fwlink/p/?linkid=256156) sample in the MSDN Developer Samples code gallery.

.

For your driver to use the following **CPixel** class methods, you must include the *pixel.hpp* file in your code and link to *PixLib.lib* when you build your driver.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">CPixel Class Method</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>[<strong>ComputeSurfaceSize</strong>](cpixel-computesurfacesize.md)</p></td>
<td align="left"><p>Determines the amount of memory required to allocate a surface.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>ComputeVolumeSize</strong>](cpixel-computevolumesize.md)</p></td>
<td align="left"><p>Determines the amount of memory required to allocate a volume.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>ComputeMipMapSize</strong>](cpixel-computemipmapsize.md)</p></td>
<td align="left"><p>Determines the amount of memory required to allocate a MIP-map texture.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>ComputeMipVolumeSize</strong>](cpixel-computemipvolumesize.md)</p></td>
<td align="left"><p>Determines the amount of memory required to allocate a MIP-map texture volume.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>ComputeMipMapOffset</strong>](cpixel-computemipmapoffset.md)</p></td>
<td align="left"><p>Determines the sublevel offset of a MIP-map texture.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>ComputeMipVolumeOffset</strong>](cpixel-computemipvolumeoffset.md)</p></td>
<td align="left"><p>Determines the subvolume offset of a MIP-map volume texture.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>ComputeSurfaceOffset</strong>](cpixel-computesurfaceoffset.md)</p></td>
<td align="left"><p>Determines the subrectangular offset of a surface.</p></td>
</tr>
</tbody>
</table>

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20CPixel%20Support%20Methods%20for%20Lightweight%20MIP%20Maps%20%20RELEASE:%20%281/4/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




