---
title: PoolMon Display
description: PoolMon Display
keywords:
- PoolMon WDK , displays
- Memory Pool Monitor WDK , displays
ms.date: 04/20/2017
---

# PoolMon Display

PoolMon displays columns of data about pool memory allocations in a command window. Use the arrow keys, PAGE UP, and PAGE DOWN keys to scroll through the data.

>[!NOTE]
>To see the entire PoolMon display, the Command Prompt window size must be at least 80 characters wide (width=80) and at least 53 rows high (height=53); and the Command Prompt window buffer must be at least 500 characters wide (width=500) and at least 2000 rows high (height=2000). Otherwise, the display might be truncated.

The following table describes the columns in the PoolMon display.

|Column Name|Description|
|----|----|
|**Tag**|The 4-byte tag assigned to the pool allocation.|
|**Type**|Whether the memory allocations are in paged or nonpaged bytes.|
|**Allocs**|The number of allocations.|
|**( )**|The change in the number of allocations since the last update.|
|**Frees**|The number of free operations.|
|**( )**|The change in the number of allocations since the last update.|
|**Diff**|The number of allocations minus the number of free operations.|
|**Bytes**|The size of the allocations, in bytes used.|
|**( )**|The change in the allocation size since the last update.|
|**Per Alloc**|The value of Bytes divided by the value of Diff.|
|**Mapped_Driver**|The local drivers (**/c**) and other commonly used drivers and system components (**/g**) that assign the pool tag value. This column appears only when you use the **/c** or **/g** parameters.|

The following sample PoolMon output is sorted by number of allocations. (To sort your display this way, start PoolMon with the **/a** parameter.)

```command
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

## Update Rate

PoolMon updates its display every five seconds. You cannot programmatically change the update rate. You can, however, force a refresh of the PoolMon results by clicking some keys, if the window PoolMon is running in has focus. **CTRL** and **ALT**, for instance, force a refresh; however, **Print screen** does not.

## Accumulated Values

The data that PoolMon displays is collected and calculated by Windows whenever pool tagging is enabled. The values for allocations, free operations, and bytes used accumulate from the time that Windows starts, and increase monotonically until Windows is restarted. If a driver or component is started after Windows has already started, the values are accumulated from the last time that the driver or component started and reset only when the driver or system is restarted.

## Interpreting Tag Values

All pool memory allocations have tags, but they do not all have characteristic tag values. Pool memory allocations have characteristic tag values when the driver that allocates the memory sets the tag value by using [**ExAllocatePoolWithTag**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exallocatepoolwithtag) or [**ExAllocatePoolWithQuotaTag**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exallocatepoolwithquotatag). If the driver does not assign a tag value ([**ExAllocatePool**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exallocatepool), [**ExAllocatePoolWithQuota**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exallocatepoolwithquota)), Windows still creates a tag, but it assigns the default tag value None. As a result, you cannot distinguish the statistics for that driver's allocations from that of other pool allocations.
