---
title: C++ Numbers and Operators
description: C++ Numbers and Operators
ms.assetid: e5d3ac7f-fd79-48bb-b927-9ad72570dcbe
keywords: ["expressions, C++ expression syntax", "C++ expressions, numbers", "C++ expressions, operators", "numerical expressions, C++", "operators, C++", "precedence rules (C++)", "methods", "methods, syntax", "members of classes"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# C++ Numbers and Operators


## <span id="ddk_c_numbers_and_operators_dbg"></span><span id="DDK_C_NUMBERS_AND_OPERATORS_DBG"></span>


The C++ expression parser supports all forms of C++ expression syntax. The syntax includes all data types (including pointers, floating-point numbers, and arrays) and all C++ unary and binary operators.

### <span id="numbers_in_c___expressions"></span><span id="NUMBERS_IN_C___EXPRESSIONS"></span>Numbers in C++ Expressions

Numbers in C++ expressions are interpreted as decimal numbers, unless you specify them in another manner. To specify a hexadecimal integer, add **0x** before the number. To specify an octal integer, add **0** (zero) before the number.

The default debugger radix does not affect how you enter C++ expressions. You cannot directly enter a binary number (except by nesting a MASM expression within the C++ expression).

You can enter a hexadecimal 64-bit value in the <em>xxxxxxxx</em>**\`**<em>xxxxxxxx</em> format. (You can also omit the grave accent ( **\`** ).) Both formats produce the same value.

You can use the **L**, **U**, and **I64** suffixes with integer values. The actual size of the number that is created depends on the suffix and the number that you enter. For more information about this interpretation, see a C++ language reference.

The *output* of the C++ expression evaluator keeps the data type that the C++ expression rules specify. However, if you use this expression as an argument for a command, a cast is always made. For example, you do not have to cast integer values to pointers when they are used as addresses in command arguments. If the expression's value cannot be validly cast to an integer or a pointer, a syntax error occurs.

You can use the **0n** (decimal) prefix for some *output*, but you cannot use it for C++ expression input.

### <span id="characters_and_strings_in_c___expressions"></span><span id="CHARACTERS_AND_STRINGS_IN_C___EXPRESSIONS"></span>Characters and Strings in C++ Expressions

You can enter a character by surrounding it with single quotation marks ( ' ). The standard C++ escape characters are permitted.

You can enter string literals by surrounding them with double quotation marks ( " ). You can use **\\"** as an escape sequence within such a string. However, strings have no meaning to the [expression evaluator](evaluating-expressions.md).

### <span id="symbols_in_c___expressions"></span><span id="SYMBOLS_IN_C___EXPRESSIONS"></span>Symbols in C++ Expressions

In a C++ expression, each symbol is interpreted according to its type. Depending on what the symbol refers to, it might be interpreted as an integer, a data structure, a function pointer, or any other data type. If you use a symbol that does not correspond to a C++ data type (such as an unmodified module name) within a C++ expression, a syntax error occurs.

If the symbol might be ambiguous, you can add a module name and an exclamation point ( **!** ) or only an exclamation point before the symbol. For more information about symbol recognition, see [Symbol Syntax and Symbol Matching](symbol-syntax-and-symbol-matching.md).

You can use a grave accent ( **\`** ) or an apostrophe ( **'** ) in a symbol name only if you add a module name and exclamation point before the symbol name.

When you add the **&lt;** and **&gt;** delimiters after a template name, you can add spaces between these delimiters.

### <span id="operators_in_c___expressions"></span><span id="OPERATORS_IN_C___EXPRESSIONS"></span>Operators in C++ Expressions

You can always use parentheses to override precedence rules.

If you enclose part of a C++ expression in parentheses and add two at signs (**@@**) before the expression, the expression is interpreted according to MASM expression rules. You cannot add a space between the two at signs and the opening parenthesis. The final value of this expression is passed to the C++ expression evaluator as a ULONG64 value. You can also specify the expression evaluator by using **@@c++( ... )** or **@@masm( ... )**.

Data types are indicated as usual in the C++ language. The symbols that indicate arrays ( **\[ \]** ), pointer members ( **-&gt;** ), UDT members ( **.** ), and members of classes ( **::** ) are all recognized. All arithmetic operators are supported, including assignment and side-effect operators. However, you cannot use the **new**, **delete**, and **throw** operators, and you cannot actually call a function.

Pointer arithmetic is supported and offsets are scaled correctly. Note that you cannot add an offset to a function pointer. (If you have to add an offset to a function pointer, cast the offset to a character pointer first.)

As in C++, if you use operators with invalid data types, a syntax error occurs. The debugger's C++ expression parser uses slightly more relaxed rules than most C++ compilers, but all major rules are enforced. For example, you cannot shift a non-integer value.

You can use the following operators. The operators in each cell take precedence over those in lower cells. Operators in the same cell are of the same precedence and are parsed from left to right. As with C++, expression evaluation ends when its value is known. This ending enables you to effectively use expressions such as **?? myPtr && \*myPtr**.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Operator</th>
<th align="left">Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><em>Expression</em> <strong>//</strong> <em>Comment</em></p></td>
<td align="left"><p>Ignore all subsequent text</p></td>
</tr>
<tr class="even">
<td align="left"><p><em>Class</em> <strong>::</strong> <em>Member</em></p>
<p><em>Class</em> <strong>::~</strong><em>Member</em></p>
<p><strong>::</strong> <em>Name</em></p></td>
<td align="left"><p>Member of class</p>
<p>Member of class (destructor)</p>
<p>Global</p></td>
</tr>
<tr class="odd">
<td align="left"><p><em>Structure</em> <strong>.</strong> <em>Field</em></p>
<p><em>Pointer</em> <strong>-&gt;</strong> <em>Field</em></p>
<p><em>Name</em> <strong>[</strong><em>integer</em><strong>]</strong></p>
<p><em>LValue</em> <strong>++</strong></p>
<p><em>LValue</em> <strong>--</strong></p>
<p><strong>dynamic_cast &lt;</strong><em>type</em><strong>&gt;(</strong><em>Value</em><strong>)</strong></p>
<p><strong>static_cast &lt;</strong><em>type</em><strong>&gt;(</strong><em>Value</em><strong>)</strong></p>
<p><strong>reinterpret_cast &lt;</strong><em>type</em><strong>&gt;(</strong><em>Value</em><strong>)</strong></p>
<p><strong>const_cast &lt;</strong><em>type</em><strong>&gt;(</strong><em>Value</em><strong>)</strong></p></td>
<td align="left"><p>Field in a structure</p>
<p>Field in referenced structure</p>
<p>Array subscript</p>
<p>Increment (after evaluation)</p>
<p>Decrement (after evaluation)</p>
<p>Typecast (always performed)</p>
<p>Typecast (always performed)</p>
<p>Typecast (always performed)</p>
<p>Typecast (always performed)</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>(</strong><em>type</em><strong>)</strong> <em>Value</em></p>
<p><strong>sizeof</strong> <em>value</em></p>
<p><strong>sizeof(</strong> <em>type</em> <strong>)</strong></p>
<p><strong>++</strong> <em>LValue</em></p>
<p><strong>--</strong> <em>LValue</em></p>
<p><strong>~</strong> <em>Value</em></p>
<p><strong>!</strong> <em>Value</em></p>
<p><em>Value</em></p>
<p><strong>+</strong> <em>Value</em></p>
<p><strong>&amp;</strong> <em>LValue</em></p>
<p><strong><em></strong> <em>Value</em></p></td>
<td align="left"><p>Typecast (always performed)</p>
<p>Size of expression</p>
<p>Size of data type</p>
<p>Increment (before evaluation)</p>
<p>Decrement (before evaluation)</p>
<p>Bit complement</p>
<p>Not (Boolean)</p>
<p>Unary minus</p>
<p>Unary plus</p>
<p>Address of data type</p>
<p>Dereference</p></td>
</tr>
<tr class="odd">
<td align="left"><p><em>Structure</em> <strong>. <em></strong> <em>Pointer</em></p>
<p><em>Pointer</em> <strong>-&gt; *</strong> <em>Pointer</em></p></td>
<td align="left"><p>Pointer to member of structure</p>
<p>Pointer to member of referenced structure</p></td>
</tr>
<tr class="even">
<td align="left"><p><em>Value</em> <strong></em></strong> <em>Value</em></p>
<p><em>Value</em> <strong>/</strong> <em>Value</em></p>
<p><em>Value</em> <strong>%</strong> <em>Value</em></p></td>
<td align="left"><p>Multiplication</p>
<p>Division</p>
<p>Modulus</p></td>
</tr>
<tr class="odd">
<td align="left"><p><em>Value</em> <strong>+</strong> <em>Value</em></p>
<p><em>Value</em> <strong>-</strong> <em>Value</em></p></td>
<td align="left"><p>Addition</p>
<p>Subtraction</p></td>
</tr>
<tr class="even">
<td align="left"><p><em>Value</em> <strong>&lt;&lt;</strong> <em>Value</em></p>
<p><em>Value</em> <strong>&gt;&gt;</strong> <em>Value</em></p></td>
<td align="left"><p>Bitwise shift left</p>
<p>Bitwise shift right</p></td>
</tr>
<tr class="odd">
<td align="left"><p><em>Value</em> <strong>&lt;</strong> <em>Value</em></p>
<p><em>Value</em> <strong>&lt;=</strong> <em>Value</em></p>
<p><em>Value</em> <strong>&gt;</strong> <em>Value</em></p>
<p><em>Value</em> <strong>&gt;=</strong> <em>Value</em></p></td>
<td align="left"><p>Less than (comparison)</p>
<p>Less than or equal (comparison)</p>
<p>Greater than (comparison)</p>
<p>Greater than or equal (comparison)</p></td>
</tr>
<tr class="even">
<td align="left"><p><em>Value</em> <strong>==</strong> <em>Value</em></p>
<p><em>Value</em> <strong>!=</strong> <em>Value</em></p></td>
<td align="left"><p>Equal (comparison)</p>
<p>Not equal (comparison)</p></td>
</tr>
<tr class="odd">
<td align="left"><p><em>Value</em> <strong>&amp;</strong> <em>Value</em></p></td>
<td align="left"><p>Bitwise AND</p></td>
</tr>
<tr class="even">
<td align="left"><p><em>Value</em> <strong>^</strong> <em>Value</em></p></td>
<td align="left"><p>Bitwise XOR (exclusive OR)</p></td>
</tr>
<tr class="odd">
<td align="left"><p><em>Value</em> <strong>|</strong> <em>Value</em></p></td>
<td align="left"><p>Bitwise OR</p></td>
</tr>
<tr class="even">
<td align="left"><p><em>Value</em> <strong>&amp;&amp;</strong> <em>Value</em></p></td>
<td align="left"><p>Logical AND</p></td>
</tr>
<tr class="odd">
<td align="left"><p><em>Value</em> <strong>||</strong> <em>Value</em></p></td>
<td align="left"><p>Logical OR</p></td>
</tr>
<tr class="even">
<td align="left"><p><em>LValue</em> <strong>=</strong><em>Value</em></p>
<p><em>LValue</em> <strong></em>=</strong> <em>Value</em></p>
<p><em>LValue</em> <strong>/=</strong> <em>Value</em></p>
<p><em>LValue</em> <strong>%=</strong><em>Value</em></p>
<p><em>LValue</em> <strong>+=</strong><em>Value</em></p>
<p><em>LValue</em> <strong>-=</strong> <em>Value</em></p>
<p><em>LValue</em> <strong>&lt;&lt;=</strong> <em>Value</em></p>
<p><em>LValue</em> <strong>&gt;&gt;=</strong> <em>Value</em></p>
<p><em>LValue</em> <strong>&amp;=</strong> <em>Value</em></p>
<p><em>LValue</em> <strong>|=</strong> <em>Value</em></p>
<p><em>LValue</em> <strong>^=</strong> <em>Value</em></p></td>
<td align="left"><p>Assign</p>
<p>Multiply and assign</p>
<p>Divide and assign</p>
<p>Modulo and assign</p>
<p>Add and assign</p>
<p>Subtract and assign</p>
<p>Shift left and assign</p>
<p>Shift right and assign</p>
<p>AND and assign</p>
<p>OR and assign</p>
<p>XOR and assign</p></td>
</tr>
<tr class="odd">
<td align="left"><p><em>Value</em> <strong>?</strong> <em>Value</em> <strong>:</strong> <em>Value</em></p></td>
<td align="left"><p>Conditional evaluation</p></td>
</tr>
<tr class="even">
<td align="left"><p><em>Value</em> <strong>,</strong> <em>Value</em></p></td>
<td align="left"><p>Evaluate all values, and then discard all except the rightmost value</p></td>
</tr>
</tbody>
</table>

 

### <span id="registers_and_pseudo_registers_in_c___expressions"></span><span id="REGISTERS_AND_PSEUDO_REGISTERS_IN_C___EXPRESSIONS"></span>Registers and Pseudo-Registers in C++ Expressions

You can use registers and pseudo-registers within C++ expressions. You must add an at sign ( **@** ) before the register or pseudo-register.

The expression evaluator automatically performs the proper cast. Actual registers and integer-value pseudo-registers are cast to ULONG64. All addresses are cast to PUCHAR, **$thread** is cast to ETHREAD\*, **$proc** is cast to EPROCESS\*, **$teb** is cast to TEB\*, and **$peb** is cast to PEB\*.

You cannot change a register or pseudo-register by an assignment or side-effect operator. You must use the [**r (Registers)**](r--registers-.md) command to change these values.

For more information about registers and pseudo-registers, see [Register Syntax](register-syntax.md) and [Pseudo-Register Syntax](pseudo-register-syntax.md).

### <span id="macros_in_c___expressions"></span><span id="MACROS_IN_C___EXPRESSIONS"></span>Macros in C++ Expressions

You can use macros within C++ expressions. You must add a number sign (\#) before the macros.

You can use the following macros. These macros have the same definitions as the Microsoft Windows macros with the same name. (The Windows macros are defined in Winnt.h.)

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Macro</th>
<th align="left">Return Value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>#CONTAINING_RECORD(<em>Address</em>, <em>Type</em>, <em>Field</em>)</p></td>
<td align="left"><p>Returns the base address of an instance of a structure, given the type of the structure and the address of a field within the structure.</p></td>
</tr>
<tr class="even">
<td align="left"><p>#FIELD_OFFSET(<em>Type</em>, <em>Field</em>)</p></td>
<td align="left"><p>Returns the byte offset of a named field in a known structure type.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>#RTL_CONTAINS_FIELD (<em>Struct</em>, <em>Size</em>, <em>Field</em>)</p></td>
<td align="left"><p>Indicates whether the given byte size includes the desired field.</p></td>
</tr>
<tr class="even">
<td align="left"><p>#RTL_FIELD_SIZE(<em>Type</em>, <em>Field</em>)</p></td>
<td align="left"><p>Returns the size of a field in a structure of known type, without requiring the type of the field.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>#RTL_NUMBER_OF(<em>Array</em>)</p></td>
<td align="left"><p>Returns the number of elements in a statically sized array.</p></td>
</tr>
<tr class="even">
<td align="left"><p>#RTL_SIZEOF_THROUGH_FIELD(<em>Type</em>, <em>Field</em>)</p></td>
<td align="left"><p>Returns the size of a structure of known type, up through and including a specified field.</p></td>
</tr>
</tbody>
</table>

 

 

 





