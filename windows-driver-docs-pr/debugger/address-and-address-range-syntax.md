---
title: Address and Address Range Syntax
description: Address and Address Range Syntax
ms.date: 05/28/2021
ms.localizationpriority: medium
ms.custom: contperf-fy21q4
---

# Address and Address Range Syntax

There are several ways to specify addresses in the debugger.

Addresses are normally *virtual addresses*, except when the documentation specifically indicates another kind of address. In user mode, the debugger interprets virtual addresses according to the page directory of the [current process](controlling-processes-and-threads.md). In kernel mode, the debugger interprets virtual addresses according to the page directory of the process that the [process context](changing-contexts.md#process-context) specifies. You can also directly set the *user-mode address context*. For more information about the user-mode address context, see [**.context (Set User-Mode Address Context)**](-context--set-user-mode-address-context-.md).

In MASM expressions, you can use the **poi** operator to dereference any pointer. For example, if the pointer at address 0x0000008e`ed57b108 points to address location 0x805287637256, the following two commands are equivalent.

```dbgcmd
0:000> dd 805287637256
0:000> dd poi(000000bb`7ee23108)
```

## Display memory address example 

To see an example of using poi, determine the offset for the *CurrentLocale* of the thread environment block (TEB). Use the dx command to display @$teb, which is an example of a  [pseudo-registers](pseudo-register-syntax.md), that hold common addresses, such as the current program counter location.


```dbgcmd
0:000> dx @$teb
@$teb                 : 0x1483181000 [Type: _TEB *]

...

    [+0x108] CurrentLocale    : 0x409 [Type: unsigned long]
```

*CurrentLocale* is +0x108 from the start of the TEB. Next determine the memory address of that location.

```dbgcmd
0:000> ? @$teb + 0x108
Evaluate expression: 613867303176 = 0000008e`ed57b108
```

Use poi to dereference that address to see that it contains the CurrentLocale value of 0x409.

```dbgcmd
0:000> ? poi(0000008e`ed57b108)
Evaluate expression: 1033 = 00000000`00000409
```

In C++ debugger expressions, pointers behave like pointers in C++. However, numbers are interpreted as integers. If you have to deference an actual number, you may need to cast it first, as the following example shows.

To try this, use [.expr](-expr--choose-expression-evaluator-.md) to set the expression evaluator to C++.

```dbgcmd
0:000> .expr /s C++
Current expression evaluator: C++ - C++ source expressions
```
With the expression evaluator set to C++, we can cast using long.

```dbgcmd
0:000> d *((long*)0x00000014`83181108 ) 
00000000`00000409  ???????? ???????? ???????? ????????
```

For more information about casting numeric values, see [C++ Numbers and Operators](c---numbers-and-operators.md).

If the expression evaluator is set to c++, we can wrap the poi pointer with *@@masm()*, to have just that part of the expression evaluated by the MASM expression evaluator.

```dbgcmd
0:000> .expr /s c++
Current expression evaluator: C++ - C++ source expressions

0:000> ? @@masm(poi(00000078`267d7108))
Evaluate expression: 1033 = 00000000`00000409
```

For more information about the two expression evaluators, see [Evaluating Expressions](evaluating-expressions.md).

You can also indicate an address in an application by specifying the original source file name and line number. For more information about how to specify this information, see [Source Line Syntax](source-line-syntax.md).


## Address Ranges

You can specify an address range by a pair of addresses or by an address and object count.

To specify a range by a pair of addresses, specify the starting address and the ending address. For example, the following example is a range of 8 bytes, beginning at the address 0x00001000.

```dbgcmd
0x00001000  0x00001007
```

To specify an address range by an address and object count, specify an address argument, the letter L (uppercase or lowercase), and a value argument. The address specifies the starting address. The value specifies the number of objects to be examined or displayed. The size of the object depends on the command. For example, if the object size is 1 byte, the following example is a range of 8 bytes, beginning at the address 0x00001000.

```dbgcmd
0x00001000  L8
```

However, if the object size is a double word (32 bits or 4 bytes), the following two ranges each give an 8-byte range.

```dbgcmd
0x00001000  0x00001007
0x00001000  L2
```

## L Size range specifier

There are two other ways to specify the value (the **L***Size* range specifier):

-   **L?** *Size* (with a question mark) means the same as **L***Size*, except that **L?** *Size* removes the debugger's automatic range limit. Typically, there is a range limit of 256 MB, because larger ranges are typographic errors. If you want to specify a range that is larger than 256 MB, you must use the **L?** *Size* syntax.

-   **L-** *Size* (with a hyphen) specifies a range of length *Size* that ends at the given address. For example, **80000000 L20** specifies the range from 0x80000000 through 0x8000001F, and **80000000 L-20** specifies the range from 0x7FFFFFE0 through 0x7FFFFFFF.

Some commands that ask for address ranges accept a single address as the argument. In this situation, the command uses some default object count to compute the size of the range. Typically, commands for which the address range is the final parameter permit this syntax. For the exact syntax and the default range size for each command, see the reference topics for each command.

## Search memory range example 

First we will determine the address of the rip instruction pointer register using the MASM expression evaluator.

```dbgcmd
0:000> ? @rip 
Evaluate expression: 140720561719153 = 00007ffc`0f180771
```

Then we will search starting at 00007ffc`0f180771, for 100000 using the [s (Search Memory)](s--search-memory-.md) command. We specify the range to search using L100000.

```dbgcmd
0:000> s -a 00007ffc`0f180771 L100000 "ntdll"  
00007ffc`0f1d48fa  6e 74 64 6c 6c 5c 6c 64-72 69 6e 69 74 2e 63 00  ntdll\ldrinit.c.
00007ffc`0f1d49c2  6e 74 64 6c 6c 5c 6c 64-72 6d 61 70 2e 63 00 00  ntdll\ldrmap.c..
00007ffc`0f1d4ab2  6e 74 64 6c 6c 5c 6c 64-72 72 65 64 69 72 65 63  ntdll\ldrredirec
00007ffc`0f1d4ad2  6e 74 64 6c 6c 5c 6c 64-72 73 6e 61 70 2e 63 00  ntdll\ldrsnap.c.
...
```

We can also specify the same range like this using two memory addresses.

```dbgcmd
0:000> s -a 0x00007ffc`0f180771 0x00007ffc`0f280771 "ntdll"  
00007ffc`0f1d48fa  6e 74 64 6c 6c 5c 6c 64-72 69 6e 69 74 2e 63 00  ntdll\ldrinit.c.
00007ffc`0f1d49c2  6e 74 64 6c 6c 5c 6c 64-72 6d 61 70 2e 63 00 00  ntdll\ldrmap.c..
00007ffc`0f1d4ab2  6e 74 64 6c 6c 5c 6c 64-72 72 65 64 69 72 65 63  ntdll\ldrredirec
00007ffc`0f1d4ad2  6e 74 64 6c 6c 5c 6c 64-72 73 6e 61 70 2e 63 00  ntdll\ldrsnap.c.
...
```

Lastly we can search backwards in the memory range by using the L- length parameter.

```dbgcmd
0:000> s -a 00007ffc`0f1d4ad2 L-100000 "ntdll"  
00007ffc`0f1d48fa  6e 74 64 6c 6c 5c 6c 64-72 69 6e 69 74 2e 63 00  ntdll\ldrinit.c.
00007ffc`0f1d49c2  6e 74 64 6c 6c 5c 6c 64-72 6d 61 70 2e 63 00 00  ntdll\ldrmap.c..
00007ffc`0f1d4ab2  6e 74 64 6c 6c 5c 6c 64-72 72 65 64 69 72 65 63  ntdll\ldrredirec
```

## Unassemble memory example

This example, uses the [u (unassemble)](u--unassemble-.md) command and the L parameter to unassemble three bytes of code.

```dbgcmd
0:000> u 00007ffc`0f1d48fa L3
ntdll!`string'+0xa:
00007ffc`0f1d48fa 6e              outs    dx,byte ptr [rsi]
00007ffc`0f1d48fb 7464            je      ntdll!`string'+0x21 (00007ffc`0f1d4961)
00007ffc`0f1d48fd 6c              ins     byte ptr [rdi],dx
```

Or specify a three byte range of memory to unassemble like this.

```dbgcmd
0:000> u 00007ffc`0f1d48fa 00007ffc`0f1d48fd
ntdll!`string'+0xa:
00007ffc`0f1d48fa 6e              outs    dx,byte ptr [rsi]
00007ffc`0f1d48fb 7464            je      ntdll!`string'+0x21 (00007ffc`0f1d4961)
00007ffc`0f1d48fd 6c              ins     byte ptr [rdi],dx
```

## Address Modes and Segment Support

On x86-based platforms, CDB and KD support the following addressing modes. These modes are distinguished by their prefixes.

|Prefix|Name|Address types|
|--- |--- |--- |
|%|flat|32-bit addresses (also 16-bit selectors that point to 32-bit segments) and 64-bit addresses on 64-bit systems.|
|&|virtual 86|Real-mode addresses. x86-based only.|
|#|plain|Real-mode addresses. x86-based only.|

The difference between the plain and virtual 86 modes is that a plain 16-bit address uses the segment value as a selector and looks up the segment descriptor. But a virtual 86 address does not use selectors and instead maps directly into the lower 1 MB.

If you access memory through an addressing mode that is not the current default mode, you can use the address mode prefixes to override the current address mode.

## Address Arguments

Address arguments specify the location of variables and functions. The following table explains the syntax and meaning of the various addresses that you can use in CDB and KD.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Syntax</th>
<th align="left">Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>offset</p></td>
<td align="left"><p>The absolute address in virtual memory space, with a type that corresponds to the current execution mode. For example, if the current execution mode is 16 bit, the offset is 16 bit. If the execution mode is 32-bit segmented, the offset is 32-bit segmented.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>&</strong>[[ segment:]] offset</p></td>
<td align="left"><p>The real address. x86-based and x64-based.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>%</strong>segment:[[ offset]]</p></td>
<td align="left"><p>A segmented 32-bit or 64-bit address. x86-based and x64-based.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>%</strong>[[ offset]]</p></td>
<td align="left"><p>An absolute address (32-bit or 64-bit) in virtual memory space. x86-based and x64-based.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>name[[ <strong>+</strong>|<strong>−</strong> ]] offset</p></td>
<td align="left"><p>A flat 32-bit or 64-bit address. <em>name</em> can be any symbol. <em>offset</em> specifies the offset. This offset can be whatever address mode its prefix indicates. No prefix specifies a default mode address. You can specify the offset as a positive (+) or negative (−) value.</p></td>
</tr>
</tbody>
</table>

Use the [**dg (Display Selector)**](dg--display-selector-.md) command to view segment descriptor information.

## See Also

To display information about memory, use the [!address](-address.md) command. 

To search memory, use the [s (Search Memory)](s--search-memory-.md) command. 

To display the contents of memory use the [d, da, db, dc, dd, dD, df, dp, dq, du, dw (Display Memory)](d--da--db--dc--dd--dd--df--dp--dq--du--dw--dw--dyb--dyd--display-memor.md) command. 

For information on how you can view and edit memory using a Memory window see [Using a Memory Window](memory-window.md).
