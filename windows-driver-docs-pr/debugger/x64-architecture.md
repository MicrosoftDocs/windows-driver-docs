---
title: x64 Architecture
description: x64 Architecture
ms.assetid: 6c0d92d5-cb16-4909-bae5-39fc5c15f736
keywords: ["x64 processor, architecture", "registers, on an x64 processor", "x64 processor, registers"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# x64 Architecture


## <span id="ddk_x64_architecture_dbg"></span><span id="DDK_X64_ARCHITECTURE_DBG"></span>


The x64 architecture is a backwards-compatible extension of x86. It provides a legacy 32-bit mode, which is identical to x86, and a new 64-bit mode.

The term "x64" includes both AMD 64 and Intel64. The instruction sets are close to identical.

### <span id="Registers"></span><span id="registers"></span><span id="REGISTERS"></span>Registers

x64 extends x86's 8 general-purpose registers to be 64-bit, and adds 8 new 64-bit registers. The 64-bit registers have names beginning with "r", so for example the 64-bit extension of **eax** is called **rax**. The new registers are named **r8** through **r15**.

The lower 32 bits, 16 bits, and 8 bits of each register are directly addressable in operands. This includes registers, like **esi**, whose lower 8 bits were not previously addressable. The following table specifies the assembly-language names for the lower portions of 64-bit registers.

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">64-bit register</th>
<th align="left">Lower 32 bits</th>
<th align="left">Lower 16 bits</th>
<th align="left">Lower 8 bits</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>rax</strong></p></td>
<td align="left"><p><strong>eax</strong></p></td>
<td align="left"><p><strong>ax</strong></p></td>
<td align="left"><p><strong>al</strong></p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>rbx</strong></p></td>
<td align="left"><p><strong>ebx</strong></p></td>
<td align="left"><p><strong>bx</strong></p></td>
<td align="left"><p><strong>bl</strong></p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>rcx</strong></p></td>
<td align="left"><p><strong>ecx</strong></p></td>
<td align="left"><p><strong>cx</strong></p></td>
<td align="left"><p><strong>cl</strong></p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>rdx</strong></p></td>
<td align="left"><p><strong>edx</strong></p></td>
<td align="left"><p><strong>dx</strong></p></td>
<td align="left"><p><strong>dl</strong></p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>rsi</strong></p></td>
<td align="left"><p><strong>esi</strong></p></td>
<td align="left"><p><strong>si</strong></p></td>
<td align="left"><p><strong>sil</strong></p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>rdi</strong></p></td>
<td align="left"><p><strong>edi</strong></p></td>
<td align="left"><p><strong>di</strong></p></td>
<td align="left"><p><strong>dil</strong></p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>rbp</strong></p></td>
<td align="left"><p><strong>ebp</strong></p></td>
<td align="left"><p><strong>bp</strong></p></td>
<td align="left"><p><strong>bpl</strong></p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>rsp</strong></p></td>
<td align="left"><p><strong>esp</strong></p></td>
<td align="left"><p><strong>sp</strong></p></td>
<td align="left"><p><strong>spl</strong></p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>r8</strong></p></td>
<td align="left"><p><strong>r8d</strong></p></td>
<td align="left"><p><strong>r8w</strong></p></td>
<td align="left"><p><strong>r8b</strong></p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>r9</strong></p></td>
<td align="left"><p><strong>r9d</strong></p></td>
<td align="left"><p><strong>r9w</strong></p></td>
<td align="left"><p><strong>r9b</strong></p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>r10</strong></p></td>
<td align="left"><p><strong>r10d</strong></p></td>
<td align="left"><p><strong>r10w</strong></p></td>
<td align="left"><p><strong>r10b</strong></p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>r11</strong></p></td>
<td align="left"><p><strong>r11d</strong></p></td>
<td align="left"><p><strong>r11w</strong></p></td>
<td align="left"><p><strong>r11b</strong></p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>r12</strong></p></td>
<td align="left"><p><strong>r12d</strong></p></td>
<td align="left"><p><strong>r12w</strong></p></td>
<td align="left"><p><strong>r12b</strong></p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>r13</strong></p></td>
<td align="left"><p><strong>r13d</strong></p></td>
<td align="left"><p><strong>r13w</strong></p></td>
<td align="left"><p><strong>r13b</strong></p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>r14</strong></p></td>
<td align="left"><p><strong>r14d</strong></p></td>
<td align="left"><p><strong>r14w</strong></p></td>
<td align="left"><p><strong>r14b</strong></p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>r15</strong></p></td>
<td align="left"><p><strong>r15d</strong></p></td>
<td align="left"><p><strong>r15w</strong></p></td>
<td align="left"><p><strong>r15b</strong></p></td>
</tr>
</tbody>
</table>

 

Operations that output to a 32-bit subregister are automatically zero-extended to the entire 64-bit register. Operations that output to 8-bit or 16-bit subregisters are *not* zero-extended (this is compatible x86 behavior).

The high 8 bits of **ax**, **bx**, **cx**, and **dx** are still addressable as **ah**, **bh**, **ch**, **dh**, but cannot be used with all types of operands.

The instruction pointer, **eip**, and **flags** register have been extended to 64 bits (**rip** and **rflags**, respectively) as well.

The x64 processor also provides several sets of floating-point registers:

-   Eight 80-bit x87 registers.

-   Eight 64-bit MMX registers. (These overlap with the x87 registers.)

-   The original set of eight 128-bit SSE registers is increased to sixteen.

### <span id="Calling_Conventions"></span><span id="calling_conventions"></span><span id="CALLING_CONVENTIONS"></span>Calling Conventions

Unlike the x86, the C/C++ compiler only supports one calling convention on x64. This calling convention takes advantage of the increased number of registers available on x64:

-   The first four integer or pointer parameters are passed in the **rcx**, **rdx**, **r8**, and **r9** registers.

-   The first four floating-point parameters are passed in the first four SSE registers, **xmm0**-**xmm3**.

-   The caller reserves space on the stack for arguments passed in registers. The called function can use this space to spill the contents of registers to the stack.

-   Any additional arguments are passed on the stack.

-   An integer or pointer return value is returned in the **rax** register, while a floating-point return value is returned in **xmm0**.

-   **rax**, **rcx**, **rdx**, **r8**-**r11** are volatile.

-   **rbx**, **rbp**, **rdi**, **rsi**, **r12**-**r15** are nonvolatile.

The calling convention for C++ is very similar: the **this** pointer is passed as an implicit first parameter. The next three parameters are passed in registers, while the rest are passed on the stack.

### <span id="Addressing_Modes"></span><span id="addressing_modes"></span><span id="ADDRESSING_MODES"></span>Addressing Modes

The addressing modes in 64-bit mode are similar to, but not identical to, x86.

-   Instructions that refer to 64-bit registers are automatically performed with 64-bit precision. (For example **mov rax, \[rbx\]** moves 8 bytes beginning at **rbx** into **rax**.)

-   A special form of the **mov** instruction has been added for 64-bit immediate constants or constant addresses. For all other instructions, immediate constants or constant addresses are still 32 bits.

-   x64 provides a new **rip**-relative addressing mode. Instructions that refer to a single constant address are encoded as offsets from **rip**. For example, the **mov rax, \[***addr***\]** instruction moves 8 bytes beginning at *addr* + **rip** to **rax**.

Instructions, such as **jmp**, **call**, **push**, and **pop**, that implicitly refer to the instruction pointer and the stack pointer treat them as 64 bits registers on x64.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20x64%20Architecture%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




