---
title: "ln (List Nearest Symbols)"
description: "The ln command displays the symbols at or near the given address."
keywords: ["ln (List Nearest Symbols) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- ln (List Nearest Symbols)
api_type:
- NA
---

# ln (List Nearest Symbols)


The **ln** command displays the symbols at or near the given address.

```dbgcmd
ln Address
ln /D Address 
```

## <span id="ddk_cmd_list_nearest_symbols_dbg"></span><span id="DDK_CMD_LIST_NEAREST_SYMBOLS_DBG"></span>Parameters


<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the address where the debugger should start to search for symbols. The nearest symbols, either before or after *Address*, are displayed. For more information about the syntax, see [Address and Address Range Syntax](address-and-address-range-syntax.md).

<span id="_D"></span><span id="_d"></span>**/D**  
Specifies that the output is displayed using [Debugger Markup Language (DML)](../debugger/debugger-markup-language-commands.md). The DML output includes a link that you can use to explore the module that contains the nearest symbol. It also includes a link that you can use to set a breakpoint.

## Environment

|  Item  | Description          |
|--------|----------------------|
|Modes|User mode, kernel mode|
|Targets|Live, crash dump|
|Platforms|All|

 

## Remarks

You can use the **ln** command to help determine what a pointer is pointing to. This command can also be useful when you are looking at a corrupted stack to determine which procedure made a call.

If source line information is available, the **ln** display also includes the source file name and line number information.

If you are using a [source server](../debugger/using-a-source-server.md), the **ln** command displays information that is related to the source server.

