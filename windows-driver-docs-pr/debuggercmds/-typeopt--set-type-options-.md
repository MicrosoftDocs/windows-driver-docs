---
title: ".typeopt (Set Type Options)"
description: "The .typeopt command sets or displays the type options."
keywords: [".typeopt (Set Type Options) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- .typeopt (Set Type Options)
api_type:
- NA
---

# .typeopt (Set Type Options)

The **.typeopt** command sets or displays the type options.

```dbgcmd
.typeopt +Flags 
.typeopt -Flags 
.typeopt +FlagName 
.typeopt -FlagName 
.typeopt 
```

## Parameters

<span id="______________"></span> **+**   
Causes the type option(s) specified by *Flags* or *FlagName* to be set.

<span id="_______-______"></span> **-**   
Causes the type option(s) specified by *Flags* or *FlagName* to be cleared.

<span id="_______Flags______"></span><span id="_______flags______"></span><span id="_______FLAGS______"></span> *Flags*   
Specifies the type options to be changed. *Flags* can be a sum of any of the following values (there is no default):

<span id="0x1"></span><span id="0X1"></span>**0x1**  
Displays unsigned 16-bit integer values in all Watch windows and the Locals window as having UNICODE data type.

<span id="0x2"></span><span id="0X2"></span>**0x2**  
Displays signed 32-bit integer values in all Watch windows and the Locals window as unsigned integers in the default radix.

<span id="0x4"></span><span id="0X4"></span>**0x4**  
Displays signed integers of all sizes in all Watch windows and the Locals window as unsigned values in the default radix.

<span id="0x8"></span><span id="0X8"></span>**0x8**  
Causes the debugger to choose the matching symbol with the largest size when the Locals window or Watch window references a symbol by name but there is more than one symbol that matches this name. The size of a symbol is defined as follows: if the symbol is the name of a function, its size is the size of the function in memory. Otherwise, the size of the symbol is the size of the data type that it represents.

<span id="_______FlagName______"></span><span id="_______flagname______"></span><span id="_______FLAGNAME______"></span> *FlagName*   
Specifies the type options to be changed. *FlagName* can be any one of the following strings (there is no default):

<span id="uni"></span><span id="UNI"></span>**uni**  
Displays unsigned 16-bit integer values in all Watch windows and the Locals window as having UNICODE data type. (This has the same effect as **0x1**.)

<span id="longst"></span><span id="LONGST"></span>**longst**  
Displays signed 32-bit integer values in all Watch windows and the Locals window as unsigned integers in the default radix. (This has the same effect as **0x2**.)

<span id="radix"></span><span id="RADIX"></span>**radix**  
Displays signed integers of all sizes in all Watch windows and the Locals window as unsigned values in the default radix. (This has the same effect as **0x4**.)

<span id="size"></span><span id="SIZE"></span>**size**  
Causes the debugger to choose the matching symbol with the largest size when the Locals window or Watch window references a symbol by name but there is more than one symbol that matches this name. The size of a symbol is defined as follows: if the symbol is the name of a function, its size is the size of the function in memory. Otherwise, the size of the symbol is the size of the data type that it represents. (This has the same effect as **0x8**.)

## Environment

|  Item  | Description          |
|--------|----------------------|
|Modes   |User mode, kernel mode|
|Targets |Live, crash dump      |
|Platforms|All                  |

## Remarks

Without any arguments, **.typeopt** displays the current symbol options.

To change the default radix, use the [**n (Set Number Base)**](n--set-number-base-.md) command.
