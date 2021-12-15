---
title: Debugger Data Model - Operand Objects
description: Individual operands of a machine instruction are described by operand objects.
ms.date: 12/12/2018
---
# Operand Objects 
## Summary
Individual operands of a machine instruction are described by operand objects. The string conversion of an operand will be a portion of the string conversion of an entire instruction. 
## Object Properties
|Name|Description|
|--- |--- |
|Attributes|An [operand attributes](dbgmodel-object-operand-attributes.md) object describing certain aspects of the operand.|
|Registers|A [collection](dbgmodel-namespace-collections.md) of [register](dbgmodel-object-register.md) objects which describe all registers that the operand utilizes.|
