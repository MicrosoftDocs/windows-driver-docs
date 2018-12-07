---
title: Destination Parameter Token
description: Destination Parameter Token
ms.assetid: 1a9842c5-0ea9-47ee-a341-77e705ab5e25
ms.date: 01/05/2018
ms.localizationpriority: medium
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

 

 





