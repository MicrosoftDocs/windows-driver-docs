---
title: MASM Expressions vs. C++ Expressions
description: MASM Expressions vs.
ms.assetid: 3ec06b61-9f17-49b1-b7c5-66a349b5d275
keywords: ["expressions, MASM and C++", "MASM expressions, MASM vs. C++", "C++ expressions, C++ vs. MASM"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20MASM%20Expressions%20vs.%20C++%20Expressions%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




