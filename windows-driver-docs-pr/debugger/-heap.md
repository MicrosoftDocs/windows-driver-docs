---
title: heap
description: The heap extension displays heap usage information, controls breakpoints in the heap manager, detects leaked heap blocks, searches for heap blocks, or displays page heap information.
ms.assetid: 70947b56-1a8c-4e78-85d0-d5df87f3150c
keywords: ["heap usage", "GFlags, enabling page heap", "heap Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- heap
api_type:
- NA
ms.localizationpriority: medium
---

# !heap


The **!heap** extension displays heap usage information, controls breakpoints in the heap manager, detects leaked heap blocks, searches for heap blocks, or displays page heap information.

This extension supports the segment heap and the NT heap. Use !heap with no parameter to list all heaps and their type.

```dbgcmd
!heap [HeapOptions] [ValidationOptions] [Heap] 
!heap -b [{alloc|realloc|free} [Tag]] [Heap | BreakAddress] 
!heap -B {alloc|realloc|free} [Heap | BreakAddress] 
!heap -l 
!heap -s [SummaryOptions] [StatHeapAddress] 
!heap -i HeapAddress
!heap -x [-v] Address 
!heap -p [PageHeapOptions] 
!heap -srch [Size] Pattern
!heap -flt FilterOptions
!heap -stat [-h Handle [-grp GroupBy [MaxDisplay]]]
!heap [-p] -?
!heap -triage [Handle | Address] 
```

## <span id="Segment_and_NT_Heap_Parameters"></span><span id="segment_and_nt_heap_parameters"></span><span id="SEGMENT_AND_NT_HEAP_PARAMETERS"></span>Segment and NT Heap Parameters


These parameters work with Segment and NT heaps.

<span id="_______-s______"></span><span id="_______-S______"></span> **-s**   
Specifies that summary information is being requested. If *SummaryOptions* and *StatHeapAddress* are omitted, then summary information is displayed for all heaps associated with the current process.

<span id="_______SummaryOptions______"></span><span id="_______summaryoptions______"></span><span id="_______SUMMARYOPTIONS______"></span> *SummaryOptions*   
Can be any combination of the following options. The *SummaryOptions* are not case-sensitive. Type !heap -s -? for additional information.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Option</th>
<th align="left">Effect</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>-v</strong></p></td>
<td align="left"><p>Verifies all data blocks.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>-b</strong> <strong></strong> <em>BucketSize</em></p></td>
<td align="left"><p>Specifies the bucket size. The default is 1024 bits.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>-d</strong> <strong></strong> <em>DumpBlockSize</em></p></td>
<td align="left"><p>Specifies the bucket size.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>-a</strong></p></td>
<td align="left"><p>Dumps all heap blocks.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>-c</strong></p></td>
<td align="left"><p>Specifies that the contents of each block should be displayed.</p></td>
</tr>
</tbody>
</table>

 

<span id="_______-triage__Handle___Address___"></span><span id="_______-triage__handle___address___"></span><span id="_______-TRIAGE__HANDLE___ADDRESS___"></span> **-triage \[**<em>Handle</em> **|** <em>Address</em>**\]**   
Causes the debugger to automatically search for failures in a process's heaps. If a heap handle is specified as an argument, that heap is examined; otherwise, all the heaps are searched for one that contains the given address, and if one is found, it is examined. Using **-triage** is the only way to validate low-fragmentation heap (LFH) corruption.

<span id="_______-x_-v_"></span><span id="_______-X_-V_"></span> **-x** **** \[**-v**\]   
Causes the debugger to search for the heap block containing the specified address. If -v is added, the command will search the entire virtual memory space of the current process for pointers to this heap block.

<span id="_______-l______"></span><span id="_______-L______"></span> **-l**   
Causes the debugger to detect leaked heap blocks.

<span id="_______-i________Address______-h_HeapAddress______"></span><span id="_______-i________address______-h_heapaddress______"></span><span id="_______-I________ADDRESS______-H_HEAPADDRESS______"></span> **-i** **** *Address* **-h** *HeapAddress*   
Displays information about the specified *Heap*.

<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the address to search for.

<span id="_______-_______"></span> **-?**   
Displays some brief Help text for this extension in the Debugger Command window. Use **!heap -?** for generic help, and **!heap -p -?** for page heap help.

## <span id="ddk__heap_dbg"></span><span id="DDK__HEAP_DBG"></span>NT Heap Parameters


These parameters work only with the NT Heap.

<span id="_______HeapOptions______"></span><span id="_______heapoptions______"></span><span id="_______HEAPOPTIONS______"></span> *HeapOptions*   
Can be any combination of the following options. The *HeapOptions* values are case-sensitive.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Option</th>
<th align="left">Effect</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>-v</strong></p></td>
<td align="left"><p>Causes the debugger to validate the specified heap.</p>
<div class="alert">
<strong>Note</strong>  This option does not detect low fragmentation heap (LFH) corruption. Use <strong>-triage</strong> instead.
</div>
<div>
 
</div></td>
</tr>
<tr class="even">
<td align="left"><p><strong>-a</strong></p></td>
<td align="left"><p>Causes the display to include all information for the specified heap. Size, in this case, is rounded up to the heap granularity. (Running <strong>!heap</strong> with the <strong>-a</strong> option is equivalent to running it with the three options <strong>-h -f -m</strong>, which can take a long time.)</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>-h</strong></p></td>
<td align="left"><p>Causes the display to include all non-LFH entries for the specified heap.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>-hl</strong></p></td>
<td align="left"><p>Causes the display to include all the entries for the specified heap(s), including LFH entries.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>-f</strong></p></td>
<td align="left"><p>Causes the display to include all the free list entries for the specified heap.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>-m</strong></p></td>
<td align="left"><p>Causes the display to include all the segment entries for the specified heap.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>-t</strong></p></td>
<td align="left"><p>Causes the display to include the tag information for the specified heap.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>-T</strong></p></td>
<td align="left"><p>Causes the display to include the pseudo-tag entries for the specified heap.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>-g</strong></p></td>
<td align="left"><p>Causes the display to include the global tag information. Global tags are associated with each untagged allocation.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>-s</strong></p></td>
<td align="left"><p>Causes the display to include summary information for the specified heap.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>-k</strong></p></td>
<td align="left"><p>(x86-based targets only) Causes the display to include the stack backtrace associated with each entry.</p></td>
</tr>
</tbody>
</table>

 

<span id="_______ValidationOptions______"></span><span id="_______validationoptions______"></span><span id="_______VALIDATIONOPTIONS______"></span> *ValidationOptions*   
Can be any single one of the following options. The *ValidationOptions* are case-sensitive.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Option</th>
<th align="left">Effect</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>-D</strong></p></td>
<td align="left"><p>Disables validate-on-call for the specified heap.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>-E</strong></p></td>
<td align="left"><p>Enables validate-on-call for the specified heap.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>-d</strong></p></td>
<td align="left"><p>Disables heap checking for the specified heap.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>-e</strong></p></td>
<td align="left"><p>Enables heap checking for the specified heap.</p></td>
</tr>
</tbody>
</table>

 

<span id="_______-i________Heap_Address______or_HeapAddress______"></span><span id="_______-i________heap_address______or_heapaddress______"></span><span id="_______-I________HEAP_ADDRESS______OR_HEAPADDRESS______"></span> **-i** **** *Heap* **** *Address* **or** *HeapAddress*   
Displays information about the specified *Heap*.

<span id="_______BreakAddress______"></span><span id="_______breakaddress______"></span><span id="_______BREAKADDRESS______"></span> *BreakAddress*   
Specifies the address of a block where a breakpoint is to be set or removed.

<span id="_______-b______"></span><span id="_______-B______"></span> **-b**   
Causes the debugger to create a conditional breakpoint in the heap manager. The **-b** option can be followed by **alloc**, **realloc**, or **free**; this specifies whether the breakpoint will be activated by allocating, reallocating, or freeing memory. If *BreakAddress* is used to specify the address of the block, the breakpoint type can be omitted. If *Heap* is used to specify the heap address or heap index, the type must be included, as well as the *Tag* parameter.

<span id="_______Tag______"></span><span id="_______tag______"></span><span id="_______TAG______"></span> *Tag*   
Specifies the tag name within the heap.

<span id="_______-B______"></span><span id="_______-b______"></span> **-B**   
Causes the debugger to remove a conditional breakpoint from the heap manager. The breakpoint type (**alloc**, **realloc**, or **free**) must be specified, and must be the same as that used with the **-b** option.

<span id="_______StatHeapAddress______"></span><span id="_______statheapaddress______"></span><span id="_______STATHEAPADDRESS______"></span> *StatHeapAddress*   
Specifies the address of the heap. If this is 0 or omitted, all heaps associated with the current process are displayed.

<span id="_______-p______"></span><span id="_______-P______"></span> **-p**   
Specifies that page heap information is being requested. If this is used without any *PageHeapOptions*, all page heaps will be displayed.

<span id="_______PageHeapOptions______"></span><span id="_______pageheapoptions______"></span><span id="_______PAGEHEAPOPTIONS______"></span> *PageHeapOptions*   
Can be any single one of the following options. The *PageHeapOptions* are case-sensitive. If no options are specified, then all possible page heap handles will be displayed.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Option</th>
<th align="left">Effect</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>-h</strong> <strong></strong> <em>Handle</em></p></td>
<td align="left"><p>Causes the debugger to display detailed information about a page heap with handle <em>Handle</em>.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>-a</strong> <strong></strong> <em>Address</em></p></td>
<td align="left"><p>Causes the debugger to find the page heap whose block contains <em>Address</em>. Full details of how this address relates to full-page heap blocks will be included, such as whether this address is part of a page heap, its offset inside the block, and whether the block is allocated or was freed. Stack traces are included whenever available. When using this option, size is displayed in multiples of the heap allocation granularity.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>-t</strong>[<strong>c</strong>|<strong>s</strong>] <strong></strong> [<em>Traces</em>]</p></td>
<td align="left"><p>Causes the debugger to display the collected traces of the heavy heap users. <em>Traces</em> specifies the number of traces to display; the default is four. If there are more traces than the specified number, the earliest traces are displayed. If <strong>-t</strong> or <strong>-tc</strong> is used, the traces are sorted by count usage. If <strong>-ts</strong> is used, the traces are sorted by size. (The <strong>-tc</strong> and <strong>-ts</strong> options are supported in Windows XP only; the <strong>-t</strong> option is supported only in Windows XP and earlier versions of Windows.)</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>-fi</strong> <strong></strong> [<em>Traces</em>]</p></td>
<td align="left"><p>Causes the debugger to display the most recent fault injection traces. <em>Traces</em> specifies the quantity to be displayed; the default is 4.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>-all</strong></p></td>
<td align="left"><p>Causes the debugger to display detailed information about all page heaps.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>-?</strong></p></td>
<td align="left"><p>Causes the debugger to display page heap help, including a diagram of heap blocks. (These diagrams can also be seen in the following Remarks section.)</p></td>
</tr>
</tbody>
</table>

 

Before you can use any **!heap -p** extension command, the page heap must be enabled for your target process. See details in the following Remarks section.

<span id="_______-srch______"></span><span id="_______-SRCH______"></span> **-srch**   
Scans all heaps for the given pattern.

<span id="_______Pattern______"></span><span id="_______pattern______"></span><span id="_______PATTERN______"></span> *Pattern*   
Specifies a pattern for which to look.

<span id="_______Size______"></span><span id="_______size______"></span><span id="_______SIZE______"></span> *Size*   
Can be any single one of the following options. This specifies the size of the pattern. The '-' is required.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Option</th>
<th align="left">Effect</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>-b</strong></p></td>
<td align="left"><p>The pattern is one BYTE in size.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>-w</strong></p></td>
<td align="left"><p>The pattern is one WORD in size.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>-d</strong></p></td>
<td align="left"><p>The pattern is one DWORD in size.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>-q</strong></p></td>
<td align="left"><p>The pattern is one QWORD in size.</p></td>
</tr>
</tbody>
</table>

 

If none of the above are specified, then the pattern is assumed to be of the same size as the machine pointer.

<span id="_______-flt______"></span><span id="_______-FLT______"></span> **-flt**   
Limits the display to include only heaps with the specified size or size range.

<span id="_______FilterOptions______"></span><span id="_______filteroptions______"></span><span id="_______FILTEROPTIONS______"></span> *FilterOptions*   
Can be any single one of the following options. The *FilterOptions* are case-sensitive.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Option</th>
<th align="left">Effect</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>s</strong> <strong></strong> <em>Size</em></p></td>
<td align="left"><p>Limits the display to include only heaps of the specified size.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>r</strong> <strong></strong> <em>SizeMin</em> <strong></strong> <em>SizeMax</em></p></td>
<td align="left"><p>Limits the display to include only heaps within the specified size range.</p></td>
</tr>
</tbody>
</table>

 

<span id="_______-stat______"></span><span id="_______-STAT______"></span> **-stat**   
Displays usage statistics for the specified heap.

<span id="_______-h________Handle______"></span><span id="_______-h________handle______"></span><span id="_______-H________HANDLE______"></span> **-h** *Handle*   
Causes usage statistics for only the heap at *Handle* to be displayed. If *Handle* is 0 or omitted, then usage statistics for all heaps are displayed.

<span id="_______-grp________GroupBy______"></span><span id="_______-grp________groupby______"></span><span id="_______-GRP________GROUPBY______"></span> **-grp** **** *GroupBy*   
Reorders the display as specified by *GroupBy*. The options for *GroupBy* can be found in the following table.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Option</th>
<th align="left">Effect</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>A</strong></p></td>
<td align="left"><p>Displays the usage statistics according to allocation size.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>B</strong></p></td>
<td align="left"><p>Displays the usage statistics according to block count.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>S</strong></p></td>
<td align="left"><p>Displays the usage statistics according to the total size of each allocation.</p></td>
</tr>
</tbody>
</table>

 

<span id="_______MaxDisplay______"></span><span id="_______maxdisplay______"></span><span id="_______MAXDISPLAY______"></span> *MaxDisplay*   
Limits the output to only *MaxDisplay* number of lines.

### <span id="DLL"></span><span id="dll"></span>DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Windows XP and later</strong></p></td>
<td align="left"><p></p>
Ext.dll
Exts.dll</td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For information about heaps, see the Microsoft Windows SDK documentation, the Windows Driver Kit (WDK) documentation, and *Microsoft Windows Internals* by Mark Russinovich and David Solomon. (These resources may not be available in some languages and countries.)

Remarks
-------

This extension command can be used to perform a variety of tasks.

The standard **!heap** command is used to display heap information for the current process. (This should be used only for user-mode processes. The [**!pool**](-pool.md) extension command should be used for system processes.)

The **!heap -b** and **!heap -B** commands are used to create and delete conditional breakpoints in the heap manager.

The **!heap -l** command detects leaked heap blocks. It uses a garbage collector algorithm to detect all busy blocks from the heaps that are not referenced anywhere in the process address space. For huge applications, it can take a few minutes to complete. This command is only available in Windows XP and later versions of Windows.

The **!heap -x** command searches for a heap block containing a given address. If the **-v** option is used, this command will additionally search the entire virtual memory space of the current process for pointers to this heap block. This command is only available in Windows XP and later versions of Windows.

The **!heap -p** command displays various forms of page heap information. Before using **!heap -p**, you must enable the page heap for the target process. This is done through the Global Flags (gflags.exe) utility. To do this, start the utility, fill in the name of the target application in the **Image File Name** text box, select **Image File Options** and **Enable page heap**, and click **Apply**. Alternatively, you can start the Global Flags utility from a Command Prompt window by typing **gflags /i** *xxx.exe* **+hpa**, where *xxx.exe* is the name of the target application.

The **!heap -p -t\[c|s\]** commands are not supported beyond Windows XP. Use the [UMDH](umdh.md) tool provided with the debugger package to obtain similar results.

The **!heap -srch** command displays those heap entries that contain a certain specified pattern.

The **!heap -flt** command limits the display to only heap allocations of a specified size.

The **!heap -stat** command displays heap usage statistics.

Here is an example of the standard **!heap** command:

```dbgcmd
0:000> !ntsdexts.heap -a
Index   Address  Name      Debugging options enabled
  1:   00250000 
    Segment at 00250000 to 00350000 (00056000 bytes committed)
    Flags:               50000062
    ForceFlags:          40000060
    Granularity:         8 bytes
    Segment Reserve:     00100000
    Segment Commit:      00004000
    DeCommit Block Thres:00000400
    DeCommit Total Thres:00002000
    Total Free Size:     000003be
    Max. Allocation Size:7ffddfff
    Lock Variable at:    00250b54
    Next TagIndex:       0012
    Maximum TagIndex:    07ff
    Tag Entries:         00350000
    PsuedoTag Entries:   00250548
    Virtual Alloc List:  00250050
    UCR FreeList:        002504d8
    128-bit bitmap of free lists
    FreeList Usage:      00000014 00000000 00000000 00000000
              Free    Free
              List    List
#       Head      Blink      Flink
    FreeList[ 00 ] at 002500b8: 002a4378 . 002a4378
                                0x02 - HEAP_ENTRY_EXTRA_PRESENT
                                0x04 - HEAP_ENTRY_FILL_PATTERN
        Entry     Prev    Cur   0x10 - HEAP_ENTRY_LAST_ENTRY

Address   Size    Size  flags
002a4370: 00098 . 01c90 [14] - free
    FreeList[ 02 ] at 002500c8: 0025cb30 . 002527b8
002527b0: 00058 . 00010 [04] - free
0025cb28: 00088 . 00010 [04] - free
    FreeList[ 04 ] at 002500d8: 00269a08 . 0026e530
0026e528: 00038 . 00020 [04] - free
0026a4d0: 00038 . 00020 [06] - free
0026f9b8: 00038 . 00020 [04] - free
0025cda0: 00030 . 00020 [06] - free
00272660: 00038 . 00020 [04] - free
0026ab60: 00038 . 00020 [06] - free
00269f20: 00038 . 00020 [06] - free
00299818: 00038 . 00020 [04] - free
0026c028: 00038 . 00020 [06] - free
00269a00: 00038 . 00020 [46] - free
 
    Segment00 at 00250b90:
Flags:           00000000
Base:            00250000
First Entry:     00250bc8
Last Entry:      00350000
Total Pages:     00000080
Total UnCommit:  00000055
Largest UnCommit:000aa000
UnCommitted Ranges: (1)
    002a6000: 000aa000

    Heap entries for Segment00 in Heap 250000
                        0x01 - HEAP_ENTRY_BUSY            
                        0x02 - HEAP_ENTRY_EXTRA_PRESENT   
                        0x04 - HEAP_ENTRY_FILL_PATTERN    
                        0x08 - HEAP_ENTRY_VIRTUAL_ALLOC   
                        0x10 - HEAP_ENTRY_LAST_ENTRY      
                        0x20 - HEAP_ENTRY_SETTABLE_FLAG1  
                        0x40 - HEAP_ENTRY_SETTABLE_FLAG2  
Entry     Prev    Cur   0x80 - HEAP_ENTRY_SETTABLE_FLAG3  

Address   Size    Size  flags       (Bytes used)    (Tag name)
00250000: 00000 . 00b90 [01] - busy (b90)
00250b90: 00b90 . 00038 [01] - busy (38) 
00250bc8: 00038 . 00040 [07] - busy (24), tail fill (NTDLL!LDR Database)
00250c08: 00040 . 00060 [07] - busy (48), tail fill (NTDLL!LDR Database)
00250c68: 00060 . 00028 [07] - busy (10), tail fill (NTDLL!LDR Database)
00250c90: 00028 . 00060 [07] - busy (48), tail fill (NTDLL!LDR Database)
00250cf0: 00060 . 00050 [07] - busy (38), tail fill (Objects=  80)
00250d40: 00050 . 00048 [07] - busy (2e), tail fill (NTDLL!LDR Database)
00250d88: 00048 . 00c10 [07] - busy (bf4), tail fill (Objects>1024)
00251998: 00c10 . 00030 [07] - busy (12), tail fill (NTDLL!LDR Database)
...
002525c0: 00030 . 00060 [07] - busy (48), tail fill (NTDLL!LDR Database)
00252620: 00060 . 00050 [07] - busy (38), tail fill (NTDLL!LDR Database)
00252670: 00050 . 00040 [07] - busy (22), tail fill (NTDLL!CSRSS Client)
002526b0: 00040 . 00040 [07] - busy (24), tail fill (Objects=  64)
002526f0: 00040 . 00040 [07] - busy (24), tail fill (Objects=  64)
00252730: 00040 . 00028 [07] - busy (10), tail fill (Objects=  40)
00252758: 00028 . 00058 [07] - busy (3c), tail fill (Objects=  88)
002527b0: 00058 . 00010 [04] free fill
002527c0: 00010 . 00058 [07] - busy (3c), tail fill (NTDLL!LDR Database)
00252818: 00058 . 002d0 [07] - busy (2b8), tail fill (Objects= 720)
00252ae8: 002d0 . 00330 [07] - busy (314), tail fill (Objects= 816)
00252e18: 00330 . 00330 [07] - busy (314), tail fill (Objects= 816)
00253148: 00330 . 002a8 [07] - busy (28c), tail fill (NTDLL!LocalAtom)
002533f0: 002a8 . 00030 [07] - busy (18), tail fill (NTDLL!LocalAtom)
00253420: 00030 . 00030 [07] - busy (18), tail fill (NTDLL!LocalAtom)
00253450: 00030 . 00098 [07] - busy (7c), tail fill (BASEDLL!LMEM)
002534e8: 00098 . 00060 [07] - busy (44), tail fill (BASEDLL!TMP)
00253548: 00060 . 00020 [07] - busy (1), tail fill (Objects=  32)
00253568: 00020 . 00028 [07] - busy (10), tail fill (Objects=  40)
00253590: 00028 . 00030 [07] - busy (16), tail fill (Objects=  48)
...
0025ccb8: 00038 . 00060 [07] - busy (48), tail fill (NTDLL!LDR Database)
0025cd18: 00060 . 00058 [07] - busy (3c), tail fill (NTDLL!LDR Database)
0025cd70: 00058 . 00030 [07] - busy (18), tail fill (NTDLL!LDR Database)
0025cda0: 00030 . 00020 [06] free fill (NTDLL!Temporary)
0025cdc0: 00020 . 00258 [07] - busy (23c), tail fill (Objects= 600)
0025d018: 00258 . 01018 [07] - busy (1000), tail fill (Objects>1024)
0025e030: 01018 . 00060 [07] - busy (48), tail fill (NTDLL!LDR Database)
...
002a4190: 00028 . 00118 [07] - busy (100), tail fill (BASEDLL!GMEM)
002a42a8: 00118 . 00030 [07] - busy (18), tail fill (Objects=  48)
002a42d8: 00030 . 00098 [07] - busy (7c), tail fill (Objects= 152)
002a4370: 00098 . 01c90 [14] free fill
002a6000:      000aa000      - uncommitted bytes.
```

Here is an example of the **!heap -l** command:

```dbgcmd
1:0:011> !heap -l
1:Heap 00170000
Heap 00280000
Heap 00520000
Heap 00b50000
Heap 00c60000
Heap 01420000
Heap 01550000
Heap 016d0000
Heap 019b0000
Heap 01b40000
Scanning VM ...
## Entry     User      Heap      Segment       Size  PrevSize  Flags

001b2958  001b2960  00170000  00000000        40        18  busy extra
001b9cb0  001b9cb8  00170000  00000000        80       300  busy extra
001ba208  001ba210  00170000  00000000        80        78  busy extra
001cbc90  001cbc98  00170000  00000000        e0        48  busy extra
001cbd70  001cbd78  00170000  00000000        d8        e0  busy extra
001cbe90  001cbe98  00170000  00000000        68        48  busy extra
001cbef8  001cbf00  00170000  00000000        58        68  busy extra
001cc078  001cc080  00170000  00000000        f8       128  busy extra
001cc360  001cc368  00170000  00000000        80        50  busy extra
001cc3e0  001cc3e8  00170000  00000000        58        80  busy extra
001fe550  001fe558  00170000  00000000       150       278  busy extra
001fe6e8  001fe6f0  00170000  00000000        48        48  busy extra
002057a8  002057b0  00170000  00000000        58        58  busy extra
00205800  00205808  00170000  00000000        48        58  busy extra
002058b8  002058c0  00170000  00000000        58        70  busy extra
00205910  00205918  00170000  00000000        48        58  busy extra
00205958  00205960  00170000  00000000        90        48  busy extra
00246970  00246978  00170000  00000000        60        88  busy extra
00251168  00251170  00170000  00000000        78        d0  busy extra user_flag
00527730  00527738  00520000  00000000        40        40  busy extra
00527920  00527928  00520000  00000000        40        80  busy extra
21 leaks detected.
```

The table in this example contains all 21 leaks found.

Here is an example of the **!heap -x** command:

```dbgcmd
0:011> !heap 002057b8 -x
## Entry     User      Heap      Segment       Size  PrevSize  Flags

002057a8  002057b0  00170000  00170640        58        58  busy extra
```

Here is an example of the **!heap -x -v** command:

```dbgcmd
1:0:011> !heap 002057b8 -x -v
## 1:Entry     User      Heap      Segment       Size  PrevSize  Flags

002057a8  002057b0  00170000  00170640        58        58  busy extra

Search VM for address range 002057a8 - 002057ff : 00205990 (002057d0),
```

In this example, there is a pointer to this heap block at address 0x00205990.

Here is an example of the **!heap -flt s** command:

```dbgcmd
0:001>!heap -flt s 0x50
```

This will display all of the allocations of size 0x50.

Here is an example of the **!heap -flt r** command:

```dbgcmd
0:001>!heap -flt r 0x50 0x80
```

This will display each allocation whose size is between 0x50 and 0x7F.

Here is an example of the **!heap -srch** command.

```dbgcmd
0:001> !heap -srch 77176934
    _HEAP @ 00090000
   in HEAP_ENTRY: Size : Prev Flags - UserPtr UserSize - state
        00099A48: 0018 : 0005 [01] - 00099A50 (000000B8) - (busy)
          ole32!CALLFRAME_CACHE<INTERFACE_HELPER_CLSID>::`vftable'
    _HEAP @ 00090000
   in HEAP_ENTRY: Size : Prev Flags - UserPtr UserSize - state
        00099B58: 0018 : 0005 [01] - 00099B60 (000000B8) - (busy)
          ole32!CALLFRAME_CACHE<INTERFACE_HELPER_CLSID>::`vftable'
```

The following diagrams show the arrangement of heap blocks.

Light page heap block -- allocated:

```dbgcmd
 +-----+---------------+---+                                  
 |     |               |   |                                  
 +-----+---------------+---+                                  
    ^         ^          ^                                    
    |         |          8 suffix bytes (filled with 0xA0)    
    |         User allocation (filled with E0 if zeroing not requested) 
    Block header (starts with 0xABCDAAAA and ends with 0xDCBAAAAA) 
```

Light page heap block -- freed:

```dbgcmd
 +-----+---------------+---+                                  
 |     |               |   |                                  
 +-----+---------------+---+                                  
    ^         ^          ^                                    
    |         |          8 suffix bytes (filled with 0xA0)    
    |         User allocation (filled with F0 bytes)          
    Block header (starts with 0xABCDAAA9 and ends with 0xDCBAAA9) 
```

Full page heap block -- allocated:

```dbgcmd
 +-----+---------+---+-------                                 
 |     |         |   |  ... N/A page                          
 +-----+---------+---+-------                                 
    ^       ^      ^                                          
    |       |      0-7 suffix bytes (filled with 0xD0)        
    |       User allocation (if zeroing not requested, filled   
            with E0 in Windows 2000 and C0 in Windows XP)       
    Block header (starts with 0xABCDBBBB and ends with 0xDCBABBBB) 
```

Full page heap block -- freed:

```dbgcmd
 +-----+---------+---+-------                                 
 |     |         |   |  ... N/A page                          
 +-----+---------+---+-------                                 
    ^       ^      ^                                          
    |       |      0-7 suffix bytes (filled with 0xD0)        
    |       User allocation (filled with F0 bytes)            
    Block header (starts with 0xABCDBBA and ends with 0xDCBABBBA) 
```

To see the stack trace of the allocation or the freeing of a heap block or full page heap block, use [**dt DPH\_BLOCK\_INFORMATION**](dt--display-type-.md) with the header address, followed by [**dds**](dds--dps--dqs--display-words-and-symbols-.md) with the block's **StackTrace** field.

 

 





