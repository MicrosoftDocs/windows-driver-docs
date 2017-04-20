---
title: Benefits of NDIS SGDMA Support
description: Benefits of NDIS SGDMA Support
ms.assetid: 5668fd27-a6f6-4183-9272-03365dd5305e
keywords:
- scatter/gather DMA WDK networking , benefits
- SGDMA WDK networking , benefits
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Benefits of NDIS SGDMA Support


## <a href="" id="ddk-ndis-6-0-sgdma-support-ng"></a>


In the NDIS 6.0 and later SGDMA interface, NDIS does not map the data buffer before sending it down to the miniport driver. Instead, NDIS provides an interface for the driver to map the network data.

This approach yields the following benefits:

-   Since NDIS provides the interface to HAL for mapping the network data, NDIS shields miniport drivers from the complexity and details of the mapping process.

-   Miniport drivers have access to the data before it is mapped. Therefore, any changes made to the original data are reflected in the data represented by the SG list even if NDIS or HAL double-buffers the data.

-   Miniport drivers can optimize the transmission of small or highly fragmented packets by copying them to a preallocated buffer with a known physical address. This approach avoids mapping that is not required and therefore improves system performance.

-   NDIS can send multiple buffers to the miniport driver safely. This results in fewer calls to miniport drivers and therefore improves system performance.

-   Miniport drivers can preallocate the memory for an SG list as part of the transmit descriptor blocks. Therefore, NDIS or miniport drivers are not required to allocate memory for SG lists at run time.

-   Because miniport drivers can be running at IRQL = DISPATCH\_LEVEL, miniport drivers can avoid unnecessary calls to raise the IRQL to DISPATCH\_LEVEL. For example, because completing a send happens in the context of an interrupt DPC, miniport drivers can free the SG list without raising the IRQL.

## Related topics


[Miniport Driver Scatter/Gather DMA](scatter-gather-dma2.md)

[NDIS Scatter/Gather DMA](ndis-scatter-gather-dma.md)

 

 






