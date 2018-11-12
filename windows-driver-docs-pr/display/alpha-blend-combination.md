---
title: Alpha-Blend Combination
description: Alpha-Blend Combination
ms.assetid: 567810da-ad8d-4ceb-b914-868632384d09
keywords:
- alpha-blend combination WDK DirectX VA
- blended pictures WDK DirectX VA
- alpha-blend combination WDK DirectX VA , about alpha-blend combination
- blended pictures WDK DirectX VA , about alpha-blend combination
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Alpha-Blend Combination


## <span id="ddk_alpha_blend_combination_gg"></span><span id="DDK_ALPHA_BLEND_COMBINATION_GG"></span>


When the [bDXVA\_Func variable](bdxva-func-variable.md) is equal to 3, the operation specified is an alpha-blend combination. An alpha-blend combination takes the last loaded alpha-blend source information and combines it with a reference picture to create a blended picture for display.

The alpha-blend combination buffer specified by the **dwTypeIndex** member of the [**DXVA\_BufferDescription**](https://msdn.microsoft.com/library/windows/hardware/ff563122) structure is used to generate a blended picture from a source picture and alpha-blending information. In the event that the source and destination pictures are not in 4:4:4 format, every second sample (for example, the first, third, fifth, and so on) of the graphic blending information in an AYUV alpha-blending surface or equivalent is applied to the (lower resolution) source chrominance information in the vertical or horizontal direction, as applicable, to produce the blended result.

The following structures are used to implement alpha-blend combination.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Structure</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff563122" data-raw-source="[&lt;strong&gt;DXVA_BufferDescription&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff563122)"><strong>DXVA_BufferDescription</strong></a></p></td>
<td align="left"><p>Specifies the alpha-blend combination buffer to be used. This buffer governs the generation of a blended picture from a source picture and alpha-blending information.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff563120" data-raw-source="[&lt;strong&gt;DXVA_BlendCombination&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff563120)"><strong>DXVA_BlendCombination</strong></a></p></td>
<td align="left"><p>Specifies how a blended picture is generated from an alpha-blend combination buffer.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff563126" data-raw-source="[&lt;strong&gt;DXVA_ConfigAlphaCombine&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff563126)"><strong>DXVA_ConfigAlphaCombine</strong></a></p></td>
<td align="left"><p>Establishes the configuration for how alpha-blending combination operations are to be performed.</p></td>
</tr>
</tbody>
</table>

 

 

 





