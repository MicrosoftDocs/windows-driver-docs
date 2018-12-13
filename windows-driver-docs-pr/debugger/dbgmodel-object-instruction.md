---
title: Debugger Data Model - Instruction Objects
description: Instruction Objects describe a single machine instruction.
ms.date: 12/12/2018
---
# Instruction Objects 
## Summary
Instruction Objects describe a single machine instruction and are returned via either an instruction based disassembly or as part of the contents of a  `basic block object `. 
## Object Properties
|Name|Description|
|--- |--- |
|Address|The address of the machine instruction.|
|Attributes|An  `instruction attributes object ` which describes details about the instruction.|
|CodeBytes|An array of bytes representing the bytes which comprise the machine instruction.|
|Length|The number of bytes that the instruction takes in memory.|
|LiveVariables|A  `collection` of  `live variable objects ` which describe the data which the compiler optimizer has emitted for variables at this particular location.|
|Operands|A  `collection` of  `operand objects ` describing the operands of the instruction.|
|SourceInformation|A  `source information object ` which describes the relationship between the machine instruction and higher level source code.|
|SourceDataFlow|A  `collection` of  `instructions ` within the function that comprise the data flow for source operands of the machine instruction.|