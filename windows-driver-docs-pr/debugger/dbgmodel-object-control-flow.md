---
title: Debugger Data Model - Control Flow Objects
description: For fully analyzed disassembly, each basic block contains a set of control flow objects.
ms.date: 03/10/2023
ms.topic: reference
---
# Control Flow Objects

## Summary

For fully analyzed disassembly, each `basic block` contains a set of control flow objects in both the InboundControlFlows and OutboundControlFlows properties.

## Object Properties

|Name|Description|
|--- |--- |
|LinkedBlock|The basic block object on the other side of the link. If this is an inbound control flow, this refers to the basic block which had the branch instruction. If this is an outbound control flow, this refers to the basic block which is the target of a branch instruction.|
|LinkKind|Indicates what kind of control flow resulted in a link between the two blocks (e.g.: "FallThrough" or "Branch").|
|SourceInstruction|The source of the control flow link. This is the branch instruction or the last instruction in a basic block.|
|TargetInstruction|The destination of the control flow link. This is the branch target or the instruction after the last instruction of a basic block with a fall through.|
