---
title: Debugger Data Model - Register Objects
description: The registers which are used by operands within machine instructions are described by register objects.
ms.date: 03/10/2023
ms.topic: reference
---
# Register Objects

## Summary

The registers which are used by operands within machine instructions are described by register objects. The string conversion of a register object is the name of the register.

## Object Properties

|Name|Description|
|--- |--- |
|Id|A unique identifier (within the domain of a specific architecture) for the register.|

## Remarks
Currently, you can only get the register's name through string conversion.
