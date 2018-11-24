---
title: Dividing a Memory-Space Segment into Banks
description: Dividing a Memory-Space Segment into Banks
ms.assetid: 7fdbe511-ae92-44c2-9651-51b3ead11425
keywords:
- memory segments WDK display , banks
- banked memory WDK display
- banks WDK display
- linear memory-space segments WDK display
- memory segments WDK display , linear memory-space segments
- dividing linear memory-space segments WDK display
- memory-space segments WDK display
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Dividing a Memory-Space Segment into Banks


## <span id="ddk_dividing_a_memory_space_segment_into_banks_gg"></span><span id="DDK_DIVIDING_A_MEMORY_SPACE_SEGMENT_INTO_BANKS_GG"></span>


The display miniport driver can provide fine-grained hints to the video memory manager about the optimal placement for allocations of video resources within a [linear memory-space segment](linear-memory-space-segments.md) by dividing the segment into banked memory (banks). If the driver divides the linear memory-space segment into banks, the driver must set the **UseBanking** bit-field flag in the **Flags** member of the [**DXGK\_SEGMENTDESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff562035) structure for the segment. The driver returns hints about banked memory in the **HintedBank** member of [**DXGK\_ALLOCATIONINFO**](https://msdn.microsoft.com/library/windows/hardware/ff560960) structures for allocations when the video memory manager calls the driver's [**DxgkDdiCreateAllocation**](https://msdn.microsoft.com/library/windows/hardware/ff559606) function. For more information, see [Specifying Segments When Creating Allocations](specifying-segments-when-creating-allocations.md).

While an allocation must be entirely contained within a segment, the allocation can cross the boundaries of banks within a segment.

If banks are used, the driver must cover the entire address space of the segment with banks. The first bank always starts at offset zero within the segment and the last bank always ends at the end of the segment. Banks are contiguous and have no free space between them.

 

 





