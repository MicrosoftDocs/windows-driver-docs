---
title: Mixed Expression Examples
description: Mixed Expression Examples
keywords: ["expressions, examples", "MASM expressions, examples", "C++ expressions, examples"]
ms.date: 03/31/2021
ms.localizationpriority: medium
---

# Mixed Expression Examples

This topics contains examples of MASM and C++ expressions that are used in various commands.

All other sections of this Help documentation use MASM expression syntax in the examples (unless otherwise noted). C++ expression syntax is very useful for manipulating structures and variables, but it does not parse the parameters of debugger commands very well.

If you are using debugger commands for general purposes or using debugger extensions, you should set MASM expression syntax as the default syntax, for example by using [.expr (Choose Expression Evaluator)](-expr--choose-expression-evaluator-.md). If you must have a specific parameter to use C++ expression syntax, use the **@@( )** syntax.

If **myInt** is a ULONG32 value and if you are using the MASM expression evaluator, the following two examples show the value of **MyInt**.

```dbgcmd
0:000> ?? myInt 
0:000> dd myInt L1 
```

However, the following example shows the *address* of **myInt**.

```dbgcmd
0:000> ? myInt 
```

### Conditional Breakpoints

You can use comparison operators to create [conditional breakpoints](setting-a-conditional-breakpoint.md). The following code example uses MASM expression syntax. Because the current default radix is 16, the example uses the **0n** prefix so that the number 20 is understood as a decimal number.

```dbgcmd
0:000> bp MyFunction+0x43 "j ( poi(MyVar)>0n20 ) ''; 'gc' " 
```

In the previous example, **MyVar** is an integer in the C source. Because the MASM parser treats all symbols as addresses, the example must have the **poi** operator to dereference **MyVar**.

### Conditional Expressions

The following example prints the value of **ecx** if **eax** is greater than **ebx**, 7 if **eax** is less than **ebx**, and 3 if **eax** equals **ebx**. This example uses the MASM expression evaluator, so the equal sign (=) is a comparison operator, not an assignment operator.

```dbgcmd
0:000> ? ecx*(eax>ebx) + 7*(eax<ebx) + 3*(eax=ebx) 
```

In C++ syntax, the **@** sign indicates a register, a double equal sign (==) is the comparison operator, and code must explicitly cast from BOOL to **int**. Therefore, in C++ syntax, the previous command becomes the following.

```dbgcmd
0:000> ?? @ecx*(int)(@eax>@ebx) + 7*(int)(@eax<@ebx) + 3*(int)(@eax==@ebx) 
```
## MASM and C++ Mixed Expression Examples

You cannot use source-line expressions in a C++ expression. The following example uses the **@@( )** alternative evaluator syntax to nest an MASM expression within a C++ expression. This example sets **MyPtr** equal to the address of line 43 of the Myfile.c file.

```dbgcmd
0:000> ?? MyPtr = @@( `myfile.c:43` )
```

The following examples set the default expression evaluator to MASM and then evaluate *Expression2* as a C++ expression, and evaluate *Expression1* and *Expression3* as MASM expressions.

```dbgcmd
0:000> .expr /s masm 
0:000> bp Expression1 + @@( Expression2 ) + Expression3 
```

If **myInt** is a ULONG64 value and if you know that this value is followed in memory by another ULONG64, you can set an access breakpoint at that location by using one of the following examples. (Note the use of pointer arithmetic.)

```dbgcmd
0:000> ba r8 @@( &myInt + 1 ) 
0:000> ba r8 myInt + 8 
```

## See also

[MASM Numbers and Operators](masm-numbers-and-operators.md)

[C++ Numbers and Operators](c---numbers-and-operators.md)

[MASM Expressions vs. C++ Expressions](masm-expressions-vs--c---expressions.md)

[Sign Extension](sign-extension.md) 
