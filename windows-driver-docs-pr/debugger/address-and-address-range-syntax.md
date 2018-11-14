---
title: Address and Address Range Syntax
description: Address and Address Range Syntax
ms.assetid: 3d4f41f1-07ec-484d-a748-27fbbb9bd0b2
ms.author: domars
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# Address and Address Range Syntax


## <span id="ddk_address_and_address_range_syntax_dbg"></span><span id="DDK_ADDRESS_AND_ADDRESS_RANGE_SYNTAX_DBG"></span>


There are several ways to specify addresses in the debugger.

Addresses are always *virtual addresses*, except when the documentation specifically indicates another kind of address. In user mode, the debugger interprets virtual addresses according to the page directory of the [current process](controlling-processes-and-threads.md). In kernel mode, the debugger interprets virtual addresses according to the page directory of the process that the [process context](changing-contexts.md#process-context) specifies. You can also directly set the *user-mode address context*. For more information about the user-mode address context, see [**.context (Set User-Mode Address Context)**](-context--set-user-mode-address-context-.md).

### <span id="address_modes_and_segment_support"></span><span id="ADDRESS_MODES_AND_SEGMENT_SUPPORT"></span>Address Modes and Segment Support

On x86-based platforms, CDB and KD support the following addressing modes. These modes are distinguished by their prefixes.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Prefix</th>
<th align="left">Name</th>
<th align="left">Address types</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>%</p></td>
<td align="left"><p>flat</p></td>
<td align="left"><p>32-bit addresses (also 16-bit selectors that point to 32-bit segments) and 64-bit addresses on 64-bit systems.</p></td>
</tr>
<tr class="even">
<td align="left"><p>&amp;</p></td>
<td align="left"><p>virtual 86</p></td>
<td align="left"><p>Real-mode addresses. x86-based only.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>#</p></td>
<td align="left"><p>plain</p></td>
<td align="left"><p>Real-mode addresses. x86-based only.</p></td>
</tr>
</tbody>
</table>

 

The difference between the plain and virtual 86 modes is that a plain 16-bit address uses the segment value as a selector and looks up the segment descriptor. But a virtual 86 address does not use selectors and instead maps directly into the lower 1 MB.

If you access memory through an addressing mode that is not the current default mode, you can use the address mode prefixes to override the current address mode.

### <span id="address_arguments"></span><span id="ADDRESS_ARGUMENTS"></span>Address Arguments

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
<td align="left"><p><strong>&amp;</strong>[[ segment:]] offset</p></td>
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

In MASM expressions, you can also use the **poi** operator to dereference any pointer. For example, if the pointer at address 0x00123456 points to address location 0x00420000, the following two commands are equivalent.

```dbgcmd
0:000> dd 420000 
0:000> dd poi(123456) 
```

In C++ expressions, pointers behave like pointers in C++. However, numbers are interpreted as integers. If you have to deference an actual number, you must cast it first, as the following example shows.

```dbgcmd
0:000> dd *( (long*) 0x123456 ) 
```

Some [pseudo-registers](pseudo-register-syntax.md) also hold common addresses, such as the current program counter location.

You can also indicate an address in an application by specifying the original source file name and line number. For more information about how to specify this information, see [Source Line Syntax](source-line-syntax.md).

### <span id="address_ranges"></span><span id="ADDRESS_RANGES"></span>Address Ranges

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

There are two other ways to specify the value (the **L***Size* range specifier):

-   **L?** *Size* (with a question mark) means the same as **L***Size*, except that **L?** *Size* removes the debugger's automatic range limit. Typically, there is a range limit of 256 MB, because larger ranges are typographic errors. If you want to specify a range that is larger than 256 MB, you must use the **L?** *Size* syntax.

-   **L-** *Size* (with a hyphen) specifies a range of length *Size* that ends at the given address. For example, **80000000 L20** specifies the range from 0x80000000 through 0x8000001F, and **80000000 L-20** specifies the range from 0x7FFFFFE0 through 0x7FFFFFFF.

Some commands that ask for address ranges accept a single address as the argument. In this situation, the command uses some default object count to compute the size of the range. Typically, commands for which the address range is the final parameter permit this syntax. For the exact syntax and the default range size for each command, see the reference topics for each command.

 

 





