---
title: vm
description: The vm extension displays summary information about virtual memory use statistics on the target system.
ms.assetid: 25e4f80c-d4ca-407c-991d-e8ee5dfbb309
keywords: ["vm Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- vm
api_type:
- NA
ms.localizationpriority: medium
---

# !vm


The **!vm** extension displays summary information about virtual memory use statistics on the target system.

```dbgcmd
!vm [Flags]
```

## <span id="ddk__vm_dbg"></span><span id="DDK__VM_DBG"></span>Parameters


<span id="_______Flags______"></span><span id="_______flags______"></span><span id="_______FLAGS______"></span> *Flags*   
Specifies what information will be displayed in the output from this command. This can be any sum of the following bits. The default is 0, which causes the display to include system-wide virtual memory statistics as well as memory statistics for each process.

<span id="Bit_0__0x1_"></span><span id="bit_0__0x1_"></span><span id="BIT_0__0X1_"></span>Bit 0 (0x1)  
Causes the display to omit process-specific statistics.

<span id="Bit_1__0x2_"></span><span id="bit_1__0x2_"></span><span id="BIT_1__0X2_"></span>Bit 1 (0x2)  
Causes the display to include memory management thread stacks.

<span id="Bit_2__0x4_"></span><span id="bit_2__0x4_"></span><span id="BIT_2__0X4_"></span>Bit 2 (0x4)  
(Windows XP and later) Causes the display to include terminal server memory usage.

<span id="Bit_3__0x8_"></span><span id="bit_3__0x8_"></span><span id="BIT_3__0X8_"></span>Bit 3 (0x8)  
(Windows XP and later) Causes the display to include the page file write log.

<span id="Bit_4__0x10_"></span><span id="bit_4__0x10_"></span><span id="BIT_4__0X10_"></span>Bit 4 (0x10)  
(Windows XP and later) Causes the display to include working set owner thread stacks.

<span id="Bit_5__0x20_"></span><span id="bit_5__0x20_"></span><span id="BIT_5__0X20_"></span>Bit 5 (0x20)  
(Windows Vista and later) Causes the display to include kernel virtual address usage.

### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

|       |                  |
|-------|------------------|
| Modes | kernel mode only |

 

### <span id="DLL"></span><span id="dll"></span>DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Windows 2000</strong></p></td>
<td align="left"><p>Kdextx86.dll</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Windows XP and later</strong></p></td>
<td align="left"><p>Kdexts.dll</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

The [**!memusage**](-memusage.md) extension command can be used to analyze physical memory usage. For more information about memory management, see *Microsoft Windows Internals*, by Mark Russinovich and David Solomon. (These resources may not be available in some languages and countries.)

Remarks
-------

Here is an example of the short output produced when *Flags* is 1:

```dbgcmd
kd> !vm 1

*** Virtual Memory Usage ***
      Physical Memory:     16270   (   65080 Kb)
      Page File: \??\E:\pagefile.sys
         Current:     98304Kb Free Space:     61044Kb
 Minimum:     98304Kb Maximum:       196608Kb
      Available Pages:      5543   (   22172 Kb)
      ResAvail Pages:       6759   (   27036 Kb)
      Locked IO Pages:       112   (     448 Kb)
 Free System PTEs:    45089   (  180356 Kb)
      Free NP PTEs:         5145   (   20580 Kb)
      Free Special NP:       336   (    1344 Kb)
      Modified Pages:        714   (    2856 Kb)
      NonPagedPool Usage:    877   (    3508 Kb)
      NonPagedPool Max:     6252   (   25008 Kb)
      PagedPool 0 Usage:     729   (    2916 Kb)
      PagedPool 1 Usage:     432   (    1728 Kb)
      PagedPool 2 Usage:     436   (    1744 Kb)
      PagedPool Usage:      1597   (    6388 Kb)
      PagedPool Maximum:   13312   (   53248 Kb)
      Shared Commit:        1097   (    4388 Kb)
      Special Pool:          229   (     916 Kb)
      Shared Process:       1956   (    7824 Kb)
      PagedPool Commit:     1597   (    6388 Kb)
      Driver Commit:         828   (    3312 Kb)
      Committed pages:     21949   (   87796 Kb)
      Commit limit:        36256   (  145024 Kb)
```

All memory use is listed in pages and in kilobytes. The most useful information in this display is the following:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Parameter</th>
<th align="left">Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>physical memory</strong></p></td>
<td align="left"><p>Total physical memory in the system.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>available pages</strong></p></td>
<td align="left"><p>Number of pages of memory available on the system, both virtual and physical.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>nonpaged pool usage</strong></p></td>
<td align="left"><p>The amount of pages allocated to the nonpaged pool. The nonpaged pool is memory that cannot be swapped out to the paging file, so it must always occupy physical memory. If this number is too large, this is usually an indication that there is a memory leak somewhere in the system.</p></td>
</tr>
</tbody>
</table>

 

 

 





