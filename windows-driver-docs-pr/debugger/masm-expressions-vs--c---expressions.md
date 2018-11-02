---
title: MASM Expressions vs. C++ Expressions
description: MASM Expressions vs.
ms.assetid: 3ec06b61-9f17-49b1-b7c5-66a349b5d275
keywords: ["expressions, MASM and C++", "MASM expressions, MASM vs. C++", "C++ expressions, C++ vs. MASM"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# MASM Expressions vs. C++ Expressions


## <span id="ddk_masm_expressions_vs__c_expressions_dbg"></span><span id="DDK_MASM_EXPRESSIONS_VS__C_EXPRESSIONS_DBG"></span>


The most significant differences between MASM expression evaluation and C++ expression evaluation are as follows:

-   In an MASM expression, the numeric value of any symbol is its memory address. In a C++ expression, the numeric value of a variable is its actual value, not its address. Data structures do not have numeric values. Instead, they are treated as actual structures and you must use them accordingly. The value of a function name or any other entry point is the memory address and is treated as a function pointer. If you use a symbol that does not correspond to a C++ data type (such as an unmodified module name), a syntax error occurs.

-   The MASM expression evaluator treats all numbers as ULONG64 values. The C++ expression evaluator casts numbers to ULONG64 and preserves type information of all data types.

-   The MASM expression evaluator lets you to use any operator together with any number. The C++ expression evaluator generates an error if you use an operator together with an incorrect data type.

-   In the MASM expression evaluator, all arithmetic is performed literally. In the C++ expression evaluator, pointer arithmetic is scaled properly and is not permitted when inappropriate.

-   An MASM expression can use two underscores ( **\_\_** ) or two colons ( **::** ) to indicate members of a class. The C++ expression evaluator uses only the two-colon syntax. Debugger *output* always uses two colons.

-   In an MASM expression, you should add an at sign (**@**) before all except the most common registers. If you omit this at sign, the register name might be interpreted as a hexadecimal number or as a symbol. In a C++ expression, this prefix is required for all registers.

-   MASM expressions might contain references to source lines. These references are indicated by grave accents ( **\`** ). You cannot reference source line numbers in a C++ expression.

 

 





