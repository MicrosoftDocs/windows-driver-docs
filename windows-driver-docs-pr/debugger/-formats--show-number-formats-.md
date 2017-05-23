---
title: .formats (Show Number Formats)
description: The .formats command evaluates an expression or symbol in the context of the current thread and process and displays it in multiple numeric formats.
ms.assetid: 9eac92b3-5137-4adb-a074-31510dc9bff7
keywords: [".formats (Show Number Formats) Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- .formats (Show Number Formats)
api_type:
- NA
---

# .formats (Show Number Formats)


The **.formats** command evaluates an expression or symbol in the context of the current thread and process and displays it in multiple numeric formats.

``` syntax
.formats expression 
```

## <span id="ddk_meta_show_number_formats_dbg"></span><span id="DDK_META_SHOW_NUMBER_FORMATS_DBG"></span>Parameters


<span id="_______expression______"></span><span id="_______EXPRESSION______"></span> *expression*   
Specifies the expression to evaluate. For more information about the syntax, see [Numerical Expression Syntax](numerical-expression-syntax.md).

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

The evaluated expression is displayed in hexadecimal, decimal, octal, and binary formats, as well as single-precision and double-precision floating-point format. ASCII character formats are also displayed when the bytes correspond to standard ASCII characters. The expression is also interpreted as a time stamp if it is in the allowed range.

The following example shows a **.formats** command.

```
0:000> .formats 1c407e62
Evaluate expression:
  Hex:     1c407e62
  Decimal: 473988706
  Octal:   03420077142
  Binary:  00011100 01000000 01111110 01100010
  Chars:   .@~b
  Time:    Mon Jan 07 15:31:46 1985
  Float:   low 6.36908e-022 high 0
  Double:  2.34182e-315
```

The **Time** field displays a 32-bit value in CRT time stamp format and displays a 64-bit value in FILETIME format. You can distinguish these formats because the FILETIME format includes milliseconds and the CRT format does not.

## <span id="see_also"></span>See also


[**? (Evaluate Expression)**](---evaluate-expression-.md)

[**?? (Evaluate C++ Expression)**](----evaluate-c---expression-.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20.formats%20%28Show%20Number%20Formats%29%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





