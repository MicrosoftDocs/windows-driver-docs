---
title: ls, lsa (List Source Lines)
description: The ls and lsa commands display a series of lines from the current source file and advance the current source line number.
ms.assetid: ca5cd2f7-4920-4d36-b338-c934451bc511
keywords: ["ls, lsa (List Source Lines) Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- ls, lsa (List Source Lines)
api_type:
- NA
---

# ls, lsa (List Source Lines)


The **ls** and **lsa** commands display a series of lines from the current source file and advance the current source line number.

``` syntax
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

### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Modes</strong></p></td>
<td align="left"><p>User mode, kernel mode</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Targets</strong></p></td>
<td align="left"><p>Live, crash dump</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Platforms</strong></p></td>
<td align="left"><p>All</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

After you run the **ls** or **lsa** command, the current line is redefined as the final line that is displayed plus one. The current line is used in future **ls**, **lsa**, and [**lsc**](lsc--list-current-source-.md) commands.

## <span id="see_also"></span>See also


[**lsc (List Current Source)**](lsc--list-current-source-.md)

[**lsf, lsf- (Load or Unload Source File)**](lsf--lsf---load-or-unload-source-file-.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20ls,%20lsa%20%28List%20Source%20Lines%29%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





