---
title: (Evaluate Expression)
description: The question mark ( ) command evaluates and displays the value of an expression.Note � A question mark by itself ( ) displays command help.
ms.assetid: fae689b3-47c9-44bd-992d-8344805fb4b7
keywords: ["(Evaluate Expression) Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- (Evaluate Expression)
api_type:
- NA
---

# ? (Evaluate Expression)


The question mark (**?**) command evaluates and displays the value of an expression.

**Note**   A question mark by itself ([**?**](---command-help-.md)) displays command help. The **?** *expression* command evaluates the given expression.

 

```
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

```
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
Syntax error at &#39;( "c:\dir\", "*filename*" )
```

In the first two examples, even though the string does match the pattern, the evaluator is returning a value of **FALSE**. In the third, the evaluator cannot make a comparison because the string ends in a backslash ( \\ ), and so the **\\"** is translated by the evaluator.

To get the evaluator to interpret a string literally, you must use the **@"***String***"** syntax. The following code example shows the correct results:

```
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20?%20%28Evaluate%20Expression%29%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





