---
title: Appending DMA Descriptors to a DMA Channel
description: Appending DMA Descriptors to a DMA Channel
ms.assetid: 02b1b617-4021-4a88-8091-6510abb74fbb
keywords:
- memory-to-memory data transfers WDK NetDMA , appending DMA descriptors
- data transfers WDK NetDMA , appending DMA descriptors
- transferring data WDK NetDMA , appending DMA descriptors
- DMA transfers WDK NetDMA , appending DMA descriptors
- NetDMA WDK n
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Appending DMA Descriptors to a DMA Channel


**Note**  The NetDMA interface is not supported in Windows 8 and later.

 




The NetDMA interface calls a NetDMA provider driver's [**ProviderAppendDma**](https://msdn.microsoft.com/library/windows/hardware/ff570394) function to finish appending a linked list of dynamic memory access (DMA) descriptors after the last descriptor on a DMA channel. The NetDMA interface always starts a DMA transfer before appending descriptors to a DMA channel. For more information about starting a DMA transfer, see [Starting a DMA Transfer](starting-a-dma-transfer.md).

The NetDMA interface sets the **NextDescriptor** member of the last descriptor to the beginning of the new chain of descriptors before calling *ProviderAppendDma*. The NetDMA interface can call *ProviderAppendDma* any number of times after the transfer is started.

If the current descriptor in an active DMA transfer is the last descriptor, the DMA engine must reread the last descriptor. The **NextDescriptor** member in the current [**NET\_DMA\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff568734) structure has a new address, and the DMA engine should continue with the next descriptor. If the current descriptor is not the last descriptor, the DMA engine can continue processing DMA descriptors with no additional tasks.

 

 





