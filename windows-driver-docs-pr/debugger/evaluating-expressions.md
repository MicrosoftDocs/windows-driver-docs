---
title: Evaluating Expressions
description: Evaluating Expressions
ms.assetid: f2fbdac1-2c20-4132-b43e-4c7a90a2f5b7
keywords: ["expressions, overview", "expressions, different types", "MASM expressions, when to use", "C++ expressions, when to use", "MASM expressions, overview", "C++ expressions, overview"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Evaluating Expressions


## <span id="ddk_evaluating_expressions_dbg"></span><span id="DDK_EVALUATING_EXPRESSIONS_DBG"></span>


The debugger understands two different forms of expressions: *MASM expressions* and *C++ expressions*.

Microsoft Macro Assembler (MASM) expressions are used in the examples in this Help documentation, except when otherwise noted. In MASM expressions, all symbols are treated as addresses.

C++ expressions are the same as those used in actual C++ code. In these expressions, symbols are understood as the appropriate data types.

### <span id="when_each_syntax_is_used"></span><span id="WHEN_EACH_SYNTAX_IS_USED"></span>When Each Syntax is Used

You can select the default expression evaluator in one of the following ways:

-   Use the \_NT\_EXPR\_EVAL [environment variable](general-environment-variables.md) before the debugger is started.

-   Use the **-ee** {**masm**|**c++**} [command-line option](command-line-options.md) when the debugger is started.

-   Use the [**.expr (Choose Expression Evaluator)**](-expr--choose-expression-evaluator-.md) command to display or change the expression evaluator after the debugger is running.

If you do not use one of the preceding methods, the debugger uses the MASM expression evaluator.

If you want to evaluate an expression without changing the debugger state, you can use the [**? (Evaluate Expression)**](---evaluate-expression-.md) command.

All commands and debugging information windows interpret their arguments through the default expression evaluator, with the following exceptions:

-   The [**?? (Evaluate C++ Expression)**](----evaluate-c---expression-.md) command always uses the C++ expression evaluator.

-   The Watch window always uses the C++ expression evaluator.

-   The [Locals window](locals-window.md) always uses the C++ expression evaluator.

-   Some extension commands always use the MASM expression evaluator (and other extension commands accept only numeric arguments instead of full expressions).

-   If any part of an expression is enclosed in parentheses and you insert two at signs (**@@**) before the expression, the expression is evaluated by the expression evaluator that would not typically be used in this case.

The two at signs (**@@**) enable you to use two different evaluators for different parameters of a single command. It also enables you to evaluate different pieces of a long expression by different methods. You can nest the two at signs. Each appearance of the two at signs switches to the other expression evaluator.

**Warning**   C++ expression syntax is useful for manipulating structures and variables, but it is not well-suited as a parser for the parameters of debugger commands. When you are using debugger commands for general purposes or you are using debugger extensions, you should set MASM expression syntax as the default expression evaluator. If you must have a specific parameter use C++ expression syntax, use the two at sign (**@@**) syntax.

 

For more information about the two different expression types, see [Numerical Expression Syntax](numerical-expression-syntax.md).

### <span id="numbers_in_expressions"></span><span id="NUMBERS_IN_EXPRESSIONS"></span>Numbers in Expressions

Numbers in MASM expressions are interpreted according to the current radix. The [**n (Set Number Base)**](n--set-number-base-.md) command can be used to set the default radix to 16, 10, or 8. All un-prefixed numbers will be interpreted in this base. The default radix can be overridden by specifying the **0x** prefix (hexadecimal), the **0n** prefix (decimal), the **0t** prefix (octal), or the **0y** prefix (binary).

Numbers in C++ expressions are interpreted as decimal numbers unless you specify differently. To specify a hexadecimal integer, add **0x** before the number. To specify an octal integer, add **0** (zero) before the number. (However, in the debugger's *output*, the **0n** decimal prefix is sometimes used.)

If you want to display a number in several bases at the same time, use the [**.formats (Show Number Formats)**](-formats--show-number-formats-.md) command.

### <span id="symbols_in_expressions"></span><span id="SYMBOLS_IN_EXPRESSIONS"></span>Symbols in Expressions

The two types of expressions interpret symbols differently:

-   In MASM expressions, each symbol is interpreted as an address. Depending on what the symbol refers to, this address is the address of a global variable, local variable, function, segment, module, or any other recognized label.

-   In C++ expressions, each symbol is interpreted according to its type. Depending on what the symbol refers to, it might be interpreted as an integer, a data structure, a function pointer, or any other data type. A symbol that does not correspond to a C++ data type (such as an unmodified module name) creates a syntax error.

If a symbol might be ambiguous, precede it with the module name and an exclamation point ( **!** ). If the symbol name could be interpreted as a hexadecimal number, precede it with the module name and an exclamation point ( **!** ) or only an exclamation point. In order to specify that a symbol is meant to be local, omit the module name, and include a dollar sign and an exclamation point ( **$!** ) before the symbol name. For more information about interpreting symbols, see [Symbol Syntax and Symbol Matching](symbol-syntax-and-symbol-matching.md).

### <span id="operators_in_expressions"></span><span id="OPERATORS_IN_EXPRESSIONS"></span>Operators in Expressions

Each expression type uses a different collection of operators.

For more information about the operators that you can use in MASM expressions and their precedence rules, see [MASM Numbers and Operators](masm-numbers-and-operators.md).

For more information about the operators that you can use in C++ expressions and their precedence rules, see [C++ Numbers and Operators](c---numbers-and-operators.md).

Remember that MASM operations are always byte-based, and C++ operations follow C++ type rules (including the scaling of pointer arithmetic).

For some examples of the different syntaxes, see [Expression Examples](expression-examples.md).

 

 





