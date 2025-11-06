---
title: x64 Architecture Overview and Registers
description: "Learn about x64 architecture: a backward-compatible extension of x86 with 64-bit registers, calling conventions, and addressing modes. Get started with x64 programming."
keywords: ["x64 processor, architecture", "registers, on an x64 processor", "x64 processor, registers"]
ms.date: 11/05/2025
ms.topic: concept-article
---

# x64 architecture

The x64 architecture is a backward-compatible extension of x86 that provides a new 64-bit mode and a legacy 32-bit mode identical to x86. This architecture extends x86's eight general-purpose registers to 64-bit, adds eight new registers, and introduces enhanced calling conventions and addressing modes for modern 64-bit programming.

The term "x64" includes both AMD64 and Intel 64. The instruction sets are almost identical.

## Registers

x64 extends x86's eight general-purpose registers to be 64-bit and adds eight new 64-bit registers. The 64-bit registers have names that begin with "r". For example, the 64-bit extension of **eax** is called **rax**. The new registers are named **r8** through **r15**.

The lower 32 bits, 16 bits, and 8 bits of each register are directly addressable in operands. This direct addressability includes registers like **esi**, whose lower 8 bits weren't previously addressable. The following table specifies the assembly-language names for the lower portions of 64-bit registers.

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

Operations that output to a 32-bit subregister automatically zero-extend to the entire 64-bit register. Operations that output to 8-bit or 16-bit subregisters don't zero-extend (this behavior is compatible with x86).

The high 8 bits of **ax**, **bx**, **cx**, and **dx** are still addressable as **ah**, **bh**, **ch**, and **dh** but can't be used with all types of operands.

The instruction pointer **eip** and **flags** register are extended to 64 bits (**rip** and **rflags**, respectively).

The x64 processor also provides several sets of floating-point registers:

- Eight 80-bit x87 registers.

- Eight 64-bit MMX registers. (These registers overlap with the x87 registers.)

- The original set of eight 128-bit SSE registers is increased to 16.

## Calling conventions

Unlike the x86 architecture, the C/C++ compiler supports only one calling convention on x64. This calling convention takes advantage of the increased number of registers available on x64:

- The first four integer or pointer parameters are passed in the **rcx**, **rdx**, **r8**, and **r9** registers.

- The first four floating-point parameters are passed in the first four SSE registers, **xmm0**-**xmm3**.

- The caller reserves space on the stack for arguments passed in registers. The called function can use this space to spill the contents of registers to the stack.

- You pass any other arguments on the stack.

- An integer or pointer return value is returned in the **rax** register, while a floating-point return value is returned in **xmm0**.

- **rax**, **rcx**, **rdx**, **r8**-**r11** are volatile.

- **rbx**, **rbp**, **rdi**, **rsi**, **r12**-**r15** are nonvolatile.

The calling convention for C++ is similar. The **this** pointer is passed as an implicit first parameter. The next three parameters are passed in remaining registers, while the rest are passed on the stack.

## Addressing modes

The addressing modes in 64-bit mode are similar but not identical to x86.

- Instructions that refer to 64-bit registers automatically perform with 64-bit precision. For example, **mov rax, [rbx]** moves 8 bytes beginning at **rbx** into **rax**.

- A special form of the **mov** instruction exists for 64-bit immediate constants or constant addresses. For all other instructions, immediate constants or constant addresses are still 32 bits.

- x64 provides a new **rip**-relative addressing mode. Instructions that refer to a single constant address encode as offsets from **rip**. For example, the **mov rax, [**<em>addr</em>**]** instruction moves 8 bytes beginning at *addr* + **rip** to **rax**.

Instructions, such as **jmp**, **call**, **push**, and **pop**, that implicitly refer to the instruction pointer and the stack pointer treat them as 64-bit registers on x64.

## Related content

- [X86-64 Wikipedia](https://en.wikipedia.org/wiki/x86-64)

- [AMD 64 developer resources](https://developer.amd.com/resources/)

- [Intel - Introduction to x64 assembly](https://software.intel.com/content/www/us/en/develop/articles/introduction-to-x64-assembly.html)

- [x64 Primer - Everything You Need To Know To Start Programming 64-Bit Windows Systems - Matt Pietrek](/archive/msdn-magazine/2006/may/x64-starting-out-in-64-bit-windows-systems-with-visual-c)

- [The history of calling conventions, part 5: amd64 Raymond Chen](https://devblogs.microsoft.com/oldnewthing/20040114-00/?p=41053)
