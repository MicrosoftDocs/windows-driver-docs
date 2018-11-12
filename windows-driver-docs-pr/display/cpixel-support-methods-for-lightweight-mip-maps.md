---
title: CPixel Support Methods for Lightweight MIP Maps
description: CPixel Support Methods for Lightweight MIP Maps
ms.assetid: 79204a0c-c3a8-4059-a1be-9febf20a8cbd
keywords: ["CPixel interface, described"]
ms.date: 01/05/2018
ms.localizationpriority: medium
---

# CPixel Support Methods for Lightweight MIP Maps


## <span id="ddk_cpixel_support_methods_for_lightweight_mip_maps_gg"></span><span id="DDK_CPIXEL_SUPPORT_METHODS_FOR_LIGHTWEIGHT_MIP_MAPS_GG"></span>


This section describes the methods defined for the **CPixel** class. These methods are used to recover the layout of lightweight system memory MIP-map textures. Method prototypes are defined in the *pixel.hpp* file. This file along with *pixel.cpp* and *pixlib.cpp* were originally included in the Microsoft Windows Driver Development Kit (DDK) and are used to build the *PixLib.lib* support library. (The DDK preceded the Windows Driver Kit \[WDK\].)

For more information about the *PixLib.lib* library, see the [PixLib](http://go.microsoft.com/fwlink/p/?linkid=256156) sample in the Hardware Dev Center.

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
<td align="left"><p><a href="cpixel-computesurfacesize.md" data-raw-source="[&lt;strong&gt;ComputeSurfaceSize&lt;/strong&gt;](cpixel-computesurfacesize.md)"><strong>ComputeSurfaceSize</strong></a></p></td>
<td align="left"><p>Determines the amount of memory required to allocate a surface.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="cpixel-computevolumesize.md" data-raw-source="[&lt;strong&gt;ComputeVolumeSize&lt;/strong&gt;](cpixel-computevolumesize.md)"><strong>ComputeVolumeSize</strong></a></p></td>
<td align="left"><p>Determines the amount of memory required to allocate a volume.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="cpixel-computemipmapsize.md" data-raw-source="[&lt;strong&gt;ComputeMipMapSize&lt;/strong&gt;](cpixel-computemipmapsize.md)"><strong>ComputeMipMapSize</strong></a></p></td>
<td align="left"><p>Determines the amount of memory required to allocate a MIP-map texture.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="cpixel-computemipvolumesize.md" data-raw-source="[&lt;strong&gt;ComputeMipVolumeSize&lt;/strong&gt;](cpixel-computemipvolumesize.md)"><strong>ComputeMipVolumeSize</strong></a></p></td>
<td align="left"><p>Determines the amount of memory required to allocate a MIP-map texture volume.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="cpixel-computemipmapoffset.md" data-raw-source="[&lt;strong&gt;ComputeMipMapOffset&lt;/strong&gt;](cpixel-computemipmapoffset.md)"><strong>ComputeMipMapOffset</strong></a></p></td>
<td align="left"><p>Determines the sublevel offset of a MIP-map texture.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="cpixel-computemipvolumeoffset.md" data-raw-source="[&lt;strong&gt;ComputeMipVolumeOffset&lt;/strong&gt;](cpixel-computemipvolumeoffset.md)"><strong>ComputeMipVolumeOffset</strong></a></p></td>
<td align="left"><p>Determines the subvolume offset of a MIP-map volume texture.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="cpixel-computesurfaceoffset.md" data-raw-source="[&lt;strong&gt;ComputeSurfaceOffset&lt;/strong&gt;](cpixel-computesurfaceoffset.md)"><strong>ComputeSurfaceOffset</strong></a></p></td>
<td align="left"><p>Determines the subrectangular offset of a surface.</p></td>
</tr>
</tbody>
</table>

 

 

 





