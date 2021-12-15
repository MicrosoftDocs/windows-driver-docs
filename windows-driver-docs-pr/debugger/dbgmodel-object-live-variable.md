---
title: Debugger Data Model - Live Variable Objects
description: Collection of information about the variables which are live at that particular instruction and where they are located
ms.date: 12/12/2018
---
# Live Variable Objects 
## Summary
When operating with full symbolic information, each instruction contains a collection of information about the variables which are live at that particular instruction and where they are located.
## Object Properties
|Name|Description|
|--- |--- |
|LocationKind|A string describing what kind of location the variable is stored in (e.g.: "Register", "RegisterRelative", etc...)|
|Offset|The offset from the location where the variable is stored. For a variable stored at [rbp + 8], for instance, the offset would be 8.|
|Register|A [register](dbgmodel-object-register.md) object which describes the register where the variable is stored or relative to.|
|VariableName|The name of the variable which is being described.|
