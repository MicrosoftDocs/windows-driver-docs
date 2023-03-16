---
title: Debugger Data Model - Disassembler Objects
description: Disassembler objects enable the ability to disassemble code for a specific architecture.
ms.date: 03/10/2023
ms.topic: reference
---
# Disassembler Objects

## Summary

Disassembler objects enable the ability to disassemble code for a specific architecture.

## Object Methods

|Name|Return Type|Signature|Description|
|--- |--- |--- |--- |
|DisassembleBlocks|[collection](dbgmodel-namespace-collections.md) of [basic block](dbgmodel-object-basic-block.md)|DisassembleBlocks(address)|Starts disassembling at *address* and returns a  [collection](dbgmodel-namespace-collections.md) of basic blocks. The disassembly here is linearly forward from *address* on an instruction-by-instruction basis. Since this is not performing complete flow analysis of a function, it is entirely possible that there may be jumps into the middle of blocks returned by this method. There will only be a single exit point from each; however.|
|DisassembleInstructions|[collection](dbgmodel-namespace-collections.md) of [instruction](dbgmodel-object-instruction.md)|DisassembleInstructions(address)|Starts disassembling at *address*. |
|DisassembleFunction|[collection](dbgmodel-namespace-collections.md) of [basic block](dbgmodel-object-basic-block.md)|DisassembleFunction(address)|Assuming a function starts at *address*, this performs a complete flow analysis of the function. The result is a [collection](dbgmodel-namespace-collections.md) of basic blocks with one entry point and one exit point.|
|GetRegister|[register](dbgmodel-object-register.md)|GetRegister(regId)|Returns a register object from the given register id.|

## Remarks
The disassembler provided here has significantly better disassembly output if full symbolic information is present for the disassembled function (e.g.: it will utilize address and operand size to determine what field of a struct/union is being touched).

A given instance of a disassembler may cache a significant amount of data in order to provide a better experience.
