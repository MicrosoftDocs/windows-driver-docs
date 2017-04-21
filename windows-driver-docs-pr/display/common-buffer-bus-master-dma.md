---
title: Common-Buffer Bus-Master DMA
description: Common-Buffer Bus-Master DMA
ms.assetid: 4758e084-1d9e-4e17-8627-05edc6b664ba
keywords:
- bus-master DMA WDK video miniport , common buffer
- DMA bus-master WDK video miniport , common buffer
- common-buffer DMA WDK video miniport , description
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Common-Buffer Bus-Master DMA


## <span id="ddk_common_buffer_bus_master_dma_gg"></span><span id="DDK_COMMON_BUFFER_BUS_MASTER_DMA_GG"></span>


The miniport driver performs the following sequence of operations to use common-buffer DMA:

1.  Get an adapter object.

    The miniport driver calls the video port driver's [**VideoPortGetDmaAdapter**](https://msdn.microsoft.com/library/windows/hardware/ff570312) function, usually within the miniport driver's [*HwVidFindAdapter*](https://msdn.microsoft.com/library/windows/hardware/ff567332) routine, to get a pointer to a [**VP\_DMA\_ADAPTER**](https://msdn.microsoft.com/library/windows/hardware/ff570570) structure. The miniport driver uses this pointer for subsequent DMA operations.

2.  Allocate a common buffer.

    The miniport driver calls the video port driver's [**VideoPortAllocateCommonBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff570178) function, using the pointer obtained in the previous step.

3.  Release the common buffer.

    When the miniport driver no longer requires the common buffer, it calls the video port driver's [**VideoPortReleaseCommonBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff570355) function.

4.  Discard the adapter object.

    This step is optional. If, for some reason, the miniport driver decides that there will be no further DMA operations for the rest of its lifetime, it should discard the DMA adapter object by calling the video port driver's [**VideoPortPutDmaAdapter**](https://msdn.microsoft.com/library/windows/hardware/ff570335) function.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Common-Buffer%20Bus-Master%20DMA%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




