---
title: ".holdmem (Hold and Compare Memory)"
description: "The .holdmem command saves memory ranges and compares them to other memory ranges."
keywords: ["Hold and Compare Memory (.holdmem) command", "memory, Hold and Compare Memory (.holdmem) command", ".holdmem (Hold and Compare Memory) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- .holdmem (Hold and Compare Memory)
api_type:
- NA
---

# .holdmem (Hold and Compare Memory)


The **.holdmem** command saves memory ranges and compares them to other memory ranges.

```dbgcmd
.holdmem -a Range 
.holdmem -d { Range | Address } 
.holdmem -D 
.holdmem -o 
.holdmem -c Range 
```

## <span id="ddk_meta_hold_and_compare_memory_dbg"></span><span id="DDK_META_HOLD_AND_COMPARE_MEMORY_DBG"></span>Parameters


<span id="_______-a_Range_____________"></span><span id="_______-a_range_____________"></span><span id="_______-A_RANGE_____________"></span> **-a** **** *Range*   
Specifies the memory range to save. For more information about the syntax, see [Address and Address Range Syntax](address-and-address-range-syntax.md).

<span id="_______-d___Range___Address__"></span><span id="_______-d___range___address__"></span><span id="_______-D___RANGE___ADDRESS__"></span> **-d** **** { *Range* | *Address* }  
Specifies memory ranges to delete. If you specify *Address*, the debugger deletes any saved range that contains that address. If you specify *Range*, the debugger deletes any saved range that overlaps with *Range*. For more information about the syntax, see [Address and Address Range Syntax](address-and-address-range-syntax.md).

<span id="_______-D______"></span><span id="_______-d______"></span> **-D**   
Deletes all saved memory ranges.

<span id="_______-o______"></span><span id="_______-O______"></span> **-o**   
Displays all saved memory ranges.

<span id="_______-c_______Range______"></span><span id="_______-c_______range______"></span><span id="_______-C_______RANGE______"></span> **-c** *Range*   
Compares the specified range to all saved memory ranges. For more information about the syntax, see [Address and Address Range Syntax](address-and-address-range-syntax.md).

## Environment

|  Item  | Description          |
|--------|----------------------|
|Modes   |User mode, kernel mode|
|Targets |Live, crash dump      |
|Platforms|All                  |

 

## Additional Information

For more information about how to manipulate memory and a description of other memory-related commands, see [Reading and Writing Memory](../debugger/reading-and-writing-memory.md).

## Remarks

The **.holdmem** command compares memory ranges byte-for-byte.

If any of the specified memory locations do not exist in the virtual address space, the command returns an error.

