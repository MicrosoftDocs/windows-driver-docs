---
title: Registers
description: Registers
ms.assetid: fa334c9f-46c6-4288-95ce-43128fff7f03
keywords: ["memory access, registers", "registers"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Registers


## <span id="ddk_registers_dbx"></span><span id="DDK_REGISTERS_DBX"></span>


The [debugger engine](introduction.md#debugger-engine) can be used to examine and alter the target's registers.

The registers available on the target depend on its processor architecture. For a description of the registers for the x86 and Itanium processors, see [Processor Architecture](processor-architecture.md). For a complete description of the registers available for a processor, see that processor's documentation.

### <span id="the_register_set"></span><span id="THE_REGISTER_SET"></span>The Register Set

The [**GetNumberRegisters**](https://msdn.microsoft.com/library/windows/hardware/ff547960) method can be used to find the number of registers on the target.

Each register is referred to by its index. The index of the first register is zero, and the index of the last register is the number of registers minus one. To find the index of a register whose name is known, use [**GetIndexByName**](https://msdn.microsoft.com/library/windows/hardware/ff546881).

The method [**GetDescription**](https://msdn.microsoft.com/library/windows/hardware/ff546575) returns information about a register. This includes the register's name, the type of values it can hold, and whether it is a subregister.

A *subregister* is a register that is contained within another register. When the subregister changes, the register that contains it also changes. For example, on an x86 processor, the **ax** subregister is the same as the low 16 bits of the 32-bit **eax** register.

There are three special registers whose values may be found by using the following methods. The interpretation of the values of these registers is platform dependent.

-   The location of the current instruction may be found with [**GetInstructionOffset**](https://msdn.microsoft.com/library/windows/hardware/ff546916) and [**GetInstructionOffset2**](https://msdn.microsoft.com/library/windows/hardware/ff546933).

-   The location of the current processor stack slot may be found with [**GetStackOffset**](https://msdn.microsoft.com/library/windows/hardware/ff548403) and [**GetStackOffset2**](https://msdn.microsoft.com/library/windows/hardware/ff548414).

-   The location of the stack frame for the current function may be found with [**GetFrameOffset**](https://msdn.microsoft.com/library/windows/hardware/ff546806) and [**GetFrameOffset2**](https://msdn.microsoft.com/library/windows/hardware/ff546815).

### <span id="manipulating_registers"></span><span id="MANIPULATING_REGISTERS"></span>Manipulating Registers

The value of a register can be read by using the method [**GetValue**](https://msdn.microsoft.com/library/windows/hardware/ff549476). Multiple registers can be read by using [**GetValues**](https://msdn.microsoft.com/library/windows/hardware/ff549480) and [**GetValues2**](https://msdn.microsoft.com/library/windows/hardware/ff549487).

A value can be written to a register by using the method [**SetValue**](https://msdn.microsoft.com/library/windows/hardware/ff556881). Multiple registers can be written by using [**SetValues**](https://msdn.microsoft.com/library/windows/hardware/ff556883) and [**SetValues2**](https://msdn.microsoft.com/library/windows/hardware/ff556884).

When writing a value to a register, if the value supplied has a different type to the type of the register then the value is converted into the register's type. This conversion is the same as that performed by the method [**CoerceValue**](https://msdn.microsoft.com/library/windows/hardware/ff539158). This conversion may result in data loss if the register's type is not capable of holding the value supplied.

### <span id="pseudo_registers"></span><span id="PSEUDO_REGISTERS"></span> Pseudo-Registers

*Pseudo-registers* are variables maintained by the debugger engine that hold certain values, for example, **$teb** is the name of the pseudo-register whose value is the address of the current thread's Thread Environment Block (TEB). For more information, and a list of the pseudo-registers, see [Pseudo-Register Syntax](pseudo-register-syntax.md).

Each pseudo-register has an index. The index is a number between zero and the number of pseudo-registers - (returned by [**GetNumberPseudoRegisters**](https://msdn.microsoft.com/library/windows/hardware/ff547957)) minus one. To find the index of a pseudo-register by its name, use [**GetPseudoIndexByName**](https://msdn.microsoft.com/library/windows/hardware/ff548206). The values of pseudo-registers can be read using [**GetPseudoValues**](https://msdn.microsoft.com/library/windows/hardware/ff548215), and values can be written to pseudo-registers using [**SetPseudoValues**](https://msdn.microsoft.com/library/windows/hardware/ff556767). For a description of a pseudo-register, including its type, use [**GetPseudoDescription**](https://msdn.microsoft.com/library/windows/hardware/ff548189).

**Note**   Not all of the pseudo-registers are available in all debugging sessions or at all times in a particular session.

 

### <span id="displaying_registers"></span><span id="DISPLAYING_REGISTERS"></span>Displaying Registers

The methods [**OutputRegisters**](https://msdn.microsoft.com/library/windows/hardware/ff553242) and [**OutputRegisters2**](https://msdn.microsoft.com/library/windows/hardware/ff553245) format the target's registers and sends them to the clients as output.

### <span id="events"></span><span id="EVENTS"></span>Events

Whenever the values of the target's registers change, the engine will call the [**IDebugEventCallbacks::ChangeDebuggeeState**](https://msdn.microsoft.com/library/windows/hardware/ff550678) callback method with the parameter *Flags* set to DEBUG\_CDS\_REGISTERS.

 

 





