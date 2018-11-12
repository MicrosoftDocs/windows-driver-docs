---
title: dt (Display Type)
description: The dt command displays information about a local variable, global variable or data type. This can display information about simple data types, as well as structures and unions.
ms.assetid: 82aba13e-6604-46ca-b3e5-bb865ecf3f1f
keywords: ["dt (Display Type) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- dt (Display Type)
api_type:
- NA
ms.localizationpriority: medium
---

# dt (Display Type)


The **dt** command displays information about a local variable, global variable or data type. This can display information about simple data types, as well as structures and unions.

User-Mode Syntax

```dbgcmd
dt [-DisplayOpts] [-SearchOpts] [module!]Name [[-SearchOpts] Field] [Address] [-l List] 
dt [-DisplayOpts] Address [-l List] 
dt -h 
```

Kernel-Mode Syntax

```dbgcmd
[Processor] dt [-DisplayOpts] [-SearchOpts] [module!]Name [[-SearchOpts] Field] [Address] [-l List] 
dt [-DisplayOpts] Address [-l List] 
dt -h 
```

## <span id="ddk_cmd_display_type_dbg"></span><span id="DDK_CMD_DISPLAY_TYPE_DBG"></span>Parameters


<span id="_______Processor______"></span><span id="_______processor______"></span><span id="_______PROCESSOR______"></span> *Processor*   
Specifies the processor that is running the process containing the information needed. For more information, see [Multiprocessor Syntax](multiprocessor-syntax.md). Processors can only be specified in kernel mode.

<span id="_______DisplayOpts______"></span><span id="_______displayopts______"></span><span id="_______DISPLAYOPTS______"></span> *DisplayOpts*   
Specifies one or more of the options given in the following table. These options are preceded by a hyphen.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Option</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>-a</strong>[<em>quantity</em>]</p></td>
<td align="left"><p>Show each array element on a new line, with its index. A total of <em>quantity</em> elements will be displayed. There must be no space between the <strong>a</strong> and the <em>quantity</em>. If <strong>-a</strong> is not followed by a digit, all items in the array are shown. The <strong>-a</strong>[<em>quantity</em>] switch should appear immediately before each type name or field name that you want displayed in this manner.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>-b</strong></p></td>
<td align="left"><p>Display blocks recursively. If a displayed structure contains substructures, it is expanded recursively to arbitrary depths and displayed in full. Pointers are expanded only if they are in the original structure, not in substructures.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>-c</strong></p></td>
<td align="left"><p>Compact output. All fields are displayed on one line, if possible. (When used with the <strong>-a</strong> switch, each array element takes one line rather than being formatted as a several-line block.)</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>-d</strong></p></td>
<td align="left"><p>When used with a <em>Name</em> that is ended with an asterisk, display verbose output for all types that begin with <em>Name</em>. If <em>Name</em> does not end with an asterisk, display verbose output.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>-e</strong></p></td>
<td align="left"><p>Forces <strong>dt</strong> to enumerate types. This option is only needed if <strong>dt</strong> is mistakenly interpreting the <em>Name</em> value as an instance rather than as a type.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>-i</strong></p></td>
<td align="left"><p>Do not indent the subtypes.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>-o</strong></p></td>
<td align="left"><p>Omit offset values of the structure fields.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>-p</strong></p></td>
<td align="left"><p><em>Address</em> is a physical address, rather than a virtual address.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>-r</strong>[<em>depth</em>]</p></td>
<td align="left"><p>Recursively dumps the subtype fields. If <em>depth</em> is given, this recursion will stop after <em>depth</em> levels. The <em>depth</em> must be a digit between 1 and 9, and there must be no space between the <strong>r</strong> and the <em>depth</em>. The <strong>-r</strong>[<em>depth</em>] switch should appear immediately before the address.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>-s</strong> <em>size</em></p></td>
<td align="left"><p>Enumerate only those types whose size in bytes equals the value of <em>size</em>. The <strong>-s</strong> option is only useful when types are being enumerated. When <strong>-s</strong> is specified, <strong>-e</strong> is always implied as well.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>-t</strong></p></td>
<td align="left"><p>Enumerate types only.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>-v</strong></p></td>
<td align="left"><p>Verbose output. This gives additional information such as the total size of a structure and the number of its elements. When this is used along with the <strong>-y</strong> search option, all symbols are displayed, even those with no associated type information.</p></td>
</tr>
</tbody>
</table>

 

<span id="_______SearchOpts______"></span><span id="_______searchopts______"></span><span id="_______SEARCHOPTS______"></span> *SearchOpts*   
Specifies one or more of the options given in the following table. These options are preceded by a hyphen.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Option</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>-n</strong></p></td>
<td align="left"><p>This indicates that the next parameter is a name. This should be used if the next item consists entirely of hexadecimal characters, because it will otherwise be taken as an address.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>-y</strong></p></td>
<td align="left"><p>This indicates that the next parameter is the beginning of the name, not necessarily the entire name. When <strong>-y</strong> is included, all matches are listed, followed by detailed information on the first match in the list. If <strong>-y</strong> is not included, only exact matches will be displayed.</p></td>
</tr>
</tbody>
</table>

 

<span id="_______module______"></span><span id="_______MODULE______"></span> *module*   
An optional parameter specifying the module that defines this structure. If there is a local variable or type with the same name as a global variable or type, you should include *module* to specify that you mean the global variable. Otherwise, the **dt** command will display the local variable, even if the local variable is a case-insensitive match and the global variable is a case-sensitive match.

<span id="_______Name______"></span><span id="_______name______"></span><span id="_______NAME______"></span> *Name*   
Specifies the name of a type or global variable. If *Name* ends with an asterisk (**\\***), a list of all matches is displayed. Thus, **dt A\\*** will list all data types, globals, and statics beginning with "A", but will not display the actual instances of these types. (If the **-v** display option is used at the same time, all symbols will be displayed -- not just those with associated type information.) You can also replace *Name* with a period (**.**) to signify that you want to repeat the most recently used value of *Name*.

If *Name* contains a space, it should be enclosed in parentheses.

<span id="_______Field______"></span><span id="_______field______"></span><span id="_______FIELD______"></span> *Field*   
Specifies the field(s) to be displayed. If *Field* is omitted, all fields are displayed. If *Field* is followed by a period (**.**), the first-level subfields of this field will be displayed as well. If *Field* is followed with a series of periods, the subfields will be displayed to a depth equal to the number of periods. Any field name followed by a period will be treated as a prefix match, as if the **-y** search option was used. If *Field* is followed by an asterisk (\*), it is treated as only the beginning of the field, not necessarily the entire field, and all matching fields are displayed.

<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the address of the structure to be displayed. If *Name* is omitted, *Address* must be included and must specify the address of a global variable. *Address* is taken to be a virtual address unless otherwise specified. Use the **-p** option to specify a physical address. Use an "at" sign ( **@** ) to specify a register (for example, <strong>@eax</strong>).

<span id="_______List______"></span><span id="_______list______"></span><span id="_______LIST______"></span> *List*   
Specifies the field name that links a linked list. The *Address* parameter must be included.

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

The **dt** command output will always display signed numbers in base 10, and unsigned numbers in hexadecimal.

All parameters of **dt** that allow symbol values also allow string wildcards. See [String Wildcard Syntax](string-wildcard-syntax.md) for details.

The **-y** and **-n** options can precede any *Name* or *Field*. The **-y** option allows you to specify the beginning of the type or structure name. For example, **dt -y ALLEN** will display data about the type **ALLENTOWN**. However, you could not display the type **ALLENTOWN** with **dt -y A**. Instead, you would have to use **dt -ny A**, because **A** is a valid hexadecimal value and would be interpreted as an address without the **-n** option.

If *Name* indicates a structure, all fields will be displayed (for example, **dt myStruct**). If you only want one specific field, you can do **dt myStruct myField**. This displays the member that C would call **myStruct.myField**. However, note that the command **dt myStruct myField1 myField2** displays **myStruct.myField1** and **myStruct.myField2**. It does not display **myStruct.myField1.myField2**.

If a structure name or field is followed by a subscript, this specifies a single instance of an array. For example, **dt myStruct myFieldArray\[3\]** will display the fourth element of the array in question. But if a type name is followed by a subscript, this specifies an entire array. For example, **dt CHAR\[8\] myPtr** will display an eight-character string. The subscript is always taken as decimal regardless of the current radix; an **0x** prefix will cause an error.

Because the command uses type information from the .*pdb* file, it can freely be used to debug any CPU platform.

The type information used by **dt** includes all type names created with **typedef**, including all the Windows-defined types. For example, **unsigned long** and **char** are not valid type names, but **ULONG** and **CHAR** are. See the Microsoft Windows SDK for a full list of all Windows type names.

All types created by **typedefs** within your own code will be present, as long as they have actually been used in your program. However, types that are defined in your headers but never actually used will not be stored in the .pdb symbol files and will not be accessible to the debugger. To make such a type available to the debugger, use it as the *input* of a **typedef** statement. For example, if the following appears in your code, the structure MY\_DATA will be stored in the .pdb symbol file and can be displayed by the **dt** command:

```dbgcmd
typedef struct _MY_DATA {
    . . .
    } MY_DATA;
typedef  MY_DATA *PMY_DATA; 
```

On the other hand, the following code would not suffice because both MY\_DATA and PMY\_DATA are defined by the initial **typedef** and, therefore, MY\_DATA has not itself been used as the input of any **typedef** statement:

```dbgcmd
typedef struct _MY_DATA {
    . . .
    } MY_DATA, *PMY_DATA; 
```

In any event, type information is included only in a full symbol file, not a symbol file that has been stripped of all private symbol information. For more information, see [Public and Private Symbols](public-and-private-symbols.md).

If you want to display unicode strings, you need to use the [**.enable\_unicode (Enable Unicode Display)**](-enable-unicode--enable-unicode-display-.md) command first. You can control the display of long integers with the [**.enable\_long\_status (Enable Long Integer Display)**](-enable-long-status--enable-long-integer-display-.md) command.

In the following example, **dt** displays a global variable:

```dbgcmd
0:000> dt mt1 
   +0x000 a                : 10
   +0x004 b                : 98 'b'
   +0x006 c                : 0xdd
   +0x008 d                : 0xabcd
   +0x00c gn               : [6] 0x1
   +0x024 ex               : 0x0 
```

In the following example, **dt** displays the array field **gn**:

```dbgcmd
0:000> dt mt1 -a gn 
   +0x00c gn : 
    [00] 0x1
    [01] 0x2
    [02] 0x3
    [03] 0x4
    [04] 0x5
    [05] 0x6 
```

The following command displays some subfields of a variable:

```dbgcmd
0:000> dt mcl1 m_t1 dpo 
   +0x010 dpo  : DEEP_ONE
   +0x070 m_t1 : MYTYPE1 
```

The following command displays the subfields of the field **m\_t1**. Because the period automatically causes prefix matching, this will also display subfields of any field that begins with "m\_t1":

```dbgcmd
0:000> dt mcl1 m_t1. 
   +0x070 m_t1  : 
      +0x000 a     : 0
      +0x004 b     : 0 '
      +0x006 c     : 0x0
      +0x008 d     : 0x0
      +0x00c gn    : [6] 0x0
      +0x024 ex    : 0x0 
```

You could repeat this to any depth. For example, the command **dt mcl1 a..c.** would display all fields to depth four, such that the first field name began with **a** and the third field name began with **c**.

Here is a more detailed example of how subfields can be displayed. First, display the **Ldr** field:

```dbgcmd
0:000> dt nt!_PEB Ldr 7ffdf000 
   +0x00c Ldr : 0x00191ea0 
```

Now expand the pointer type field:

```dbgcmd
0:000> dt nt!_PEB Ldr Ldr. 7ffdf000 
   +0x00c Ldr  : 0x00191ea0
      +0x000 Length : 0x28
      +0x004 Initialized : 0x1 '
      +0x008 SsHandle : (null)
      +0x00c InLoadOrderModuleList : _LIST_ENTRY [ 0x191ee0 - 0x192848 ]
      +0x014 InMemoryOrderModuleList : _LIST_ENTRY [ 0x191ee8 - 0x192850 ]
      +0x01c InInitializationOrderModuleList : _LIST_ENTRY [ 0x191f58 - 0x192858 ]
      +0x024 EntryInProgress : (null) 
```

Now display the **CriticalSectionTimeout** field:

```dbgcmd
0:000> dt nt!_PEB CriticalSectionTimeout 7ffdf000 
   +0x070 CriticalSectionTimeout : _LARGE_INTEGER 0xffffe86d`079b8000 
```

Now expand the **CriticalSectionTimeout** structure subfields one level deep:

```dbgcmd
0:000> dt nt!_PEB CriticalSectionTimeout. 7ffdf000 
   +0x070 CriticalSectionTimeout  :  0xffffe86d`079b8000
      +0x000 LowPart                 : 0x79b8000
      +0x004 HighPart                : -6035
      +0x000 u                       : __unnamed
      +0x000 QuadPart                : -25920000000000 
```

Now expand the **CriticalSectionTimeout** structure subfields two levels deep:

```dbgcmd
0:000> dt nt!_PEB CriticalSectionTimeout.. 7ffdf000 
   +0x070 CriticalSectionTimeout   :  0xffffe86d`079b8000
      +0x000 LowPart                  : 0x79b8000
      +0x004 HighPart                 : -6035
      +0x000 u                        :
         +0x000 LowPart                  : 0x79b8000
         +0x004 HighPart                 : -6035
      +0x000 QuadPart                 : -25920000000000 
```

The following command displays an instance of the data type MYTYPE1 that is located at the address 0x0100297C:

```dbgcmd
0:000> dt 0x0100297c MYTYPE1 
   +0x000 a                : 22
   +0x004 b                : 43 '+'
   +0x006 c                : 0x0
   +0x008 d                : 0x0
   +0x00c gn               : [6] 0x0
   +0x024 ex               : 0x0 
```

The following command displays an array of 10 ULONGs at the address 0x01002BE0:

```dbgcmd
0:000> dt -ca10 ULONG 01002be0 
[0] 0x1001098
[1] 0x1
[2] 0xdead
[3] 0x7d0
[4] 0x1
[5] 0xcd
[6] 0x0
[7] 0x0
[8] 0x0
[9] 0x0 
```

The following command continues the previous display at a different address. Note that "ULONG" does not need to be re-entered:

```dbgcmd
0:000> dt -ca4 . 01002d00 
Using sym ULONG
[0] 0x12
[1] 0x4ac
[2] 0xbadfeed
[3] 0x2 
```

Here are some examples of type display. The following command displays all types and globals beginning with the string "MY" in the module *thismodule*. Those prefixed with an address are actual instances; those without addresses are type definitions:

```dbgcmd
0:000> dt thismodule!MY* 
010029b8  thismodule!myglobal1
01002990  thismodule!myglobal2
          thismodule!MYCLASS1
          thismodule!MYCLASS2
          thismodule!MYCLASS3
          thismodule!MYTYPE3::u
          thismodule!MYTYPE1
          thismodule!MYTYPE3
          thismodule!MYTYPE3
          thismodule!MYFLAGS 
```

When performing type display, the **-v** option can be used to display the size of each item. The **-s** *size* option can be used to only enumerate items of a specific size. Again, those prefixed with an address are actual instances; those without addresses are type definitions:

```dbgcmd
0:001> dt -s 2 -v thismodule!* 
Enumerating symbols matching thismodule!*, Size = 0x2
Address   Size Symbol
           002 thismodule!wchar_t
           002 thismodule!WORD
           002 thismodule!USHORT
           002 thismodule!SHORT
           002 thismodule!u_short
           002 thismodule!WCHAR
00427a34   002 thismodule!numberOfShips
00427a32   002 thismodule!numberOfPlanes
00427a30   002 thismodule!totalNumberOfItems 
```

Here is an example of the **-b** option. The structure is expanded and the **OwnerThreads** array within the structure is expanded, but the **Flink** and **Blink** list pointers are not followed:

```dbgcmd
kd> dt nt!_ERESOURCE -b 0x8154f040 
   +0x000 SystemResourcesList :  [ 0x815bb388 - 0x816cd478 ]
      +0x000 Flink            : 0x815bb388
      +0x004 Blink            : 0x816cd478
   +0x008 OwnerTable       : (null)
   +0x00c ActiveCount      : 1
   +0x00e Flag             : 8
   +0x010 SharedWaiters    : (null)
   +0x014 ExclusiveWaiters : (null)
   +0x018 OwnerThreads     :
    [00]
      +0x000 OwnerThread      : 0
      +0x004 OwnerCount       : 0
      +0x004 TableSize        : 0
    [01]
      +0x000 OwnerThread      : 0x8167f563
      +0x004 OwnerCount       : 1
      +0x004 TableSize        : 1
   +0x028 ContentionCount  : 0
   +0x02c NumberOfSharedWaiters : 0
   +0x02e NumberOfExclusiveWaiters : 0
   +0x030 Address          : (null)
   +0x030 CreatorBackTraceIndex : 0
   +0x034 SpinLock         : 0
```

Here is an example of **dt** in kernel mode. The following command produces results similar to [**!process 0 0**](-process.md):

```dbgcmd
kd> dt nt!_EPROCESS -l ActiveProcessLinks.Flink -y Ima -yoi Uni 814856f0 
## ActiveProcessLinks.Flink at 0x814856f0

UniqueProcessId : 0x00000008
ImageFileName : [16] "System"

## ActiveProcessLinks.Flink at 0x8138a030

UniqueProcessId : 0x00000084
ImageFileName : [16] "smss.exe"

## ActiveProcessLinks.Flink at 0x81372368

UniqueProcessId : 0x000000a0
ImageFileName : [16] "csrss.exe"

## ActiveProcessLinks.Flink at 0x81369930

UniqueProcessId : 0x000000b4
ImageFileName : [16] "winlogon.exe"

.... 
```

If you want to execute a command for each element of the list, use the [**!list**](-list.md) extension.

Finally, the **dt -h** command will display a short help text summarizing the **dt** syntax.

 

 





