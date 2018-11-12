---
title: .formats (Show Number Formats)
description: The .formats command evaluates an expression or symbol in the context of the current thread and process and displays it in multiple numeric formats.
ms.assetid: 9eac92b3-5137-4adb-a074-31510dc9bff7
keywords: [".formats (Show Number Formats) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- .formats (Show Number Formats)
api_type:
- NA
ms.localizationpriority: medium
---

# .formats (Show Number Formats)


The **.formats** command evaluates an expression or symbol in the context of the current thread and process and displays it in multiple numeric formats.

```dbgcmd
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

```dbgcmd
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

 

 






