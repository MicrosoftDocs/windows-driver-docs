---
title: .typeopt (Set Type Options)
description: The .typeopt command sets or displays the type options.
ms.assetid: 17842897-26e3-4b61-aa65-e5cfe8576324
keywords: [".typeopt (Set Type Options) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- .typeopt (Set Type Options)
api_type:
- NA
ms.localizationpriority: medium
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

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="______________"></span> **+**   
Causes the type options specified by *FlagName* to be set.

<span id="_______-______"></span> **-**   
Causes the type options specified by *FlagName* to be cleared.

<span id="_______Flags______"></span><span id="_______flags______"></span><span id="_______FLAGS______"></span> *Flags*   
Specifies the type options to be changed. *FlagName* can be a sum of any of the following values (there is no default):

<span id="0x1"></span><span id="0X1"></span>**0x1**  
Displays values in all Watch windows and the Locals window as having UNICODE data type.

<span id="0x2"></span><span id="0X2"></span>**0x2**  
Displays values in all Watch windows and the Locals window as having LONG data type.

<span id="0x4"></span><span id="0X4"></span>**0x4**  
Displays integers in all Watch windows and the Locals window in the default radix.

<span id="0x8"></span><span id="0X8"></span>**0x8**  
Causes the debugger to choose the matching symbol with the largest size when the Locals window or Watch window references a symbol by name but there is more than one symbol that matches this name. The size of a symbol is defined as follows: if the symbol is the name of a function, its size is the size of the function in memory. Otherwise, the size of the symbol is the size of the data type that it represents.

<span id="_______FlagName______"></span><span id="_______flagname______"></span><span id="_______FLAGNAME______"></span> *FlagName*   
Specifies the type options to be changed. *FlagName* can be any one of the following strings (there is no default):

<span id="uni"></span><span id="UNI"></span>**uni**  
Displays values in all Watch windows and the Locals window as having UNICODE data type. (This has the same effect as **0x1**.)

<span id="longst"></span><span id="LONGST"></span>**longst**  
Displays values in all Watch windows and the Locals window as having LONG data type. (This has the same effect as **0x2**.)

<span id="radix"></span><span id="RADIX"></span>**radix**  
Displays integers in all Watch windows and the Locals window in the default radix. (This has the same effect as **0x4**.)

<span id="size"></span><span id="SIZE"></span>**size**  
Causes the debugger to choose the matching symbol with the largest size when the Locals window or Watch window references a symbol by name but there is more than one symbol that matches this name. The size of a symbol is defined as follows: if the symbol is the name of a function, its size is the size of the function in memory. Otherwise, the size of the symbol is the size of the data type that it represents. (This has the same effect as **0x8**.)

### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Modes</strong></p></td>
<td align="left"><p>user mode, kernel mode</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Targets</strong></p></td>
<td align="left"><p>live, crash dump</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Platforms</strong></p></td>
<td align="left"><p>all</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

Without any arguments, **.typeopt** displays the current symbol options.

 

 





