---
title: Texture Addressing and Filtering Operations
description: Texture Addressing and Filtering Operations
ms.assetid: d468c83e-2e9c-4e4b-885e-0427714dd8a3
keywords:
- multiple textures WDK Direct3D , addressing
- multiple textures WDK Direct3D , filtering
- multiple textures WDK Direct3D , blending
- blending WDK Direct3D
- texture management WDK Direct3D , addressing
- texture management WDK Direct3D , filtering
- texture management WDK Direct3D , blending
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Texture Addressing and Filtering Operations


## <span id="ddk_texture_addressing_and_filtering_operations_gg"></span><span id="DDK_TEXTURE_ADDRESSING_AND_FILTERING_OPERATIONS_GG"></span>


In Direct3D, texture addressing, filtering, and blending operations are performed by a separate logical unit called a [texture stage](texture-stages.md). Addressing and filtering operations are described here because they form a logical grouping independent of the blending operations. For further information about texture operations, see the D3DTEXTUREOP enumerated type in the DirectX SDK documentation.

Although addressing and sampling operations are defined in conjunction with blending operations in DirectX 6.0 and later versions, in later releases of DirectX they are likely to be independent of the blending operations. The texture stage states listed in the following table are used to set up texture addressing and filtering operations for each stage in the texture pipeline.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Operation</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>D3DTSS_ANISOTROPY</p></td>
<td align="left"><p>Specifies the anisotropic filtering ratio limit. It specifies the maximum aspect ratio of anisotropic filtering to be applied during sampling of this texture.</p></td>
</tr>
<tr class="even">
<td align="left"><p>D3DTSS_MAGFILTER</p></td>
<td align="left"><p>Defines the type of filter used to sample textures when they are being magnified (that is, when one texel is getting stretched onto multiple rendering surface pixels). The filters that can be used for texture magnification are enumerated in D3DTEXTUREMAGFILTER.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>D3DTSS_MAXMIPLEVEL</p></td>
<td align="left"><p>Specifies the maximum MIP map level to be used. It indicates that this texture should never sample MIP map levels that are larger that the one indicated. Therefore, the maximum dimension is 2<sup>MAXMIPLEVEL</sup>. Zero indicates that there is no limit.</p></td>
</tr>
<tr class="even">
<td align="left"><p>D3DTSS_MINFILTER</p></td>
<td align="left"><p>Defines the type of filtering that is used to sample textures when they are being <em>minified</em>, that is, one texel is mapped onto less than one screen pixel. The filters that can be used to minify textures are enumerated in D3DTEXTUREMINFILTER.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>D3DTSS_MIPFILTER</p></td>
<td align="left"><p>Defines the type of filtering that is used to sample between layers of a MIP map. The filters that can be used for this are enumerated in D3DTEXTUREMIPFILTER.</p></td>
</tr>
<tr class="even">
<td align="left"><p>D3DTSS_MIPLEVEL</p></td>
<td align="left"><p>Allows application to set the MIP level when hardware cannot. This is overridden when the MIP level is determined by hardware.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>D3DTSS_MIPMAPLODBIAS</p></td>
<td align="left"><p>Is a D3DVALUE that specifies the MIP map level of detail (LOD) bias. This bias affects the MIP map level calculation, allowing more or less blurring of textures (and more aliasing) as desired. Units are in MIP levels.</p>
<p>Current WHQL/DCT tests require the MIP map LOD bias to operate in the range -3.0 to 3.0.</p></td>
</tr>
<tr class="even">
<td align="left"><p>D3DTSS_TEXCOORDINDEX</p></td>
<td align="left"><p>Specifies the index of a texture coordinate set. This integer indicates the index of the set of texture coordinates from which the addressing unit should sample. These coordinates are listed in the incoming flexible vertex format (<a href="fvf--flexible-vertex-format-.md" data-raw-source="[FVF](fvf--flexible-vertex-format-.md)">FVF</a>) vertex data in numerical order, with zero being the standard DirectX set of texture coordinates, one being a second texture coordinate set, and so on. This allows textures to share sets of texture coordinates as desired.</p></td>
</tr>
</tbody>
</table>

 

**Note**   To be Direct3D-compliant, drivers are required to properly parse up to eight texture coordinate sets, even if the device can only iterate and use the number of coordinates defined in **dwFVFCaps**. The driver must use D3DTSS\_TEXCOORDINDEX to grab the right coordinates to use for texturing.

 

 

 





