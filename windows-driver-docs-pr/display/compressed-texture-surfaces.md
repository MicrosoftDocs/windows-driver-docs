---
title: Compressed Texture Surfaces
description: Compressed Texture Surfaces
ms.assetid: 72096a2a-5a4b-4800-bd99-6d403c54889d
keywords:
- drawing compressed textures WDK DirectDraw , about compressed texture surfaces
- DirectDraw compressed textures WDK Windows 2000 display , about compressed texture surfaces
- compressed texture surfaces WDK DirectDraw , about compressed texture surfaces
- surfaces WDK DirectDraw , compressed textures
- textures WDK DirectDraw , compressed
- drawing compressed textures WDK DirectDraw
- DirectDraw compressed textures WDK Windows 2000 display
- compressed texture surfaces WDK DirectDraw
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Compressed Texture Surfaces


## <span id="ddk_compressed_texture_surfaces_gg"></span><span id="DDK_COMPRESSED_TEXTURE_SURFACES_GG"></span>


A surface can contain a bitmap to be used for texturing 3D objects. To reduce the amount of memory consumed by textures, Microsoft DirectDraw supports the compression of texture surfaces.

**Note**   No new callbacks have been added to support compressed texture surfaces. DirectDraw passes information about compressed texture surfaces to the driver through the existing driver callbacks.

 

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">FOURCC</th>
<th align="left">Description</th>
<th align="left">Alpha
<div>
 
</div>
premultiplied?</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>DXT1</p></td>
<td align="left"><p>Opaque / one-bit alpha</p></td>
<td align="left"><p>N/A</p></td>
</tr>
<tr class="even">
<td align="left"><p>DXT2</p></td>
<td align="left"><p>Explicit alpha</p></td>
<td align="left"><p>Yes</p></td>
</tr>
<tr class="odd">
<td align="left"><p>DXT3</p></td>
<td align="left"><p>Explicit alpha</p></td>
<td align="left"><p>No</p></td>
</tr>
<tr class="even">
<td align="left"><p>DXT4</p></td>
<td align="left"><p>Interpolated alpha</p></td>
<td align="left"><p>Yes</p></td>
</tr>
<tr class="odd">
<td align="left"><p>DXT5</p></td>
<td align="left"><p>Interpolated alpha</p></td>
<td align="left"><p>No</p></td>
</tr>
</tbody>
</table>

 

The preceding shows the five types of compressed textures that drivers should support.

For more information about the format of compressed textures, see **Compressed Texture Formats** in the DirectDraw SDK documentation.

 

 





