---
title: Alpha-Blend Combination
description: Alpha-Blend Combination
ms.assetid: 567810da-ad8d-4ceb-b914-868632384d09
keywords: ["alpha-blend combination WDK DirectX VA", "blended pictures WDK DirectX VA", "alpha-blend combination WDK DirectX VA , about alpha-blend combination", "blended pictures WDK DirectX VA , about alpha-blend combination"]
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
<td align="left"><p>[<strong>DXVA_BufferDescription</strong>](https://msdn.microsoft.com/library/windows/hardware/ff563122)</p></td>
<td align="left"><p>Specifies the alpha-blend combination buffer to be used. This buffer governs the generation of a blended picture from a source picture and alpha-blending information.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>DXVA_BlendCombination</strong>](https://msdn.microsoft.com/library/windows/hardware/ff563120)</p></td>
<td align="left"><p>Specifies how a blended picture is generated from an alpha-blend combination buffer.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>DXVA_ConfigAlphaCombine</strong>](https://msdn.microsoft.com/library/windows/hardware/ff563126)</p></td>
<td align="left"><p>Establishes the configuration for how alpha-blending combination operations are to be performed.</p></td>
</tr>
</tbody>
</table>

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Alpha-Blend%20Combination%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




