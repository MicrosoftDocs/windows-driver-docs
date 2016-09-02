---
title: Allocating and Freeing Scatter/Gather Lists
description: Allocating and Freeing Scatter/Gather Lists
ms.assetid: 95463617-65df-4c02-82f4-e3aba44d42fb
keywords: ["scatter/gather DMA WDK networking , scatter/gather lists", "SGDMA WDK networking , scatter/gather lists", "NdisMAllocateNetBufferSGList", "NdisMFreeNetBufferSGList", "lists WDK SGDMA"]
---

# Allocating and Freeing Scatter/Gather Lists


## <a href="" id="ddk-allocating-and-freeing-scatter-gather-lists-ng"></a>


An NDIS miniport driver calls the [**NdisMAllocateNetBufferSGList**](https://msdn.microsoft.com/library/windows/hardware/ff562776) function in its [*MiniportSendNetBufferLists*](https://msdn.microsoft.com/library/windows/hardware/ff559440) function. The miniport driver calls **NdisMAllocateNetBufferSGList** once for each [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376) structure that it must map. After the resources become available and HAL has the SG list ready, NDIS calls the driver's [*MiniportProcessSGList*](https://msdn.microsoft.com/library/windows/hardware/ff559420) function. NDIS can call *MiniportProcessSGList* before or after the miniport driver's call to **NdisMAllocateNetBufferSGList** returns.

To improve system performance, the scatter/gather list is generated from the network data starting at the beginning of the MDL that is specified at the **CurrentMdl** member of the associated [**NET\_BUFFER\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff568381) structure. The start of the network data in the SG list is offset from the beginning of the SG list by the value specified in the **CurrentMdlOffset** member of the associated **NET\_BUFFER\_DATA** structure.

While handling a DPC for a send-complete interrupt, and after the miniport driver does not need the SG list any more, the miniport driver should call the [**NdisMFreeNetBufferSGList**](https://msdn.microsoft.com/library/windows/hardware/ff563586) function to free the SG list.

**Note**  Do not call [**NdisMFreeNetBufferSGList**](https://msdn.microsoft.com/library/windows/hardware/ff563586) while the driver or hardware is still accessing the memory that is described by the [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376) structure that is associated with the scatter/gather list.

 

Before accessing received data, miniport drivers must call [**NdisMFreeNetBufferSGList**](https://msdn.microsoft.com/library/windows/hardware/ff563586) to flush the memory cache.

## Related topics


[Miniport Driver Scatter/Gather DMA](scatter-gather-dma2.md)

[NDIS Scatter/Gather DMA](ndis-scatter-gather-dma.md)

[Registering and Deregistering DMA Channels](registering-and-deregistering-dma-channels.md)

 

 






