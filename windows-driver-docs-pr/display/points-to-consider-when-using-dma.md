---
title: Points to Consider When Using DMA
description: Points to Consider When Using DMA
ms.assetid: 7bbd11d2-858c-4ed6-81a4-74ba003e7dcd
keywords:
- bus-master DMA WDK video miniport , considerations
- DMA bus-master WDK video miniport , considerations
- concurrent DMA WDK video miniport
- VideoPortStartDma
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Points to Consider When Using DMA


## <span id="ddk_points_to_consider_when_using_dma_gg"></span><span id="DDK_POINTS_TO_CONSIDER_WHEN_USING_DMA_GG"></span>


This section provides some important points to consider if you plan to use DMA operations in your miniport driver.

### <span id="additional_notes_on_videoportstartdma"></span><span id="ADDITIONAL_NOTES_ON_VIDEOPORTSTARTDMA"></span>Additional Notes on VideoPortStartDma

The display driver usually sends transfer requests to the miniport driver, which actually carries out those DMA transfers. The display driver cannot assume that just because its DMA engine is idle, all data in a transfer request has been transferred. This is because the miniport driver needs to call [**VideoPortStartDma**](https://msdn.microsoft.com/library/windows/hardware/ff570369) and [**VideoPortCompleteDma**](https://msdn.microsoft.com/library/windows/hardware/ff570286) multiple times for a large transfer request. The hardware's DMA engine is idle between two such DMA operations, even though there might be additional data to transfer. It is the miniport driver's responsibility to inform the display driver when the transfer request has been completely accomplished.

The *Context* parameter of **VideoPortStartDma** should point to nonpaged memory, such as memory in the hardware extension. This parameter is passed through to the miniport driver's [**HwVidExecuteDma**](https://msdn.microsoft.com/library/windows/hardware/ff567330) callback routine, which runs at IRQL DISPATCH\_LEVEL.

### <span id="dma_and_interrupts"></span><span id="DMA_AND_INTERRUPTS"></span>DMA and Interrupts

For many devices, an interrupt is generated when a hardware DMA operation is complete. The video miniport driver's interrupt service routine (ISR) should queue a DPC routine for further DMA-related tasks. Do not call the video port driver's DMA functions in an ISR since they can only be called at or below IRQL DISPATCH\_LEVEL.

It is safe to check the size being transferred in the aforementioned DPC routine, even if the **VideoPortStartDma** function has not yet returned, since the variable pointed to by the *pLength* argument of **VideoPortStartDma** has already been updated at the time *HwVidExecuteDma* was called.

### <span id="logical_addresses_versus_physical_addresses"></span><span id="LOGICAL_ADDRESSES_VERSUS_PHYSICAL_ADDRESSES"></span>Logical Addresses Versus Physical Addresses

The video port driver's DMA implementation uses the concept of logical addresses, which are addresses used by the DMA hardware. Logical addresses can be different from physical addresses. The video port driver-provided DMA functions take into account any platform-specific memory restrictions. For this reason, it is important to use the video port driver DMA functions instead of such kernel-mode functions as [**MmGetPhysicalAddress**](https://msdn.microsoft.com/library/windows/hardware/ff554547). Please refer to [Adapter Objects and DMA](https://msdn.microsoft.com/library/windows/hardware/ff540519) for more information about logical addresses.

### <span id="concurrent_dma"></span><span id="CONCURRENT_DMA"></span>Concurrent DMA

For devices that support concurrent DMA transfers, either on a DMA controller that supports simultaneous reads and writes, or on two separate DMA controllers, miniport drivers should obtain a separate DMA adapter object for each concurrent path. For example, if a device has two DMA controllers that work in parallel, the miniport driver should make two calls to **VideoPortGetDmaAdapter**, thereby obtaining pointers to two VP\_DMA\_ADAPTER structures. After that, whenever the miniport driver makes a DMA transfer request of a particular DMA controller, it should use the appropriate pointer in that request.

 

 





