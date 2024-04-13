---
title: "m (Move Memory)"
description: "The m command copies the contents of memory from one location to another. Do not confuse this command with the ~m (Resume Thread) command."
keywords: ["m (Move Memory) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- m (Move Memory)
api_type:
- NA
---

# m (Move Memory)


The **m** command copies the contents of memory from one location to another.

Do not confuse this command with the [**~m (Resume Thread)**](-m--resume-thread-.md) command.

```dbgcmd
m Range Address 
```

## <span id="ddk_cmd_move_memory_dbg"></span><span id="DDK_CMD_MOVE_MEMORY_DBG"></span>Parameters


<span id="_______Range______"></span><span id="_______range______"></span><span id="_______RANGE______"></span> *Range*   
Specifies the memory area to copy. For more information about the syntax of this parameter, see [Address and Address Range Syntax](address-and-address-range-syntax.md).

<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the starting address of the destination memory area. For more information about the syntax of this parameter, see [Address and Address Range Syntax](address-and-address-range-syntax.md).

## Environment

|  Item  | Description          |
|--------|----------------------|
|Modes   |User mode, kernel mode|
|Targets |Live, crash dump      |
|Platforms|All                  |

 

## Additional Information

For more information about memory manipulation and a description of other memory-related commands, see [Reading and Writing Memory](../debugger/reading-and-writing-memory.md).

## Remarks

The memory area that *Address* specifies can be part of the memory area that *Range* specifies. Overlapping moves are handled correctly.

