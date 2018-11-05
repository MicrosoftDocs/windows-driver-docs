---
title: Obtaining Sublevels of Lightweight MIP Map Textures
description: Obtaining Sublevels of Lightweight MIP Map Textures
ms.assetid: a2781c9a-b4bb-42a9-8ed5-9f62c1d2ee64
keywords:
- MIP map textures WDK DirectX 9.0 , obtaining sublevels
- lightweight MIP-map textures WDK DirectX 9.0 , obtaining sublevels
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Obtaining Sublevels of Lightweight MIP Map Textures


## <span id="ddk_obtaining_sublevels_of_lightweight_mip_map_textures_gg"></span><span id="DDK_OBTAINING_SUBLEVELS_OF_LIGHTWEIGHT_MIP_MAP_TEXTURES_GG"></span>


A DirectX 9.0 version driver can use the [CPixel class methods](https://msdn.microsoft.com/library/windows/hardware/ff540585) to obtain information about the sublevels of a lightweight system memory MIP-map texture -- only information about the top level of a lightweight MIP-map texture is stored. If the driver must copy a lightweight system memory MIP-map texture to video memory, the driver can use the CPixel class methods to calculate the source texture's size and the offset to the source texture's sublevels.

Driver writers are not required to use the CPixel class methods to calculate the locations of sublevels for lightweight MIP-map textures. However, the DirectX 9.0 runtime uses **CPixel** class methods to recover the memory layout of lightweight system memory MIP-map textures. Therefore, to ensure that the runtime and drivers recover the memory layout of lightweight system memory MIP-map textures in the same manner, driver writers must follow the same **CPixel** class rules to implement their own code.

For information about how the **CPixel** class is implemented, see the *pixel.hpp*, *pixel.cpp*, and *pixlib.cpp* files in the [PixLib](http://go.microsoft.com/fwlink/p/?linkid=256156) code sample.

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
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff540577" data-raw-source="[&lt;strong&gt;ComputeSurfaceSize&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540577)"><strong>ComputeSurfaceSize</strong></a></p></td>
<td align="left"><p>Determines the amount of memory required to allocate a surface.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff540583" data-raw-source="[&lt;strong&gt;ComputeVolumeSize&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540583)"><strong>ComputeVolumeSize</strong></a></p></td>
<td align="left"><p>Determines the amount of memory required to allocate a volume.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff540556" data-raw-source="[&lt;strong&gt;ComputeMipMapSize&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540556)"><strong>ComputeMipMapSize</strong></a></p></td>
<td align="left"><p>Determines the amount of memory required to allocate a MIP-map texture.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff540567" data-raw-source="[&lt;strong&gt;ComputeMipVolumeSize&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540567)"><strong>ComputeMipVolumeSize</strong></a></p></td>
<td align="left"><p>Determines the amount of memory required to allocate a MIP-map texture volume.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff540553" data-raw-source="[&lt;strong&gt;ComputeMipMapOffset&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540553)"><strong>ComputeMipMapOffset</strong></a></p></td>
<td align="left"><p>Determines the sublevel offset of a MIP-map texture.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff540563" data-raw-source="[&lt;strong&gt;ComputeMipVolumeOffset&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540563)"><strong>ComputeMipVolumeOffset</strong></a></p></td>
<td align="left"><p>Determines the subvolume offset of a MIP-map volume texture.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff540572" data-raw-source="[&lt;strong&gt;ComputeSurfaceOffset&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540572)"><strong>ComputeSurfaceOffset</strong></a></p></td>
<td align="left"><p>Determines the subrectangular offset of a surface.</p></td>
</tr>
</tbody>
</table>

 

 

 





