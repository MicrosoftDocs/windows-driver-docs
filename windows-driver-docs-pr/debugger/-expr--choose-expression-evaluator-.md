---
title: .expr (Choose Expression Evaluator)
description: The .expr command specifies the default expression evaluator.
keywords: [".expr (Choose Expression Evaluator) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- .expr (Choose Expression Evaluator)
api_type:
- NA
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

### Environment

|  Item  | Description          |
|--------|----------------------|
|Modes   |User mode, kernel mode|
|Targets |Live, crash dump      |
|Platforms|All                  |

 

## Remarks

When you use the **.expr** command without an argument, the debugger displays the current default expression type.

The [**?? (Evaluate C++ Expression)**](----evaluate-c---expression-.md) command, the Watch window, and the [Locals window](locals-window.md) always use C++ expression syntax. All other commands and debugging information windows use the default expression evaluator.

For more information about how to control which syntax is used, see [Evaluating Expressions](evaluating-expressions.md). For more information about the syntax, see [Numerical Expression Syntax](numerical-expression-syntax.md).


## See also

[? (Evaluate Expression)](---evaluate-expression-.md)

[MASM Numbers and Operators](masm-numbers-and-operators.md)

[C++ Numbers and Operators](c---numbers-and-operators.md)








