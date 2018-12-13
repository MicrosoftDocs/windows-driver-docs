---
title: Debugger Data Model - Code Namespace
description: Contains attributes of code and dissasembly.
ms.date: 12/12/2018
---

> [!IMPORTANT]
>  This interface is under active development and will change.
>
# The Code Namespace

## Summary
The Code namespace contains attributes of code and disassembly.


## Object Methods
|Name|Return Type|Signature|Description|
|--- |--- |--- |--- |
|CreateDisassembler| `Disassembler `|CreateDisassembler([architecture])|Creates a disassembler object of the specified architecture. Architecture may be one of "ARM", "ARM64", "X64", or "X86". If the architecture is not specified, X64 is assumed. |
|TraceDataFlow| `Collection ` of  `Instructions `|TraceDataFlow([address])|Looks at the instruction at the specified *address* (or the current instruction pointer if no address is specified) and all of its source operands. This method walks backwards through the control flow of the function looking for any instruction which influenced the source operands of the traced instruction.|

## Remarks
Eventually, the default architecture of CreateDisassembler will be pulled from the architecture of the module at the current thread's instruction pointer.