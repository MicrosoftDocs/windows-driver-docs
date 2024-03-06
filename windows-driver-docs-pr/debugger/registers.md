---
title: Registers
description: Registers
keywords: ["memory access, registers", "registers"]
ms.date: 05/23/2017
---

# Registers


## <span id="ddk_registers_dbx"></span><span id="DDK_REGISTERS_DBX"></span>


The [debugger engine](introduction.md#debugger-engine) can be used to examine and alter the target's registers.

The registers available on the target depend on its processor architecture. For a description of the registers for the x86 processor, see [Processor Architecture](processor-architecture.md). For a complete description of the registers available for a processor, see that processor's documentation.

### <span id="the_register_set"></span><span id="THE_REGISTER_SET"></span>The Register Set

The [**GetNumberRegisters**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugregisters2-getnumberregisters) method can be used to find the number of registers on the target.

Each register is referred to by its index. The index of the first register is zero, and the index of the last register is the number of registers minus one. To find the index of a register whose name is known, use [**GetIndexByName**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugregisters2-getindexbyname).

The method [**GetDescription**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugregisters2-getdescription) returns information about a register. This includes the register's name, the type of values it can hold, and whether it is a subregister.

A *subregister* is a register that is contained within another register. When the subregister changes, the register that contains it also changes. For example, on an x86 processor, the **ax** subregister is the same as the low 16 bits of the 32-bit **eax** register.

There are three special registers whose values may be found by using the following methods. The interpretation of the values of these registers is platform dependent.

-   The location of the current instruction may be found with [**GetInstructionOffset**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugregisters2-getinstructionoffset) and [**GetInstructionOffset2**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugregisters2-getinstructionoffset2).

-   The location of the current processor stack slot may be found with [**GetStackOffset**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugregisters2-getstackoffset) and [**GetStackOffset2**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugregisters2-getstackoffset2).

-   The location of the stack frame for the current function may be found with [**GetFrameOffset**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugregisters2-getframeoffset) and [**GetFrameOffset2**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugregisters2-getframeoffset2).

### <span id="manipulating_registers"></span><span id="MANIPULATING_REGISTERS"></span>Manipulating Registers

The value of a register can be read by using the method [**GetValue**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugregisters2-getvalue). Multiple registers can be read by using [**GetValues**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugregisters2-getvalues) and [**GetValues2**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugregisters2-getvalues2).

A value can be written to a register by using the method [**SetValue**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugregisters2-setvalue). Multiple registers can be written by using [**SetValues**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugregisters2-setvalues) and [**SetValues2**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugregisters2-setvalues2).

When writing a value to a register, if the value supplied has a different type to the type of the register then the value is converted into the register's type. This conversion is the same as that performed by the method [**CoerceValue**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugcontrol3-coercevalue). This conversion may result in data loss if the register's type is not capable of holding the value supplied.

### <span id="pseudo_registers"></span><span id="PSEUDO_REGISTERS"></span> Pseudo-Registers

*Pseudo-registers* are variables maintained by the debugger engine that hold certain values, for example, **$teb** is the name of the pseudo-register whose value is the address of the current thread's Thread Environment Block (TEB). For more information, and a list of the pseudo-registers, see [Pseudo-Register Syntax](../debuggercmds/pseudo-register-syntax.md).

Each pseudo-register has an index. The index is a number between zero and the number of pseudo-registers - (returned by [**GetNumberPseudoRegisters**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugregisters2-getnumberpseudoregisters)) minus one. To find the index of a pseudo-register by its name, use [**GetPseudoIndexByName**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugregisters2-getpseudoindexbyname). The values of pseudo-registers can be read using [**GetPseudoValues**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugregisters2-getpseudovalues), and values can be written to pseudo-registers using [**SetPseudoValues**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugregisters2-setpseudovalues). For a description of a pseudo-register, including its type, use [**GetPseudoDescription**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugregisters2-getpseudodescription).

**Note**   Not all of the pseudo-registers are available in all debugging sessions or at all times in a particular session.

 

### <span id="displaying_registers"></span><span id="DISPLAYING_REGISTERS"></span>Displaying Registers

The methods [**OutputRegisters**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugregisters2-outputregisters) and [**OutputRegisters2**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugregisters2-outputregisters2) format the target's registers and sends them to the clients as output.

### <span id="events"></span><span id="EVENTS"></span>Events

Whenever the values of the target's registers change, the engine will call the [**IDebugEventCallbacks::ChangeDebuggeeState**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugeventcallbacks-changedebuggeestate) callback method with the parameter *Flags* set to DEBUG\_CDS\_REGISTERS.

 

