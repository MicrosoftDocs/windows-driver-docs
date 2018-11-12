---
title: Instruction Token
description: Instruction Token
ms.assetid: bfeee1ad-aaf3-41d0-a667-15d22eccd1e9
ms.date: 01/05/2018
ms.localizationpriority: medium
---

# Instruction Token


## <span id="ddk_instruction_token_gg"></span><span id="DDK_INSTRUCTION_TOKEN_GG"></span>


An instruction token informs the driver of a specific operation to perform and is composed of the following bits:

### <span id="bits"></span><span id="BITS"></span>Bits

<span id="_15_00_"></span>**\[15:00\]**
Bits 0 through 15 indicate an [operation code](https://msdn.microsoft.com/library/windows/hardware/ff569706). D3DSIO\_\* is an example of an operation code, where \* represents the instruction. For example, the following code snippet shows an [ADD instruction](https://msdn.microsoft.com/library/windows/hardware/ff538212):

```cpp
// D3DSIO_ADD d, s1, s2
```

<span id="_23_16_"></span>**\[23:16\]**
Bits 16 through 23 indicate specific controls related to the operation code.

<span id="_27_24_"></span>**\[27:24\]**
For pixel and vertex shader versions earlier than 2\_0, bits 24 through 27 are reserved and set to 0x0.

For pixel and vertex shader versions 2\_0 and later, bits 24 through 27 specify the size in DWORDs of the instruction excluding the instruction token itself (that is, the number of tokens that comprise the instruction excluding the instruction token).

<span id="_28_"></span>**\[28\]**
For pixel and vertex shader versions earlier than 2\_0, bit 28 is reserved and set to 0x0.

For pixel and vertex shader versions 2\_0 and later, bit 28 indicates whether the instruction is predicated (that is, contains an extra predicate source token at the end of the shader code. If this bit is set to 0x1, the instruction is predicated.

<span id="_29_"></span>**\[29\]**
Reserved. This value is set to 0x0.

<span id="_30_"></span>**\[30\]**
For pixel shader versions earlier than 2\_0, bit 30 is the co-issue bit. If set to 1, execute this instruction with previous instructions; otherwise, execute separately.

For pixel shader version 2\_0 and later and all vertex shader versions, bit 30 is reserved and set to 0x0.

<span id="_31_"></span>**\[31\]**
Bit 31 is zero (0x0).

### <span id="comments"></span><span id="COMMENTS"></span>Comments

See the Pixel Shader Reference and Vertex Shader Reference in the latest DirectX SDK documentation for more information about operations that can be specified in bits 0 through 15 of instruction tokens.

After the DirectX3D runtime receives shader code from an application, the runtime validates the code before passing the code to the driver. Typically, the runtime prefixes assembler instructions with "D3DSIO\_" to create the operation code. For example, the following assembler instructions correspond to kernel-mode operations:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Assembler instruction</th>
<th align="left">Kernel-mode operation</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>add</strong></p></td>
<td align="left"><p>D3DSIO_ADD</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>mov</strong></p></td>
<td align="left"><p>D3DSIO_MOV</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>sub</strong></p></td>
<td align="left"><p>D3DSIO_SUB</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>tex</strong></p></td>
<td align="left"><p>D3DSIO_TEX</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>texcoord</strong></p></td>
<td align="left"><p>D3DSIO_TEXCOORD</p></td>
</tr>
</tbody>
</table>

 

Note that in all vertex shader versions, the **sub** assembler instruction is implemented as a D3DSIO\_ADD operation with the source modifier (bits 27:24) of the second source set to negate (0x1).

The **tex** and **texcoord** instructions apply to pixel shader versions 1\_0 through 1\_3; each instruction has one [destination parameter](destination-parameter-token.md) associated with it.

The **texld** and **texcrd** instructions are new to pixel shader version 1\_4 and later; each instruction has both destination and [source parameters](source-parameter-token.md) associated with it.

The runtime converts the **tex** and **texld** assembler instructions to the D3DSIO\_TEX kernel-mode operation. The runtime converts the **texcoord** and **texcrd** assembler instructions to the D3DSIO\_TEXCOORD kernel-mode operation. Drivers first verify the pixel shader version of the shader code and then process the instructions accordingly. For example, if a driver verifies that it received version 1\_4 pixel shader code with a D3DSIO\_TEX operation, the driver determines that destination and source parameters follow the instruction token.

## <span id="Requirements"></span><span id="requirements"></span><span id="REQUIREMENTS"></span>Requirements


Available in Windows Vista and later versions of the Windows operating systems.

 

 





