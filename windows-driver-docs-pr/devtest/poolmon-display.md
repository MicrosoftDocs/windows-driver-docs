---
title: PoolMon Display
description: PoolMon Display
ms.assetid: 1dee4331-a508-4e7f-b621-4d22f6572aec
keywords:
- PoolMon WDK , displays
- Memory Pool Monitor WDK , displays
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# PoolMon Display


## <span id="ddk_poolmon_display_tools"></span><span id="DDK_POOLMON_DISPLAY_TOOLS"></span>


PoolMon displays columns of data about pool memory allocations in a command window. Use the arrow keys, PAGE UP, and PAGE DOWN keys to scroll through the data.

**Note**  To see the entire PoolMon display, the Command Prompt window size must be at least 80 characters wide (width=80) and at least 53 rows high (height=53); and the Command Prompt window buffer must be at least 500 characters wide (width=500) and at least 2000 rows high (height=2000). Otherwise, the display might be truncated.

 

The following table describes the columns in the PoolMon display.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Column Name</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Tag</strong></p></td>
<td align="left"><p>The 4-byte tag assigned to the pool allocation.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Type</strong></p></td>
<td align="left"><p>Whether the memory allocations are in paged or nonpaged bytes.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Allocs</strong></p></td>
<td align="left"><p>The number of allocations.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>( )</strong></p></td>
<td align="left"><p>The change in the number of allocations since the last update.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Frees</strong></p></td>
<td align="left"><p>The number of free operations.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>( )</strong></p></td>
<td align="left"><p>The change in the number of allocations since the last update.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Diff</strong></p></td>
<td align="left"><p>The number of allocations minus the number of free operations.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Bytes</strong></p></td>
<td align="left"><p>The size of the allocations, in bytes used.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>( )</strong></p></td>
<td align="left"><p>The change in the allocation size since the last update.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Per Alloc</strong></p></td>
<td align="left"><p>The value of Bytes divided by the value of Diff.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Mapped_Driver</strong></p></td>
<td align="left"><p>The local drivers (<strong>/c</strong>) and other commonly used drivers and system components (<strong>/g</strong>) that assign the pool tag value. This column appears only when you use the <strong>/c</strong> or <strong>/g</strong> parameters.</p></td>
</tr>
</tbody>
</table>

 

The following sample PoolMon output is sorted by number of allocations. (To sort your display this way, start PoolMon with the **/a** parameter.)

```
 Memory:  260620K Avail:   96364K  PageFlts:     0   InRam Krnl: 1916K P:17856K
 Commit: 203500K Limit: 640916K Peak: 260632K            Pool N: 8332K P:27220K
 System pool information
 Tag  Type     Allocs            Frees            Diff   Bytes       Per Alloc

 Wait Nonp    3971107 (   0)   3971077 (   0)       30    8456 (     0)    281
 ObSt Nonp    2791258 (   0)   2791258 (   0)        0       0 (     0)      0
 Gxlt Paged   1161638 (   0)   1161630 (   0)        8     864 (     0)    108
 Ustm Paged   1088342 (   0)   1088298 (   0)       44    2464 (     0)     56
 Io   Nonp    1021112 (   1)   1020985 (   1)      127   91912 (     0)    723
 ObSq Paged    967615 (   0)    967615 (   0)        0       0 (     0)      0
 Key  Paged    954821 (   0)    953979 (   0)      842   87528 (     0)    103
 SePa Nonp     680348 (   0)    680321 (   0)       27    3656 (     0)    135
```

### <span id="Update_Rate"></span><span id="update_rate"></span><span id="UPDATE_RATE"></span>Update Rate

PoolMon updates its display every five seconds. You cannot change the update rate.

### <span id="Accumulated_Values"></span><span id="accumulated_values"></span><span id="ACCUMULATED_VALUES"></span>Accumulated Values

The data that PoolMon displays is collected and calculated by Windows whenever pool tagging is enabled. The values for allocations, free operations, and bytes used accumulate from the time that Windows starts, and increase monotonically until Windows is restarted. If a driver or component is started after Windows has already started, the values are accumulated from the last time that the driver or component started and reset only when the driver or system is restarted.

### <span id="Interpreting_Tag_Values"></span><span id="interpreting_tag_values"></span><span id="INTERPRETING_TAG_VALUES"></span>Interpreting Tag Values

All pool memory allocations have tags, but they do not all have characteristic tag values. Pool memory allocations have characteristic tag values when the driver that allocates the memory sets the tag value by using [**ExAllocatePoolWithTag**](https://msdn.microsoft.com/library/windows/hardware/ff544520) or [**ExAllocatePoolWithQuotaTag**](https://msdn.microsoft.com/library/windows/hardware/ff544513). If the driver does not assign a tag value ([**ExAllocatePool**](https://msdn.microsoft.com/library/windows/hardware/ff544501), [**ExAllocatePoolWithQuota**](https://msdn.microsoft.com/library/windows/hardware/ff544506)), Windows still creates a tag, but it assigns the default tag value None. As a result, you cannot distinguish the statistics for that driver's allocations from that of other pool allocations.

 

 





