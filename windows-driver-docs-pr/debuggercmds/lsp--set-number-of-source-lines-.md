---
title: "lsp (Set Number of Source Lines)"
description: "The lsp command controls how many source lines are displayed while you step through or execute code or use the ls and lsa commands."
keywords: ["lsp (Set Number of Source Lines) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- lsp (Set Number of Source Lines)
api_type:
- NA
---

# lsp (Set Number of Source Lines)


The **lsp** command controls how many source lines are displayed while you step through or execute code or use the [**ls and lsa commands**](ls--lsa--list-source-lines-.md).

```dbgcmd
lsp [-a] LeadingLines TrailingLines 
lsp [-a] TotalLines 
lsp [-a] 
```

## <span id="ddk_cmd_set_number_of_source_lines_dbg"></span><span id="DDK_CMD_SET_NUMBER_OF_SOURCE_LINES_DBG"></span>Parameters


<span id="_______-a______"></span><span id="_______-A______"></span> **-a**   
Sets or displays the number of lines that **ls** and **lsa** show. If you omit **-a**, **lsp** sets or displays the number of lines that are shown while you step through and execute code.

<span id="_______LeadingLines______"></span><span id="_______leadinglines______"></span><span id="_______LEADINGLINES______"></span> *LeadingLines*   
Specifies the number of lines to show before the current line.

<span id="_______TrailingLines______"></span><span id="_______trailinglines______"></span><span id="_______TRAILINGLINES______"></span> *TrailingLines*   
Specifies the number of lines to show after the current line.

<span id="_______TotalLines______"></span><span id="_______totallines______"></span><span id="_______TOTALLINES______"></span> *TotalLines*   
Specifies the total number of lines to show. This number is divided evenly between leading and trailing lines. (If this number is odd, more trailing lines are displayed.)

## Environment

|  Item  | Description          |
|--------|----------------------|
|Modes   |User mode, kernel mode|
|Targets |Live, crash dump      |
|Platforms|All                  |

 

## Remarks

When you use the **lsp** command together with no parameters, **lsp** displays the current leading line and trailing line values that you used while stepping. When you use this command together with only the **-a** parameter, **lsp** displays the values that you used while stepping and for the [**ls and lsa commands**](ls--lsa--list-source-lines-.md).

When you step through a program or break in after program execution, the previous **lsp** command determines the number of leading and trailing lines that are displayed. When you use **lsa**, the previous **lsp -a** command determines the number of leading and trailing lines that are displayed. When you use **ls**, all lines appear as a single block, so the previous **lsp -a** command determines the total number of lines that are displayed.

## Additional Information

For more information about source debugging and related commands, see [Debugging in Source Mode](../debugger/debugging-in-source-mode.md).

