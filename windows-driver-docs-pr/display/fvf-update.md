---
title: FVF Update
description: FVF Update
ms.assetid: 2bbcb1fd-b29f-41f4-93eb-5bd1cde9cb20
keywords:
- FVF WDK Direct3D
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# FVF Update


## <span id="ddk_fvf_update_gg"></span><span id="DDK_FVF_UPDATE_GG"></span>


The FVF codes originally defined in DirectX 6.0 now support the specifications for texture coordinate sets in DirectX 7.0.

In addition to the normal 2D textures, supported in DirectX 6.0, DirectX 7.0 supports 1D, 3D, and 4D textures. In addition, the textures may be projected. The **dwVertexType** member of [**D3DHAL\_DRAWPRIMITIVES2DATA**](https://msdn.microsoft.com/library/windows/hardware/ff545957) can be examined when [**D3dDrawPrimitives2**](https://msdn.microsoft.com/library/windows/hardware/ff544704) is called, to determine the dimensions of each texture coordinate set.

For example, if there is a vertex with five texture coordinate sets, each one of these textures can be 1D, 2D, 3D, or 4D and they may be projected textures. Each texture stage is independent, so the dimensions can be different for each set of coordinates. The upper 16 bits of the FVF flag contained in **dwVertexType** can be examined to determine the dimensions of the texture coordinates.

The texture coordinate count is a 4-bitfield that can range from zero through eight. This gives the number of texture coordinate sets given in the upper 16 bits of the word. The upper 16 bits of the [FVF](fvf--flexible-vertex-format-.md) code are allocated as two bits each for each of eight texture coordinate sets. The meaning of the texture coordinate bits is as follows:

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Bit
<div>
 
</div>
Pattern</th>
<th align="left">Decimal
<div>
 
</div>
Value</th>
<th align="left">Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>00</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>Two-dimensional texture coordinate pair, (u, v) as in DirectX 6.0</p></td>
</tr>
<tr class="even">
<td align="left"><p>01</p></td>
<td align="left"><p>1</p></td>
<td align="left"><p>Three-dimensional texture coordinate triple, (u, v, q)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>10</p></td>
<td align="left"><p>2</p></td>
<td align="left"><p>Four-dimensional texture coordinate quadruple, (u, v, w, q)</p></td>
</tr>
<tr class="even">
<td align="left"><p>11</p></td>
<td align="left"><p>3</p></td>
<td align="left"><p>One-dimensional texture coordinate, u</p></td>
</tr>
</tbody>
</table>

 

3D texture coordinate sets can be used for any of three different purposes: projected textures (signaled by D3DTTFF\_PROJECTED - see D3DTEXTURETRANSFORMFLAGS in the DirectX SDK documentation), volume textures, or cube map vector textures, as determined by a set of render states analogous to the D3DRENDERSTATE\_WRAP0 to D3DRENDERSTATE\_WRAP7 modes that are already specified on a texture coordinate set basis.

The flags used with the D3DRENDERSTATE\_WRAP*n* render states for 1D through 4D texture coordinates, respectively, are described in the following table.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Flags</th>
<th align="left">Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>D3DWRAPCOORD_0</p></td>
<td align="left"><p>Same as D3DWRAP_U, which specifies wrapping in the <em>u</em> coordinate direction.</p></td>
</tr>
<tr class="even">
<td align="left"><p>D3DWRAPCOORD_1</p></td>
<td align="left"><p>Same as D3DWRAP_V, which specifies wrapping in the <em>v</em> coordinate direction.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>D3DWRAPCOORD_2</p></td>
<td align="left"><p>Specifies wrapping in the <em>w</em> coordinate direction.</p></td>
</tr>
<tr class="even">
<td align="left"><p>D3DWRAPCOORD_3</p></td>
<td align="left"><p>Specifies wrapping in the <em>q</em> coordinate direction.</p></td>
</tr>
</tbody>
</table>

 

When projected textures are in use, they take the RHW value from the corresponding texture coordinate field, instead of from the position field. However, the position field's RHW is still used for both w-buffering and fog calculations, and therefore must be provided when either of these is in use.

 

 





