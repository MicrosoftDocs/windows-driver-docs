---
title: Specifying Segments for DMA Buffers
description: Specifying Segments for DMA Buffers
keywords:
- memory segments WDK display , DMA buffers
- DMA buffers WDK display , memory segments
- buffers WDK display
ms.date: 04/20/2017
---

# Specifying Segments for DMA Buffers


## <span id="ddk_specifying_segments_for_dma_buffers_gg"></span><span id="DDK_SPECIFYING_SEGMENTS_FOR_DMA_BUFFERS_GG"></span>


The display miniport driver can specify aperture segments from which DMA buffers can be allocated. DMA buffers can also be allocated as contiguous locked-down system memory.

The video memory manager allocates and destroys DMA buffers when applications require them. Therefore, the video memory manager requires a set of segments from which it can allocate DMA buffers. Note that the segment set might consist of only one segment.

When the Microsoft DirectX graphics kernel subsystem calls the display miniport driver's [**DxgkDdiCreateDevice**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_createdevice) function to create a graphics context device, the display miniport driver can specify a segment set from which the video memory manager can allocate DMA buffers. If the display miniport driver sets the **DmaBufferSegmentSet** member of the [**DXGK\_DEVICEINFO**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_deviceinfo) structure to 0, then the video memory manager will allocate contiguous nonpaged memory for DMA buffers; in this case, the display miniport driver must access the memory by using PCI cycles, and through DMA, must send data directly from the memory's physical address. If the display miniport driver sets **DmaBufferSegmentSet** to nonzero, then the video memory manager will allocate pageable memory and will map the pages to the specified aperture segments. The pages within the aperture segments are revealed to the display miniport driver in a call to its [**DxgkDdiSubmitCommand**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_submitcommand) function.

Note that the basic video memory manager model does not support DMA buffers in local video memory.

 

