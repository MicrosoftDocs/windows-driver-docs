---
title: Sign Extension
description: Sign Extension
ms.assetid: 58e84d09-ab70-4cb2-b12f-4addb34f69d6
keywords: ["sign extension of numbers", "sign extension of registers", "MASM expressions, sign extension", "registers, sign extension"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Sign Extension


## <span id="ddk_sign_extension_dbg"></span><span id="DDK_SIGN_EXTENSION_DBG"></span>


When a 32-bit signed integer is negative, its highest bit is equal to one. When this 32-bit signed integer is cast to a 64-bit number, the high bits can be set to zero (preserving the unsigned integer and hexadecimal value of the number) or the high bits can be set to one (preserving the signed value of the number). The latter situation is called *sign extension*.

The debugger follows different rules for sign extension in MASM expressions, in C++ expressions, and when displaying numbers.

### <span id="sign_extension_in_masm_expressions"></span><span id="SIGN_EXTENSION_IN_MASM_EXPRESSIONS"></span>Sign Extension in MASM Expressions

Under certain conditions, numbers are automatically *sign extended* by the MASM expression evaluator. Sign extension can affect only numbers from 0x80000000 through 0xFFFFFFFF. That is, sign extension affects only numbers that can be written in 32 bits with the high bit equal to 1.

The number 0x12345678 always remains 0x00000000\`12345678 when the debugger treats it as a 64-bit number. On the other hand, when 0x890ABCDE is treated as a 64-bit value, it might remain 0x00000000\`890ABCDE or the MASM expression evaluator might sign extend it to 0xFFFFFFFF\`890ABCDE.

A number from 0x80000000 through 0xFFFFFFFF is sign extended based on the following criteria:

-   Numeric constants are never sign extended in user mode. In kernel mode, a numeric constant is sign extended unless it contains a grave accent ( **\`** ) before the low bytes. For example, in kernel mode, the hexadecimal numbers **EEAA1122** and **00000000EEAA1122** are sign extended, but **00000000\`EEAA1122** and **0\`EEAA1122** are not.

-   A 32-bit register is sign extended in both modes.

-   Pseudo-registers are always stored as 64-bit values. They are not sign extended when they are evaluated. When a pseudo-register is *assigned* a value, the expression that is used is evaluated according to the standard C++ criteria.

-   Individual numbers and registers in an expression can be sign extended, but no other calculations during expression evaluation are sign extended. As a result, you can mask the high bits of a number or register by using the following syntax.
    ```console
    ( 0x0`FFFFFFFF & expression )
    ```

### <span id="sign_extension_in_c___expressions"></span><span id="SIGN_EXTENSION_IN_C___EXPRESSIONS"></span>Sign Extension in C++ Expressions

When the debugger evaluates a C++ expression, the following rules apply:

-   Registers and pseudo-registers are never sign extended.

-   All other values are treated exactly like C++ would treat values of their type.

### <span id="displaying_sign_extended_and_64_bit_numbers"></span><span id="DISPLAYING_SIGN_EXTENDED_AND_64_BIT_NUMBERS"></span>Displaying Sign-Extended and 64-Bit Numbers

Other than 32-bit and 16-bit registers, all numbers are stored internally within the debugger as 64-bit values. However, when a number satisfies certain criteria, the debugger displays it as a 32-bit number in command output.

The debugger uses the following criteria to determine how to display numbers:

-   If the high 32 bits of a number are all zeros (that is, if the number is from 0x00000000\`00000000 through 0x00000000\`FFFFFFFF), the debugger displays the number as a 32-bit number.

-   If the high 32 bits of a number are all ones and if the highest bit of the low 32 bits is also a one (that is, if the number is from 0xFFFFFFFF\`80000000 through 0xFFFFFFFF\`FFFFFFFF), the debugger assumes the number is a sign-extended 32-bit number and displays it as a 32-bit number.

-   If the previous two condition do not apply (that is, if the number is from 0x00000001\`00000000 through 0xFFFFFFFF\`7FFFFFFF) the debugger displays the number as a 64-bit number.

Because of these display rules, when a number is displayed as a 32-bit number from 0x80000000 through 0xFFFFFFFF, you cannot confirm whether the high 32 bits are all ones or all zeros. To distinguish between these two cases, you must perform an additional computation on the number (such as masking one or more of the high bits and displaying the result).

 

 





