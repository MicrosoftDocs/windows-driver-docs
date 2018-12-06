---
title: W-Buffering
description: W-Buffering
ms.assetid: 0f06a709-11dc-4407-a230-85a689fb46a2
keywords:
- Direct3D WDK Windows 2000 display , w-buffering
- w-buffering WDK Direct3D
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# W-Buffering


## <span id="ddk_w_buffering_gg"></span><span id="DDK_W_BUFFERING_GG"></span>


Normally, z-buffering uses perspective-correct *z* for depth comparison and storage in the z-buffer, as this is the *z* that the rasterizer iterators must generate in order to maintain planar polygons. Some implementations can perform hidden surface elimination by filling the z-buffer with depth information expressed as *w*, or *z* relative to the eye. This is what is referred to as w-buffering. This can be achieved by linearly interpolating the vertex 1/w term specified in the classic transformed and lit vertex structure (TLVERTEX), computing its reciprocal per pixel, and then using this *w* value for the depth comparison and conditionally storing it into the depth buffer. For more information about TLVERTEX, see the Direct3D SDK documentation.

Typically, the hardware stores a floating-point value in the buffer. The following precision formats are common:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Size</th>
<th align="left">Format</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>16 bits</p></td>
<td align="left"><p>12.4</p></td>
</tr>
<tr class="even">
<td align="left"><p>24 bits</p></td>
<td align="left"><p>IEEE single-precision float with no low byte of mantissa.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>32 bits</p></td>
<td align="left"><p>Standard IEEE single-precision float.</p></td>
</tr>
</tbody>
</table>

 

Conventional z-buffering was developed for the technical markets that use CAD or authoring tools, in which the viewing volume/workspace is of known and limited extent. The range of depth values stored can therefore be of limited extent, allowing the ratio of far/near (the distances to the far and near clip planes) to be on the order of two to ten.

Typical hardware designed for such applications iterates perspective-correct z and stores it directly into the z-buffer. Due to the mathematics involved, this perspective-correct z is not distributed evenly within the z-buffer range. Using a far/near ratio of 100 results in 90 percent of the depth buffer range being used on the first 10 percent of the scene depth range. While this may be sufficient for tools, typical applications for entertainment or visual simulations with exterior scenes require far/near ratios of 1000 to 1 or 10000 to 1. At a ration of 1000 to 1, 98 percent of the range is used on the first two percent of the depth. This can cause hidden surface artifacts in distant objects, especially when using 16-bit depth buffers.

By contrast, when *w* (or eye-relative *z*) is used, the buffer bits can be more evenly allocated between the near and far clip planes in world space. The key benefit is that the ratio of far to near is no longer an issue, allowing applications to support a maximum range of miles, yet still get reasonably accurate depth buffering within inches of the eye point.

 

 





