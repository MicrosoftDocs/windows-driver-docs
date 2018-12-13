---
title: Debugger Data Model - Basic Block Objects
description: Basic Blocks are regions of code with (typically) one entry point and one exit point.
ms.date: 12/12/2018
---
# Basic Block Objects 
## Summary
Basic Blocks are regions of code with (typically) one entry point and one exit point. The `disassembler`'s  `DisassembleBlocks ` and `DisassembleFunction ` methods both return collections of basic blocks. The  `DisassembleBlocks ` method does a simple analysis for basic blocks and may result in blocks with multiple entry points.  `DisassembleFunction ` will perform a complete flow analysis of the function resulting in basic blocks with a single entry and single exit.
## Object Properties
|Name|Description|
|--- |--- |
|StartAddress|The starting address of the basic block.|
|EndAddress|The ending address of the basic block. The block is defined by the half-open set [*StartAddress*, *EndAddress*).|
|Instructions|A  `collection ` of  `instruction objects ` in the basic block.|
|InboundControlFlows|This property is only present on basic blocks which are the result of full flow analysis (e.g.: *DisassembleFunction*). It is a  `collection` of  `control flow objects ` which describe what other blocks have inbound control flow links to this one.|
|OutboundControlFlows|This property is only present on basic blocks which are the result of full flow analysis (e.g.: *DisassembleFunction*). It is a  `collection` of  `control flow objects ` which describe the outbound control flow links from this block to other blocks in the function.|