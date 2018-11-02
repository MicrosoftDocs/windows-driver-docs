---
title: Assembling and Disassembling Instructions
description: Assembling and Disassembling Instructions
ms.assetid: 7681bea1-4d4e-4260-950d-69cb8feb3807
keywords: ["Debugger Engine API, assembling and disassembling"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Assembling and Disassembling Instructions


The debugger engine supports the use of assembly language for displaying and changing code in the target. For an overview of the use of assembly language in the debugger, see [Debugging in Assembly Mode](debugging-in-assembly-mode.md).

**Note**   Assembly language is not supported for all architectures. And on some architectures not all instructions are supported.

 

To assemble a single assembly-language instruction and place the resulting processor instruction in the target's memory, use [**Assemble**](https://msdn.microsoft.com/library/windows/hardware/ff538121).

To disassemble a single instruction by taking a processor instruction from the target and producing a string that represents the assembly instruction, use [**Disassemble**](https://msdn.microsoft.com/library/windows/hardware/ff541948).

The method [**GetDisassembleEffectiveOffset**](https://msdn.microsoft.com/library/windows/hardware/ff546581) returns the first effective address of the last instruction to be disassembled. For example, if the last instruction to be disassembled is `move ax, [ebp+4]`, the effective address is the value of `ebp+4`. This corresponds to the **$ea** pseudo-register.

To send disassembled instructions to the output callbacks, use the methods [*OutputDisassembly*](https://msdn.microsoft.com/library/windows/hardware/ff553211) and [*OutputDisassemblyLines*](https://msdn.microsoft.com/library/windows/hardware/ff553216).

The debugger engine has some options that control the assembly and disassembly. These options are returned by [**GetAssemblyOptions**](https://msdn.microsoft.com/library/windows/hardware/ff545605). They can be set using [**SetAssemblyOptions**](https://msdn.microsoft.com/library/windows/hardware/ff556626) and some options can be turned on with [**AddAssemblyOptions**](https://msdn.microsoft.com/library/windows/hardware/ff537852) or turned off with [**RemoveAssemblyOptions**](https://msdn.microsoft.com/library/windows/hardware/ff554483).

 

 





