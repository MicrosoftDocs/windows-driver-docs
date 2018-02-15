---
title: Assembling and Disassembling Instructions
description: Assembling and Disassembling Instructions
ms.assetid: 7681bea1-4d4e-4260-950d-69cb8feb3807
keywords: ["Debugger Engine API, assembling and disassembling"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Assembling and Disassembling Instructions


The debugger engine supports the use of assembly language for displaying and changing code in the target. For an overview of the use of assembly language in the debugger, see [Debugging in Assembly Mode](debugging-in-assembly-mode.md).

**Note**   Assembly language is not supported for all architectures. And on some architectures not all instructions are supported.

 

To assemble a single assembly-language instruction and place the resulting processor instruction in the target's memory, use [**Assemble**](https://msdn.microsoft.com/library/windows/hardware/ff538121).

To disassemble a single instruction by taking a processor instruction from the target and producing a string that represents the assembly instruction, use [**Disassemble**](https://msdn.microsoft.com/library/windows/hardware/ff541948).

The method [**GetDisassembleEffectiveOffset**](https://msdn.microsoft.com/library/windows/hardware/ff546581) returns the first effective address of the last instruction to be disassembled. For example, if the last instruction to be disassembled is `move ax, [ebp+4]`, the effective address is the value of `ebp+4`. This corresponds to the **$ea** pseudo-register.

To send disassembled instructions to the output callbacks, use the methods [*OutputDisassembly*](https://msdn.microsoft.com/library/windows/hardware/ff553211) and [*OutputDisassemblyLines*](https://msdn.microsoft.com/library/windows/hardware/ff553216).

The debugger engine has some options that control the assembly and disassembly. These options are returned by [**GetAssemblyOptions**](https://msdn.microsoft.com/library/windows/hardware/ff545605). They can be set using [**SetAssemblyOptions**](https://msdn.microsoft.com/library/windows/hardware/ff556626) and some options can be turned on with [**AddAssemblyOptions**](https://msdn.microsoft.com/library/windows/hardware/ff537852) or turned off with [**RemoveAssemblyOptions**](https://msdn.microsoft.com/library/windows/hardware/ff554483).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Assembling%20and%20Disassembling%20Instructions%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




