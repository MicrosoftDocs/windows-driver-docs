---
title: History of NDIS SGDMA
description: History of NDIS SGDMA
ms.assetid: bb2db346-1272-40e0-896a-95e14dd9d2f8
keywords:
- scatter/gather DMA WDK networking , history
- SGDMA WDK networking , history
- scatter/gather DMA WDK networking , limitations
- SGDMA WDK networking , limitations
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# History of NDIS SGDMA


## <a href="" id="ddk-ndis-sgdma-history-ng"></a>


In NDIS versions prior to NDIS 6.0, NDIS obtains a scatter gather (SG) list for each packet before sending the packet to the miniport driver. NDIS also handles the case where the original attempt to get the SG list fails due to excessive fragmentation. In this case, NDIS double-buffers the packet to a contiguous buffer and tries again. HAL can also double-buffer the data to a physical address that the NIC supports if, for example, the physical address of the data is above the 32-bit maximum and the NIC does not support 64-bit DMA.

To avoid a deadlock situation, NDIS obtains a SG list for a packet, and sends one packet at a time. If NDIS attempts to map all the packets before sending them to the miniport driver, the system could run out resources. In this case, NDIS would be waiting for map registers to become available while some map registers are locked down for the packets that have not been sent. Locked down packets cannot be reused.

This approach to SGDMA support has the following limitations:

-   Because the packet is mapped before it gets to the miniport driver, the driver cannot optimize for small packets or packets that are too fragmented. The miniport driver cannot double buffer the packet to a known physical address.

-   There is no guarantee that the physical address array that NDIS passed to the miniport driver maps to the virtual address of the original data. Therefore, if the driver changes the data at the virtual address in the MDL chain before sending it, the modifications made to the data are not reflected in the data in the physical addresses. In this case, the NIC sends the unmodified data.

-   NDIS is limited to sending one packet at a time to avoid a deadlock due to resource issues. This is not as efficient as sending multiple packets.

-   Because NDIS cannot determine the transmit capabilities of miniport drivers, it cannot preallocate the storage for an SG list buffer. Therefore, NDIS must allocate the necessary storage at run time. This is not as efficient as preallocating the storage.

-   HAL functions that allocate an SG list should be called at IRQL = DISPATCH\_LEVEL. NDIS does not have the current IRQL information, so it has to set the IRQL to DISPATCH\_LEVEL even if it is already at DISPATCH\_LEVEL. This is not efficient if the IRQL is already at DISPATCH\_LEVEL.

## Related topics


[Miniport Driver Scatter/Gather DMA](scatter-gather-dma2.md)

[NDIS Scatter/Gather DMA](ndis-scatter-gather-dma.md)

 

 






