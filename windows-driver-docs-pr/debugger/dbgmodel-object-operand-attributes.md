---
title: Debugger Data Model - Operand Attributes Objects
description: An operand of a machine instruction is described by an operand attributes object.
ms.date: 03/10/2023
ms.topic: reference
---

# Operand Attributes Objects 

## Summary

An operand of a machine instruction is described by an operand attributes object.
## Object Properties

|Name|Description|
|--- |--- |
|HasImmediate|Indicates whether the operand has an immediate value as part of the operand.|
|IsInput|Indicates whether the operand is a data source for the instruction (an input to whatever the instruction does).|
|IsOutput|Indicates whether the operand is a data destination for the instruction (an output of whatever the instruction does).|
|IsMemoryReference|Indicates whether the operand is a memory reference.|
|IsImmediate|Indicates whether the operand is an immediate value. Such an operand will also have *HasImmediate* set to true.|
|IsRegister|Indicates whether the operand is simply a register.|
