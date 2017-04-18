---
title: Dividing a Memory-Space Segment into Banks
description: Dividing a Memory-Space Segment into Banks
ms.assetid: 7fdbe511-ae92-44c2-9651-51b3ead11425
keywords: ["memory segments WDK display , banks", "banked memory WDK display", "banks WDK display", "linear memory-space segments WDK display", "memory segments WDK display , linear memory-space segments", "dividing linear memory-space segments WDK display", "memory-space segments WDK display"]
---

# Dividing a Memory-Space Segment into Banks


## <span id="ddk_dividing_a_memory_space_segment_into_banks_gg"></span><span id="DDK_DIVIDING_A_MEMORY_SPACE_SEGMENT_INTO_BANKS_GG"></span>


The display miniport driver can provide fine-grained hints to the video memory manager about the optimal placement for allocations of video resources within a [linear memory-space segment](linear-memory-space-segments.md) by dividing the segment into banked memory (banks). If the driver divides the linear memory-space segment into banks, the driver must set the **UseBanking** bit-field flag in the **Flags** member of the [**DXGK\_SEGMENTDESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff562035) structure for the segment. The driver returns hints about banked memory in the **HintedBank** member of [**DXGK\_ALLOCATIONINFO**](https://msdn.microsoft.com/library/windows/hardware/ff560960) structures for allocations when the video memory manager calls the driver's [**DxgkDdiCreateAllocation**](https://msdn.microsoft.com/library/windows/hardware/ff559606) function. For more information, see [Specifying Segments When Creating Allocations](specifying-segments-when-creating-allocations.md).

While an allocation must be entirely contained within a segment, the allocation can cross the boundaries of banks within a segment.

If banks are used, the driver must cover the entire address space of the segment with banks. The first bank always starts at offset zero within the segment and the last bank always ends at the end of the segment. Banks are contiguous and have no free space between them.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Dividing%20a%20Memory-Space%20Segment%20into%20Banks%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




