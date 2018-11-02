---
title: x86 Instructions
description: x86 Instructions
ms.assetid: 237796d5-ef82-4eab-8d56-3191b3e63597
keywords: ["x86 processor, instructions", "x86 processor, arithmetic"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# x86 Instructions


## <span id="ddk_x86_instructions_dbg"></span><span id="DDK_X86_INSTRUCTIONS_DBG"></span>


In the lists in this section, instructions marked with an asterisk (**\\***) are particularly important. Instructions not so marked are not critical.

On the x86 processor, instructions are variable-sized, so disassembling backward is an exercise in pattern matching. To disassemble backward from an address, you should start disassembling at a point further back than you really want to go, then look forward until the instructions start making sense. The first few instructions may not make any sense because you may have started disassembling in the middle of an instruction. There is a possibility, unfortunately, that the disassembly will never synchronize with the instruction stream and you will have to try disassembling at a different starting point until you find a starting point that works.

For well-packed **switch** statements, the compiler emits data directly into the code stream, so disassembling through a **switch** statement will usually stumble across instructions that make no sense (because they are really data). Find the end of the data and continue disassembling there.

### <span id="Instruction_Notation"></span><span id="instruction_notation"></span><span id="INSTRUCTION_NOTATION"></span>Instruction Notation

The general notation for instructions is to put the destination register on the left and the source on the right. However, there can be some exceptions to this rule.

Arithmetic instructions are typically two-register with the source and destination registers combining. The result is stored into the destination.

Some of the instructions have both 16-bit and 32-bit versions, but only the 32-bit versions are listed here. Not listed here are floating-point instructions, privileged instructions, and instructions that are used only in segmented models (which Microsoft Win32 does not use).

To save space, many of the instructions are expressed in combined form, as shown in the following example.

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>*</strong></p></td>
<td align="left"><p>MOV</p></td>
<td align="left"><p><strong>r1</strong>, <strong>r</strong>/m/#n</p></td>
<td align="left"><p><strong>r1</strong> = <strong>r</strong>/m/#n</p></td>
</tr>
</tbody>
</table>

 

means that the first parameter must be a register, but the second can be a register, a memory reference, or an immediate value.

To save even more space, instructions can also be expressed as shown in the following.

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>*</strong></p></td>
<td align="left"><p>MOV</p></td>
<td align="left"><p><strong>r1</strong>/m, <strong>r</strong>/m/#n</p></td>
<td align="left"><p><strong>r1</strong>/m = <strong>r</strong>/m/#n</p></td>
</tr>
</tbody>
</table>

 

which means that the first parameter can be a register or a memory reference, and the second can be a register, memory reference, or immediate value.

Unless otherwise noted, when this abbreviation is used, you cannot choose memory for both source and destination.

Furthermore, a bit-size suffix (8, 16, 32) can be appended to the source or destination to indicate that the parameter must be of that size. For example, r8 means an 8-bit register.

### <span id="Memory__Data_Transfer__and_Data_Conversion"></span><span id="memory__data_transfer__and_data_conversion"></span><span id="MEMORY__DATA_TRANSFER__AND_DATA_CONVERSION"></span>Memory, Data Transfer, and Data Conversion

Memory and data transfer instructions do not affect flags.

### <span id="Effective_Address"></span><span id="effective_address"></span><span id="EFFECTIVE_ADDRESS"></span>Effective Address

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>*</strong></p></td>
<td align="left"><p>LEA</p></td>
<td align="left"><p><strong>r</strong>, m</p></td>
<td align="left"><p>Load effective address.</p>
<p>(r = address of m)</p></td>
</tr>
</tbody>
</table>

 

For example, **LEA eax, \[esi+4\]** means **eax** = **esi** + 4. This instruction is often used to perform arithmetic.

### <span id="Data_Transfer"></span><span id="data_transfer"></span><span id="DATA_TRANSFER"></span>Data Transfer

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong><em></strong></p></td>
<td align="left"><p>MOV</p></td>
<td align="left"><p><strong>r1</strong>/m, <strong>r2</strong>/m/#n</p></td>
<td align="left"><p><strong>r1</strong>/m = <strong>r</strong>/m/#n</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong></em></strong></p></td>
<td align="left"><p>MOVSX</p></td>
<td align="left"><p><strong>r1</strong>, <strong>r</strong>/m</p></td>
<td align="left"><p>Move with sign extension.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>*</strong></p></td>
<td align="left"><p>MOVZX</p></td>
<td align="left"><p><strong>r1</strong>, <strong>r</strong>/m</p></td>
<td align="left"><p>Move with zero extension.</p></td>
</tr>
</tbody>
</table>

 

**MOVSX** and **MOVZX** are special versions of the **mov** instruction that perform sign extension or zero extension from the source to the destination. This is the only instruction that allows the source and destination to be different sizes. (And in fact, they must be different sizes.

### <span id="Stack_Manipulation"></span><span id="stack_manipulation"></span><span id="STACK_MANIPULATION"></span>Stack Manipulation

The stack is pointed to by the **esp** register. The value at **esp** is the top of the stack (most recently pushed, first to be popped); older stack elements reside at higher addresses.

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong><em></strong></p></td>
<td align="left"><p>PUSH</p></td>
<td align="left"><p><strong>r</strong>/m/#n</p></td>
<td align="left"><p>Push value onto stack.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong></em></strong></p></td>
<td align="left"><p>POP</p></td>
<td align="left"><p><strong>r</strong>/m</p></td>
<td align="left"><p>Pop value from stack.</p></td>
</tr>
<tr class="odd">
<td align="left"></td>
<td align="left"><p>PUSHFD</p></td>
<td align="left"></td>
<td align="left"><p>Push flags onto stack.</p></td>
</tr>
<tr class="even">
<td align="left"></td>
<td align="left"><p>POPFD</p></td>
<td align="left"></td>
<td align="left"><p>Pop flags from stack.</p></td>
</tr>
<tr class="odd">
<td align="left"></td>
<td align="left"><p>PUSHAD</p></td>
<td align="left"></td>
<td align="left"><p>Push all integer registers.</p></td>
</tr>
<tr class="even">
<td align="left"></td>
<td align="left"><p>POPAD</p></td>
<td align="left"></td>
<td align="left"><p>Pop all integer registers.</p></td>
</tr>
<tr class="odd">
<td align="left"></td>
<td align="left"><p>ENTER</p></td>
<td align="left"><p>#n, #n</p></td>
<td align="left"><p>Build stack frame.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>*</strong></p></td>
<td align="left"><p>LEAVE</p></td>
<td align="left"></td>
<td align="left"><p>Tear down stack frame</p></td>
</tr>
</tbody>
</table>

 

The C/C++ compiler does not use the **enter** instruction. (The **enter** instruction is used to implement nested procedures in languages like Algol or Pascal.)

The **leave** instruction is equivalent to:

```asm
mov esp, ebp
pop ebp
```

### <span id="Data_Conversion"></span><span id="data_conversion"></span><span id="DATA_CONVERSION"></span>Data Conversion

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>CBW</p></td>
<td align="left"><p>Convert byte (<strong>al</strong>) to word (<strong>ax</strong>).</p></td>
</tr>
<tr class="even">
<td align="left"><p>CWD</p></td>
<td align="left"><p>Convert word (<strong>ax</strong>) to dword (<strong>dx</strong>:<strong>ax</strong>).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>CWDE</p></td>
<td align="left"><p>Convert word (<strong>ax</strong>) to dword (<strong>eax</strong>).</p></td>
</tr>
<tr class="even">
<td align="left"><p>CDQ</p></td>
<td align="left"><p>convert dword (<strong>eax</strong>) to qword (<strong>edx</strong>:<strong>eax</strong>).</p></td>
</tr>
</tbody>
</table>

 

All conversions perform sign extension.

### <span id="Arithmetic_and_Bit_Manipulation"></span><span id="arithmetic_and_bit_manipulation"></span><span id="ARITHMETIC_AND_BIT_MANIPULATION"></span>Arithmetic and Bit Manipulation

All arithmetic and bit manipulation instructions modify flags.

### <span id="Arithmetic"></span><span id="arithmetic"></span><span id="ARITHMETIC"></span>Arithmetic

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong><em></strong></p></td>
<td align="left"><p>ADD</p></td>
<td align="left"><p><strong>r1</strong>/m, <strong>r2</strong>/m/#n</p></td>
<td align="left"><p><strong>r1</strong>/m += <strong>r2</strong>/m/#n</p></td>
</tr>
<tr class="even">
<td align="left"></td>
<td align="left"><p>ADC</p></td>
<td align="left"><p><strong>r1</strong>/m, <strong>r2</strong>/m/#n</p></td>
<td align="left"><p><strong>r1</strong>/m += <strong>r2</strong>/m/#n + carry</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong></em></strong></p></td>
<td align="left"><p>SUB</p></td>
<td align="left"><p><strong>r1</strong>/m, <strong>r2</strong>/m/#n</p></td>
<td align="left"><p><strong>r1</strong>/m -= <strong>r2</strong>/m/#n</p></td>
</tr>
<tr class="even">
<td align="left"></td>
<td align="left"><p>SBB</p></td>
<td align="left"><p><strong>r1</strong>/m, <strong>r2</strong>/m/#n</p></td>
<td align="left"><p><strong>r1</strong>/m -= <strong>r2</strong>/m/#n + carry</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong><em></strong></p></td>
<td align="left"><p>NEG</p></td>
<td align="left"><p><strong>r1</strong>/m</p></td>
<td align="left"><p><strong>r1</strong>/m = -<strong>r1</strong>/m</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong></em></strong></p></td>
<td align="left"><p>INC</p></td>
<td align="left"><p><strong>r</strong>/m</p></td>
<td align="left"><p><strong>r</strong>/m += 1</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong><em></strong></p></td>
<td align="left"><p>DEC</p></td>
<td align="left"><p><strong>r</strong>/m</p></td>
<td align="left"><p><strong>r</strong>/m -= 1</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong></em></strong></p></td>
<td align="left"><p>CMP</p></td>
<td align="left"><p><strong>r1</strong>/m, <strong>r2</strong>/m/#n</p></td>
<td align="left"><p>Compute <strong>r1</strong>/m - <strong>r2</strong>/m/#n</p></td>
</tr>
</tbody>
</table>

 

The **cmp** instruction computes the subtraction and sets flags according to the result, but throws the result away. It is typically followed by a conditional **jump** instruction that tests the result of the subtraction.

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"></td>
<td align="left"><p>MUL</p></td>
<td align="left"><p><strong>r</strong>/m8</p></td>
<td align="left"><p><strong>ax</strong> = <strong>al</strong> * <strong>r</strong>/m8</p></td>
</tr>
<tr class="even">
<td align="left"></td>
<td align="left"><p>MUL</p></td>
<td align="left"><p><strong>r</strong>/m16</p></td>
<td align="left"><p><strong>dx</strong>:<strong>ax</strong> = <strong>ax</strong> * <strong>r</strong>/m16</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong><em></strong></p></td>
<td align="left"><p>MUL</p></td>
<td align="left"><p><strong>r</strong>/m32</p></td>
<td align="left"><p><strong>edx</strong>:<strong>eax</strong> = <strong>eax</strong> * <strong>r</strong>/m32</p></td>
</tr>
<tr class="even">
<td align="left"></td>
<td align="left"><p>IMUL</p></td>
<td align="left"><p><strong>r</strong>/m8</p></td>
<td align="left"><p><strong>ax</strong> = <strong>al</strong> * <strong>r</strong>/m8</p></td>
</tr>
<tr class="odd">
<td align="left"></td>
<td align="left"><p>IMUL</p></td>
<td align="left"><p><strong>r</strong>/m16</p></td>
<td align="left"><p><strong>dx</strong>:<strong>ax</strong> = <strong>ax</strong> * <strong>r</strong>/m16</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong></em></strong></p></td>
<td align="left"><p>IMUL</p></td>
<td align="left"><p><strong>r</strong>/m32</p></td>
<td align="left"><p><strong>edx</strong>:<strong>eax</strong> = <strong>eax</strong> * <strong>r</strong>/m32</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong><em></strong></p></td>
<td align="left"><p>IMUL</p></td>
<td align="left"><p><strong>r1</strong>, <strong>r2</strong>/m</p></td>
<td align="left"><p><strong>r1</strong> *= <strong>r2</strong>/m</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong></em></strong></p></td>
<td align="left"><p>IMUL</p></td>
<td align="left"><p><strong>r1</strong>, <strong>r2</strong>/m, #n</p></td>
<td align="left"><p><strong>r1</strong> = <strong>r2</strong>/m * #n</p></td>
</tr>
</tbody>
</table>

 

Unsigned and signed multiplication. The state of flags after multiplication is undefined.

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"></td>
<td align="left"><p>DIV</p></td>
<td align="left"><p><strong>r</strong>/m8</p></td>
<td align="left"><p>(<strong>ah</strong>, <strong>al</strong>) = (<strong>ax</strong> % <strong>r</strong>/m8, <strong>ax</strong> / <strong>r</strong>/m8)</p></td>
</tr>
<tr class="even">
<td align="left"></td>
<td align="left"><p>DIV</p></td>
<td align="left"><p><strong>r</strong>/m16</p></td>
<td align="left"><p>(<strong>dx</strong>, <strong>ax</strong>) = <strong>dx</strong>:<strong>ax</strong> / <strong>r</strong>/m16</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong><em></strong></p></td>
<td align="left"><p>DIV</p></td>
<td align="left"><p><strong>r</strong>/m32</p></td>
<td align="left"><p>(<strong>edx</strong>, <strong>eax</strong>) = <strong>edx</strong>:<strong>eax</strong> / <strong>r</strong>/m32</p></td>
</tr>
<tr class="even">
<td align="left"></td>
<td align="left"><p>IDIV</p></td>
<td align="left"><p><strong>r</strong>/m8</p></td>
<td align="left"><p>(<strong>ah</strong>, <strong>al</strong>) = <strong>ax</strong> / <strong>r</strong>/m8</p></td>
</tr>
<tr class="odd">
<td align="left"></td>
<td align="left"><p>IDIV</p></td>
<td align="left"><p><strong>r</strong>/m16</p></td>
<td align="left"><p>(<strong>dx</strong>, <strong>ax</strong>) = <strong>dx</strong>:<strong>ax</strong> / <strong>r</strong>/m16</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong></em></strong></p></td>
<td align="left"><p>IDIV</p></td>
<td align="left"><p><strong>r</strong>/m32</p></td>
<td align="left"><p>(<strong>edx</strong>, <strong>eax</strong>) = <strong>edx</strong>:<strong>eax</strong> / <strong>r</strong>/m32</p></td>
</tr>
</tbody>
</table>

 

Unsigned and signed division. The first register in the pseudocode explanation receives the remainder and the second receives the quotient. If the result overflows the destination, a division overflow exception is generated.

The state of flags after division is undefined.

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>*</p></td>
<td align="left"><p>SET<em>cc</em></p></td>
<td align="left"><p><strong>r</strong>/m8</p></td>
<td align="left"><p>Set <strong>r</strong>/m8 to 0 or 1</p></td>
</tr>
</tbody>
</table>

 

If the condition *cc* is true, then the 8-bit value is set to 1. Otherwise, the 8-bit value is set to zero.

### <span id="Binary-coded_Decimal"></span><span id="binary-coded_decimal"></span><span id="BINARY-CODED_DECIMAL"></span>Binary-coded Decimal

You will not see these instructions unless you are debugging code written in COBOL.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"></td>
<td align="left"><p>DAA</p></td>
<td align="left"><p>Decimal adjust after addition.</p></td>
</tr>
<tr class="even">
<td align="left"></td>
<td align="left"><p>DAS</p></td>
<td align="left"><p>Decimal adjust after subtraction.</p></td>
</tr>
</tbody>
</table>

 

These instructions adjust the **al** register after performing a packed binary-coded decimal operation.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>AAA</p></td>
<td align="left"><p>ASCII adjust after addition.</p></td>
</tr>
<tr class="even">
<td align="left"><p>AAS</p></td>
<td align="left"><p>ASCII adjust after subtraction.</p></td>
</tr>
</tbody>
</table>

 

These instructions adjust the **al** register after performing an unpacked binary-coded decimal operation.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>AAM</p></td>
<td align="left"><p>ASCII adjust after multiplication.</p></td>
</tr>
<tr class="even">
<td align="left"><p>AAD</p></td>
<td align="left"><p>ASCII adjust after division.</p></td>
</tr>
</tbody>
</table>

 

These instructions adjust the **al** and **ah** registers after performing an unpacked binary-coded decimal operation.

### <span id="Bits"></span><span id="bits"></span><span id="BITS"></span>Bits

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong><em></strong></p></td>
<td align="left"><p>AND</p></td>
<td align="left"><p><strong>r1</strong>/m, <strong>r2</strong>/m/#n</p></td>
<td align="left"><p><strong>r1</strong>/m = <strong>r1</strong>/m and <strong>r2</strong>/m/#n</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong></em></strong></p></td>
<td align="left"><p>OR</p></td>
<td align="left"><p><strong>r1</strong>/m, <strong>r2</strong>/m/#n</p></td>
<td align="left"><p><strong>r1</strong>/m = <strong>r1</strong>/m or <strong>r2</strong>/m/#n</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong><em></strong></p></td>
<td align="left"><p>XOR</p></td>
<td align="left"><p><strong>r1</strong>/m, <strong>r2</strong>/m/#n</p></td>
<td align="left"><p><strong>r1</strong>/m = <strong>r1</strong>/m xor <strong>r2</strong>/m/#n</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong></em></strong></p></td>
<td align="left"><p>NOT</p></td>
<td align="left"><p><strong>r1</strong>/m</p></td>
<td align="left"><p><strong>r1</strong>/m = bitwise not <strong>r1</strong>/m</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>*</strong></p></td>
<td align="left"><p>TEST</p></td>
<td align="left"><p><strong>r1</strong>/m, <strong>r2</strong>/m/#n</p></td>
<td align="left"><p>Compute <strong>r1</strong>/m and <strong>r2</strong>/m/#n</p></td>
</tr>
</tbody>
</table>

 

The **test** instruction computes the logical AND operator and sets flags according to the result, but throws the result away. It is typically followed by a conditional jump instruction that tests the result of the logical AND.

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong><em></strong></p></td>
<td align="left"><p>SHL</p></td>
<td align="left"><p><strong>r1</strong>/m, <strong>cl</strong>/#n</p></td>
<td align="left"><p><strong>r1</strong>/m &lt;&lt;= <strong>cl</strong>/#n</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong></em></strong></p></td>
<td align="left"><p>SHR</p></td>
<td align="left"><p><strong>r1</strong>/m, <strong>cl</strong>/#n</p></td>
<td align="left"><p><strong>r1</strong>/m &gt;&gt;= <strong>cl</strong>/#n zero-fill</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>*</strong></p></td>
<td align="left"><p>SAR</p></td>
<td align="left"><p><strong>r1</strong>/m, <strong>cl</strong>/#n</p></td>
<td align="left"><p><strong>r1</strong>/m &gt;&gt;= <strong>cl</strong>/#n sign-fill</p></td>
</tr>
</tbody>
</table>

 

The last bit shifted out is placed in the carry.

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"></td>
<td align="left"><p>SHLD</p></td>
<td align="left"><p><strong>r1</strong>, <strong>r2</strong>/m, <strong>cl</strong>/#n</p></td>
<td align="left"><p>Shift left double.</p></td>
</tr>
</tbody>
</table>

 

Shift **r1** left by **cl**/\#n, filling with the top bits of **r2**/m. The last bit shifted out is placed in the carry.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>SHRD</p></td>
<td align="left"><p><strong>r1</strong>, <strong>r2</strong>/m, <strong>cl</strong>/#n</p></td>
<td align="left"><p>Shift right double.</p></td>
</tr>
</tbody>
</table>

 

Shift **r1** right by **cl**/\#n, filling with the bottom bits of **r2**/m. The last bit shifted out is placed in the carry.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>ROL</p></td>
<td align="left"><p><strong>r1</strong>, <strong>cl</strong>/#n</p></td>
<td align="left"><p>Rotate <strong>r1</strong> left by <strong>cl</strong>/#n.</p></td>
</tr>
<tr class="even">
<td align="left"><p>ROR</p></td>
<td align="left"><p><strong>r1</strong>, <strong>cl</strong>/#n</p></td>
<td align="left"><p>Rotate <strong>r1</strong> right by <strong>cl</strong>/#n.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>RCL</p></td>
<td align="left"><p><strong>r1</strong>, <strong>cl</strong>/#n</p></td>
<td align="left"><p>Rotate <strong>r1</strong>/C left by <strong>cl</strong>/#n.</p></td>
</tr>
<tr class="even">
<td align="left"><p>RCR</p></td>
<td align="left"><p><strong>r1</strong>, <strong>cl</strong>/#n</p></td>
<td align="left"><p>Rotate <strong>r1</strong>/C right by <strong>cl</strong>/#n.</p></td>
</tr>
</tbody>
</table>

 

Rotation is like shifting, except that the bits that are shifted out reappear as the incoming fill bits. The C-language version of the rotation instructions incorporate the carry bit into the rotation.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>BT</p></td>
<td align="left"><p><strong>r1</strong>, <strong>r2</strong>/#n</p></td>
<td align="left"><p>Copy bit <strong>r2</strong>/#n of <strong>r1</strong> into carry.</p></td>
</tr>
<tr class="even">
<td align="left"><p>BTS</p></td>
<td align="left"><p><strong>r1</strong>, <strong>r2</strong>/#n</p></td>
<td align="left"><p>Set bit <strong>r2</strong>/#n of <strong>r1</strong>, copy previous value into carry.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>BTC</p></td>
<td align="left"><p><strong>r1</strong>, <strong>r2</strong>/#n</p></td>
<td align="left"><p>Clear bit <strong>r2</strong>/#n of <strong>r1</strong>, copy previous value into carry.</p></td>
</tr>
</tbody>
</table>

 

### <span id="Control_Flow"></span><span id="control_flow"></span><span id="CONTROL_FLOW"></span>Control Flow

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong><em></strong></p></td>
<td align="left"><p>J<em>cc</em></p></td>
<td align="left"><p>dest</p></td>
<td align="left"><p>Branch conditional.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong></em></strong></p></td>
<td align="left"><p>JMP</p></td>
<td align="left"><p>dest</p></td>
<td align="left"><p>Jump direct.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong><em></strong></p></td>
<td align="left"><p>JMP</p></td>
<td align="left"><p><strong>r</strong>/m</p></td>
<td align="left"><p>Jump indirect.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong></em></strong></p></td>
<td align="left"><p>CALL</p></td>
<td align="left"><p>dest</p></td>
<td align="left"><p>Call direct.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>*</strong></p></td>
<td align="left"><p>CALL</p></td>
<td align="left"><p><strong>r</strong>/m</p></td>
<td align="left"><p>Call indirect.</p></td>
</tr>
</tbody>
</table>

 

The **call** instruction pushes the return address onto the stack then jumps to the destination.

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>*</strong></p></td>
<td align="left"><p>RET</p></td>
<td align="left"><p><em>#n</em></p></td>
<td align="left"><p>Return</p></td>
</tr>
</tbody>
</table>

 

The **ret** instruction pops and jumps to the return address on the stack. A nonzero *\#n* in the **RET** instruction indicates that after popping the return address, the value *\#n* should be added to the stack pointer.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>LOOP</p></td>
<td align="left"><p>Decrement <strong>ecx</strong> and jump if result is nonzero.</p></td>
</tr>
<tr class="even">
<td align="left"><p>LOOPZ</p></td>
<td align="left"><p>Decrement <strong>ecx</strong> and jump if result is nonzero and <strong>zr</strong> was set.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>LOOPNZ</p></td>
<td align="left"><p>Decrement <strong>ecx</strong> and jump if result is nonzero and <strong>zr</strong> was clear.</p></td>
</tr>
<tr class="even">
<td align="left"><p>JECXZ</p></td>
<td align="left"><p>Jump if <strong>ecx</strong> is zero.</p></td>
</tr>
</tbody>
</table>

 

These instructions are remnants of the x86's CISC heritage and in recent processors are actually slower than the equivalent instructions written out the long way.

### <span id="String_Manipulation"></span><span id="string_manipulation"></span><span id="STRING_MANIPULATION"></span>String Manipulation

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong><em></strong></p></td>
<td align="left"><p>MOVS<em>T</em></p></td>
<td align="left"><p>Move <em>T</em> from <strong>esi</strong> to <strong>edi.</strong></p></td>
</tr>
<tr class="even">
<td align="left"></td>
<td align="left"><p>CMPS<em>T</em></p></td>
<td align="left"><p>Compare <em>T</em> from <strong>esi</strong> with <strong>edi.</strong></p></td>
</tr>
<tr class="odd">
<td align="left"></td>
<td align="left"><p>SCAS<em>T</em></p></td>
<td align="left"><p>Scan <em>T</em> from <strong>edi</strong> for acc<em>T.</em></p></td>
</tr>
<tr class="even">
<td align="left"></td>
<td align="left"><p>LODS<em>T</em></p></td>
<td align="left"><p>Load <em>T</em> from <strong>esi</strong> into acc<em>T.</em></p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong></em></strong></p></td>
<td align="left"><p>STOS<em>T</em></p></td>
<td align="left"><p>Store <em>T</em> to <strong>edi</strong> from acc<em>T.</em></p></td>
</tr>
</tbody>
</table>

 

After performing the operation, the source and destination register are incremented or decremented by sizeof(*T*), according to the setting of the direction flag (up or down).

The instruction can be prefixed by **REP** to repeat the operation the number of times specified by the **ecx** register.

The **rep mov** instruction is used to copy blocks of memory.

The **rep stos** instruction is used to fill a block of memory with acc*T*.

### <span id="Flags"></span><span id="flags"></span><span id="FLAGS"></span>Flags

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>LAHF</p></td>
<td align="left"><p>Load <strong>ah</strong> from flags.</p></td>
</tr>
<tr class="even">
<td align="left"><p>SAHF</p></td>
<td align="left"><p>Store <strong>ah</strong> to flags.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>STC</p></td>
<td align="left"><p>Set carry.</p></td>
</tr>
<tr class="even">
<td align="left"><p>CLC</p></td>
<td align="left"><p>Clear carry.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>CMC</p></td>
<td align="left"><p>Complement carry.</p></td>
</tr>
<tr class="even">
<td align="left"><p>STD</p></td>
<td align="left"><p>Set direction to <em>down.</em></p></td>
</tr>
<tr class="odd">
<td align="left"><p>CLD</p></td>
<td align="left"><p>Set direction to <em>up.</em></p></td>
</tr>
<tr class="even">
<td align="left"><p>STI</p></td>
<td align="left"><p>Enable interrupts.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>CLI</p></td>
<td align="left"><p>Disable interrupts.</p></td>
</tr>
</tbody>
</table>

 

### <span id="Interlocked_Instructions"></span><span id="interlocked_instructions"></span><span id="INTERLOCKED_INSTRUCTIONS"></span>Interlocked Instructions

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>XCHG</p></td>
<td align="left"><p><strong>r1</strong>, <strong>r</strong>/m</p></td>
<td align="left"><p>Swap <strong>r1</strong> and <strong>r</strong>/m.</p></td>
</tr>
<tr class="even">
<td align="left"><p>XADD</p></td>
<td align="left"><p><strong>r1</strong>, <strong>r</strong>/m</p></td>
<td align="left"><p>Add <strong>r1</strong> to <strong>r</strong>/m, put original value in <strong>r1.</strong></p></td>
</tr>
<tr class="odd">
<td align="left"><p>CMPXCHG</p></td>
<td align="left"><p><strong>r1</strong>, <strong>r</strong>/m</p></td>
<td align="left"><p>Compare and exchange conditional.</p></td>
</tr>
</tbody>
</table>

 

The **cmpxchg** instruction is the atomic version of the following:

```asm
   cmp     accT, r/m
   jz      match
   mov     accT, r/m
   jmp     done
match:
   mov     r/m, r1
done:
```

### <span id="Miscellaneous"></span><span id="miscellaneous"></span><span id="MISCELLANEOUS"></span>Miscellaneous

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"></td>
<td align="left"><p>INT</p></td>
<td align="left"><p>#n</p></td>
<td align="left"><p>Trap to kernel.</p></td>
</tr>
<tr class="even">
<td align="left"></td>
<td align="left"><p>BOUND</p></td>
<td align="left"><p><strong>r</strong>, m</p></td>
<td align="left"><p>Trap if <strong>r</strong> not in range.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>*</strong></p></td>
<td align="left"><p>NOP</p></td>
<td align="left"></td>
<td align="left"><p>No operation.</p></td>
</tr>
<tr class="even">
<td align="left"></td>
<td align="left"><p>XLATB</p></td>
<td align="left"></td>
<td align="left"><p><strong>al</strong> = [<strong>ebx</strong> + <strong>al</strong>]</p></td>
</tr>
<tr class="odd">
<td align="left"></td>
<td align="left"><p>BSWAP</p></td>
<td align="left"><p><strong>r</strong></p></td>
<td align="left"><p>Swap byte order in register.</p></td>
</tr>
</tbody>
</table>

 

Here is a special case of the **int** instruction.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>INT</p></td>
<td align="left"><p>3</p></td>
<td align="left"><p>Debugger breakpoint trap.</p></td>
</tr>
</tbody>
</table>

 

The opcode for **INT 3** is 0xCC. The opcode for **NOP** is 0x90.

When debugging code, you may need to patch out some code. You can do this by replacing the offending bytes with 0x90.

### <span id="Idioms"></span><span id="idioms"></span><span id="IDIOMS"></span>Idioms

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong><em></strong></p></td>
<td align="left"><p>XOR</p></td>
<td align="left"><p><strong>r</strong>, <strong>r</strong></p></td>
<td align="left"><p><strong>r</strong> = 0</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong></em></strong></p></td>
<td align="left"><p>TEST</p></td>
<td align="left"><p><strong>r</strong>, <strong>r</strong></p></td>
<td align="left"><p>Check if <strong>r</strong> = 0.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>*</strong></p></td>
<td align="left"><p>ADD</p></td>
<td align="left"><p><strong>r</strong>, <strong>r</strong></p></td>
<td align="left"><p>Shift <strong>r</strong> left by 1.</p></td>
</tr>
</tbody>
</table>

 

 

 





