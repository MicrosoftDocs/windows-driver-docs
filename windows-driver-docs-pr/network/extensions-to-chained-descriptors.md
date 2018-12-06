---
title: Extensions to Chained Descriptors
description: Extensions to Chained Descriptors
ms.assetid: a558c6c8-359c-487b-a51a-5cb16b1a541d
keywords:
- memory-to-memory data transfers WDK NetDMA , descriptor handling
- data transfers WDK NetDMA , descriptor handling
- transferring data WDK NetDMA , descriptor handling
- DMA transfers WDK NetDMA , descriptor handling
- NetDMA WDK networking , descriptor handling
- NetDMA 2.0 WDK networking , descriptor handling
- NetDMA 2.0 WDK networking , chained descriptors
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Extensions to Chained Descriptors


**Note**  The NetDMA interface is not supported in Windows 8 and later.

 




In NetDMA versions before 2.0, the linked list of descriptors is NULL-terminated. The DMA engine stops after processing a descriptor with **NULL** for the address of the next descriptor (that is, the **NextDescriptor** member in [**NET\_DMA\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff568734) structure). This design requires the NetDMA interface to go back and modify the last submitted descriptor every time that the NetDMA interface needed to submit a new batch of descriptors. This design also forces the DMA engine to perform a DMA re-read on the last submitted descriptor, and there were some caching issues that negatively impact the computer performance.

NetDMA version 2.0 employs a more efficient descriptor handling design. In the NetDMA 2.0 design, the address of the next descriptor is always valid and the DMA engine reads it as the descriptor is processed. The DMA engine maintains a counter to keep track of outstanding submitted descriptors. The DMA engine decrements the counter for each descriptor that the DMA engine processes. The DMA engine continues to process the next descriptor until the counter reaches zero. To add a new batch of descriptors, simply add the number of new descriptors to the counter. The NetDMA interface is not required to modify (and the DMA engine does not need to read) the last submitted descriptor.

The [**ProviderAppendDma**](https://msdn.microsoft.com/library/windows/hardware/ff570394) and [**ProviderStartDma**](https://msdn.microsoft.com/library/windows/hardware/ff570404) functions in NetDMA version 1.0 provide the *DescriptorCount* parameter to specify the number of posted descriptors. Therefore, there is no change in the *ProviderAppendDma* and *ProviderStartDma* function parameters for NetDMA 2.0. However, when NetDMA posts a linked list of DMA descriptors to a NetDMA version 2.0 provider, NetDMA ensures that the **NextDescriptor** member for the last submitted descriptor points to a valid descriptor that will be used in subsequent DMA operations.

 

 





