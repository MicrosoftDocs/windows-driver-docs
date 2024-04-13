---
title: "dl (Display Linked List)"
description: "The dl command displays a LIST_ENTRY or SINGLE_LIST_ENTRY linked list."
keywords: ["dl (Display Linked List) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- dl (Display Linked List)
api_type:
- NA
---

# dl (Display Linked List)


The **dl** command displays a LIST\_ENTRY or SINGLE\_LIST\_ENTRY linked list.

```dbgcmd
dl[b] Address MaxCount Size
```

## <span id="ddk_cmd_display_linked_list_dbg"></span><span id="DDK_CMD_DISPLAY_LINKED_LIST_DBG"></span>Parameters


<span id="_______b______"></span><span id="_______B______"></span> **b**   
If this is included, the list is dumped in reverse order. (In other words, the debugger follows the **Blink**s instead of the **Flink**s.) This cannot be used with a SINGLE\_LIST\_ENTRY.

<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
The starting address of the list. For more syntax details, see [Address and Address Range Syntax](address-and-address-range-syntax.md).

<span id="_______MaxCount______"></span><span id="_______maxcount______"></span><span id="_______MAXCOUNT______"></span> *MaxCount*   
Maximum number of elements to dump.

<span id="_______Size______"></span><span id="_______size______"></span><span id="_______SIZE______"></span> *Size*   
Size of each element. This is the number of consecutive ULONG\_PTRs that will be displayed for each element in the list.

## Environment

|  Item  | Description          |
|--------|----------------------|
|Modes   |User mode, kernel mode|
|Targets |Live, crash dump      |
|Platforms|All                  |

 

## Additional Information

For an overview of memory manipulation and a description of other memory-related commands, see [Reading and Writing Memory](../debugger/reading-and-writing-memory.md).

## Remarks

This list must be a LIST\_ENTRY or SINGLE\_LIST\_ENTRY structure. If this is embedded in a larger structure, be sure that *Address* points to the linked list structure and not to the beginning of the outer structure.

The display begins with *Address*. Therefore, if you are supplying the address of a pointer that points to the beginning of the list, you should disregard the first element printed.

The *Address*, *MaxCount*, and *Size* parameters are in the current default radix. You can use the [**n (Set Number Base)**](n--set-number-base-.md) command or the **0x** prefix to change the radix.

If the list loops back on itself, the dump will stop. If a null pointer is encountered, the dump will stop.

If you want to execute some command for each element of the list, use the [**!list**](-list.md) extension.

