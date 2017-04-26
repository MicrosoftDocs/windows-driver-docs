---
title: Registering and Deregistering DMA Channels
description: Registering and Deregistering DMA Channels
ms.assetid: b24e0a56-1864-4f70-a646-c35e8eccd9e3
keywords:
- scatter/gather DMA WDK networking , DMA channels
- SGDMA WDK networking , DMA channels
- NdisMRegisterScatterGatherDma
- NdisMDeregisterScatterGatherDma
- DMA channels WDK networking
- channels WDK SGDMA
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Registering and Deregistering DMA Channels


## <a href="" id="ddk-registering-and-deregistering-dma-channels-ng"></a>


An NDIS miniport driver calls the [**NdisMRegisterScatterGatherDma**](https://msdn.microsoft.com/library/windows/hardware/ff563659) function from its [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) function to register a DMA channel with NDIS.

The miniport driver passes a DMA description to [**NdisMRegisterScatterGatherDma**](https://msdn.microsoft.com/library/windows/hardware/ff563659) in the *DmaDescription* parameter. **NdisMRegisterScatterGatherDma** returns a size for the buffer that should be large enough to hold the scatter/gather list. Miniport drivers should use this size to preallocate the storage for scatter/gather lists.

The miniport driver also passes [**NdisMRegisterScatterGatherDma**](https://msdn.microsoft.com/library/windows/hardware/ff563659) the entry points for the *MiniportXxx* functions that NDIS calls to process the scatter/gather list. NDIS calls the miniport driver's [*MiniportProcessSGList*](https://msdn.microsoft.com/library/windows/hardware/ff559420) function after HAL has built the scatter/gather list for a buffer. **NdisMRegisterScatterGatherDma** supplies a handle in the *pNdisMiniportDmaHandle* parameter, which the miniport driver must use in subsequent calls to NDIS scatter/gather DMA functions.

An NDIS miniport driver calls the [**NdisMDeregisterScatterGatherDma**](https://msdn.microsoft.com/library/windows/hardware/ff563581) function from its [*MiniportHaltEx*](https://msdn.microsoft.com/library/windows/hardware/ff559388) function to release scatter/gather DMA resources.

## Related topics


[Allocating and Freeing Scatter/Gather Lists](allocating-and-freeing-scatter-gather-lists.md)

[Miniport Driver Scatter/Gather DMA](scatter-gather-dma2.md)

[NDIS Scatter/Gather DMA](ndis-scatter-gather-dma.md)

 

 






