---
title: Using PoolMon to Find a Kernel-Mode Memory Leak
description: Using PoolMon to Find a Kernel-Mode Memory Leak
ms.assetid: 383b5d9a-3e99-4dc5-bce9-bd44f2ef1dc0
keywords: ["memory leak, kernel-mode, PoolMon", "PoolMon", "PoolMon, finding a memory leak"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Using PoolMon to Find a Kernel-Mode Memory Leak


If you suspect there is a kernel-mode memory leak, the easiest way to determine which pool tag is associated with the leak is to use the PoolMon tool.

PoolMon (Poolmon.exe) monitors pool memory usage by pool tag name. This tool is included in the Windows Driver Kit (WDK). For a full description, see [PoolMon](https://go.microsoft.com/fwlink/p/?linkid=122776) in the WDK documentation.

### <span id="enable_pool_tagging__windows_2000_and_windows_xp_"></span><span id="ENABLE_POOL_TAGGING__WINDOWS_2000_AND_WINDOWS_XP_"></span>Enable Pool Tagging (Windows 2000 and Windows XP)

On Windows 2000 and Windows XP you must first use GFlags to enable pool tagging. GFlags is included in Debugging Tools for Windows. Start GFlags, choose the **System Registry** tab, check the **Enable Pool Tagging** box, and then click **Apply**. You must restart Windows for this setting to take effect. For more details, see [GFlags](gflags.md).

On Windows Server 2003 and later versions of Windows, pool tagging is always enabled.

### <span id="using_poolmon"></span><span id="USING_POOLMON"></span>Using PoolMon

The PoolMon header displays the total paged and non-paged pool bytes. The columns show pool use for each pool tag. The display is updated automatically every few seconds. For example:

```dbgcmd
Memory: 16224K Avail: 4564K PageFlts: 31 InRam Krnl: 684K P: 680K
Commit: 24140K Limit: 24952K Peak: 24932K Pool N: 744K P: 2180K

## Tag   Type  Allocs       Frees        Diff    Bytes       Per Alloc


CM    Paged   1283  ( 0)  1002  ( 0)   281  1377312   ( 0)  4901
Strg  Paged  10385 ( 10)  6658  ( 4)  3727   317952 ( 512)    85
Fat   Paged   6662  ( 8)  4971  ( 6)  1691   174560 ( 128)   103
MmSt  Paged    614  ( 0)   441  ( 0)   173    83456   ( 0)   482 
```

PoolMon has command keys that sort the output according to various criteria. Press the letter associated with each command in order to re-sort the data. It takes a few seconds for each command to work.

The sort commands include:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Command Key</th>
<th align="left">Operation</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>P</strong></p></td>
<td align="left"><p>Limits the tags shown to nonpaged pool, paged pool, or both. Repeatedly pressing <strong>P</strong> cycles through each of these options, in that order.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>B</strong></p></td>
<td align="left"><p>Sorts tags by maximum byte usage.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>M</strong></p></td>
<td align="left"><p>Sorts tags by maximum byte allocations.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>T</strong></p></td>
<td align="left"><p>Sorts tags alphabetically by tag name.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>E</strong></p></td>
<td align="left"><p>Causes the display to include the paged and non-paged totals across the bottom.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>A</strong></p></td>
<td align="left"><p>Sorts tags by allocation size.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>F</strong></p></td>
<td align="left"><p>Sorts tags by free operations.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>S</strong></p></td>
<td align="left"><p>Sorts tags by the difference between allocations and frees.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Q</strong></p></td>
<td align="left"><p>Quits PoolMon.</p></td>
</tr>
</tbody>
</table>

 

### <span id="using_the_poolmon_utility_to_find_a_memory_leak"></span><span id="USING_THE_POOLMON_UTILITY_TO_FIND_A_MEMORY_LEAK"></span>Using the PoolMon Utility to Find a Memory Leak

To find a memory leak with the PoolMon utility, follow this procedure:

1.  Start PoolMon.

2.  If you have determined that the leak is occurring in non-paged pool, press **P** once; if you have determined that it is occurring in paged pool, press **P** twice. If you do not know, do not press **P** and both kinds of pool are included.

3.  Press **B** to sort the display by maximum byte use.

4.  Start your test. Take a screen shot and copy it to Notepad.

5.  Take a new screen shot every half hour. By comparing screen shots, determine which tag's bytes are increasing.

6.  Stop your test and wait a few hours. How much of the tag was freed up in this time?

Typically, after an application reaches a stable running state, it allocates memory and free memory at roughly the same rate. If it tends to allocate memory faster than it frees it, its memory use will grow over time. This often indicates a memory leak.

### <span id="addressing_the_leak"></span><span id="ADDRESSING_THE_LEAK"></span>Addressing the Leak

After you have determined which pool tag is associated with the leak, this might reveal all you need to know about the leak. If you need to determine which specific instance of the allocation routine is causing the leak, see [Using the Kernel Debugger to Find Kernel-Mode Memory Leaks](using-the-kernel-debugger-to-find-a-kernel-mode-memory-leak.md).

 

 





