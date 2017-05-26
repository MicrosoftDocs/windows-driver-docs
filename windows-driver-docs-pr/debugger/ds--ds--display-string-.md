---
title: ds, dS (Display String)
description: The ds and dS commands display a STRING, ANSI\_STRING, or UNICODE\_STRING structure.
ms.assetid: cb05e89c-6c83-476b-a577-a6aeefd8cdd6
keywords: ["ds, dS (Display String) Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- ds, dS (Display String)
api_type:
- NA
---

# ds, dS (Display String)


The **ds** and **dS** commands display a STRING, ANSI\_STRING, or UNICODE\_STRING structure. (These commands do not display null-delimited character strings.)

``` syntax
d{s|S} [/c Width] [Address]
```

## <span id="ddk_cmd_display_string_dbg"></span><span id="DDK_CMD_DISPLAY_STRING_DBG"></span>Parameters


<span id="_______s______"></span><span id="_______S______"></span> **s**   
Specifies that a STRING or ANSI\_STRING structure is to be displayed. (This **s** is case-sensitive.)

<span id="_______S______"></span><span id="_______s______"></span> **S**   
Specifies that a UNICODE\_STRING structure is to be displayed. (This **S** is case-sensitive.)

<span id="________c_______Width______"></span><span id="________c_______width______"></span><span id="________C_______WIDTH______"></span> **/c** *Width*   
Specifies the number of characters to display on each line. This number includes null characters, which will not be visible.

<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
The memory address where the string begins. For more syntax details, see [Address and Address Range Syntax](address-and-address-range-syntax.md). If omitted, the last address used in a display command is assumed.

### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Modes</strong></p></td>
<td align="left"><p>user mode, kernel mode</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Targets</strong></p></td>
<td align="left"><p>live, crash dump</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Platforms</strong></p></td>
<td align="left"><p>all</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For an overview of memory manipulation and a description of other memory-related commands, see [Reading and Writing Memory](reading-and-writing-memory.md).

Remarks
-------

If you want to display Unicode strings in the Locals window or Watch window of WinDbg, you need to use the [**.enable\_unicode (Enable Unicode Display)**](-enable-unicode--enable-unicode-display-.md) command first.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20ds,%20dS%20%28Display%20String%29%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




