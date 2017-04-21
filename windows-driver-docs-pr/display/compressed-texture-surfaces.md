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
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Compressed%20Texture%20Surfaces%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




