---
title: Packet-Based Bus-Master DMA
description: Packet-Based Bus-Master DMA
ms.assetid: f94b9ca9-6e29-4801-a092-30af19345f6d
keywords:
- bus-master DMA WDK video miniport , packet based
- DMA bus-master WDK video miniport , packet based
- packet-based DMA WDK video miniport , description
- VideoPortStartDma
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Packet-Based Bus-Master DMA


## <span id="ddk_packet_based_bus_master_dma_gg"></span><span id="DDK_PACKET_BASED_BUS_MASTER_DMA_GG"></span>


Ordinarily, a display driver initiates a DMA operation by sending a transfer request to the miniport driver. When a miniport driver supporting packet-based DMA operations receives such a request, it first locks the buffer involved in the data transfer. The miniport driver then initiates the transfer by calling the video port driver's [**VideoPortStartDma**](https://msdn.microsoft.com/library/windows/hardware/ff570369) function, which in turn calls the miniport driver's [**HwVidExecuteDma**](https://msdn.microsoft.com/library/windows/hardware/ff567330) callback routine to carry out the data transfer. This DMA operation is handled asynchronously: **VideoPortStartDma** does not wait for the DMA operation to complete before returning control to the miniport driver.

Depending on the size of the transfer request and the number of system resources assigned to the adapter, the driver may not be able to transfer all of the data in a single DMA operation. The miniport driver should inspect the actual transfer size returned in order to find out whether there is more data to be transferred. As soon as the DMA hardware finishes the current transfer, the miniport driver should call the video port driver's [**VideoPortCompleteDma**](https://msdn.microsoft.com/library/windows/hardware/ff570286) function to complete the current DMA operation. If there is still data remaining to be transferred, the miniport driver repeats the process of calling the video port driver's **VideoPortStartDma** and **VideoPortCompleteDma** functions iteratively until no more data remains to be transferred. When all of the data has been transferred, the miniport driver should unlock the buffer.

The miniport driver performs the following sequence of operations to use packet-based DMA:

1.  Report hardware capabilities to the system and acquire an adapter object.

    The miniport driver calls the video port driver's [**VideoPortGetDmaAdapter**](https://msdn.microsoft.com/library/windows/hardware/ff570312) function, which returns a pointer to a [**VP\_DMA\_ADAPTER**](https://msdn.microsoft.com/library/windows/hardware/ff570570) structure. This is usually done at initialization time, typically within the miniport driver's [*HwVidFindAdapter*](https://msdn.microsoft.com/library/windows/hardware/ff567332) routine. The miniport driver uses this pointer for subsequent DMA operations.

2.  Lock host memory.

    The miniport driver calls the video port driver's [**VideoPortLockBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff570326) function, which probes the buffer, makes those memory pages resident, and locks them.

3.  Start the DMA transfer.

    The miniport driver calls the video port driver's [**VideoPortStartDma**](https://msdn.microsoft.com/library/windows/hardware/ff570369) function, which flushes the host processor memory caches, builds the scatter/gather list, and calls the miniport driver's [**HwVidExecuteDma**](https://msdn.microsoft.com/library/windows/hardware/ff567330) callback routine to carry out the DMA operation asynchronously. **VideoPortStartDma** returns control to the miniport driver without waiting for the DMA operation to complete.

4.  Complete the DMA transfer.

    The miniport driver should call the video port driver's [**VideoPortCompleteDma**](https://msdn.microsoft.com/library/windows/hardware/ff570286) function as soon as the hardware finishes the DMA operation. Many video adapters generate an interrupt when a DMA operation is complete. For example, a system with this type of adapter could react to the interrupt in the following way. When the hardware generates the interrupt to notify the miniport driver that the DMA operation has completed, the miniport driver's interrupt service routine (ISR) calls the video port driver's [**VideoPortQueueDpc**](https://msdn.microsoft.com/library/windows/hardware/ff570339) function to queue a DPC routine, which in turn calls the video port driver's **VideoPortCompleteDma** function. The ISR cannot directly call **VideoPortCompleteDma** since this video port driver function must be called at or below IRQL DISPATCH\_LEVEL.

    **VideoPortCompleteDma** flushes any data remaining in the bus-master adapter's internal cache, and frees any unused resources (including the scatter/gather list built by **VideoPortStartDma**).

    If only part of the data has been transferred (due to limitations on the number of available map registers, for example), the miniport driver must make repeated calls to **VideoPortStartDma** and **VideoPortCompleteDma** until all of the data has been transferred.

5.  Unlock host memory.

    When all of the data has been transferred, the miniport driver should call the video port driver's [**VideoPortUnlockBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff570373) function to unlock the data buffer it acquired in the second step.

6.  Discard the adapter object.

    *This step is optional*. If, for some reason, the miniport driver decides that there will be no further DMA operations for the rest of its lifetime, it should discard the DMA adapter object by calling the video port driver's [**VideoPortPutDmaAdapter**](https://msdn.microsoft.com/library/windows/hardware/ff570335) function.

 

 





