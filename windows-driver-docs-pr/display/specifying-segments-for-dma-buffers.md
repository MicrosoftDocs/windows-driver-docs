---
title: Specifying Segments for DMA Buffers
description: Specifying Segments for DMA Buffers
ms.assetid: 7cd51f22-bf9b-4c45-98f0-e9e0d41dab96
keywords:
- memory segments WDK display , DMA buffers
- DMA buffers WDK display , memory segments
- buffers WDK display
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Specifying Segments for DMA Buffers


## <span id="ddk_specifying_segments_for_dma_buffers_gg"></span><span id="DDK_SPECIFYING_SEGMENTS_FOR_DMA_BUFFERS_GG"></span>


The display miniport driver can specify aperture segments from which DMA buffers can be allocated. DMA buffers can also be allocated as contiguous locked-down system memory.

The video memory manager allocates and destroys DMA buffers when applications require them. Therefore, the video memory manager requires a set of segments from which it can allocate DMA buffers. Note that the segment set might consist of only one segment.

When the Microsoft DirectX graphics kernel subsystem calls the display miniport driver's [**DxgkDdiCreateDevice**](https://msdn.microsoft.com/library/windows/hardware/ff559615) function to create a graphics context device, the display miniport driver can specify a segment set from which the video memory manager can allocate DMA buffers. If the display miniport driver sets the **DmaBufferSegmentSet** member of the [**DXGK\_DEVICEINFO**](https://msdn.microsoft.com/library/windows/hardware/ff561047) structure to 0, then the video memory manager will allocate contiguous nonpaged memory for DMA buffers; in this case, the display miniport driver must access the memory by using PCI cycles, and through DMA, must send data directly from the memory's physical address. If the display miniport driver sets **DmaBufferSegmentSet** to nonzero, then the video memory manager will allocate pageable memory and will map the pages to the specified aperture segments. The pages within the aperture segments are revealed to the display miniport driver in a call to its [**DxgkDdiSubmitCommand**](https://msdn.microsoft.com/library/windows/hardware/ff560790) function.

Note that the basic video memory manager model does not support DMA buffers in local video memory.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Specifying%20Segments%20for%20DMA%20Buffers%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




