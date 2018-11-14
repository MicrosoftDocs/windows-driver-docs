---
title: address
description: The address extension displays information about the memory that the target process or target computer uses.
ms.assetid: 9bbde680-8523-4db2-bb7e-fdacdaf1aa89
keywords: ["address Windows Debugging"]
ms.author: domars
ms.date: 09/17/2018
topic_type:
- apiref
api_name:
- address
api_type:
- NA
ms.localizationpriority: medium
---

# !address


The **!address** extension displays information about the memory that the target process or target computer uses.

User-Mode

```dbgcmd
!address Address
!address -summary 
!address [-f:F1,F2,...] {[-o:{csv | tsv | 1}] | [-c:"Command"]}
!address -? | -help
```

Kernel-Mode

```dbgcmd
!address Address 
!address
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Displays only the region of the address space that contains *Address*.

<span id="_______-summary______"></span><span id="_______-SUMMARY______"></span> **-summary**   
Displays only summary information.

<span id="_______-f_F1__F2__..."></span><span id="_______-f_f1__f2__..."></span><span id="_______-F_F1__F2__..."></span> **-f**:*F1*, *F2*, ...  
Displays only the regions specified by the filters *F1*, *F2*, and so on.

The following filter values specify memory regions by the way that the target process is using them.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Filter value</th>
<th align="left">Memory regions displayed</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>VAR</p></td>
<td align="left"><p>Busy regions. These regions include all virtual allocation blocks, the SBH heap, memory from custom allocators, and all other regions of the address space that fall into no other classification.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Free</p></td>
<td align="left"><p>Free memory. This includes all memory that has not been reserved.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Image</p></td>
<td align="left"><p>Memory that is mapped to a file that is part of an executable image.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Stack</p></td>
<td align="left"><p>Memory used for thread stacks.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Teb</p></td>
<td align="left"><p>Memory used for thread environment blocks (TEBs).</p></td>
</tr>
<tr class="even">
<td align="left"><p>Peb</p></td>
<td align="left"><p>Memory used for the process environment block (PEB).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Heap</p></td>
<td align="left"><p>Memory used for heaps.</p></td>
</tr>
<tr class="even">
<td align="left"><p>PageHeap</p></td>
<td align="left"><p>The memory region used for the full-page heap.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>CSR</p></td>
<td align="left"><p>CSR shared memory.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Actx</p></td>
<td align="left"><p>Memory used for activation context data.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>NLS</p></td>
<td align="left"><p>Memory used for National Language Support (NLS) tables.</p></td>
</tr>
<tr class="even">
<td align="left"><p>FileMap</p></td>
<td align="left"><p>Memory used for memory-mapped files. This filter is applicable only during live debugging.</p></td>
</tr>
</tbody>
</table>

 

The following filter values specify memory regions by the memory type.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Filter value</th>
<th align="left">Memory regions displayed</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>MEM_IMAGE</p></td>
<td align="left"><p>Memory that is mapped to a file that is part of an executable image.</p></td>
</tr>
<tr class="even">
<td align="left"><p>MEM_MAPPED</p></td>
<td align="left"><p>Memory that is mapped to a file that is not part of an executable image. This includes memory that is mapped to the paging file.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>MEM_PRIVATE</p></td>
<td align="left"><p>Private memory. This memory is not shared by any other process, and it is not mapped to any file.</p></td>
</tr>
</tbody>
</table>

 

The following filter values specify memory regions by the state of the memory.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Filter value</th>
<th align="left">Memory regions displayed</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>MEM_COMMIT</p></td>
<td align="left"><p>Committed memory.</p></td>
</tr>
<tr class="even">
<td align="left"><p>MEM_FREE</p></td>
<td align="left"><p>Free memory. This includes all memory that has not been reserved.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>MEM_RESERVE</p></td>
<td align="left"><p>Reserved memory.</p></td>
</tr>
</tbody>
</table>

 

The following filter values specify memory regions by the protection applied to the memory.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Filter value</th>
<th align="left">Memory regions displayed</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>PAGE_NOACCESS</p></td>
<td align="left"><p>Memory that cannot be accessed.</p></td>
</tr>
<tr class="even">
<td align="left"><p>PAGE_READONLY</p></td>
<td align="left"><p>Memory that is readable, but not writable and not executable.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>PAGE_READWRITE</p></td>
<td align="left"><p>Memory that is readable and writable, but not executable.</p></td>
</tr>
<tr class="even">
<td align="left"><p>PAGE_WRITECOPY</p></td>
<td align="left"><p>Memory that has copy-on-write behavior.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>PAGE_EXECUTE</p></td>
<td align="left"><p>Memory that is executable, but not readable and not writeable.</p></td>
</tr>
<tr class="even">
<td align="left"><p>PAGE_EXECUTE_READ</p></td>
<td align="left"><p>Memory that is executable and readable, but not writable.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>PAGE_EXECUTE_READWRITE</p></td>
<td align="left"><p>Memory that is executable, readable, and writable.</p></td>
</tr>
<tr class="even">
<td align="left"><p>PAGE_EXECUTE_WRITECOPY</p></td>
<td align="left"><p>Memory that is executable and has copy-on-write behavior.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>PAGE_GUARD</p></td>
<td align="left"><p>Memroy that acts as a guard page.</p></td>
</tr>
<tr class="even">
<td align="left"><p>PAGE_NOCACHE</p></td>
<td align="left"><p>Memory that is not cached.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>PAGE_WRITECOMBINE</p></td>
<td align="left"><p>Memory that has write-combine access enabled.</p></td>
</tr>
</tbody>
</table>

 

<span id="_______-o__csv___tsv___1_"></span><span id="_______-O__CSV___TSV___1_"></span> **-o:**{**csv** | **tsv** | **1**}  
Displays the output according to one of the following options.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Option</th>
<th align="left">Output format</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>csv</p></td>
<td align="left"><p>Displays the output as comma-separated values.</p></td>
</tr>
<tr class="even">
<td align="left"><p>tsv</p></td>
<td align="left"><p>Displays the output as tab-separated values.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>1</p></td>
<td align="left"><p>Displays the output in bare format. This format works well when <strong>!address</strong> is used as input to <strong><a href="-foreach.md" data-raw-source="[.foreach](-foreach.md)">.foreach</a></strong>.</p></td>
</tr>
</tbody>
</table>

 

<span id="_______-c__Command_"></span><span id="_______-c__command_"></span><span id="_______-C__COMMAND_"></span> **-c**:"*Command*"  
Executes a custom command for each memory region. You can use the following placeholders in your command to represent output fields of the **!address** extension.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Placeholder</th>
<th align="left">Output field</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>%1</p></td>
<td align="left"><p>Base address</p></td>
</tr>
<tr class="even">
<td align="left"><p>%2</p></td>
<td align="left"><p>End address + 1</p></td>
</tr>
<tr class="odd">
<td align="left"><p>%3</p></td>
<td align="left"><p>Region size</p></td>
</tr>
<tr class="even">
<td align="left"><p>%4</p></td>
<td align="left"><p>Type</p></td>
</tr>
<tr class="odd">
<td align="left"><p>%5</p></td>
<td align="left"><p>State</p></td>
</tr>
<tr class="even">
<td align="left"><p>%6</p></td>
<td align="left"><p>Protection</p></td>
</tr>
<tr class="odd">
<td align="left"><p>%7</p></td>
<td align="left"><p>Usage</p></td>
</tr>
</tbody>
</table>

 

For example, `!address -f:Heap -c:".echo %1 %3 %5"` displays the base address, size, and state for each memory region of type **Heap**.

Quotes in the command must be preceded by a back slash (\\"). For example, !address -f:Heap -c:"s -a %1 %2 \\"pad\\"" searches each memory region of type **Heap** for the string "pad".

Multiple commands separated by semicolons are not supported.

<span id="_______-_______"></span> **-?**   
Displays minimal Help text for this extension in the [Debugger Command window](debugger-command-window.md).

### <span id="DLL"></span><span id="dll"></span>DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Windows 2000</strong></p></td>
<td align="left"><p>Ext.dll</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Windows XP and later</strong></p></td>
<td align="left"><p>Ext.dll</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information about how to display and search memory, see [Reading and Writing Memory](reading-and-writing-memory.md). For additional extensions that display memory properties, see [**!vm**](-vm.md) (kernel mode) and [**!vprot**](-vprot.md) (user mode).

Remarks
-------

Without any parameters, the **!address** extension displays information about the whole address space. The **!address -summary** command shows only the summary.

In kernel mode, this extension searches only kernel memory, even if you used [**.process (Set Process Context)**](-process--set-process-context-.md) to specify a given process' virtual address space. In user mode, the **!address** extension always refers to the memory that the target process owns.

In user mode, **!address** *Address* shows the characteristics of the region that the specified address belongs to. Without parameters, **!address** shows the characteristics of all memory regions. These characteristics include the memory usage, memory type, memory state, and memory protection. For more information about the meaning of this information, see the earlier tables in the description of the **-f** parameter.

The following example uses **!address** to retrieve information about a region of memory that is mapped to kernel32.dll.

```console
0:000> !address 75831234
Usage:                  Image
Base Address:           75831000
End Address:            758f6000
Region Size:            000c5000
Type:                   01000000MEM_IMAGE
State:                  00001000MEM_COMMIT
Protect:                00000020PAGE_EXECUTE_READ
More info:              lmv m kernel32
More info:              !lmi kernel32
More info:              ln 0x75831234
```

This example uses an *Address* value of 0x75831234. The display shows that this address is in a memory region that begins with the address 0x75831000 and ends with the address 0x758f6000. The region has usage **Image**, type **MEM\_IMAGE**, state **MEM\_COMMIT**, and protection **PAGE\_EXECUTE\_READ**. (For more information about the meaning of these values, see the earlier tables.) The display also lists three other debugger commands that you can use to get more information about this memory address.

If you are starting with an address and trying to determine information about it, the usage information is frequently the most valuable. After you know the usage, you can use additional extensions to learn more about this memory. For example, if the usage is **Heap**, you can use the [**!heap**](-heap.md) extension to learn more.

The following example uses the [**s (Search Memory)**](s--search-memory-.md) command to search each memory region of type **Image** for the wide-character string "Note".

```console
!address /f:Image /c:"s -u %1 %2 \"Note\""

*** Executing: s -u 0xab0000 0xab1000 "Note"
*** Executing: s -u 0xab1000 0xabc000 "Note"
00ab2936  004e 006f 0074 0065 0070 0061 0064 0000  N.o.t.e.p.a.d...
00ab2f86  004e 006f 0074 0065 0070 0061 0064 005c  N.o.t.e.p.a.d.\.
00ab32e4  004e 006f 0074 0065 0070 0061 0064 0000  N.o.t.e.p.a.d...
*** Executing: s -u 0xabc000 0xabd000 "Note"
. . .
```

In kernel mode, the output of **!address** is similar to the user mode output but contains less information. The following example shows the kernel mode output.

```console
kd> !address
  804de000 - 00235000                           
 Usage       KernelSpaceUsageImage
          ImageName   ntoskrnl.exe

  80c00000 - 001e1000
          Usage       KernelSpaceUsagePFNDatabase

....

  f85b0000 - 00004000
          Usage       KernelSpaceUsageKernelStack
          KernelStack 817b4da0 : 324.368

 f880d000 - 073d3000
          Usage       KernelSpaceUsageNonPagedPoolExpansion
```

The meaning of "usage" is the same as in user mode. "ImageName" indicates the module that is associated with this address. "KernelStack" shows the address of this thread's ETHREAD block (0x817B4DA0), the process ID (0x324), and the thread ID (0x368).

 

 





