---
title: e, ea, eb, ed, eD, ef, ep, eq, eu, ew, eza (Enter Values)
description: The e* commands enter into memory the values that you specify.This command should not be confused with the ~E (Thread-Specific Command) qualifier.
ms.assetid: d21b13ac-2268-4218-b562-4c466956b05d
keywords: ["e, ea, eb, ed, eD, ef, ep, eq, eu, ew, eza (Enter Values) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- e, ea, eb, ed, eD, ef, ep, eq, eu, ew, eza (Enter Values)
api_type:
- NA
ms.localizationpriority: medium
---

# e, ea, eb, ed, eD, ef, ep, eq, eu, ew, eza (Enter Values)


The **e\\*** commands enter into memory the values that you specify.

This command should not be confused with the [**~E (Thread-Specific Command)**](-e--thread-specific-command-.md) qualifier.

```dbgcmd
e{b|d|D|f|p|q|w} Address [Values] 
e{a|u|za|zu} Address "String" 
e Address [Values]
```

## <span id="ddk_cmd_enter_values_dbg"></span><span id="DDK_CMD_ENTER_VALUES_DBG"></span>Parameters


### <span id="syntax__ed_ef"></span><span id="SYNTAX__ED_EF"></span>Syntax eD ef

<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the starting address where to enter values. The debugger replaces the value at *Address* and each subsequent memory location until all *Values* have been used.

<span id="_______Values______"></span><span id="_______values______"></span><span id="_______VALUES______"></span> *Values*   
Specifies one or more values to enter into memory. Multiple numeric values should be separated with spaces. If you do not specify any values, the current address and the value at that address will be displayed, and you will be prompted for input.

<span id="_______String______"></span><span id="_______string______"></span><span id="_______STRING______"></span> *String*   
Specifies a string to be entered into memory. The **ea** and **eza** commands will write this to memory as an ASCII string; the **eu** and **ezu** commands will write this to memory as a Unicode string. The **eza** and **ezu** commands write a terminal **NULL**; the **ea** and **eu** commands do not. *String* must be enclosed in quotation marks.

### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Modes</strong></p></td>
<td align="left"><p>user mode, kernel mode</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Targets</strong></p></td>
<td align="left"><p>live, crash dump</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Platforms</strong></p></td>
<td align="left"><p>all</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For an overview of memory manipulation and a description of other memory-related commands, see [Reading and Writing Memory](reading-and-writing-memory.md).

Remarks
-------

This command exists in the following forms. The second characters of the **ed** and **eD** commands are case-sensitive.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Command</th>
<th align="left">Enter</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>e</strong></p></td>
<td align="left"><p>This enters data in the same format as the most recent <strong>e<em></strong> command. (If the most recent <strong>e</em></strong> command was <strong>ea</strong>, <strong>eza</strong>, <strong>eu</strong>, or <strong>ezu</strong>, the final parameter will be <em>String</em> and may not be omitted.)</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>ea</strong></p></td>
<td align="left"><p>ASCII string (not NULL-terminated).</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>eb</strong></p></td>
<td align="left"><p>Byte values.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>ed</strong></p></td>
<td align="left"><p>Double-word values (4 bytes).</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>eD</strong></p></td>
<td align="left"><p>Double-precision floating-point numbers (8 bytes).</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>ef</strong></p></td>
<td align="left"><p>Single-precision floating-point numbers (4 bytes).</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>ep</strong></p></td>
<td align="left"><p>Pointer-sized values. This command is equivalent to <strong>ed</strong> or <strong>eq</strong>, depending on whether the target computer&#39;s processor architecture is 32-bit or 64-bit, respectively.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>eq</strong></p></td>
<td align="left"><p>Quad-word values (8 bytes).</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>eu</strong></p></td>
<td align="left"><p>Unicode string (not NULL-terminated).</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>ew</strong></p></td>
<td align="left"><p>Word values (2 bytes).</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>eza</strong></p></td>
<td align="left"><p>NULL-terminated ASCII string.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>ezu</strong></p></td>
<td align="left"><p>NULL-terminated Unicode string.</p></td>
</tr>
</tbody>
</table>

 

Numeric values will be interpreted as numbers in the current radix (16, 10, or 8). To change the default radix, use the [**n (Set Number Base)**](n--set-number-base-.md) command. The default radix can be overridden by specifying the **0x** prefix (hexadecimal), the **0n** prefix (decimal), the **0t** prefix (octal), or the **0y** prefix (binary).

**Note**   The default radix behaves differently when C++ expressions are being used. See [Evaluating Expressions](evaluating-expressions.md) for details.

 

When entering byte values with the **eb** command, you can use single straight quotation marks to specify characters. If you want to include multiple characters, each must be surrounded with its own quotation marks. This allows you to enter a character string that is not terminated by a null character. For example:

```dbgcmd
eb 'h' 'e' 'l' 'l' 'o'
```

C-style escape characters (such as '\\0' or '\\n') may not be used with these commands.

If you omit the *Values* parameter, you will be prompted for input. The address and its current contents will be displayed, and an **Input&gt;** prompt will appear. You can then do any of the following:

-   Enter a new value, by typing the value and pressing ENTER.

-   Preserve the current value in memory by pressing SPACE followed by ENTER.

-   Exit from the command by pressing ENTER.

 

 





