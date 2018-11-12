---
title: Register Syntax
description: Register Syntax
ms.assetid: 64a566b1-c10b-4329-947c-af69904a21f8
keywords: ["expressions, registers", "registers, command syntax", "(register prefix)", "syntax rules for commands, (register prefix)", "syntax rules for commands, registers"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Register Syntax


## <span id="ddk_register_syntax_dbg"></span><span id="DDK_REGISTER_SYNTAX_DBG"></span>


The debugger can control registers and floating-point registers.

When you use a register in an expression, you should add an at sign ( **@** ) before the register. This at sign tells the debugger that the following text is the name of a register.

If you are using MASM expression syntax, you can omit the at sign for certain very common registers. On x86-based systems, you can omit the at sign for the **eax**, **ebx**, **ecx**, **edx**, **esi**, **edi**, **ebp**, **eip**, and **efl** registers. However, if you specify a less common register without an at sign, the debugger first tries to interpret the text as a hexadecimal number. If the text contains non-hexadecimal characters, the debugger next interprets the text as a symbol. Finally, if the debugger does not find a symbol match, the debugger interprets the text as a register.

If you are using C++ expression syntax, the at sign is always required.

The [**r (Registers)**](r--registers-.md) command is an exception to this rule. The debugger always interprets its first argument as a register. (An at sign is not required or permitted.) If there is a second argument for the **r** command, it is interpreted according to the default expression syntax. If the default expression syntax is C++, you must use the following command to copy the **ebx** register to the **eax** register.

```dbgcmd
0:000> r eax = @ebx
```

For more information about the registers and instructions that are specific to each processor, see [Processor Architecture](processor-architecture.md).

### <span id="flags_on_an_x86_based_processor"></span><span id="FLAGS_ON_AN_X86_BASED_PROCESSOR"></span>Flags on an x86-based Processor

x86-based processors also use several 1-bit registers known as *flags*. For more information about these flags and the syntax that you can use to view or change them, see [x86 Flags](x86-architecture.md#x86-flags).

### <span id="registers_and_threads"></span><span id="REGISTERS_AND_THREADS"></span>Registers and Threads

Each thread has its own register values. These values are stored in the CPU registers when the thread is executing and in memory when another thread is executing.

In user mode, any reference to a register is interpreted as the register that is associated with the current thread. For more information about the current thread, see [Controlling Processes and Threads](controlling-processes-and-threads.md).

In kernel mode, any reference to a register is interpreted as the register that is associated with the current register context. You can set the register context to match a specific thread, context record, or trap frame. You can display only the most important registers for the specified register context, and you cannot change their values.

 

 





