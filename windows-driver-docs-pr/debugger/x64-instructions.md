---
title: x64 Instructions
description: x64 Instructions
ms.assetid: f05cbf3e-001c-43cc-8a53-0e22fd161a53
keywords: ["x64 processor, instructions"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# x64 Instructions


## <span id="ddk_x64_instructions_dbg"></span><span id="DDK_X64_INSTRUCTIONS_DBG"></span>


Most x86 instructions continue to be valid for x64 in 64-bit mode. Some rarely-used operations are no longer supported in 64-bit mode, such as:

-   binary-coded decimal arithmetic instructions: AAA, AAD, AAM, AAS, DAA, DAS

-   BOUND

-   PUSHAD and POPAD

-   most operations that dealt with segment registers, such as PUSH DS and POP DS. (Operations that use the FS or GS segment registers are still valid.)

The x64 instruction set includes recent additions to the x86, such as SSE 2. Programs compiled for x64 can freely use these instructions.

### <span id="Data_Transfer"></span><span id="data_transfer"></span><span id="DATA_TRANSFER"></span>Data Transfer

The x64 provides new variants of the MOV instruction that can handle 64-bit immediate constants or memory addresses.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>MOV</p></td>
<td align="left"><p><strong>r</strong>,#n</p></td>
<td align="left"><p><strong>r</strong> = #n</p></td>
</tr>
<tr class="even">
<td align="left"><p>MOV</p></td>
<td align="left"><p><strong>rax</strong>, m</p></td>
<td align="left"><p>Move contents at 64-bit address to <strong>rax</strong>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>MOV</p></td>
<td align="left"><p>m, <strong>rax</strong></p></td>
<td align="left"><p>Move contents of <strong>rax</strong> to 64-bit address.</p></td>
</tr>
</tbody>
</table>

 

The x64 also provides a new instruction to sign-extend 32-bit operands to 64 bits.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>MOVSXD</p></td>
<td align="left"><p><strong>r1</strong>, <strong>r</strong>/m</p></td>
<td align="left"><p>Move DWORD with sign extension to QWORD.</p></td>
</tr>
</tbody>
</table>

 

Ordinary MOV operations into 32-bit subregisters automatically zero extend to 64 bits, so there is no MOVZXD instruction.

Two SSE instructions can be used to move 128-bit values (such as GUIDs) from memory to an **xmm***n* register or vice versa.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>MOVDQA</p></td>
<td align="left"><p><strong>r1</strong>/m, <strong>r2</strong>/m</p></td>
<td align="left"><p>Move 128-bit aligned value to <strong>xmm</strong><em>n</em> register, or vice versa.</p></td>
</tr>
<tr class="even">
<td align="left"><p>MOVDQU</p></td>
<td align="left"><p><strong>r1</strong>/m, <strong>r2</strong>/m</p></td>
<td align="left"><p>Move 128-bit value (not necessarily aligned) to register, or vice versa.</p></td>
</tr>
</tbody>
</table>

 

### <span id="Data_Conversion"></span><span id="data_conversion"></span><span id="DATA_CONVERSION"></span>Data Conversion

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>CDQE</p></td>
<td align="left"><p>Convert dword (<strong>eax</strong>) to qword (<strong>rax</strong>).</p></td>
</tr>
<tr class="even">
<td align="left"><p>CQO</p></td>
<td align="left"><p>convert qword (<strong>rax</strong>) to oword (<strong>rdx</strong>:<strong>rax</strong>).</p></td>
</tr>
</tbody>
</table>

 

### <span id="String_Manipulation"></span><span id="string_manipulation"></span><span id="STRING_MANIPULATION"></span>String Manipulation

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>MOVSQ</p></td>
<td align="left"><p>Move qword from <strong>rsi</strong> to <strong>rdi.</strong></p></td>
</tr>
<tr class="even">
<td align="left"><p>CMPSQ</p></td>
<td align="left"><p>Compare qword at <strong>rsi</strong> with <strong>rdi.</strong></p></td>
</tr>
<tr class="odd">
<td align="left"><p>SCASQ</p></td>
<td align="left"><p>Scan qword at <strong>rdi</strong>. Compares qword at <strong>rdi</strong> to <strong>rax</strong>.</p></td>
</tr>
<tr class="even">
<td align="left"><p>LODSQ</p></td>
<td align="left"><p>Load qword from <strong>rsi</strong> into <strong>rax</strong><em>.</em></p></td>
</tr>
<tr class="odd">
<td align="left"><p>STOSQ</p></td>
<td align="left"><p>Store qword to <strong>rdi</strong> from <strong>rax</strong><em>.</em></p></td>
</tr>
</tbody>
</table>

 

 

 





