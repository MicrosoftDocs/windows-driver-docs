---
title: lsp (Set Number of Source Lines)
description: The lsp command controls how many source lines are displayed while you step through or execute code or use the ls and lsa commands.
ms.assetid: 350933f1-5459-4ba2-9ca7-a42341cf95de
keywords: ["lsp (Set Number of Source Lines) Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- lsp (Set Number of Source Lines)
api_type:
- NA
---

# lsp (Set Number of Source Lines)


The **lsp** command controls how many source lines are displayed while you step through or execute code or use the [**ls and lsa commands**](ls--lsa--list-source-lines-.md).

``` syntax
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

When you use the **lsp** command together with no parameters, **lsp** displays the current leading line and trailing line values that you used while stepping. When you use this command together with only the **-a** parameter, **lsp** displays the values that you used while stepping and for the [**ls and lsa commands**](ls--lsa--list-source-lines-.md).

When you step through a program or break in after program execution, the previous **lsp** command determines the number of leading and trailing lines that are displayed. When you use **lsa**, the previous **lsp -a** command determines the number of leading and trailing lines that are displayed. When you use **ls**, all lines appear as a single block, so the previous **lsp -a** command determines the total number of lines that are displayed.

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information about source debugging and related commands, see [Debugging in Source Mode](debugging-in-source-mode.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20lsp%20%28Set%20Number%20of%20Source%20Lines%29%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




