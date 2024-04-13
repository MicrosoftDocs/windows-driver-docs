---
title: "c (Compare Memory)"
description: "The c command compares the values held in two memory areas."
keywords: ["c (Compare Memory) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- c (Compare Memory)
api_type:
- NA
---

# c (Compare Memory)


The **c** command compares the values held in two memory areas.

```dbgcmd
c Range Address 
```

## <span id="ddk_cmd_compare_memory_dbg"></span><span id="DDK_CMD_COMPARE_MEMORY_DBG"></span>Parameters


<span id="_______Range______"></span><span id="_______range______"></span><span id="_______RANGE______"></span> *Range*   
The first of the two memory ranges to be compared. For more syntax details, see [Address and Address Range Syntax](address-and-address-range-syntax.md).

<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
The starting address of the second memory range to be compared. The size of this range will be the same as that specified for the first range. For more syntax details, see [Address and Address Range Syntax](address-and-address-range-syntax.md).

## Environment

|  Item  | Description          |
|--------|----------------------|
|Modes   |User mode, kernel mode|
|Targets |Live, crash dump      |
|Platforms|All                  |

 

## Additional Information

For an overview of memory manipulation and a description of other memory-related commands, see [Reading and Writing Memory](../debugger/reading-and-writing-memory.md).

## Remarks

If the two areas are not identical, the debugger will display all memory addresses in the first range where they do not agree.

As an example, consider the following code:

```cpp
void main()
{
    char rgBuf1[100];
    char rgBuf2[100];

    memset(rgBuf1, 0xCC, sizeof(rgBuf1));
    memset(rgBuf2, 0xCC, sizeof(rgBuf2));

    rgBuf1[42] = 0xFF;
}
```

To compare **rgBuf1** and **rgBuf2**, use either of the following commands:

```dbgcmd
0:000> c rgBuf1 (rgBuf1+0n100) rgBuf2

0:000> c rgBuf1 L 0n100 rgBuf2
```

