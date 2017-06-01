---
title: (Evaluate C++ Expression)
description: The double question mark ( ) command evaluates and displays the value of an expression according to C++ expression rules.
ms.assetid: 3a15a0a3-03d0-4807-a6df-054de819c0a0
keywords: ["(Evaluate C++ Expression) Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- (Evaluate C++ Expression)
api_type:
- NA
---

# ?? (Evaluate C++ Expression)


The double question mark (**??**) command evaluates and displays the value of an expression according to C++ expression rules.

```
?? Expression
```

## <span id="ddk_cmd_evaluate_c_expression_dbg"></span><span id="DDK_CMD_EVALUATE_C_EXPRESSION_DBG"></span>Parameters


<span id="_______Expression______"></span><span id="_______expression______"></span><span id="_______EXPRESSION______"></span> *Expression*   
Specifies the C++ expression to evaluate. For more information about the syntax, see [C++ Numbers and Operators](c---numbers-and-operators.md).

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

The **??** command evaluates symbols in the expression in the context of the current thread and process.

If you want to evaluate a part of the **Expression** expression according to MASM expression rules, enclose that part in parentheses and add two at signs ( **@@** ) before it. For more information about MASM expressions and C++ expressions, see [Evaluating Expressions](evaluating-expressions.md) and [Numerical Expression Syntax](numerical-expression-syntax.md).

## <span id="see_also"></span>See also


[**? (Evaluate Expression)**](---evaluate-expression-.md)

[**.formats (Show Number Formats)**](-formats--show-number-formats-.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20??%20%28Evaluate%20C++%20Expression%29%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





