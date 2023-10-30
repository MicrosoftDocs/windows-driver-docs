---
title: x64 Architecture
description: The x64 architecture is a backwards-compatible extension of x86. It provides a legacy 32-bit mode, which is identical to x86, and a new 64-bit mode.
keywords: ["x64 processor, architecture", "registers, on an x64 processor", "x64 processor, registers"]
ms.date: 12/08/2022
---

# x64 Architecture

The x64 architecture is a backwards-compatible extension of x86. It provides a new 64-bit mode and a legacy 32-bit mode, which is identical to x86.

The term "x64" includes both AMD 64 and Intel64. The instruction sets are almost identical.

## Registers

x64 extends x86's 8 general-purpose registers to be 64-bit, and adds 8 new 64-bit registers. The 64-bit registers have names beginning with "r". For example, the 64-bit extension of **eax** is called **rax**. The new registers are named **r8** through **r15**.

The lower 32 bits, 16 bits, and 8 bits of each register are directly addressable in operands. This includes registers, like **esi**, whose lower 8 bits weren't previously addressable. The following table specifies the assembly-language names for the lower portions of 64-bit registers.

| 64-bit register | Lower 32 bits | Lower 16 bits | Lower 8 bits |
|-----------------|---------------|---------------|--------------|
| rax             | eax           | ax            | al           |
| rbx             | ebx           | bx            | bl           |
| rcx             | ecx           | cx            | cl           |
| rdx             | edx           | dx            | dl           |
| rsi             | esi           | si            | sil          |
| rdi             | edi           | di            | dil          |
| rbp             | ebp           | bp            | bpl          |
| rsp             | esp           | sp            | spl          |
| r8              | r8d           | r8w           | r8b          |
| r9              | r9d           | r9w           | r9b          |
| r10             | r10d          | r10w          | r10b         |
| r11             | r11d          | r11w          | r11b         |
| r12             | r12d          | r12w          | r12b         |
| r13             | r13d          | r13w          | r13b         |
| r14             | r14d          | r14w          | r14b         |
| r15             | r15d          | r15w          | r15b         |

Operations that output to a 32-bit subregister are automatically zero-extended to the entire 64-bit register. Operations that output to 8-bit or 16-bit subregisters aren't zero-extended (this is compatible x86 behavior).

The high 8 bits of **ax**, **bx**, **cx**, and **dx** are still addressable as **ah**, **bh**, **ch**, **dh** but can't be used with all types of operands.

The instruction pointer **eip** and **flags** register have been extended to 64 bits (**rip** and **rflags**, respectively).

The x64 processor also provides several sets of floating-point registers:

- Eight 80-bit x87 registers.

- Eight 64-bit MMX registers. (These registers overlap with the x87 registers.)

- The original set of eight 128-bit SSE registers is increased to sixteen.

## Calling Conventions

Unlike the x86, the C/C++ compiler only supports one calling convention on x64. This calling convention takes advantage of the increased number of registers available on x64:

- The first four integer or pointer parameters are passed in the **rcx**, **rdx**, **r8**, and **r9** registers.

- The first four floating-point parameters are passed in the first four SSE registers, **xmm0**-**xmm3**.

- The caller reserves space on the stack for arguments passed in registers. The called function can use this space to spill the contents of registers to the stack.

- Any additional arguments are passed on the stack.

- An integer or pointer return value is returned in the **rax** register, while a floating-point return value is returned in **xmm0**.

- **rax**, **rcx**, **rdx**, **r8**-**r11** are volatile.

- **rbx**, **rbp**, **rdi**, **rsi**, **r12**-**r15** are nonvolatile.

The calling convention for C++ is similar. The **this** pointer is passed as an implicit first parameter. The next three parameters are passed in remaining registers, while the rest are passed on the stack.

## Addressing Modes

The addressing modes in 64-bit mode are similar but not identical to x86.

- Instructions that refer to 64-bit registers are automatically performed with 64-bit precision. For example, **mov rax, [rbx]** moves 8 bytes beginning at **rbx** into **rax**.

- A special form of the **mov** instruction has been added for 64-bit immediate constants or constant addresses. For all other instructions, immediate constants or constant addresses are still 32 bits.

- x64 provides a new **rip**-relative addressing mode. Instructions that refer to a single constant address are encoded as offsets from **rip**. For example, the **mov rax, [**<em>addr</em>**]** instruction moves 8 bytes beginning at *addr* + **rip** to **rax**.

Instructions, such as **jmp**, **call**, **push**, and **pop**, that implicitly refer to the instruction pointer and the stack pointer treat them as 64 bits registers on x64.

## See also

- [X86-64 Wikipedia](https://en.wikipedia.org/wiki/X86-64)

- [AMD 64 developer resources](https://developer.amd.com/resources/)

- [Intel - Introduction to x64 assembly](https://software.intel.com/content/www/us/en/develop/articles/introduction-to-x64-assembly.html)

- [x64 Primer - Everything You Need To Know To Start Programming 64-Bit Windows Systems - Matt Pietrek](/archive/msdn-magazine/2006/may/x64-starting-out-in-64-bit-windows-systems-with-visual-c)

- [The history of calling conventions, part 5: amd64 Raymond Chen](https://devblogs.microsoft.com/oldnewthing/20040114-00/?p=41053)
