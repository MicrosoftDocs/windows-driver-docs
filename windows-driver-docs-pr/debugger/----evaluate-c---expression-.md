---
title: (Evaluate C++ Expression)
description: The double question mark ( ) command evaluates and displays the value of an expression according to C++ expression rules.
ms.assetid: 3a15a0a3-03d0-4807-a6df-054de819c0a0
keywords: ["(Evaluate C++ Expression) Windows Debugging"]
ms.author: domars
ms.date: 09/17/2018
topic_type:
- apiref
api_name:
- (Evaluate C++ Expression)
api_type:
- NA
ms.localizationpriority: medium
---

# ?? (Evaluate C++ Expression)


The double question mark (**??**) command evaluates and displays the value of an expression according to C++ expression rules.

```dbgcmd
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

 

 






