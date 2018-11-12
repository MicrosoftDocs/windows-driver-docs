---
title: Initializing Use of Memory Segments
description: Initializing Use of Memory Segments
ms.assetid: 8e4cf1dc-c428-4564-9a16-925e17e6d488
keywords:
- memory segments WDK display , initializing
- GPU address space WDK display
- paging buffers WDK display
- segments WDK display
- address space WDK display
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Initializing Use of Memory Segments


## <span id="ddk_initializing_use_of_memory_segments_gg"></span><span id="DDK_INITIALIZING_USE_OF_MEMORY_SEGMENTS_GG"></span>


Memory segments, in the context of the display driver model for Windows Vista and later (WDDM), describe the graphics processing unit's (GPU) address space to the video memory manager. Memory segments generalize and virtualize video memory resources. Memory segments are configured according to the memory types that the hardware supports (for example, frame buffer memory or system memory aperture).

To initialize how it uses memory segments, the Microsoft DirectX graphics kernel subsystem (Dxgkrnl.sys) calls the display miniport driver's [*DxgkDdiQueryAdapterInfo*](https://msdn.microsoft.com/library/windows/hardware/ff559746) function. To direct the display miniport driver to return information about memory segments from the *DxgkDdiQueryAdapterInfo* call, the graphics subsystem specifies either the **DXGKQAITYPE\_QUERYSEGMENT** or the **DXGKQAITYPE\_QUERYSEGMENT3** value in the **Type** member of the [**DXGKARG\_QUERYADAPTERINFO**](https://msdn.microsoft.com/library/windows/hardware/ff557621) structure.

The graphics subsystem calls the display miniport driver's [*DxgkDdiQueryAdapterInfo*](https://msdn.microsoft.com/library/windows/hardware/ff559746) function twice for segment information. The first call to *DxgkDdiQueryAdapterInfo* retrieves the number of segments supported by the driver, and the second call retrieves detailed information about each segment. In the calls to *DxgkDdiQueryAdapterInfo*, the driver points the **pOutputData** member of [**DXGKARG\_QUERYADAPTERINFO**](https://msdn.microsoft.com/library/windows/hardware/ff557621) to populated [**DXGK\_QUERYSEGMENTOUT**](https://msdn.microsoft.com/library/windows/hardware/ff562018) structures (for a driver version prior to Windows Display Driver Model (WDDM) 1.2) or to populated [**DXGK\_QUERYSEGMENTOUT3**](https://msdn.microsoft.com/library/windows/hardware/hh464082) structures (for a WDDM 1.2 and later driver).

In the first call, the **pSegmentDescriptor** member of [**DXGK\_QUERYSEGMENTOUT**](https://msdn.microsoft.com/library/windows/hardware/ff562018) (for a driver version prior to WDDM 1.2) or [**DXGK\_QUERYSEGMENTOUT3**](https://msdn.microsoft.com/library/windows/hardware/hh464082) (for a WDDM 1.2 and later driver) is set to **NULL**. The driver should fill only the **NbSegment** member of **DXGK\_QUERYSEGMENTOUT** or **DXGK\_QUERYSEGMENTOUT3** with the number of segment types that it supports. This number also indicates the number of unpopulated [**DXGK\_SEGMENTDESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff562035) (for a driver version prior to WDDM 1.2) or [**DXGK\_SEGMENTDESCRIPTOR3**](https://msdn.microsoft.com/library/windows/hardware/hh464086) (for a WDDM 1.2 and later driver) structures that the driver requires from the second call to [*DxgkDdiQueryAdapterInfo*](https://msdn.microsoft.com/library/windows/hardware/ff559746).

In the second call, the driver should fill all members of [**DXGK\_QUERYSEGMENTOUT**](https://msdn.microsoft.com/library/windows/hardware/ff562018) or [**DXGK\_QUERYSEGMENTOUT3**](https://msdn.microsoft.com/library/windows/hardware/hh464082). In the second call, the driver should populate an array the size of **NbSegment** of [**DXGK\_SEGMENTDESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff562035) or [**DXGK\_SEGMENTDESCRIPTOR3**](https://msdn.microsoft.com/library/windows/hardware/hh464086) structures in the **pSegmentDescriptor** member of **DXGK\_QUERYSEGMENTOUT** or **DXGK\_QUERYSEGMENTOUT3** with information about the segments that the driver supports.

In both calls to [*DxgkDdiQueryAdapterInfo*](https://msdn.microsoft.com/library/windows/hardware/ff559746), the **pInputData** member of [**DXGKARG\_QUERYADAPTERINFO**](https://msdn.microsoft.com/library/windows/hardware/ff557621) points to a [**DXGK\_QUERYSEGMENTIN**](https://msdn.microsoft.com/library/windows/hardware/ff562015) structure that contains information about the location and properties of the AGP aperture. If no AGP aperture is available, or if one is present but no appropriate GART driver is installed, the information about the AGP aperture is set to zero. If no AGP aperture is present, the display miniport driver should not indicate, in the **pSegmentDescriptor** array of [**DXGK\_QUERYSEGMENTOUT**](https://msdn.microsoft.com/library/windows/hardware/ff562018) or [**DXGK\_QUERYSEGMENTOUT3**](https://msdn.microsoft.com/library/windows/hardware/hh464082), that it supports an AGP-type aperture segment. If an AGP-type aperture segment is indicated in such circumstances, the adapter fails to initialize.

During initialization, because memory is plentiful, memory for the paging buffer can be allocated from a specific segment. The video memory manager allocates memory for the paging buffer from the segment specified in the **PagingBufferSegmentId** member of [**DXGK\_QUERYSEGMENTOUT**](https://msdn.microsoft.com/library/windows/hardware/ff562018) or [**DXGK\_QUERYSEGMENTOUT3**](https://msdn.microsoft.com/library/windows/hardware/hh464082). The driver indicates the identifier of the paging-buffer segment in the second call to [*DxgkDdiQueryAdapterInfo*](https://msdn.microsoft.com/library/windows/hardware/ff559746). The driver should also specify the size in bytes that should be allocated for the paging buffer in the **PagingBufferSize** member of **DXGK\_QUERYSEGMENTOUT** or **DXGK\_QUERYSEGMENTOUT3**.

For more information about memory segments and working with paging buffers, see [Handling Memory Segments](handling-memory-segments.md) and [Paging Video Memory Resources](paging-video-memory-resources.md).

 

 





