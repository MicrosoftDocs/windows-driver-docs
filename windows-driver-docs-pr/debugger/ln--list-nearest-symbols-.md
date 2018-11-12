---
title: ln (List Nearest Symbols)
description: The ln command displays the symbols at or near the given address.
ms.assetid: ff01ace7-398a-4e32-9d58-00873eca3201
keywords: ["ln (List Nearest Symbols) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- ln (List Nearest Symbols)
api_type:
- NA
ms.localizationpriority: medium
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
Specifies that the output is displayed using [Debugger Markup Language (DML)](debugger-markup-language-commands.md). The DML output includes a link that you can use to explore the module that contains the nearest symbol. It also includes a link that you can use to set a breakpoint.

### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Modes</p></td>
<td align="left"><p>User mode, kernel mode</p></td>
</tr>
<tr class="even">
<td align="left"><p>Targets</p></td>
<td align="left"><p>Live, crash dump</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Platforms</p></td>
<td align="left"><p>All</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

You can use the **ln** command to help determine what a pointer is pointing to. This command can also be useful when you are looking at a corrupted stack to determine which procedure made a call.

If source line information is available, the **ln** display also includes the source file name and line number information.

If you are using a [source server](using-a-source-server.md), the **ln** command displays information that is related to the source server.

 

 





