---
title: Source Parameter Token
description: Source Parameter Token
ms.assetid: 280b9fb2-9b5c-4830-9ba5-cfb6201960e0
ms.date: 01/05/2018
ms.localizationpriority: medium
---

# Source Parameter Token


## <span id="ddk_source_parameter_token_gg"></span><span id="DDK_SOURCE_PARAMETER_TOKEN_GG"></span>


A source parameter token describes properties of a source register and is composed of the following bits:

### <span id="bits"></span><span id="BITS"></span>Bits

<span id="_10_00_"></span>**\[10:00\]**
Bits 0 through 10 indicate the register number (offset in register file).

<span id="_12_11_"></span>**\[12:11\]**
Bits 11 and 12 are the fourth and fifth bits \[3,4\] for indicating the [register type](https://msdn.microsoft.com/library/windows/hardware/ff569707).

<span id="_13_"></span>**\[13\]**
For a pixel shader (PS) versions earlier than 3\_0, bit 13 is reserved and set to 0x0.

For pixel shader (PS) version 3\_0 and later and all versions of vertex shader (VS), bit 13 indicates whether relative addressing mode is used. If set to 1, [relative addressing](shader-relative-addressing.md) applies.

<span id="_15_14_"></span>**\[15:14\]**
Reserved for all versions of PS and VS. This value is set to 0x0.

<span id="_23_16_"></span>**\[23:16\]**
Bits 16 through 23 indicate channel *swizzle*. All arithmetic operations are performed in four (X,Y,Z,W) parallel channels. Swizzle specifies which source component participates in a channel of operation. For more information about swizzle, see the latest DirectX SDK documentation. The bits of this field specify swizzle for the following channels:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Bits</th>
<th align="left">Channel</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>17:16</p></td>
<td align="left"><p>Channel X swizzle</p></td>
</tr>
<tr class="even">
<td align="left"><p>19:18</p></td>
<td align="left"><p>Channel Y swizzle</p></td>
</tr>
<tr class="odd">
<td align="left"><p>21:20</p></td>
<td align="left"><p>Channel Z swizzle</p></td>
</tr>
<tr class="even">
<td align="left"><p>23:22</p></td>
<td align="left"><p>Channel W swizzle</p></td>
</tr>
</tbody>
</table>

 

The following values in any set of preceding bits specify the source component to be used in the channel of operation:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Value</th>
<th align="left">Component</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>0x0</p></td>
<td align="left"><p>Component X is used.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x1</p></td>
<td align="left"><p>Component Y is used.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x2</p></td>
<td align="left"><p>Component Z is used.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x3</p></td>
<td align="left"><p>Component W is used.</p></td>
</tr>
</tbody>
</table>

 

For example, if the 19:18 bits are set to 0x2, then component Z is used as the source for the channel Y operation.

<span id="_27_24_"></span>**\[27:24\]**
Bits 24 through 27 indicate the source modifier. This 4-bit value indicates the following source modifier types:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Value</th>
<th align="left">Source modifier type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>0x0</p></td>
<td align="left"><p>None</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x1</p></td>
<td align="left"><p>Negate</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x2</p></td>
<td align="left"><p>Bias</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x3</p></td>
<td align="left"><p>Bias and negate</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x4</p></td>
<td align="left"><p>Sign (bx2)</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x5</p></td>
<td align="left"><p>Sign (bx2) and negate</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x6</p></td>
<td align="left"><p>Complement</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x7</p></td>
<td align="left"><p>x2 (PS 1_4)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x8</p></td>
<td align="left"><p>x2 and negate (PS 1_4)</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x9</p></td>
<td align="left"><p>dz (divide through by Z component - PS 1_4)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0xa</p></td>
<td align="left"><p>dw (divide through by W component âˆ’ PS 1_4)</p></td>
</tr>
<tr class="even">
<td align="left"><p>0xb</p></td>
<td align="left"><p>abs(x) compute absolute value</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0xc</p></td>
<td align="left"><p>-abs(x) compute absolute value and negate</p></td>
</tr>
<tr class="even">
<td align="left"><p>0xd</p></td>
<td align="left"><p>NOT. Applied only to the predication register, which is BOOL. Therefore, it is logical NOT.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0xe-0xf</p></td>
<td align="left"><p>Reserved</p></td>
</tr>
</tbody>
</table>

 

<span id="_30_28_"></span>**\[30:28\]**
Bits 28 through 30 are the first three bits \[0,1,2\] for indicating the [register type](https://msdn.microsoft.com/library/windows/hardware/ff569707).

<span id="_31_"></span>**\[31\]**
Bit 31 is 0x1.

### <span id="comments"></span><span id="COMMENTS"></span>Comments

Bits 28, 29, 30, 11, and 12 form a 5-bit value that indicates the register type. For information about register types, see [Shader Register Types](https://msdn.microsoft.com/library/windows/hardware/ff569707).

## <span id="Requirements"></span><span id="requirements"></span><span id="REQUIREMENTS"></span>Requirements


Available in Windows Vista and later versions of the Windows operating systems.

 

 





