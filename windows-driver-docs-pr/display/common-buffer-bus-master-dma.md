---
title: Common-Buffer Bus-Master DMA
description: Common-Buffer Bus-Master DMA
ms.assetid: 4758e084-1d9e-4e17-8627-05edc6b664ba
keywords:
- bus-master DMA WDK video miniport , common buffer
- DMA bus-master WDK video miniport , common buffer
- common-buffer DMA WDK video miniport , description
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Common-Buffer Bus-Master DMA


## <span id="ddk_common_buffer_bus_master_dma_gg"></span><span id="DDK_COMMON_BUFFER_BUS_MASTER_DMA_GG"></span>


The miniport driver performs the following sequence of operations to use common-buffer DMA:

1.  Get an adapter object.

    The miniport driver calls the video port driver's [**VideoPortGetDmaAdapter**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/video/nf-video-videoportgetdmaadapter) function, usually within the miniport driver's [*HwVidFindAdapter*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/video/nc-video-pvideo_hw_find_adapter) routine, to get a pointer to a [**VP\_DMA\_ADAPTER**](https://docs.microsoft.com/previous-versions/ff570570(v=vs.85)) structure. The miniport driver uses this pointer for subsequent DMA operations.

2.  Allocate a common buffer.

    The miniport driver calls the video port driver's [**VideoPortAllocateCommonBuffer**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/video/nf-video-videoportallocatecommonbuffer) function, using the pointer obtained in the previous step.

3.  Release the common buffer.

    When the miniport driver no longer requires the common buffer, it calls the video port driver's [**VideoPortReleaseCommonBuffer**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/video/nf-video-videoportreleasecommonbuffer) function.

4.  Discard the adapter object.

    This step is optional. If, for some reason, the miniport driver decides that there will be no further DMA operations for the rest of its lifetime, it should discard the DMA adapter object by calling the video port driver's [**VideoPortPutDmaAdapter**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/video/nf-video-videoportputdmaadapter) function.

 

 





