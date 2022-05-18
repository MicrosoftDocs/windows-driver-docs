---
title: Debugger Data Model - Code Namespace
description: Contains attributes of code and dissasembly.
ms.date: 12/12/2018
---

# The Code Namespace

> [!IMPORTANT]
> This interface is under active development and will change.
>

## Summary

The Code namespace contains attributes of code and disassembly. It enables creations of Disassembler objects that can disassemble given addresses or functions and provide detailed information about the assembly there and any variable or source information if availabe.

## Sample

For an end-to-end example of how this namespace and objects and be used, see the [CodeFlow](https://github.com/Microsoft/WinDbg-Samples/tree/master/CodeFlow) sample on GitHub.

## Object Methods

|Name|Return Type|Signature|Description|
|--- |--- |--- |--- |
|CreateDisassembler| [disassembler](dbgmodel-object-disassembler.md)|CreateDisassembler([architecture])|Creates a disassembler object of the specified architecture. Architecture may be one of "Arm", "Arm64", "X64", or "X86". If the architecture is not specified, X64 is assumed. |
|TraceDataFlow|[collection](dbgmodel-namespace-collections.md) of [instructions](dbgmodel-object-instruction.md)|TraceDataFlow([address])|Looks at the instruction at the specified *address* (or the current instruction pointer if no address is specified) and all of its source operands. This method walks backwards through the control flow of the function looking for any instruction which influenced the source operands of the traced instruction. **This method requires loading the CodeFlow extension found in the [CodeFlow.js sample](https://github.com/Microsoft/WinDbg-Samples/tree/master/CodeFlow).**|

## Remarks

CreateDisassembler defaults to "X64" for the time being, at some point this behavior will change to pull the architecture of the module at the current thread's instruction pointer.
