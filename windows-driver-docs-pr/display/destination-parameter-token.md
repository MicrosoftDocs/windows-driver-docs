---
title: Destination Parameter Token
description: Destination Parameter Token
ms.assetid: 1a9842c5-0ea9-47ee-a341-77e705ab5e25
ms.author: windowsdriverdev
ms.date: 01/05/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Destination Parameter Token


## <span id="ddk_destination_parameter_token_gg"></span><span id="DDK_DESTINATION_PARAMETER_TOKEN_GG"></span>


A destination parameter token describes properties of a destination register and is composed of the following bits:

### <span id="bits"></span><span id="BITS"></span>Bits

<span id="_10_00_"></span>**\[10:00\]**
Bits 0 through 10 indicate the register number (offset in register file).

<span id="_12_11_"></span>**\[12:11\]**
Bits 11 and 12 are the fourth and fifth bits \[3,4\] for indicating the [register type](https://msdn.microsoft.com/library/windows/hardware/ff569707).

<span id="_13_"></span>**\[13\]**
For vertex shader (VS) version 3\_0 and later, bit 13 indicates whether relative addressing mode is used. If set to 1, [relative addressing](shader-relative-addressing.md) applies.

For all pixel shader (PS) versions and vertex shader versions earlier than 3\_0, bit 13 is reserved and set to 0x0.

<span id="_15_14_"></span>**\[15:14\]**
Reserved. This value is set to 0x0.

<span id="_19_16_"></span>**\[19:16\]**
Write mask. The bits of this mask have the following components:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Bit</th>
<th align="left">Component</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>16</p></td>
<td align="left"><p>Component 0 (X;Red)</p></td>
</tr>
<tr class="even">
<td align="left"><p>17</p></td>
<td align="left"><p>Component 1 (Y;Green)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>18</p></td>
<td align="left"><p>Component 2 (Z;Blue)</p></td>
</tr>
<tr class="even">
<td align="left"><p>19</p></td>
<td align="left"><p>Component 3 (W;Alpha)</p></td>
</tr>
</tbody>
</table>

 

<span id="_23_20_"></span>**\[23:20\]**
Bits 20 through 23 indicate the result modifier. Multiple result modifiers can be used. The following result modifier types can be ORed together in this 4-bit value:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Value</th>
<th align="left">Result modifier type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>0x1</p></td>
<td align="left"><p>Saturate (vertex shaders)</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x2</p></td>
<td align="left"><p>Partial precision (pixel shaders)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x4</p></td>
<td align="left"><p>Centroid (pixel shaders)</p></td>
</tr>
</tbody>
</table>

 

<span id="_27_24_"></span>**\[27:24\]**
For PS versions earlier than 2\_0, bits 24 through 27 specify the result shift scale (signed shift).
For PS version 2\_0 and later and VS, these bits are reserved and set to 0x0.
<span id="_30_28_"></span>**\[30:28\]**
Bits 28 through 30 are the first three bits \[0,1,2\] for indicating the [register type](https://msdn.microsoft.com/library/windows/hardware/ff569707).

<span id="_31_"></span>**\[31\]**
Bit 31 is 0x1.

### <span id="comments"></span><span id="COMMENTS"></span>Comments

Bits 28, 29, 30, 11, and 12 form a 5-bit value that indicates the register type. For information about register types, see [Shader Register Types](https://msdn.microsoft.com/library/windows/hardware/ff569707).

## <span id="Requirements"></span><span id="requirements"></span><span id="REQUIREMENTS"></span>Requirements


Available in Windows Vista and later versions of the Windows operating systems.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Destination%20Parameter%20Token%20%20RELEASE:%20%281/4/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




