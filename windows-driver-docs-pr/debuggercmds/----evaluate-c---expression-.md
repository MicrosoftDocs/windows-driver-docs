---
title: (Evaluate C++ Expression)
description: The double question mark ( ) command evaluates and displays the value of an expression according to C++ expression rules.
keywords: ["(Evaluate C++ Expression) Windows Debugging"]
ms.date: 08/30/2023
topic_type:
- apiref
ms.topic: reference
api_name:
- (Evaluate C++ Expression)
api_type:
- NA
adobe-target: true
---

# ?? (Evaluate C++ Expression)

The double question mark (**??**) command evaluates and displays the value of an expression according to C++ expression rules.

```dbgcmd
?? Expression
```

## Parameters

*Expression*

Specifies the C++ expression to evaluate. For more information about the syntax, see [C++ Numbers and Operators](c---numbers-and-operators.md).

### Environment

|  Item  | Description          |
|--------|----------------------|
|Modes   |User mode, kernel mode|
|Targets |Live, crash dump      |
|Platforms|All                  |

## Remarks

The **??** command evaluates symbols in the expression in the context of the current thread and process.

If you want to evaluate a part of the expression according to MASM expression rules, enclose that part in parentheses and add two at signs ( `@@` ) before it. For more information about MASM expressions and C++ expressions, see [Evaluating Expressions](evaluating-expressions.md) and [Numerical Expression Syntax](numerical-expression-syntax.md).

## See also

[? (Evaluate Expression)](---evaluate-expression-.md)

[.formats (Show Number Formats)](-formats--show-number-formats-.md)

[Evaluating Expressions](evaluating-expressions.md)

[Numerical Expression Syntax](numerical-expression-syntax.md)
