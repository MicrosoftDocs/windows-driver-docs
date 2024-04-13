---
title: "ls, lsa (List Source Lines)"
description: "The ls and lsa commands display a series of lines from the current source file and advance the current source line number."
keywords: ["ls, lsa (List Source Lines) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- ls, lsa (List Source Lines)
api_type:
- NA
---

# ls, lsa (List Source Lines)


The **ls** and **lsa** commands display a series of lines from the current source file and advance the current source line number.

```dbgcmd
ls [.] [first] [, count] 
lsa [.] address [, first [, count]] 
```

## <span id="ddk_cmd_list_source_lines_dbg"></span><span id="DDK_CMD_LIST_SOURCE_LINES_DBG"></span>Parameters


 **.**   
Causes the command to look for the source file that the debugger engine or the [**.srcpath (Set Source Path)**](-srcpath---lsrcpath--set-source-path-.md) command are using. If the period (**.**) is not included, **ls** uses the file that was most recently loaded with the [**lsf (Load Source File)**](lsf--lsf---load-or-unload-source-file-.md) command.

<span id="_______address______"></span><span id="_______ADDRESS______"></span> *address*   
Specifies the address where the source display is to begin.

For more information about the syntax, see [Address and Address Range Syntax](address-and-address-range-syntax.md).

<span id="_______first______"></span><span id="_______FIRST______"></span> *first*   
Specifies the first line to display. The default value is the current line.

<span id="_______count______"></span><span id="_______COUNT______"></span> *count*   
Specifies the quantity of lines to display. The default value is 20 (0x14), unless you have changed the default value by using the [**lsp -a**](lsp--set-number-of-source-lines-.md) command.

## Environment

|  Item  | Description          |
|--------|----------------------|
|Modes   |User mode, kernel mode|
|Targets |Live, crash dump      |
|Platforms|All                  |

 

## Remarks

After you run the **ls** or **lsa** command, the current line is redefined as the final line that is displayed plus one. The current line is used in future **ls**, **lsa**, and [**lsc**](lsc--list-current-source-.md) commands.

## See also


[**lsc (List Current Source)**](lsc--list-current-source-.md)

[**lsf, lsf- (Load or Unload Source File)**](lsf--lsf---load-or-unload-source-file-.md)


