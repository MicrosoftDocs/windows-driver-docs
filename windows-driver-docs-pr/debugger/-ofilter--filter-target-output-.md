---
title: .ofilter (Filter Target Output)
description: The .ofilter command filters the output from the target application or target computer.
ms.assetid: 0b94d177-0e41-4781-b0bc-ed58cee584f1
keywords: ["Filter Target Output (.ofilter) command", ".ofilter (Filter Target Output) Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- .ofilter (Filter Target Output)
api_type:
- NA
---

# .ofilter (Filter Target Output)


The **.ofilter** command filters the output from the target application or target computer.

``` syntax
.ofilter [/!] String 
.ofilter "" 
.ofilter 
```

## <span id="ddk_meta_filter_target_output_dbg"></span><span id="DDK_META_FILTER_TARGET_OUTPUT_DBG"></span>Parameters


<span id="_______________"></span> **/!**   
Reverses the filter so that the debugger displays only output that does not contain *String*. If you do not use this parameter, the debugger displays only output that contains *String*.

<span id="_______String______"></span><span id="_______string______"></span><span id="_______STRING______"></span> *String*   
Specifies the string to match in the target's output. *String* can include spaces, but you cannot use C-style control characters such as **\\"** and **\\n**. *String* might contain a variety of wildcard characters and specifiers. For more information about the syntax, see [String Wildcard Syntax](string-wildcard-syntax.md).

You can enclose *String* in quotation marks. However, if *String* includes a semicolon, leading spaces, or trailing spaces, you must use quotation marks. Alphanumeric characters in *String* are converted to uppercase letters, but the actual pattern matching is case insensitive.

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

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information about [**OutputDebugString**](https://msdn.microsoft.com/library/windows/desktop/aa363362) and other user-mode routines, see the Microsoft Windows SDK documentation. For more information about **DbgPrint**, **DbgPrintEx**, and other kernel-mode routines, see the Windows Driver Kit (WDK).

Remarks
-------

If you use the **.ofilter** command without parameters, the debugger displays the current pattern-matching criteria.

To clear the existing filter, use **.ofilter ""**. This command filters any data that is sent by user-mode routines (such as [**OutputDebugString**](https://msdn.microsoft.com/library/windows/desktop/aa363362)) and kernel-mode routines (such as **DbgPrint**). However, the debugger always displays prompts that **DbgPrompt** sends.

The **DbgPrintEx** and **KdPrintEx** routines supply another method of filtering debugging messages that you do not want.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20.ofilter%20%28Filter%20Target%20Output%29%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




