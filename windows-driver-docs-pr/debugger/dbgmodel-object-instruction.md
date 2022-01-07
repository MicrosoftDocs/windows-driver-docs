---
title: Debugger Data Model - Instruction Objects
description: Instruction Objects describe a single machine instruction.
ms.date: 12/12/2018
---
# Instruction Objects

## Summary

Instruction Objects describe a single machine instruction and are returned via either an instruction based disassembly or as part of the contents of a [basic block](dbgmodel-object-basic-block.md) object.

## Object Properties

|Name|Description|
|--- |--- |
|Address|The address of the machine instruction.|
|Attributes|An [instruction attributes](dbgmodel-object-instruction-attributes.md) object which describes details about the instruction.|
|CodeBytes|An array of bytes representing the bytes which comprise the machine instruction.|
|Length|The number of bytes that the instruction takes in memory.|
|LiveVariables|A [collection](dbgmodel-namespace-collections.md) of [live variable](dbgmodel-object-live-variable.md) objects which describe the data which the compiler optimizer has emitted for variables at this particular location.|
|Operands|A [collection](dbgmodel-namespace-collections.md) of [operand](dbgmodel-object-operand.md) objects describing the operands of the instruction.|
|SourceInformation|A [source information](dbgmodel-object-source-information.md) object which describes the relationship between the machine instruction and higher level source code.|
|SourceDataFlow|A [collection](dbgmodel-namespace-collections.md) of [instruction](dbgmodel-object-instruction.md) objects within the function that comprise the data flow for source operands of the machine instruction. **This method requires loading the [CodeFlow extension](https://github.com/Microsoft/WinDbg-Samples/tree/master/CodeFlow).**|
