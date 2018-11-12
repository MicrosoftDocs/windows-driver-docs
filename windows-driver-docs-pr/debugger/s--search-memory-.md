---
title: s (Search Memory)
description: The s command searches through memory to find a specific byte pattern.
ms.assetid: fdca07c3-95c8-46cf-8da1-07a5e6767f67
keywords: ["s (Search Memory) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- s (Search Memory)
api_type:
- NA
ms.localizationpriority: medium
---

# s (Search Memory)


The **s** command searches through memory to find a specific byte pattern.

Do not confuse this command with the [**~s (Change Current Processor)**](-s--change-current-processor-.md), [**~s (Set Current Thread)**](-s--set-current-thread-.md), [**|s (Set Current Process)**](-s--set-current-process-.md), or [**||s (Set Current System)**](--s--set-current-system-.md) commands.

```dbgcmd
s [-[[Flags]Type]] Range Pattern 
s -[[Flags]]v Range Object 
s -[[Flags]]sa Range 
s -[[Flags]]su Range 
```

## <span id="ddk_cmd_search_memory_dbg"></span><span id="DDK_CMD_SEARCH_MEMORY_DBG"></span>Parameters


<span id="_______________Flags______________"></span><span id="_______________flags______________"></span><span id="_______________FLAGS______________"></span> **\[** *Flags*\]   
Specifies one or more search options. Each flag is a single letter. You must enclose the flags in a single set of brackets (\[\]). You cannot add spaces between the brackets, except between **n** or **l** and its argument. For example, if you want to specify the **s** and **w** options, use the command s -\[sw\]Type Range Pattern.

You can specify one or more of the following flags:

<span id="s"></span><span id="S"></span>**s**  
Saves all of the results of the current search. You can use these results to repeat the search later.

<span id="r"></span><span id="R"></span>**r**  
Restricts the current search to the results from the last saved search. You cannot use the **s** and **r** flags in the same command. When you use **r**, the value of *Range* is ignored, and the debugger searches only those hits that were saved by the previous **s** command.

<span id="n_Hits"></span><span id="n_hits"></span><span id="N_HITS"></span>**n** *Hits*  
Specifies the number of hits to save when you use the **s** flag. The default value is 1024 hits. If you use **n** together with other flags, **n** must be the last flag, followed by its *Hits* argument. The space between **n** and *Hits* is optional, but you cannot add any other spaces within the brackets. If any later search that uses the **s** flag discovers more than the specified number of hits, the **Overflow error** message is displayed to notify you that not all hits are being saved.

<span id="l_Length"></span><span id="l_length"></span><span id="L_LENGTH"></span>**l** *Length*  
Causes a search for arbitrary ASCII or Unicode strings to return only strings that are at least *Length* characters long. The default length is 3. This value affects only searches that use the **-sa** or **-su** flags.

<span id="w"></span><span id="W"></span>**w**  
Searches only writeable memory regions. You must enclose the "w" in brackets.

<span id="1"></span>**1**  
Displays only the addresses of search matches in the search output. This option is useful if you are using the [**.foreach**](-foreach.md) token to pipe the command output into another command's input.

<span id="_______Type______"></span><span id="_______type______"></span><span id="_______TYPE______"></span> *Type*   
Specifies the memory type to search for. Add a hyphen (-) in front of *Type* . You can use one of the following *Type* values.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>b</strong></p></td>
<td align="left"><p>Byte (8 bits)</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>w</strong></p></td>
<td align="left"><p>WORD (16 bits)</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>d</strong></p></td>
<td align="left"><p>DWORD (32 bits)</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>q</strong></p></td>
<td align="left"><p>QWORD (64 bits)</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>a</strong></p></td>
<td align="left"><p></p>
ASCII string
(not necessarily a null-terminated string)</td>
</tr>
<tr class="even">
<td align="left"><p><strong>u</strong></p></td>
<td align="left"><p></p>
Unicode string
(not necessarily a null-terminated string)</td>
</tr>
</tbody>
</table>

 

If you omit *Type*, byte values are used. However, if you use *Flags*, you cannot omit *Type*.

<span id="_______sa______"></span><span id="_______SA______"></span> **sa**   
Searches for any memory that contains printable ASCII strings. Use the **l** *Length* flag to specify a minimum length of such strings. The default minimum length is 3 characters.

<span id="_______su______"></span><span id="_______SU______"></span> **su**   
Searches for any memory that contains printable Unicode strings. Use the **l** *Length* flag to specify a minimum length of such strings. The default minimum length is 3 characters.

<span id="_______Range______"></span><span id="_______range______"></span><span id="_______RANGE______"></span> *Range*   
Specifies the memory area to search through. This range cannot be more than 256 MB long unless you use the **L?** syntax. For more information about this syntax, see [Address and Address Range Syntax](address-and-address-range-syntax.md).

<span id="_______Pattern______"></span><span id="_______pattern______"></span><span id="_______PATTERN______"></span> *Pattern*   
Specifies one or more values to search for. By default, these values are byte values. You can specify different types of memory in *Type*. If you specify a WORD, DWORD, or QWORD value, enclose it in single quotation marks (for example, **'Tag7'**). If you specify a string, enclose it in double quotation marks (for example, **"This string"**).

<span id="_______-v______"></span><span id="_______-V______"></span> **-v**   
Searches for objects of the same type as the specified *Object*.

<span id="_______Object______"></span><span id="_______object______"></span><span id="_______OBJECT______"></span> *Object*   
Specifies the address of an object or the address of a pointer to an object. The debugger then searches for objects of the same type as the object that *Object* specifies.

### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Modes</strong></p></td>
<td align="left"><p>User mode, kernel mode</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Targets</strong></p></td>
<td align="left"><p>Live, crash dump</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Platforms</strong></p></td>
<td align="left"><p>All</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information about memory manipulation and a description of other memory-related commands, see [Reading and Writing Memory](reading-and-writing-memory.md).

Remarks
-------

If the debugger finds the byte pattern that you specify, the debugger displays the first memory address in the *Range* memory area where the pattern was found. The debugger displays an excerpt of memory that begins at that location in a format that matches the specified *Type* memory type. If *Type* is **a** or **u**, the memory contents and the corresponding ASCII or Unicode characters are displayed.

You must specify the *Pattern* parameter as a series of bytes, unless you specify a different *Type* value. You can enter byte values as numeric or ASCII characters:

-   Numeric values are interpreted as numbers in the current radix (16, 10, or 8). To change the default radix, use the [**n (Set Number Base)**](n--set-number-base-.md) command. You can override the default radix by specifying the **0x** prefix (hexadecimal), the **0n** prefix (decimal), the **0t** prefix (octal), or the **0y** prefix (binary).
    **Note**   The default radix behaves differently when you use C++ expressions. For more information about these expressions and the radix, see [Evaluating Expressions](evaluating-expressions.md).

     

-   You must enclose ASCII characters in single straight quotation marks. You cannot use C-style escape characters (such as '\\0' or '\\n').

If you specify multiple bytes, you must separate them by spaces.

The **s-a** and **s-u** commands search for specified ASCII and Unicode strings, respectively. These strings do not have to be null-terminated.

The **s-sa** and **s-su** commands search for unspecified ASCII and Unicode strings. These are useful if you are checking a range of memory to see whether it contains any printable characters. The flags options allow you to specify a minimum length of string to find.

Example: The following command finds ASCII strings that are of length &gt;=3 in the range beginning at 0000000140000000 and ending 400 bytes later.

```dbgcmd
s-sa 0000000140000000 L400
```

The following command finds ASCII strings that are of length &gt;=4 in the range beginning at 0000000140000000 and ending 400 bytes later

```dbgcmd
s -[l4]sa 0000000140000000 L400
```

The following command does the same thing, but it limits the search to writeable memory regions.

```dbgcmd
s -[wl4]sa 0000000140000000 L400
```

The following command does the same thing, but displays only the address of the match, rather than the address and the value.

```dbgcmd
s -[1wl4]sa 0000000140000000 L400
```

The **s-v** command searches for objects of the same data type as the *Object* object. You can use this command only if the desired object is a C++ class or another object that is associated with virtual function tables (Vtables). The **s-v** command searches the *Range* memory area for the addresses of this class's Vtables. If multiple Vtables exist in this class, the search algorithm looks for all of these pointer values, separated by the proper number of bytes. If any matches are found, the debugger returns the base address of the object and full information about this object--similar to the output of the [**dt (Display Type)**](dt--display-type-.md) command.

Example: Assume the current radix is 16. The following three command all do the same thing: search memory locations 0012FF40 through 0012FF5F for "Hello".

```dbgcmd
0:000> s 0012ff40 L20 'H' 'e' 'l' 'l' 'o' 
```

```dbgcmd
0:000> s 0012ff40 L20 48 65 6c 6c 6f 
```

```dbgcmd
0:000> s -a 0012ff40 L20 "Hello" 
```

These commands locate each appearance of "Hello" and return the address of each such pattern--that is, the address of the letter "H".

The debugger returns only patterns that are completely contained in the search range. Overlapping patterns are found correctly. (In other words, the pattern "QQQ" is found three times in "QQQQQ".)

The following example shows a search that uses the *Type* parameter. This command searches memory locations 0012FF40 through 0012FF5F for the double-word 'VUTS':

```dbgcmd
0:000> s -d 0012ff40 L20 'VUTS' 
```

On little-endian computers, 'VUTS' is the same as the byte pattern 'S' 'T' 'U' 'V'. However, searches for WORDs, DWORDs, and QWORDs return only results that are correctly byte-aligned.

 

 





