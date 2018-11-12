---
title: (Evaluate Expression)
description: The question mark ( ) command evaluates and displays the value of an expression.Note  A question mark by itself ( ) displays command help.
ms.assetid: fae689b3-47c9-44bd-992d-8344805fb4b7
keywords: ["(Evaluate Expression) Windows Debugging"]
ms.author: domars
ms.date: 09/17/2018
topic_type:
- apiref
api_name:
- (Evaluate Expression)
api_type:
- NA
ms.localizationpriority: medium
---

# ? (Evaluate Expression)


The question mark (**?**) command evaluates and displays the value of an expression.

**Note**   A question mark by itself ([**?**](---command-help-.md)) displays command help. The **?** *expression* command evaluates the given expression.

```dbgcmd
    ? Expression
```

## <span id="ddk_cmd_evaluate_expression_dbg"></span><span id="DDK_CMD_EVALUATE_EXPRESSION_DBG"></span>Parameters


<span id="_______Expression______"></span><span id="_______expression______"></span><span id="_______EXPRESSION______"></span> *Expression*   
Specifies the expression to evaluate.

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

The input and output of the **?** command depend on whether you are using MASM expression syntax or C++ expression syntax. For more information about these kinds of expression syntax, see [Evaluating Expressions](evaluating-expressions.md) and [Numerical Expression Syntax](numerical-expression-syntax.md).

If you are using MASM syntax, the input and output depend on the current radix. To change the radix, use the [**n (Set Number Base)**](n--set-number-base-.md) command.

The **?** command evaluates symbols in the expression in the context of the current thread and process.

Some strings may contain escapes, such as **\\n**, **\\"**, **\\r**, and **\\b**, that are meant to be read literally, rather than interpreted by the evaluator. If an escape within a string is interpreted by the evaluator, errors in evaluation can occur. For example:

```console
0:000> as AliasName c:\dir\name.txt
0:000> al
  Alias            Value
 -------          -------
 AliasName        c:\dir\name.txt
0:001> ? $spat( "c:\dir\name.txt", "*name*" )
Evaluate expression: 0 = 00000000
0:001> ? $spat( "${AliasName}", "*name*" )
Evaluate expression: 0 = 00000000
0:001> ? $spat( "c:\dir\", "*filename*" )
Syntax error at '( "c:\dir\", "*filename*" )
```

In the first two examples, even though the string does match the pattern, the evaluator is returning a value of **FALSE**. In the third, the evaluator cannot make a comparison because the string ends in a backslash ( \\ ), and so the **\\"** is translated by the evaluator.

To get the evaluator to interpret a string literally, you must use the <strong>@"</strong>*String*<strong>"</strong> syntax. The following code example shows the correct results:

```console
0:000> ? $spat( @"c:\dir\name.txt", "*name*" )
Evaluate expression: 1 = 00000000`00000001
0:000> ? $spat( @"${AliasName}", "*name*" )
Evaluate expression: 1 = 00000000`00000001
0:001> ? $spat( @"c:\dir\", "*filename*" )
Evaluate expression: 0 = 00000000
```

In the preceding examples, the **$spat** MASM operator checks the first string to determine whether it matches (case-insensitive) the pattern of the second string. For more information about MASM operators, see the [MASM Numbers and Operators](masm-numbers-and-operators.md) topic.

## <span id="see_also"></span>See also


[**?? (Evaluate C++ Expression)**](----evaluate-c---expression-.md)

[**.formats (Show Number Formats)**](-formats--show-number-formats-.md)

 

 






