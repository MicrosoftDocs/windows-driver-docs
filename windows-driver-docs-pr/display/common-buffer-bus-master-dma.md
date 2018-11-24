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

    The miniport driver calls the video port driver's [**VideoPortGetDmaAdapter**](https://msdn.microsoft.com/library/windows/hardware/ff570312) function, usually within the miniport driver's [*HwVidFindAdapter*](https://msdn.microsoft.com/library/windows/hardware/ff567332) routine, to get a pointer to a [**VP\_DMA\_ADAPTER**](https://msdn.microsoft.com/library/windows/hardware/ff570570) structure. The miniport driver uses this pointer for subsequent DMA operations.

2.  Allocate a common buffer.

    The miniport driver calls the video port driver's [**VideoPortAllocateCommonBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff570178) function, using the pointer obtained in the previous step.

3.  Release the common buffer.

    When the miniport driver no longer requires the common buffer, it calls the video port driver's [**VideoPortReleaseCommonBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff570355) function.

4.  Discard the adapter object.

    This step is optional. If, for some reason, the miniport driver decides that there will be no further DMA operations for the rest of its lifetime, it should discard the DMA adapter object by calling the video port driver's [**VideoPortPutDmaAdapter**](https://msdn.microsoft.com/library/windows/hardware/ff570335) function.

 

 





