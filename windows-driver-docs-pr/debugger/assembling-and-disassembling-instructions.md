---
title: Assembling and Disassembling Instructions
description: Assembling and Disassembling Instructions
ms.assetid: 7681bea1-4d4e-4260-950d-69cb8feb3807
keywords: ["Debugger Engine API, assembling and disassembling"]
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Assembling and Disassembling Instructions


The debugger engine supports the use of assembly language for displaying and changing code in the target. For an overview of the use of assembly language in the debugger, see [Debugging in Assembly Mode](debugging-in-assembly-mode.md).

**Note**   Assembly language is not supported for all architectures. And on some architectures not all instructions are supported.

 

To assemble a single assembly-language instruction and place the resulting processor instruction in the target's memory, use [**Assemble**](https://docs.microsoft.com/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugcontrol3-assemble).

To disassemble a single instruction by taking a processor instruction from the target and producing a string that represents the assembly instruction, use [**Disassemble**](https://docs.microsoft.com/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugcontrol3-disassemble).

The method [**GetDisassembleEffectiveOffset**](https://docs.microsoft.com/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugcontrol3-getdisassembleeffectiveoffset) returns the first effective address of the last instruction to be disassembled. For example, if the last instruction to be disassembled is `move ax, [ebp+4]`, the effective address is the value of `ebp+4`. This corresponds to the **$ea** pseudo-register.

To send disassembled instructions to the output callbacks, use the methods [*OutputDisassembly*](https://docs.microsoft.com/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugcontrol3-outputdisassembly) and [*OutputDisassemblyLines*](https://docs.microsoft.com/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugcontrol3-outputdisassemblylines).

The debugger engine has some options that control the assembly and disassembly. These options are returned by [**GetAssemblyOptions**](https://docs.microsoft.com/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugcontrol3-getassemblyoptions). They can be set using [**SetAssemblyOptions**](https://docs.microsoft.com/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugcontrol3-setassemblyoptions) and some options can be turned on with [**AddAssemblyOptions**](https://docs.microsoft.com/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugcontrol3-addassemblyoptions) or turned off with [**RemoveAssemblyOptions**](https://docs.microsoft.com/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugcontrol3-removeassemblyoptions).

 

 





