---
title: .expr (Choose Expression Evaluator)
description: The .expr command specifies the default expression evaluator.
ms.assetid: 96d246c2-10fe-4688-a04f-1325ac51e4b3
keywords: [".expr (Choose Expression Evaluator) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- .expr (Choose Expression Evaluator)
api_type:
- NA
ms.localizationpriority: medium
---

# .expr (Choose Expression Evaluator)


The **.expr** command specifies the default expression evaluator.

```dbgcmd
.expr /s masm 
.expr /s c++ 
.expr /q 
.expr 
```

## <span id="ddk_meta_choose_expression_evaluator_dbg"></span><span id="DDK_META_CHOOSE_EXPRESSION_EVALUATOR_DBG"></span>Parameters


<span id="________s_masm______"></span><span id="________S_MASM______"></span> **/s masm**   
Changes the default expression type to Microsoft Assembler expression evaluator (MASM). This type is the default value when you start the debugger.

<span id="________s_c________"></span><span id="________S_C________"></span> **/s c++**   
Changes the default expression type to the C++ expression evaluator.

<span id="________q______"></span><span id="________Q______"></span> **/q**   
Displays the list of possible expression types.

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

When you use the **.expr** command without an argument, the debugger displays the current default expression type.

The [**?? (Evaluate C++ Expression)**](----evaluate-c---expression-.md) command, the Watch window, and the [Locals window](locals-window.md) always use C++ expression syntax. All other commands and debugging information windows use the default expression evaluator.

For more information about how to control which syntax is used, see [Evaluating Expressions](evaluating-expressions.md). For more information about the syntax, see [Numerical Expression Syntax](numerical-expression-syntax.md).

 

 





