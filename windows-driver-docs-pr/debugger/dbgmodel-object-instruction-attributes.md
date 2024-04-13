---
title: Debugger Data Model - Instruction Attributes Objects
description: Contains a description of some of the details of an instruction.
ms.date: 03/10/2023
ms.topic: reference
---
# Instruction Attributes Objects

## Summary

The *Attributes* property of an [instruction](dbgmodel-object-instruction.md) object contains a description of some of the details of an instruction.

## Object Properties

|Name|Description|
|--- |--- |
|IsBranch|Indicates whether the instruction is any sort of branch instruction.|
|IsConditional|Indicates whether the result of the instruction is conditional (e.g.: a conditional branch).|
|IsCall|Indicates whether the instruction is any sort of call instruction.|
|IsReturn|Indicates whether the instruction is any sort of return instruction.|
