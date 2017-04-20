---
title: NDIS Scatter/Gather DMA
description: NDIS Scatter/Gather DMA
ms.assetid: 70b8321b-7b21-4d11-a9c2-46b0caa26ce6
keywords:
- miniport drivers WDK networking , scatter/gather DMA
- NDIS miniport drivers WDK , scatter/gather DMA
- scatter/gather DMA WDK networking
- SGDMA WDK networking
- NICs WDK networking , system memory transfers
- network interface cards WDK networking , s
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# NDIS Scatter/Gather DMA


## <a href="" id="ddk-ndis-6-0-scatter-gather-dma-ng"></a>


NDIS miniport drivers can use the [Scatter/Gather DMA](scatter-gather-dma2.md) (SGDMA) method to transfer data between a NIC and system memory. A successful DMA transfer requires the physical address of the data to be in an address range that the NIC supports. HAL provides a mechanism for drivers to obtain the physical address list for an MDL chain and, if necessary, will double-buffer the data to a physical address range.

In NDIS versions prior to NDIS 6.0, SGDMA support in miniport drivers and NDIS is limited in some respects, and in particular does not work well in a multipacket send scenario. The NDIS 6.0 SGDMA support overcomes these limitations while providing a simple interface for miniport drivers.

The following topics provide more background information about SGDMA:

-   [History of NDIS SGDMA](history-of-ndis-sgdma.md)
-   [Benefits of NDIS SGDMA Support](benefits-of-ndis-sgdma-support.md)

## Related topics


[Miniport Driver Scatter/Gather DMA](scatter-gather-dma2.md)

 

 






