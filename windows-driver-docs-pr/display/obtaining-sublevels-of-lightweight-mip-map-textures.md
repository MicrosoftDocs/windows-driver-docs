---
title: Obtaining Sublevels of Lightweight MIP Map Textures
description: Obtaining Sublevels of Lightweight MIP Map Textures
ms.assetid: a2781c9a-b4bb-42a9-8ed5-9f62c1d2ee64
keywords:
- MIP map textures WDK DirectX 9.0 , obtaining sublevels
- lightweight MIP-map textures WDK DirectX 9.0 , obtaining sublevels
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Obtaining Sublevels of Lightweight MIP Map Textures


## <span id="ddk_obtaining_sublevels_of_lightweight_mip_map_textures_gg"></span><span id="DDK_OBTAINING_SUBLEVELS_OF_LIGHTWEIGHT_MIP_MAP_TEXTURES_GG"></span>


A DirectX 9.0 version driver can use the [CPixel class methods](https://msdn.microsoft.com/library/windows/hardware/ff540585) to obtain information about the sublevels of a lightweight system memory MIP-map texture -- only information about the top level of a lightweight MIP-map texture is stored. If the driver must copy a lightweight system memory MIP-map texture to video memory, the driver can use the CPixel class methods to calculate the source texture's size and the offset to the source texture's sublevels.

Driver writers are not required to use the CPixel class methods to calculate the locations of sublevels for lightweight MIP-map textures. However, the DirectX 9.0 runtime uses **CPixel** class methods to recover the memory layout of lightweight system memory MIP-map textures. Therefore, to ensure that the runtime and drivers recover the memory layout of lightweight system memory MIP-map textures in the same manner, driver writers must follow the same **CPixel** class rules to implement their own code.

For information about how the **CPixel** class is implemented, see the *pixel.hpp*, *pixel.cpp*, and *pixlib.cpp* files in the [PixLib](http://go.microsoft.com/fwlink/p/?linkid=256156) sample in the MSDN Developer Samples code gallery.

The CPixel class contains the following methods:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">CPixel Method</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>[<strong>ComputeSurfaceSize</strong>](https://msdn.microsoft.com/library/windows/hardware/ff540577)</p></td>
<td align="left"><p>Determines the amount of memory required to allocate a surface.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>ComputeVolumeSize</strong>](https://msdn.microsoft.com/library/windows/hardware/ff540583)</p></td>
<td align="left"><p>Determines the amount of memory required to allocate a volume.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>ComputeMipMapSize</strong>](https://msdn.microsoft.com/library/windows/hardware/ff540556)</p></td>
<td align="left"><p>Determines the amount of memory required to allocate a MIP-map texture.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>ComputeMipVolumeSize</strong>](https://msdn.microsoft.com/library/windows/hardware/ff540567)</p></td>
<td align="left"><p>Determines the amount of memory required to allocate a MIP-map texture volume.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>ComputeMipMapOffset</strong>](https://msdn.microsoft.com/library/windows/hardware/ff540553)</p></td>
<td align="left"><p>Determines the sublevel offset of a MIP-map texture.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>ComputeMipVolumeOffset</strong>](https://msdn.microsoft.com/library/windows/hardware/ff540563)</p></td>
<td align="left"><p>Determines the subvolume offset of a MIP-map volume texture.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>ComputeSurfaceOffset</strong>](https://msdn.microsoft.com/library/windows/hardware/ff540572)</p></td>
<td align="left"><p>Determines the subrectangular offset of a surface.</p></td>
</tr>
</tbody>
</table>

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Obtaining%20Sublevels%20of%20Lightweight%20MIP%20Map%20Textures%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




