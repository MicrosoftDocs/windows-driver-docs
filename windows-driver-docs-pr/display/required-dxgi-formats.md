---
title: Required DXGI formats
description: This topic presents the requirements that Microsoft Direct3D feature levels place on the user-mode display driver.
ms.assetid: 1CB419B9-DD5E-492F-AAAC-CFFFDE247F7F
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Required DXGI formats


This topic presents the requirements that Microsoft Direct3D feature levels place on the user-mode display driver.

The first and second columns of the first table show all Direct3D format types that the driver must support. The third column shows all associated constant values of the Direct3D [**D3D10\_FORMAT\_SUPPORT**](https://msdn.microsoft.com/library/windows/desktop/bb205063) and/or [**D3D11\_FORMAT\_SUPPORT**](https://msdn.microsoft.com/library/windows/desktop/ff476134) enumerations that the driver must support. The fourth column shows the minimum Direct3D feature level at which the driver must support each format.

The second table shows the Direct3D 10Level 9 support algorithm for each enumeration value.

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">D3D9 format (D3DDDIFMT_* and/or D3DDECLTYPE<em></th>
<th align="left">D3D10+ API equivalent (DXGI_FORMAT_</em>)</th>
<th align="left">Required D3D10_ or D3D11_ FORMAT_SUPPORT_* enumeration values</th>
<th align="left">Minimum required Direct3D level</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left">A32B32G32R32F or D3DDECLTYPE_FLOAT4</td>
<td align="left">R32G32B32A32_FLOAT</td>
<td align="left"><p>IA_VERTEX_BUFFER</p>
<p>TEXTURE2D</p>
<p>TEXTURE3D</p>
<p>TEXTURECUBE</p>
<p>SHADER_LOAD</p>
<p>MIP</p>
<p>MIP_AUTOGEN</p>
<p>RENDER_TARGET</p>
<p>CPU_LOCKABLE</p></td>
<td align="left"><p>9_1</p>
<p>9_2</p>
<p>9_3</p>
<p>9_3</p>
<p>9_2</p>
<p>9_3</p>
<p>9_3</p>
<p>9_2</p>
<p>9_2</p></td>
</tr>
<tr class="even">
<td align="left">D3DDECLTYPE_FLOAT3</td>
<td align="left">R32G32B32_FLOAT</td>
<td align="left"><p>IA_VERTEX_BUFFER</p></td>
<td align="left"><p>9_1</p></td>
</tr>
<tr class="odd">
<td align="left">A16B16G16R16F or D3DDECLTYPE_FLOAT16_4</td>
<td align="left">R16G16B16A16_FLOAT</td>
<td align="left"><p>IA_VERTEX_BUFFER</p>
<p>TEXTURE2D</p>
<p>TEXTURE3D</p>
<p>TEXTURECUBE</p>
<p>SHADER_LOAD</p>
<p>MIP</p>
<p>MIP_AUTOGEN</p>
<p>RENDER_TARGET</p>
<p>BLENDABLE</p>
<p>CPU_LOCKABLE</p></td>
<td align="left"><p>9_3</p>
<p>9_2</p>
<p>9_2</p>
<p>9_2</p>
<p>9_2</p>
<p>9_2</p>
<p>9_2</p>
<p>9_2</p>
<p>9_3</p>
<p>9_2</p></td>
</tr>
<tr class="even">
<td align="left">A16B16G16R16 or D3DDECLTYPE_USHORT4N</td>
<td align="left">R16G16B16A16_UNORM</td>
<td align="left"><p>TEXTURE2D</p>
<p>TEXTURE3D</p>
<p>TEXTURECUBE</p>
<p>SHADER_LOAD</p>
<p>SHADER_SAMPLE</p>
<p>MIP</p>
<p>MIP_AUTOGEN</p>
<p>RENDER_TARGET</p>
<p>CPU_LOCKABLE</p></td>
<td align="left"><p>9_2</p>
<p>9_2</p>
<p>9_2</p>
<p>9_2</p>
<p>9_2</p>
<p>9_2</p>
<p>9_2</p>
<p>9_2</p>
<p>9_2</p></td>
</tr>
<tr class="odd">
<td align="left">Q16W16V16U16 or D3DDECLTYPE_SHORT4N</td>
<td align="left">R16G16B16A16_SNORM</td>
<td align="left"><p>IA_VERTEX_BUFFER</p></td>
<td align="left"><p>9_1</p></td>
</tr>
<tr class="even">
<td align="left">D3DDECLTYPE_SHORT4</td>
<td align="left">R16G16B16A16_SINT</td>
<td align="left"><p>IA_VERTEX_BUFFER</p></td>
<td align="left"><p>9_1</p></td>
</tr>
<tr class="odd">
<td align="left">G32R32F or D3DDECLTYPE_FLOAT2</td>
<td align="left">R32G32_FLOAT</td>
<td align="left"><p>IA_VERTEX_BUFFER</p>
<p>TEXTURE2D</p>
<p>TEXTURE3D</p>
<p>TEXTURECUBE</p>
<p>SHADER_LOAD</p>
<p>RENDER_TARGET</p>
<p>CPU_LOCKABLE</p></td>
<td align="left"><p>9_1</p>
<p>9_3</p>
<p>9_3</p>
<p>9_3</p>
<p>9_3</p>
<p>9_3</p>
<p>9_3</p></td>
</tr>
<tr class="even">
<td align="left">D3DDECLTYPE_UBYTE4</td>
<td align="left">R8G8B8A8_UINT</td>
<td align="left"><p>IA_VERTEX_BUFFER</p></td>
<td align="left"><p>9_1</p></td>
</tr>
<tr class="odd">
<td align="left">A8R8G8B8 or D3DDECLTYPE_UBYTE4N</td>
<td align="left">R8G8B8A8_UNORM</td>
<td align="left"><p>IA_VERTEX_BUFFER</p>
<p>TEXTURE2D</p>
<p>TEXTURE3D</p>
<p>TEXTURECUBE</p>
<p>SHADER_LOAD</p>
<p>SHADER_SAMPLE</p>
<p>MIP</p>
<p>MIP_AUTOGEN</p>
<p>RENDER_TARGET</p>
<p>BLENDABLE</p>
<p>CPU_LOCKABLE</p>
<p>DISPLAY</p>
<p>BACK_BUFFER_CAST</p></td>
<td align="left"><p>9_1</p>
<p>9_1</p>
<p>9_1</p>
<p>9_1</p>
<p>9_1</p>
<p>9_1</p>
<p>9_1</p>
<p>9_1</p>
<p>9_1</p>
<p>9_1</p>
<p>9_1</p>
<p>9_1</p>
<p>9_1</p></td>
</tr>
<tr class="even">
<td align="left">A8R8G8B8</td>
<td align="left">R8G8B8A8_UNORM_SRGB</td>
<td align="left"><p>TEXTURE2D</p>
<p>TEXTURE3D</p>
<p>TEXTURECUBE</p>
<p>SHADER_LOAD</p>
<p>SHADER_SAMPLE</p>
<p>MIP</p>
<p>MIP_AUTOGEN</p>
<p>RENDER_TARGET</p>
<p>BLENDABLE</p>
<p>CPU_LOCKABLE</p>
<p>DISPLAY</p>
<p>BACK_BUFFER_CAST</p></td>
<td align="left"><p>9_1</p>
<p>9_1</p>
<p>9_1</p>
<p>9_1</p>
<p>9_1</p>
<p>9_1</p>
<p>9_1</p>
<p>9_1</p>
<p>9_1</p>
<p>9_1</p>
<p>9_1</p>
<p>9_1</p></td>
</tr>
<tr class="odd">
<td align="left">Q8W8V8U8</td>
<td align="left">R8G8B8A8_SNORM</td>
<td align="left"><p>TEXTURE2D</p>
<p>TEXTURECUBE</p>
<p>SHADER_LOAD</p>
<p>SHADER_SAMPLE</p>
<p>MIP</p>
<p>CPU_LOCKABLE</p></td>
<td align="left"><p>9_1</p>
<p>9_1</p>
<p>9_1</p>
<p>9_1</p>
<p>9_1</p>
<p>9_1</p></td>
</tr>
<tr class="even">
<td align="left">A8R8G8B8</td>
<td align="left">B8G8R8A8_UNORM</td>
<td align="left"><p>TEXTURE2D</p>
<p>TEXTURE3D</p>
<p>TEXTURECUBE</p>
<p>SHADER_LOAD</p>
<p>SHADER_SAMPLE</p>
<p>MIP</p>
<p>MIP_AUTOGEN</p>
<p>RENDER_TARGET</p>
<p>BLENDABLE</p>
<p>CPU_LOCKABLE</p>
<p>DISPLAY</p>
<p>BACK_BUFFER_CAST</p></td>
<td align="left"><p>9_1</p>
<p>9_1</p>
<p>9_1</p>
<p>9_1</p>
<p>9_1</p>
<p>9_1</p>
<p>9_1</p>
<p>9_1</p>
<p>9_1</p>
<p>9_1</p>
<p>9_1</p>
<p>9_1</p></td>
</tr>
<tr class="odd">
<td align="left">X8R8G8B8</td>
<td align="left">B8G8R8X8_UNORM</td>
<td align="left"><p>TEXTURE2D</p>
<p>TEXTURE3D</p>
<p>TEXTURECUBE</p>
<p>SHADER_LOAD</p>
<p>SHADER_SAMPLE</p>
<p>MIP</p>
<p>MIP_AUTOGEN</p>
<p>RENDER_TARGET</p>
<p>BLENDABLE</p>
<p>CPU_LOCKABLE</p></td>
<td align="left"><p>9_1</p>
<p>9_1</p>
<p>9_1</p>
<p>9_1</p>
<p>9_1</p>
<p>9_1</p>
<p>9_1</p>
<p>9_1</p>
<p>9_1</p>
<p>9_1</p></td>
</tr>
<tr class="even">
<td align="left">A8R8G8B8</td>
<td align="left">B8G8R8A8_UNORM_SRGB</td>
<td align="left"><p>TEXTURE2D</p>
<p>TEXTURE3D</p>
<p>TEXTURECUBE</p>
<p>SHADER_LOAD</p>
<p>SHADER_SAMPLE</p>
<p>MIP</p>
<p>MIP_AUTOGEN</p>
<p>RENDER_TARGET</p>
<p>BLENDABLE</p>
<p>CPU_LOCKABLE</p>
<p>DISPLAY</p>
<p>BACK_BUFFER_CAST</p></td>
<td align="left"><p>9_1</p>
<p>9_1</p>
<p>9_1</p>
<p>9_1</p>
<p>9_1</p>
<p>9_1</p>
<p>9_1</p>
<p>9_1</p>
<p>9_1</p>
<p>9_1</p>
<p>9_1</p>
<p>9_1</p></td>
</tr>
<tr class="odd">
<td align="left">X8R8G8B8</td>
<td align="left">B8G8R8X8_UNORM_SRGB</td>
<td align="left"><p>TEXTURE2D</p>
<p>TEXTURE3D</p>
<p>TEXTURECUBE</p>
<p>SHADER_LOAD</p>
<p>SHADER_SAMPLE</p>
<p>MIP</p>
<p>MIP_AUTOGEN</p>
<p>RENDER_TARGET</p>
<p>BLENDABLE</p>
<p>CPU_LOCKABLE</p></td>
<td align="left"><p>9_1</p>
<p>9_1</p>
<p>9_1</p>
<p>9_1</p>
<p>9_1</p>
<p>9_1</p>
<p>9_1</p>
<p>9_1</p>
<p>9_1</p>
<p>9_1</p></td>
</tr>
<tr class="even">
<td align="left">G16R16F or D3DDECLTYPE_FLOAT16_2</td>
<td align="left">R16G16_FLOAT</td>
<td align="left"><p>IA_VERTEX_BUFFER</p>
<p>TEXTURE2D</p>
<p>TEXTURE3D</p>
<p>TEXTURECUBE</p>
<p>SHADER_LOAD</p>
<p>MIP</p>
<p>MIP_AUTOGEN</p>
<p>RENDER_TARGET</p>
<p>CPU_LOCKABLE</p></td>
<td align="left"><p>9_3</p>
<p>9_2</p>
<p>9_2</p>
<p>9_2</p>
<p>9_2</p>
<p>9_2</p>
<p>9_2</p>
<p>9_2</p>
<p>9_2</p></td>
</tr>
<tr class="odd">
<td align="left">G16R16 or D3DDECLTYPE_USHORT2N</td>
<td align="left">R16G16_UNORM</td>
<td align="left"><p>TEXTURE2D</p>
<p>TEXTURE3D</p>
<p>TEXTURECUBE</p>
<p>SHADER_LOAD</p>
<p>SHADER_SAMPLE</p>
<p>MIP</p>
<p>MIP_AUTOGEN</p>
<p>RENDER_TARGET</p>
<p>CPU_LOCKABLE</p></td>
<td align="left"><p>9_2</p>
<p>9_2</p>
<p>9_2</p>
<p>9_2</p>
<p>9_2</p>
<p>9_2</p>
<p>9_2</p>
<p>9_2</p>
<p>9_2</p></td>
</tr>
<tr class="even">
<td align="left">V16U16 or D3DDECLTYPE_SHORT2N</td>
<td align="left">R16G16_SNORM</td>
<td align="left"><p>IA_VERTEX_BUFFER</p>
<p>TEXTURE2D</p>
<p>TEXTURE3D</p>
<p>TEXTURECUBE</p>
<p>SHADER_LOAD</p>
<p>SHADER_SAMPLE</p>
<p>MIP</p>
<p>CPU_LOCKABLE</p></td>
<td align="left"><p>9_1</p>
<p>9_1</p>
<p>9_2</p>
<p>9_2</p>
<p>9_1</p>
<p>9_2</p>
<p>9_1</p>
<p>9_1</p></td>
</tr>
<tr class="odd">
<td align="left">D3DDECLTYPE_SHORT2</td>
<td align="left">R16G16_SINT</td>
<td align="left"><p>IA_VERTEX_BUFFER</p></td>
<td align="left"><p>9_1</p></td>
</tr>
<tr class="even">
<td align="left">R32F or D3DDECLTYPE_FLOAT1</td>
<td align="left">R32_FLOAT</td>
<td align="left"><p>IA_VERTEX_BUFFER</p>
<p>TEXTURE2D</p>
<p>TEXTURE3D</p>
<p>TEXTURECUBE</p>
<p>SHADER_LOAD</p>
<p>MIP</p>
<p>MIP_AUTOGEN</p>
<p>RENDER_TARGET</p>
<p>CPU_LOCKABLE</p></td>
<td align="left"><p>9_1</p>
<p>9_2</p>
<p>9_2</p>
<p>9_2</p>
<p>9_2</p>
<p>9_2</p>
<p>9_2</p>
<p>9_2</p>
<p>9_2</p></td>
</tr>
<tr class="odd">
<td align="left"></td>
<td align="left">R32_UINT</td>
<td align="left"><p>IA_INDEX_BUFFER</p></td>
<td align="left"><p>9_1</p></td>
</tr>
<tr class="even">
<td align="left">S8D24 or D24S8</td>
<td align="left">D24_UNORM_S8_UINT</td>
<td align="left"><p>TEXTURE2D</p>
<p>DEPTH_STENCIL</p></td>
<td align="left"><p>9_1</p>
<p>9_1</p></td>
</tr>
<tr class="odd">
<td align="left">L16</td>
<td align="left">R16_UNORM</td>
<td align="left"><p>TEXTURE2D</p>
<p>TEXTURE3D</p>
<p>TEXTURECUBE</p>
<p>SHADER_LOAD</p>
<p>SHADER_SAMPLE</p>
<p>MIP</p>
<p>CPU_LOCKABLE</p></td>
<td align="left"><p>9_2</p>
<p>9_2</p>
<p>9_2</p>
<p>9_2</p>
<p>9_2</p>
<p>9_2</p>
<p>9_2</p></td>
</tr>
<tr class="even">
<td align="left"></td>
<td align="left">R16_UINT</td>
<td align="left"><p>IA_INDEX_BUFFER</p></td>
<td align="left"><p>9_1</p></td>
</tr>
<tr class="odd">
<td align="left">D16 or D16_LOCKABLE</td>
<td align="left">D16_UNORM</td>
<td align="left"><p>TEXTURE2D</p>
<p>DEPTH_STENCIL</p></td>
<td align="left"><p>9_1</p>
<p>9_1</p></td>
</tr>
<tr class="even">
<td align="left">V8U8</td>
<td align="left">R8G8_SNORM</td>
<td align="left"><p>TEXTURE2D</p>
<p>SHADER_LOAD</p>
<p>SHADER_SAMPLE</p>
<p>MIP</p>
<p>CPU_LOCKABLE</p></td>
<td align="left"><p>9_1</p>
<p>9_1</p>
<p>9_1</p>
<p>9_1</p>
<p>9_1</p></td>
</tr>
<tr class="odd">
<td align="left">L8</td>
<td align="left">R8_UNORM</td>
<td align="left"><p>TEXTURE2D</p>
<p>TEXTURE3D</p>
<p>TEXTURECUBE</p>
<p>SHADER_LOAD</p>
<p>SHADER_SAMPLE</p>
<p>MIP</p>
<p>CPU_LOCKABLE</p></td>
<td align="left"><p>9_1</p>
<p>9_1</p>
<p>9_1</p>
<p>9_1</p>
<p>9_1</p>
<p>9_1</p>
<p>9_1</p></td>
</tr>
<tr class="even">
<td align="left">DXT1</td>
<td align="left">BC1_UNORM or BC1_UNORM_SRGB</td>
<td align="left"><p>TEXTURE2D</p>
<p>TEXTURECUBE</p>
<p>SHADER_LOAD</p>
<p>SHADER_SAMPLE</p>
<p>MIP</p>
<p>CPU_LOCKABLE</p></td>
<td align="left"><p>9_1</p>
<p>9_1</p>
<p>9_1</p>
<p>9_1</p>
<p>9_1</p>
<p>9_1</p></td>
</tr>
<tr class="odd">
<td align="left">DXT2</td>
<td align="left">BC2_UNORM or BC2_UNORM_SRGB</td>
<td align="left"><p>TEXTURE2D</p>
<p>TEXTURECUBE</p>
<p>SHADER_LOAD</p>
<p>SHADER_SAMPLE</p>
<p>MIP</p>
<p>CPU_LOCKABLE</p></td>
<td align="left"><p>9_1</p>
<p>9_1</p>
<p>9_1</p>
<p>9_1</p>
<p>9_1</p>
<p>9_1</p></td>
</tr>
<tr class="even">
<td align="left">DXT4</td>
<td align="left">BC3_UNORM or BC3_UNORM_SRGB</td>
<td align="left"><p>TEXTURE2D</p>
<p>TEXTURECUBE</p>
<p>SHADER_LOAD</p>
<p>SHADER_SAMPLE</p>
<p>MIP</p>
<p>CPU_LOCKABLE</p></td>
<td align="left"><p>9_1</p>
<p>9_1</p>
<p>9_1</p>
<p>9_1</p>
<p>9_1</p>
<p>9_1</p></td>
</tr>
</tbody>
</table>

 

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Required D3D10_ or D3D11_ FORMAT_SUPPORT_* enumeration values</th>
<th align="left">Support algorithm in Direct3D 10Level 9</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>BACK_BUFFER_CAST</p></td>
<td align="left"><p>Assumed true for any format that supports DISPLAY.</p></td>
</tr>
<tr class="even">
<td align="left"><p>BLENDABLE</p></td>
<td align="left"><p>No FORMATOP_NOALPHABLEND</p></td>
</tr>
<tr class="odd">
<td align="left"><p>CPU_LOCKABLE</p></td>
<td align="left"><p>Assumed always true.</p></td>
</tr>
<tr class="even">
<td align="left"><p>DISPLAY</p></td>
<td align="left"><p>Hard-coded.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>IA_VERTEX_BUFFER</p></td>
<td align="left"><p>D3DDTCAPS_* (See Note.)</p></td>
</tr>
<tr class="even">
<td align="left"><p>MIP</p></td>
<td align="left"><p>No FORMATOP_NOTEXCOORDWRAPNORMIP</p></td>
</tr>
<tr class="odd">
<td align="left"><p>MIP_AUTOGEN</p></td>
<td align="left"><p>(See Note.)</p></td>
</tr>
<tr class="even">
<td align="left"><p>RENDER_TARGET</p></td>
<td align="left"><p>FORMATOP_OFFSCREEN_RENDERTARGET</p></td>
</tr>
<tr class="odd">
<td align="left"><p>SHADER_LOAD</p></td>
<td align="left"><p>Assumed for all non-depth formats.</p></td>
</tr>
<tr class="even">
<td align="left"><p>SHADER_SAMPLE</p></td>
<td align="left"><p>(See Note.)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>TEXTURE2D</p></td>
<td align="left"><p>FORMATOP_TEXTURE</p></td>
</tr>
<tr class="even">
<td align="left"><p>TEXTURE3D</p></td>
<td align="left"><p>FORMATOP_VOLUMETEXTURE</p></td>
</tr>
<tr class="odd">
<td align="left"><p>TEXTURECUBE</p></td>
<td align="left"><p>FORMATOP_CUBETEXTURE</p></td>
</tr>
</tbody>
</table>

 

**Note**  These are further details on the support algorithm's requirements in Direct3D 10Level 9:
-   The IA\_VERTEX\_BUFFER and/or IA\_INDEX\_BUFFER formats are supported by software vertex processing if there is no D3DDEVCAPS\_HWTRANSFORMANDLIGHT capability.
-   The TEXTURE2D format can also be inferred from it being a depth-stencil format.
-   For the SHADER\_SAMPLE format, the driver must support FORMATOP\_TEXTURE, FORMATOP\_VOLUMETEXTURE, or FORMATOP\_CUBETEXTURE, and it must not report FORMATOP\_NOFILTER.
-   For the MIP\_AUTOGEN format, Direct3D 10Level 9 generates its own mip-maps, so it requires MIP, RENDER\_TARGET, and TEXTURE2D bits.

 

 

 





