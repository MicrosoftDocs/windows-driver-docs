---
title: Breakpoint syntax
description: This topic covers breakpoint syntax
keywords: debugger, breakpoints on methods, breakpoints, syntax rules for commands, b (breakpoint identifier), literal MASM identifier, templated functions
ms.date: 06/26/2023
---

# Breakpoint Syntax

The following syntax elements can be used when creating a [breakpoint](using-breakpoints.md), either through the Debugger Command window or through the WinDbg graphical interface.

## Addresses in breakpoints

Breakpoints support many kinds of address syntax, including virtual addresses, function offsets, and source line numbers. For example, you can use any of the following commands to set breakpoints:

```dbgcmd
0:000> bp 0040108c
0:000> bp main+5c
0:000> bp `source.c:31`
```

For more information about this syntax, see [Numerical Expression Syntax](../debuggercmds/numerical-expression-syntax.md), [Source Line Syntax](../debuggercmds/source-line-syntax.md), and the individual command topics.

## Breakpoints on methods

If you want to put a breakpoint on the *MyMethod* method in the *MyClass* class, you can use two different syntaxes:

- In MASM expression syntax, you can indicate a method by a double colon or by a double underscore.

    ```dbgcmd
    0:000> bp MyClass::MyMethod 
    0:000> bp MyClass__MyMethod 
    ```

- In C++ expression syntax, you must indicate a method by a double colon.

    ```dbgcmd
    0:000> bp @@( MyClass::MyMethod ) 
    ```

If you want to use a more complex breakpoint command, you should use MASM expression syntax. For more information about expression syntax, see [Evaluating Expressions](../debuggercmds/evaluating-expressions.md).

## Breakpoints using complicated MASM expressions

To set a breakpoint on complicated functions, including functions that contain spaces, as well as a member of a C++ public class, enclose the expression in parentheses. For example, use **bp (??MyPublic)** or **bp (operator new)**.

A more versatile technique is to use the @!"chars" syntax. This is a special escape in the MASM evaluator that enables you to provide arbitrary text for symbol resolution. You must start with the three symbols @!" and end with a quotation mark ("). Without this syntax, you cannot use spaces, angle brackets (&lt;, &gt;), or other special characters in symbol names in the MASM evaluator. This syntax is exclusively for names, and not parameters. Templates and overloads are the primary sources of symbols that require this quote notation. You can also set the **bu** command by using the @!"chars" syntax, as the following code example shows.

```dbgcmd
0:000> bu @!"ExecutableName!std::pair<unsigned int,std::basic_string<unsigned short,std::char_traits<unsigned short>,std::allocator<unsigned short> > >::operator="
```

In this example, *ExecutableName* is the name of an executable file.

This escape syntax is more useful for C++ (for example, overloaded operators) instead of C because there are no spaces (or special characters) in C function names. However, this syntax is also important for a lot of managed code because of the considerable use of overloads in the .NET Framework.

To set a breakpoint on arbitrary text in C++ syntax, use <strong>bu @@c++(</strong><em>text</em>**)** for C++-compatible symbols.

## Breakpoints in scripts

Breakpoint IDs do not have to be referred to explicitly. Instead, you can use a numerical expression that resolves to an integer that corresponds to a breakpoint ID. To indicate that the expression should be interpreted as a breakpoint, use the following syntax.

```dbgcmd
b?[Expression]
```

In this syntax, the square brackets are required, and *Expression* stands for any numerical expression that resolves to an integer that corresponds to a breakpoint ID.

This syntax allows debugger scripts to programmatically select a breakpoint. In the following example, the breakpoint changes depending on the value of a user-defined pseudo-register.

```dbgcmd
b?[@$t0]
```

## Breakpoint pseudo-registers

If you want to refer to a breakpoint address in an expression, you can use a [pseudo-register](../debuggercmds/pseudo-register-syntax.md) with the **$bp**_Number_ syntax, where *Number* is the breakpoint ID. For more information about this syntax, see Pseudo-Register Syntax.

## Ambiguous breakpoint resolution

In version 10.0.25310.1001 and later of the debugger engine, ambiguous breakpoint resolution is now supported. Ambiguous breakpoints allow for the debugger to set breakpoints in certain scenarios where a breakpoint expression resolves to multiple locations. For more information, see [Ambiguous breakpoint resolution](ambiguous-breakpoint-resolution.md).

## See also

[Using Breakpoints](using-breakpoints.md)

[Breakpoint Syntax](breakpoint-syntax.md)

[bp, bu, bm (Set Breakpoint)](../debuggercmds/bp--bu--bm--set-breakpoint-.md)

[Unresolved Breakpoints (bu Breakpoints)](unresolved-breakpoints---bu-breakpoints-.md)
