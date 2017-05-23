---
title: Expression Examples
description: Expression Examples
ms.assetid: a4915678-a83f-48f1-8b29-50cf530f9246
keywords: ["expressions, examples", "MASM expressions, examples", "C++ expressions, examples"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Expression Examples


## <span id="ddk_expression_examples_dbg"></span><span id="DDK_EXPRESSION_EXAMPLES_DBG"></span>


This topics contains examples of MASM and C++ expressions that are used in various commands.

All other sections of this Help documentation use MASM expression syntax in the examples (unless otherwise noted). C++ expression syntax is very useful for manipulating structures and variables, but it does not parse the parameters of debugger commands very well.

If you are using debugger commands for general purposes or using debugger extensions, you should set MASM expression syntax as the default syntax. If you must have a specific parameter to use C++ expression syntax, use the **@@( )** syntax.

### <span id="conditional_breakpoints"></span><span id="CONDITIONAL_BREAKPOINTS"></span>Conditional Breakpoints

You can use comparison operators to create [conditional breakpoints](setting-a-conditional-breakpoint.md). The following code example uses MASM expression syntax. Because the current default radix is 16, the example uses the **0n** prefix so that the number 20 is understood as a decimal number.

```
0:000> bp MyFunction+0x43 "j ( poi(MyVar)>0n20 ) &#39;&#39;; &#39;gc&#39; " 
```

In the previous example, **MyVar** is an integer in the C source. Because the MASM parser treats all symbols as addresses, the example must have the **poi** operator to dereference **MyVar**.

### <span id="conditional_expressions"></span><span id="CONDITIONAL_EXPRESSIONS"></span>Conditional Expressions

The following example prints the value of **ecx** if **eax** is greater than **ebx**, 7 if **eax** is less than **ebx**, and 3 if **eax** equals **ebx**. This example uses the MASM expression evaluator, so the equal sign (=) is a comparison operator, not an assignment operator.

```
0:000> ? ecx*(eax>ebx) + 7*(eax<ebx) + 3*(eax=ebx) 
```

In C++ syntax, the **@** sign indicates a register, a double equal sign (==) is the comparison operator, and code must explicitly cast from BOOL to **int**. Therefore, in C++ syntax, the previous command becomes the following.

```
0:000> ?? @ecx*(int)(@eax>@ebx) + 7*(int)(@eax<@ebx) + 3*(int)(@eax==@ebx) 
```

### <span id="c___expression_examples"></span><span id="C___EXPRESSION_EXAMPLES"></span>C++ Expression Examples

If **myInt** is a ULONG32 value and if you are using the MASM expression evaluator, the following two examples show the value of **MyInt**.

```
0:000> ?? myInt 
0:000> dd myInt L1 
```

However, the following example shows the *address* of **myInt**.

```
0:000> ? myInt 
```

### <span id="mixed_expression_examples"></span><span id="MIXED_EXPRESSION_EXAMPLES"></span>Mixed Expression Examples

You cannot use source-line expressions in a C++ expression. The following example uses the **@@( )** syntax to nest an MASM expression within a C++ expression. This example sets **MyPtr** equal to the address of line 43 of the Myfile.c file.

```
0:000> ?? MyPtr = @@( `myfile.c:43` )
```

The following examples set the default expression evaluator to MASM and then evaluate *Expression2* as a C++ expression, and evaluate *Expression1* and *Expression3* as MASM expressions.

```
0:000> .expr /s masm 
0:000> bp Expression1 + @@( Expression2 ) + Expression3 
```

If **myInt** is a ULONG64 value and if you know that this value is followed in memory by another ULONG64, you can set an access breakpoint at that location by using one of the following examples. (Note the use of pointer arithmetic.)

```
0:000> ba r8 @@( &myInt + 1 ) 
0:000> ba r8 myInt + 8 
```

### <span id="structures"></span><span id="STRUCTURES"></span>Structures

The C++ expression evaluator casts pseudo-registers to their appropriate types. For example, **$teb** is cast as a TEB\*. The following example displays the process ID.

```
kd> ??  @$teb->ClientId.UniqueProcess 
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Expression%20Examples%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




