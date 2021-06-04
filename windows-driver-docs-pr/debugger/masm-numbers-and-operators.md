---
title: MASM Numbers and Operators
description: MASM Numbers and Operators
keywords: ["expressions, MASM expression syntax", "numerical expressions (MASM)", "MASM expressions, numbers", "MASM expressions, operators", "operators (MASM)", "(MASM prefix)", "binary operators", "shift operators", "unary operators"]
ms.date: 04/30/2021
ms.localizationpriority: medium
ms.custom: contperf-fy21q4
---

# MASM Numbers and Operators

This topic describes the use of Microsoft Macro Assembler (MASM) expression syntax with the Windows Debugging tools.

The debugger accepts two different kinds of numeric expressions: C++ expressions and MASM expressions. Each of these expressions follows its own syntax rules for input and output.

For more information about when each syntax type is used, see [Evaluating Expressions](evaluating-expressions.md) and [? (Evaluate Expression)](---evaluate-expression-.md).

In this example the ? command displays the value of the instruction pointer register using the MASM expression evaluator.

```dbgcmd
0:000> ? @rip
Evaluate expression: 140709230544752 = 00007ff9`6bb40770
```

## Set the Expression Evaluator to MASM

Use the [.expr (Choose Expression Evaluator)](-expr--choose-expression-evaluator-.md) to see what the default expression evaluator is and change it to MASM.

```dbgcmd
0:000> .expr /s masm
Current expression evaluator: MASM - Microsoft Assembler expressions
```

Now that the default expression evaluator has been changed, the [? (Evaluate Expression)](---evaluate-expression-.md) command can be used to display MASM expressions. This example adds the hex value of 8 to the rip register.

```dbgcmd
0:000> ? @rip + 8
Evaluate expression: 140709230544760 = 00007ff9`6bb40778
```

The register reference of @rip is described in more detail in [Register Syntax](register-syntax.md).

## Numbers in Debugger MASM Expressions

You can put numbers in MASM expressions in base 16, 10, 8, or 2.

Use the [**n (Set Number Base)**](n--set-number-base-.md) command to set the default radix to 16, 10, or 8. All unprefixed numbers are then interpreted in this base. You can override the default radix by specifying the **0x** prefix (hexadecimal), the **0n** prefix (decimal), the **0t** prefix (octal), or the **0y** prefix (binary).

You can also specify hexadecimal numbers by adding an **h** after the number. You can use uppercase or lowercase letters within numbers. For example, "0x4AB3", "0X4aB3", "4AB3h", "4ab3h", and "4aB3H" have the same meaning.

If you do not add a number after the prefix in an expression, the number is read as 0. Therefore, you can write 0 as 0, the prefix followed by 0, and only the prefix. For example, in hexadecimal, "0", "0x0", and "0x" have the same meaning.

You can enter hexadecimal 64-bit values in the **xxxxxxxx\`xxxxxxxx** format. You can also omit the grave accent (\`). If you include the grave accent, [automatic sign extension](sign-extension.md) is disabled.

This example shows how to add a decimal, octal and binary value to register 10.

```dbgcmd
? @r10 + 0x10 + 0t10 + 0y10
Evaluate expression: 26 = 00000000`0000001a
```

## Symbols in Debugger MASM Expressions

In MASM expressions, the numeric value of any symbol is its memory address. Depending on what the symbol refers to, this address is the address of a global variable, local variable, function, segment, module, or any other recognized label.

To specify which module the address is associated with, include the module name and an exclamation point (!) before the name of the symbol. If the symbol could be interpreted as a hexadecimal number, include the module name and an exclamation point, or just an exclamation point, before the symbol name. For more information about symbol recognition, see [Symbol Syntax and Symbol Matching](symbol-syntax-and-symbol-matching.md).

Use two colons (::) or two underscores (\_\_) to indicate the members of a class.

Use a grave accent (\`) or an apostrophe (') in a symbol name only if you add a module name and exclamation point before the symbol.

## Numeric Operators in MASM Expressions

You can modify any component of an expression by using a unary operator. You can combine any two components by using a binary operator. Unary operators take precedence over binary operators. When you use multiple binary operators, the operators follow the fixed precedence rules that are described in the following tables.

You can always use parentheses to override precedence rules.

If part of an MASM expression is enclosed in parentheses and two at signs (@@) appear before the expression, the expression is interpreted according to [C++ expression rules](c---numbers-and-operators.md). You cannot add a space between the two at signs and the opening parenthesis. You can also specify the [expression evaluator](evaluating-expressions.md) by using **@@c++( ... )** or **@@masm( ... )**.

When you perform arithmetic computations, the MASM expression evaluator treats all numbers and symbols as ULONG64 types.

Unary address operators assume DS as the default segment for addresses. Expressions are evaluated in order of operator precedence. If adjacent operators have equal precedence, the expression is evaluated from left to right.

You can use the following unary operators.

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
<td align="left"><p>+</p></td>
<td align="left"><p>Unary plus</p></td>
</tr>
<tr class="even">
<td align="left"><p>-</p></td>
<td align="left"><p>Unary minus</p></td>
</tr>
<tr class="odd">
<td align="left"><p>not</p></td>
<td align="left"><p>Returns 1 if the argument is zero. Returns zero for any nonzero argument.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>hi</strong></p></td>
<td align="left"><p>High 16 bits</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>low</strong></p></td>
<td align="left"><p>Low 16 bits</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>by</strong></p></td>
<td align="left"><p>Low-order byte from the specified address.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>$pby</strong></p></td>
<td align="left"><p>Same as <strong>by</strong> except that it takes a physical address. Only physical memory that uses the default caching behavior can be read.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>wo</strong></p></td>
<td align="left"><p>Low-order word from the specified address.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>$pwo</strong></p></td>
<td align="left"><p>Same as <strong>wo</strong> except that it takes a physical address. Only physical memory that uses the default caching behavior can be read.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>dwo</strong></p></td>
<td align="left"><p>Double-word from the specified address.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>$pdwo</strong></p></td>
<td align="left"><p>Same as <strong>dwo</strong> except that it takes a physical address. Only physical memory that uses the default caching behavior can be read.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>qwo</strong></p></td>
<td align="left"><p>Quad-word from the specified address.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>$pqwo</strong></p></td>
<td align="left"><p>Same as <strong>qwo</strong> except that it takes a physical address. Only physical memory that uses the default caching behavior can be read.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>poi</strong></p></td>
<td align="left"><p>Pointer-sized data from the specified address. The pointer size is 32 bits or 64 bits. In kernel debugging, this size is based on the processor of the <em>target</em> computer. Therefore, <strong>poi</strong> is the best operator to use if you want pointer-sized data.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>$ppoi</strong></p></td>
<td align="left"><p>Same as <strong>poi</strong> except that it takes a physical address. Only physical memory that uses the default caching behavior can be read.</p></td>
</tr>
</tbody>
</table>

### Examples

The following example shows how to use poi to dereference a pointer to see the value that is stored at that memory location.

First determine the memory address of interest. For example we can look at the thread structure and decide we want to see the value of the CurrentLocale. 

```dbgcmd
0:000> dx @$teb
@$teb                 : 0x8eed57b000 [Type: _TEB *]
    [+0x000] NtTib            [Type: _NT_TIB]
    [+0x038] EnvironmentPointer : 0x0 [Type: void *]
    [+0x040] ClientId         [Type: _CLIENT_ID]
    [+0x050] ActiveRpcHandle  : 0x0 [Type: void *]
    [+0x058] ThreadLocalStoragePointer : 0x1f8f9d634a0 [Type: void *]
    [+0x060] ProcessEnvironmentBlock : 0x8eed57a000 [Type: _PEB *]
    [+0x068] LastErrorValue   : 0x0 [Type: unsigned long]
    [+0x06c] CountOfOwnedCriticalSections : 0x0 [Type: unsigned long]
    [+0x070] CsrClientThread  : 0x0 [Type: void *]
    [+0x078] Win32ThreadInfo  : 0x0 [Type: void *]
    [+0x080] User32Reserved   [Type: unsigned long [26]]
    [+0x0e8] UserReserved     [Type: unsigned long [5]]
    [+0x100] WOW32Reserved    : 0x0 [Type: void *]
    [+0x108] CurrentLocale    : 0x409 [Type: unsigned long]
```

CurrentLocale is located 0x108 beyond the start of the TEB.

```dbgcmd
0:000> ? @$teb + 0x108
Evaluate expression: 613867303176 = 0000008e`ed57b108
```

Use poi to dereference that address.

```dbgcmd
0:000> ? poi(0000008e`ed57b108)
Evaluate expression: 1033 = 00000000`00000409
```

The returned value of 409 matches value of CurrentLocale in the TEB structure.

Or use poi and parentheses to dereference the calculated address.

```dbgcmd
0:000> ? poi(@$teb + 0x108)
Evaluate expression: 1033 = 00000000`00000409
```

Use the *by* or *wo* unary operators to return a byte or word from the target address.

```dbgcmd
0:000> ? by(0000008e`ed57b108)
Evaluate expression: 9 = 00000000`00000009
0:000> ? wo(0000008e`ed57b108)
Evaluate expression: 1033 = 00000000`00000409
```


## Binary Operators

You can use the following binary operators. The operators in each cell take precedence over those in lower cells. Operators in the same cell are of the same precedence and are parsed from left to right.

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
<td align="left"><p>*</p>
<p>/</p>
<p><strong>mod</strong> (or %)</p></td>
<td align="left"><p>Multiplication</p>
<p>Integer division</p>
<p>Modulus (remainder)</p></td>
</tr>
<tr class="even">
<td align="left"><p>+</p>
<p>-</p></td>
<td align="left"><p>Addition</p>
<p>Subtraction</p></td>
</tr>
<tr class="odd">
<td align="left"><p>&lt;&lt;</p>
<p>&gt;&gt;</p>
<p>&gt;&gt;&gt;</p></td>
<td align="left"><p>Left shift</p>
<p>Logical right shift</p>
<p>Arithmetic right shift</p></td>
</tr>
<tr class="even">
<td align="left"><p>= (or ==)</p>
<p>&lt;</p>
<p>&gt;</p>
<p>&lt;=</p>
<p>&gt;=</p>
<p>!=</p></td>
<td align="left"><p>Equal to</p>
<p>Less than</p>
<p>Greater than</p>
<p>Less than or equal to</p>
<p>Greater than or equal to</p>
<p>Not equal to</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>and</strong> (or &)</p></td>
<td align="left"><p>Bitwise AND</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>xor</strong> (or ^)</p></td>
<td align="left"><p>Bitwise XOR (exclusive OR)</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>or</strong> (or |)</p></td>
<td align="left"><p>Bitwise OR</p></td>
</tr>
</tbody>
</table>


The &lt;, &gt;, =, ==, and != comparison operators evaluate to 1 if the expression is true or zero if the expression is false. A single equal sign (=) is the same as a double equal sign (==). You cannot use side effects or assignments within a MASM expression.

An invalid operation (such as division by zero) results in an "Operand error" is returned to the [Debugger Command window](debugger-command-window.md).


We can check that the returned value matches 0x409 by using the == comparison operator.

```dbgcmd
0:000> ? poi(@$teb + 0x108)==0x409
Evaluate expression: 1 = 00000000`00000001
```


## Non-Numeric Operators in MASM Expressions

You can also use the following additional operators in MASM expressions.

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
<td align="left"><p><strong>$fnsucc(</strong><em>FnAddress</em>, <em>RetVal</em>, <em>Flag</em><strong>)</strong></p></td>
<td align="left"><p>Interprets the <em>RetVal</em> value as a return value for the function that is located at the <em>FnAddress</em> address. If this return value qualifies as a success code, <strong>$fnsucc</strong> returns <strong>TRUE</strong>. Otherwise, <strong>$fnsucc</strong> returns <strong>FALSE</strong>.</p>
<p>If the return type is BOOL, bool, HANDLE, HRESULT, or NTSTATUS, <strong>$fnsucc</strong> correctly understands whether the specified return value qualifies as a success code. If the return type is a pointer, all values other than <strong>NULL</strong> qualify as success codes. For any other type, success is defined by the value of <em>Flag</em>. If <em>Flag</em> is 0, a nonzero value of <em>RetVal</em> is success. If <em>Flag</em> is 1, a zero value of <em>RetVal</em> is success.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>$iment (</strong><em>Address</em><strong>)</strong></p></td>
<td align="left"><p>Returns the address of the image entry point in the loaded module list. <em>Address</em> specifies the Portable Executable (PE) image base address. The entry is found by looking up the image entry point in the PE image header of the image that <em>Address</em> specifies.</p>
<p>You can use this function for both modules that are already in the module list and to set <a href="unresolved-breakpoints---bu-breakpoints-.md" data-raw-source="[unresolved breakpoints](unresolved-breakpoints---bu-breakpoints-.md)">unresolved breakpoints</a> by using the <strong><a href="bp--bu--bm--set-breakpoint-.md" data-raw-source="[bu](bp--bu--bm--set-breakpoint-.md)">bu</a></strong> command.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>$scmp("</strong><em>String1</em><strong>", "</strong><em>String2</em><strong>")</strong></p></td>
<td align="left"><p>Evaluates to -1, 0, or 1, like the <strong>strcmp</strong> by using the <strong><a href="/cpp/c-runtime-library/reference/strcmp-wcscmp-mbscmp" data-raw-source=" href="/cpp/c-runtime-library/reference/strcmp-wcscmp-mbscmp"> strcmp </a> C function.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>$sicmp("</strong><em>String1</em><strong>", "</strong><em>String2</em><strong>")</strong></p></td>
<td align="left"><p>Evaluates to -1, 0, or 1, like the <strong>stricmp</strong> Microsoft Win32 function .</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>$spat("</strong><em>String</em><strong>", "</strong><em>Pattern</em><strong>")</strong></p></td>
<td align="left"><p>Evaluates to <strong>TRUE</strong> or <strong>FALSE</strong> depending on whether <em>String</em> matches <em>Pattern</em>. The matching is case-insensitive. <em>Pattern</em> can contain a variety of wildcard characters and specifiers. For more information about the syntax, see <a href="string-wildcard-syntax.md" data-raw-source="[String Wildcard Syntax](string-wildcard-syntax.md)">String Wildcard Syntax</a>.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>$vvalid(</strong><em>Address</em><strong>,</strong> <em>Length</em><strong>)</strong></p></td>
<td align="left"><p>Determines whether the memory range that begins at <em>Address</em> and extends for <em>Length</em> bytes is valid. If the memory is valid, <strong>$vvalid</strong> evaluates to 1. If the memory is invalid, <strong>$vvalid</strong> evaluates to 0.</p></td>
</tr>
</tbody>
</table>

### Examples

The following shows how to use the investigate the range of valid memory around a loaded module

First determine the address of the area of interest, for example by using the [lm (List Loaded Modules](lm--list-loaded-modules-.md) command.

```dbgcmd

0:000> lm
start             end                 module name
00007ff6`0f620000 00007ff6`0f658000   notepad    (deferred)
00007ff9`591d0000 00007ff9`5946a000   COMCTL32   (deferred)        
...
```

Use $vvalid to check a memory range.

```dbgcmd
0:000> ? $vvalid(0x00007ff60f620000, 0xFFFF)
Evaluate expression: 1 = 00000000`00000001
```
Use $vvalid to confirm that this larger range, is an invalid memory range.

```dbgcmd
0:000> ? $vvalid(0x00007ff60f620000, 0xFFFFF)
Evaluate expression: 0 = 00000000`00000000
```

This is also an invalid range.

```dbgcmd
0:000> ? $vvalid(0x0, 0xF)
Evaluate expression: 0 = 00000000`00000000
```

Use *not* to return zero when the memory range is valid.

```dbgcmd
0:000> ? not($vvalid(0x00007ff60f620000, 0xFFFF))
Evaluate expression: 0 = 00000000`00000000
```

Use $imnet to look at the entry point of COMCTL32 that we previously used the lm command to determine the address. It starts at 00007ff9`591d0000.

```dbgcmd
0:000> ? $iment(00007ff9`591d0000)
Evaluate expression: 140708919287424 = 00007ff9`59269e80
```

Disassemble the returned address to examine the entry point code.

```dbgcmd
0:000> u 00007ff9`59269e80
COMCTL32!DllMainCRTStartup:
00007ff9`59269e80 48895c2408      mov     qword ptr [rsp+8],rbx
00007ff9`59269e85 4889742410      mov     qword ptr [rsp+10h],rsi
00007ff9`59269e8a 57              push    rdi
```

COMCTL32 is displayed in the output confirming this is the entry point for this module.

## Registers and Pseudo-Registers in MASM Expressions

You can use registers and pseudo-registers within MASM expressions. You can add an at sign (@) before all registers and pseudo-registers. The at sign causes the debugger to access the value more quickly. This @ sign is unnecessary for the most common x86-based registers. For other registers and pseudo-registers, we recommend that you add the at sign, but it is not actually required. If you omit the at sign for the less common registers, the debugger tries to parse the text as a hexadecimal number, then as a symbol, and finally as a register.

You can also use a period (.) to indicate the current instruction pointer. You should not add an @ sign before this period, and you cannot use a period as the first parameter of the [**r command**](r--registers-.md). This period has the same meaning as the **$ip** pseudo-register.

For more information about registers and pseudo-registers, see [Register Syntax](register-syntax.md) and [Pseudo-Register Syntax](pseudo-register-syntax.md).


Use the r register command to see that the value of the @rip register is 00007ffb`7ed00770.

```dbgcmd
0:000> r
rax=0000000000000000 rbx=0000000000000010 rcx=00007ffb7eccd2c4
rdx=0000000000000000 rsi=00007ffb7ed61a80 rdi=00000027eb6a7000
rip=00007ffb7ed00770 rsp=00000027eb87f320 rbp=0000000000000000
 r8=00000027eb87f318  r9=0000000000000000 r10=0000000000000000
r11=0000000000000246 r12=0000000000000040 r13=0000000000000000
r14=00007ffb7ed548f0 r15=00000210ea090000
iopl=0         nv up ei pl zr na po nc
cs=0033  ss=002b  ds=002b  es=002b  fs=0053  gs=002b             efl=00000246
ntdll!LdrpDoDebuggerBreak+0x30:
00007ffb`7ed00770 cc              int     3
```

This same value can be displayed using the . period shortcut.

```dbgcmd
0:000> ? .
Evaluate expression: 140718141081456 = 00007ffb`7ed00770

```

We can confirm that those values are all equivalent, and return zero if they are, using this MASM expression.

```dbgcmd
0:000>  ? NOT(($ip = .) AND ($ip = @rip) AND (@rip =. ))
Evaluate expression: 0 = 00000000`00000000
```

## Source Line Numbers in MASM Expressions

You can use source file and line number expressions within MASM expressions. You must enclose these expressions by using grave accents (\`). For more information about the syntax, see [Source Line Syntax](source-line-syntax.md).

## See also

[MASM Expressions vs. C++ Expressions](masm-expressions-vs--c---expressions.md)

[Mixed Expression Examples](expression-examples.md)

[C++ Numbers and Operators](c---numbers-and-operators.md)

[Sign Extension](sign-extension.md) 

[? (Evaluate Expression)](---evaluate-expression-.md)
