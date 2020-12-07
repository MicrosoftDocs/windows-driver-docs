---
title: Obtaining Sublevels of Lightweight MIP Map Textures
description: Obtaining Sublevels of Lightweight MIP Map Textures
keywords:
- MIP map textures WDK DirectX 9.0 , obtaining sublevels
- lightweight MIP-map textures WDK DirectX 9.0 , obtaining sublevels
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Obtaining Sublevels of Lightweight MIP Map Textures


## <span id="ddk_obtaining_sublevels_of_lightweight_mip_map_textures_gg"></span><span id="DDK_OBTAINING_SUBLEVELS_OF_LIGHTWEIGHT_MIP_MAP_TEXTURES_GG"></span>


A DirectX 9.0 version driver can use the [CPixel class methods](./cpixel-support-methods-for-lightweight-mip-maps.md) to obtain information about the sublevels of a lightweight system memory MIP-map texture -- only information about the top level of a lightweight MIP-map texture is stored. If the driver must copy a lightweight system memory MIP-map texture to video memory, the driver can use the CPixel class methods to calculate the source texture's size and the offset to the source texture's sublevels.

Driver writers are not required to use the CPixel class methods to calculate the locations of sublevels for lightweight MIP-map textures. However, the DirectX 9.0 runtime uses **CPixel** class methods to recover the memory layout of lightweight system memory MIP-map textures. Therefore, to ensure that the runtime and drivers recover the memory layout of lightweight system memory MIP-map textures in the same manner, driver writers must follow the same **CPixel** class rules to implement their own code.

For information about how the **CPixel** class is implemented, see the *pixel.hpp*, *pixel.cpp*, and *pixlib.cpp* files in the [PixLib](/samples/browse/) code sample.

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
<td align="left"><p><a href="/windows-hardware/drivers/display/cpixel-computesurfacesize" data-raw-source="[&lt;strong&gt;ComputeSurfaceSize&lt;/strong&gt;](./cpixel-computesurfacesize.md)"><strong>ComputeSurfaceSize</strong></a></p></td>
<td align="left"><p>Determines the amount of memory required to allocate a surface.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/display/cpixel-computevolumesize" data-raw-source="[&lt;strong&gt;ComputeVolumeSize&lt;/strong&gt;](./cpixel-computevolumesize.md)"><strong>ComputeVolumeSize</strong></a></p></td>
<td align="left"><p>Determines the amount of memory required to allocate a volume.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/display/cpixel-computemipmapsize" data-raw-source="[&lt;strong&gt;ComputeMipMapSize&lt;/strong&gt;](./cpixel-computemipmapsize.md)"><strong>ComputeMipMapSize</strong></a></p></td>
<td align="left"><p>Determines the amount of memory required to allocate a MIP-map texture.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/display/cpixel-computemipvolumesize" data-raw-source="[&lt;strong&gt;ComputeMipVolumeSize&lt;/strong&gt;](./cpixel-computemipvolumesize.md)"><strong>ComputeMipVolumeSize</strong></a></p></td>
<td align="left"><p>Determines the amount of memory required to allocate a MIP-map texture volume.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/display/cpixel-computemipmapoffset" data-raw-source="[&lt;strong&gt;ComputeMipMapOffset&lt;/strong&gt;](./cpixel-computemipmapoffset.md)"><strong>ComputeMipMapOffset</strong></a></p></td>
<td align="left"><p>Determines the sublevel offset of a MIP-map texture.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/display/cpixel-computemipvolumeoffset" data-raw-source="[&lt;strong&gt;ComputeMipVolumeOffset&lt;/strong&gt;](./cpixel-computemipvolumeoffset.md)"><strong>ComputeMipVolumeOffset</strong></a></p></td>
<td align="left"><p>Determines the subvolume offset of a MIP-map volume texture.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/display/cpixel-computesurfaceoffset" data-raw-source="[&lt;strong&gt;ComputeSurfaceOffset&lt;/strong&gt;](./cpixel-computesurfaceoffset.md)"><strong>ComputeSurfaceOffset</strong></a></p></td>
<td align="left"><p>Determines the subrectangular offset of a surface.</p></td>
</tr>
</tbody>
</table>

