---
title: Breakpoint Syntax
description: This topic covers breakpoint syntax
ms.assetid: 86228b87-9ca3-4d0c-be9e-63446ac6ce31
keywords: debugger, breakpoints on methods, breakpoints, syntax rules for commands, b (breakpoint identifier), literal MASM identifier, templated functions
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Breakpoint Syntax


## <span id="ddk_debugging_bios_code_dbg"></span><span id="DDK_DEBUGGING_BIOS_CODE_DBG"></span>


The following syntax elements can be used when creating a [breakpoint](using-breakpoints.md), either through the Debugger Command window or through the WinDbg graphical interface.

### <span id="addresses_in_breakpoints"></span><span id="ADDRESSES_IN_BREAKPOINTS"></span>Addresses in Breakpoints

Breakpoints support many kinds of address syntax, including virtual addresses, function offsets, and source line numbers. For example, you can use any of the following commands to set breakpoints:

```dbgcmd
0:000> bp 0040108c
0:000> bp main+5c
0:000> bp `source.c:31`
```

For more information about this syntax, see [Numerical Expression Syntax](numerical-expression-syntax.md), [Source Line Syntax](source-line-syntax.md), and the individual command topics.

### <span id="breakpoints_on_methods"></span><span id="BREAKPOINTS_ON_METHODS"></span>Breakpoints on Methods

If you want to put a breakpoint on the *MyMethod* method in the *MyClass* class, you can use two different syntaxes:

-   In MASM expression syntax, you can indicate a method by a double colon or by a double underscore.

    ```dbgcmd
    0:000> bp MyClass::MyMethod 
    0:000> bp MyClass__MyMethod 
    ```

-   In C++ expression syntax, you must indicate a method by a double colon.

    ```dbgcmd
    0:000> bp @@( MyClass::MyMethod ) 
    ```

If you want to use a more complex breakpoint command, you should use MASM expression syntax. For more information about expression syntax, see [Evaluating Expressions](evaluating-expressions.md).

### <span id="breakpoints_using_complicated_text"></span><span id="BREAKPOINTS_USING_COMPLICATED_TEXT"></span>Breakpoints Using Complicated Text

To set a breakpoint on complicated functions, including functions that contain spaces, as well as a member of a C++ public class, enclose the expression in parentheses. For example, use **bp (??MyPublic)** or **bp (operator new)**.

A more versatile technique is to use the @!"chars" syntax. This is a special escape in the MASM evaluator that enables you to provide arbitrary text for symbol resolution. You must start with the three symbols @!" and end with a quotation mark ("). Without this syntax, you cannot use spaces, angle brackets (&lt;, &gt;), or other special characters in symbol names in the MASM evaluator. This syntax is exclusively for names, and not parameters. Templates and overloads are the primary sources of symbols that require this quote notation. You can also set the **bu** command by using the @!"chars" syntax, as the following code example shows.

```dbgcmd
0:000> bu @!"ExecutableName!std::pair<unsigned int,std::basic_string<unsigned short,std::char_traits<unsigned short>,std::allocator<unsigned short> > >::operator="
```

In this example, *ExecutableName* is the name of an executable file.

This escape syntax is more useful for C++ (for example, overloaded operators) instead of C because there are no spaces (or special characters) in C function names. However, this syntax is also important for a lot of managed code because of the considerable use of overloads in the .NET Framework.

To set a breakpoint on arbitrary text in C++ syntax, use <strong>bu @@c++(</strong><em>text</em>**)** for C++-compatible symbols.

### <span id="breakpoints_in_scripts"></span><span id="BREAKPOINTS_IN_SCRIPTS"></span>Breakpoints in Scripts

Breakpoint IDs do not have to be referred to explicitly. Instead, you can use a numerical expression that resolves to an integer that corresponds to a breakpoint ID. To indicate that the expression should be interpreted as a breakpoint, use the following syntax.

```dbgcmd
b?[Expression]
```

In this syntax, the square brackets are required, and *Expression* stands for any numerical expression that resolves to an integer that corresponds to a breakpoint ID.

This syntax allows debugger scripts to programmatically select a breakpoint. In the following example, the breakpoint changes depending on the value of a user-defined pseudo-register.

```dbgcmd
b?[@$t0]
```

### <span id="breakpoint_pseudo_registers"></span><span id="BREAKPOINT_PSEUDO_REGISTERS"></span>Breakpoint Pseudo-Registers

If you want to refer to a breakpoint address in an expression, you can use a [pseudo-register](pseudo-register-syntax.md) with the **$bp***Number* syntax, where *Number* is the breakpoint ID. For more information about this syntax, see Pseudo-Register Syntax.

 

 





