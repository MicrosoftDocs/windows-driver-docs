---
title: C++ numbers and operators
description: Learn how to use C++ numbers, operators, and other expression syntax with the Windows debugging tools.
keywords: ["expressions, C++ expression syntax", "C++ expressions, numbers", "C++ expressions, operators", "numerical expressions, C++", "operators, C++", "precedence rules (C++)", "methods", "methods, syntax", "members of classes"]
ms.date: 12/16/2022
ms.custom: contperf-fy21q3
---

# C++ numbers and operators

This article describes the use of C++ expression syntax with the Windows debugging tools.

The debugger accepts two different kinds of numeric expressions: C++ expressions and Microsoft Macro Assembler (MASM) expressions. Each of these expressions follows its own syntax rules for input and output.

For more information about when each syntax type is used, see [Evaluating expressions](evaluating-expressions.md) and the [? evaluate expression](---evaluate-expression-.md) command.

The C++ expression parser supports all forms of C++ expression syntax. The syntax includes all data types, including pointers, floating-point numbers, and arrays, and all C++ unary and binary operators.

The *Watch* and the *Locals* windows in the debugger always use the C++ expression evaluator.

In the following example, the [?? evaluate C++ expression](----evaluate-c---expression-.md) command displays the value of the instruction pointer register.

```dbgcmd
0:000> ?? @eip
unsigned int 0x771e1a02
```

We can use the C++ `sizeof` function to determine the size of structures.

```dbgcmd
0:000> ?? (sizeof(_TEB))
unsigned int 0x1000
```

## Set the expression evaluator to C++

Use the [.expr choose expression](-expr--choose-expression-evaluator-.md) evaluator to see the default expression evaluator and change it to C++.

```dbgcmd
0:000> .expr
Current expression evaluator: MASM - Microsoft Assembler expressions
0:000> .expr /s c++
Current expression evaluator: C++ - C++ source expressions
```

After the default expression evaluator has been changed, the [? evaluate expression](---evaluate-expression-.md) command can be used to display C++ expressions. The following example displays the value of the instruction pointer register.

```dbgcmd
0:000> ? @eip
Evaluate expression: 1998461442 = 771e1a02
```

To learn more about the `@eip` register reference, see [Register syntax](register-syntax.md).

In this example, the hex value of 0xD is added to the eip register.

```dbgcmd
0:000> ? @eip + 0xD
Evaluate expression: 1998461455 = 771e1a0f
```

## Registers and pseudo-registers in C++ expressions

You can use registers and pseudo-registers within C++ expressions. The @ sign must be added before the register or pseudo-register.

The expression evaluator automatically performs the proper cast. Actual registers and integer-value pseudo-registers are cast to `ULONG64`. All addresses are cast to `PUCHAR`, `$thread` is cast to `ETHREAD*`, `$proc` is cast to `EPROCESS*`, `$teb` is cast to `TEB*`, and `$peb` is cast to `PEB*`.

This example displays the TEB.

```dbgcmd
0:000>  ?? @$teb
struct _TEB * 0x004ec000
   +0x000 NtTib            : _NT_TIB
   +0x01c EnvironmentPointer : (null) 
   +0x020 ClientId         : _CLIENT_ID
   +0x028 ActiveRpcHandle  : (null) 
   +0x02c ThreadLocalStoragePointer : 0x004ec02c Void
   +0x030 ProcessEnvironmentBlock : 0x004e9000 _PEB
   +0x034 LastErrorValue   : 0xbb
   +0x038 CountOfOwnedCriticalSections : 0
```

You can't change a register or pseudo-register by an assignment or side-effect operator. You must use the [r registers](r--registers-.md) command to change these values.

The following example sets the pseudo register to a value of 5 and then displays it.

```dbgcmd
0:000> r $t0 = 5

0:000> ?? @$t0
unsigned int64 5
```

For more information about registers and pseudo-registers, see [Register syntax](register-syntax.md) and [Pseudo-register syntax](pseudo-register-syntax.md).

## Numbers in C++ expressions

Numbers in C++ expressions are interpreted as decimal numbers, unless you specify them in another manner. To specify a hexadecimal integer, add 0x before the number. To specify an octal integer, add 0 (zero) before the number.

The default debugger radix doesn't affect how you enter C++ expressions. You can't directly enter a binary number, except by nesting a MASM expression within the C++ expression.

You can enter a hexadecimal 64-bit value in the xxxxxxxx\`xxxxxxxx format. You can also omit the grave accent (\`). Both formats produce the same value.

You can use the `L`, `U`, and `I64` suffixes with integer values. The actual size of the number that's created depends on the suffix and the number that you enter. For more information about this interpretation, see a C++ language reference.

The *output* of the C++ expression evaluator keeps the data type that the C++ expression rules specify. However, if you use this expression as an argument for a command, a cast is always made. For example, you don't have to cast integer values to pointers when they're used as addresses in command arguments. If the expression's value can't be validly cast to an integer or a pointer, a syntax error occurs.

You can use the `0n` (decimal) prefix for some *output*, but you can't use it for C++ expression input.

## Characters and strings in C++ expressions

You can enter a character by surrounding it with single quotation marks ('). The standard C++ escape characters are permitted.

You can enter string literals by surrounding them with double quotation marks ("). You can use **\\"** as an escape sequence within such a string. However, strings have no meaning to the [expression evaluator](evaluating-expressions.md).

## Symbols in C++ expressions

In a C++ expression, each symbol is interpreted according to its type. Depending on what the symbol refers to, it might be interpreted as an integer, a data structure, a function pointer, or any other data type. A syntax error occurs if you use a symbol that doesn't correspond to a C++ data type, such as an unmodified module name, within a C++ expression.

You can use a grave accent (\`) or an apostrophe (') in a symbol name only if you add a module name and exclamation point before the symbol name. When you add the &lt; and &gt; delimiters after a template name, you can add spaces between these delimiters.

If the symbol might be ambiguous, you can add a module name and an exclamation point (!) or only an exclamation point before the symbol. To specify that a symbol is meant to be local, omit the module name, and include a dollar sign and an exclamation point ($!) before the symbol name. For more information about symbol recognition, see [Symbol syntax and symbol matching](symbol-syntax-and-symbol-matching.md).

## Structures in C++ expressions

The C++ expression evaluator casts pseudo-registers to their appropriate types. For example, `$teb` is cast as a `TEB*`.

```dbgcmd
0:000> ??  @$teb
struct _TEB * 0x004ec000
   +0x000 NtTib            : _NT_TIB
   +0x01c EnvironmentPointer : (null) 
   +0x020 ClientId         : _CLIENT_ID
   +0x028 ActiveRpcHandle  : (null) 
   +0x02c ThreadLocalStoragePointer : 0x004ec02c Void
   +0x030 ProcessEnvironmentBlock : 0x004e9000 _PEB
   +0x034 LastErrorValue   : 0xbb
   +0x038 CountOfOwnedCriticalSections : 0
```

The following example displays the process ID in the TEB structure showing the use of a pointer to a member of referenced structure.

```dbgcmd
0:000> ??  @$teb->ClientId.UniqueProcess
void * 0x0000059c
```

## Operators in C++ expressions

You can use parentheses to override precedence rules.

If you enclose part of a C++ expression in parentheses and add two *at* signs (@@) before the expression, the expression is interpreted according to MASM expression rules. You can't add a space between the two *at* signs and the opening parenthesis. The final value of this expression is passed to the C++ expression evaluator as a ULONG64 value. You can also specify the expression evaluator by using `@@c++( ... )` or `@@masm( ... )`.

Data types are indicated as usual in the C++ language. The symbols that indicate arrays (\[ \]), pointer members (-&gt;), UDT members (**.**), and members of classes (**::**) are all recognized. All arithmetic operators are supported, including assignment and side-effect operators. However, you can't use the `new`, `delete`, and `throw` operators, and you can't actually call a function.

Pointer arithmetic is supported and offsets are scaled correctly. Note that you can't add an offset to a function pointer. If you must add an offset to a function pointer, cast the offset to a character pointer first.

As in C++, if you use operators with invalid data types, a syntax error occurs. The debugger's C++ expression parser uses slightly more relaxed rules than most C++ compilers, but all major rules are enforced. For example, you can't shift a non-integer value.

You can use the following operators. The operators in each cell take precedence over operators in lower cells. Operators in the same cell are of the same precedence and are parsed from left to right.

As with C++, expression evaluation ends when its value is known. This ending enables you to effectively use expressions such as `?? myPtr && *myPtr`.

### Reference and type casting

| Operator              | Meaning               |
|-----------------------|-----------------------|
| *Expression* // *Comment* | Ignore all subsequent text |
| *Class* :: *Member* | Member of class |
| *Class* ::~*Member* | Member of class (destructor) |
| :: *Name* | Global |
| *Structure* . *Field* | Field in a structure |
| *Pointer* -> *Field* | Field in referenced structure |
| *Name* [<em>integer</em>] | Array subscript |
| *LValue* ++ | Increment (after evaluation) |
| *LValue* -- | Decrement (after evaluation) |
| **dynamic_cast** &lt;*type*&gt;(*Value*) | Typecast (always performed) |
| **static_cast** &lt;*type*&gt;(*Value*) | Typecast (always performed) |
| **reinterpret_cast** &lt;*type*&gt;(*Value*) | Typecast (always performed) |
| **const_cast** &lt;*type*&gt;(*Value*) | Typecast (always performed) |

### Value operations

| Operator              | Meaning               |
|-----------------------|-----------------------|
| (*type*) *Value* | Typecast (always performed) |
| **sizeof** *value* | Size of expression |
| **sizeof**( *type* ) | Size of data type |
| ++ *LValue* | Increment (before evaluation) |
| -- *LValue* | Decrement (before evaluation) |
| ~ *Value* | Bit complement |
| ! *Value* | Not (Boolean) |
| *Value* | Unary minus |
| + *Value* | Unary plus |
| & *LValue* | Address of data type |
| *Value* | Dereference |
| *Structure* . *Pointer* | Pointer to member of structure |
| *Pointer* -> * *Pointer* | Pointer to member of referenced structure |

### Arithmetic

| Operator              | Meaning               |
|-----------------------|-----------------------|
| *Value Value* | Multiplication |
| *Value* / *Value* | Division
| *Value* % *Value* | Modulus |
| *Value* + *Value* | Addition
| *Value* - *Value* | Subtraction |
| *Value* &lt;&lt; *Value* | Bitwise shift left |
| *Value* &gt;&gt; *Value* | Bitwise shift right |
| *Value* &lt; *Value* | Less than (comparison) |
| *Value* &lt;= *Value* | Less than or equal (comparison) |
| *Value* &gt; *Value* | Greater than (comparison) |
| *Value* &gt;= *Value* | Greater than or equal (comparison) |
| *Value* == *Value* | Equal (comparison) |
| *Value* != *Value* | Not equal (comparison) |
| *Value* & *Value* | Bitwise AND |
| *Value* ^ *Value* | Bitwise XOR (exclusive OR) |
| *Value* \| *Value* | Bitwise OR |
| *Value* && *Value* | Logical AND |
| *Value* \|\| *Value*  | Logical OR |

The following examples assume that the pseudo registers are set as shown.

```dbgcmd
0:000> r $t0 = 0
0:000> r $t1 = 1
0:000> r $t2 = 2
```

```dbgcmd
0:000> ?? @$t1 + @$t2
unsigned int64 3
0:000> ?? @$t2/@$t1
unsigned int64 2
0:000> ?? @$t2|@$t1
unsigned int64 3
```


### Assignment

| Operator            | Meaning             |
|---------------------|---------------------|
| *LValue* = *Value* | Assign |
| *LValue* *= *Value* | *Multiply* and assign |
| *LValue* /= *Value* | Divide and assign |
| *LValue* %= *Value* | Modulo and assign |
| *LValue* += *Value* | Add and assign |
| *LValue* -= *Value* | Subtract and assign |
| *LValue* <<= *Value* | Shift left and assign |
| *LValue* >>= *Value* | Shift right and assign |
| *LValue* &= *Value* | AND and assign |
| *LValue* \|= *Value* | OR and assign |
| *LValue* ^= *Value* | XOR and assign |

### Evaluation

| Operator              | Meaning               |
|-----------------------|-----------------------|
| *Value* ? *Value* : *Value* | Conditional evaluation     |
| *Value* , *Value*         | Evaluate all values, and then discard all except the rightmost value |

### Macros in C++ expressions

You can use macros within C++ expressions. You must add a number sign (\#) before the macros.

You can use the following macros. These macros have the same definitions as the Microsoft Windows macros with the same name. The Windows macros are defined in `Winnt.h`.

| Macro    | Return value    |
|----------|-----------------|
| #CONTAINING_RECORD(*Address, Type, Field*)  | Returns the base address of an instance of a structure, given the type of the structure and the address of a field within the structure. |
| #FIELD_OFFSET(*Type, Field*)  | Returns the byte offset of a named field in a known structure type. |
| #RTL_CONTAINS_FIELD(*Struct, Size, Field*) | Indicates whether the given byte size includes the desired field. |
| #RTL_FIELD_SIZE(*Type, Field*)  | Returns the size of a field in a structure of known type, without requiring the type of the field. |
| #RTL_NUMBER_OF(*Array*)   | Returns the number of elements in a statically sized array. |
| #RTL_SIZEOF_THROUGH_FIELD(*Type, Field*)    | Returns the size of a structure of known type, up through and including a specified field. |

This example shows the use of the `#FIELD_OFFSET` macro to calculate the byte offset to a field in a structure.

```dbgcmd
0:000> ?? #FIELD_OFFSET(_PEB, BeingDebugged)
long 0n2
```

## See also

[MASM expressions vs. C++ expressions](masm-expressions-vs--c---expressions.md)

[?? evaluate C++ expression](----evaluate-c---expression-.md)

[? evaluate expression](---evaluate-expression-.md)

[.expr choose expression evaluator](-expr--choose-expression-evaluator-.md)

[Sign extension](sign-extension.md)

[Mixed expression examples](expression-examples.md)
