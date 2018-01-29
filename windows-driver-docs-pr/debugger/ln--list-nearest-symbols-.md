---
title: ln (List Nearest Symbols)
description: The ln command displays the symbols at or near the given address.
ms.assetid: ff01ace7-398a-4e32-9d58-00873eca3201
keywords: ["ln (List Nearest Symbols) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- ln (List Nearest Symbols)
api_type:
- NA
---

# ln (List Nearest Symbols)


The **ln** command displays the symbols at or near the given address.

```
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20ln%20%28List%20Nearest%20Symbols%29%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




