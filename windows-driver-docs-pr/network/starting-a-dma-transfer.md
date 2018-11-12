---
title: Starting a DMA Transfer
description: Starting a DMA Transfer
ms.assetid: 27c8a212-5727-48e5-a0bb-8978fd79f240
keywords:
- memory-to-memory data transfers WDK NetDMA , starting
- data transfers WDK NetDMA , starting
- transferring data WDK NetDMA , starting
- DMA transfers WDK NetDMA , starting
- NetDMA WDK networking , starting transfers
- starting DMA transfers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Starting a DMA Transfer


**Note**  The NetDMA interface is not supported in Windows 8 and later.

 




The NetDMA interface calls a NetDMA provider driver's [**ProviderStartDma**](https://msdn.microsoft.com/library/windows/hardware/ff570404) function to start a dynamic memory access (DMA) transfer. The NetDMA interface can call *ProviderStartDma* at any time after a DMA channel is allocated. The NetDMA interface must call *ProviderStartDma* for the first DMA transfer after a channel reset or stop, or after the DMA channel is first allocated.

To perform the start operation, the NetDMA provider must disregard the remaining unprocessed DMA descriptor list, if any, after it completes the processing of the current descriptor. That is, the NetDMA provider must ignore the **NextDescriptor** member in the current [**NET\_DMA\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff568734) structure and load the descriptor that *ProviderStartDma* specifies.

The NetDMA interface supplies a [**NET\_DMA\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff568734) structure in the *DescriptorVirtualAddress* parameter of *ProviderStartDma*. The physical address of the descriptor is passed at the *DescriptorPhysicalAddress* parameter. The NET\_DMA\_DESCRIPTOR structure contains:

-   The size of the DMA transfer that is associated with the current descriptor.

-   The physical addresses of the source and destination locations for the DMA transfer.

-   The physical address of the next DMA descriptor.

-   Reserved fields that provide space for vendor-defined information.

-   User context members that are reserved for the NetDMA interface.

The source of the DMA transfer is a linked list of DMA descriptors. The **NextDescriptor** member of a [**NET\_DMA\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff568734) structure contains the physical address of the next NET\_DMA\_DESCRIPTOR structure in the linked list. The *DescriptorCount* parameter of [**ProviderStartDma**](https://msdn.microsoft.com/library/windows/hardware/ff570404) contains the number of DMA descriptors that are in the linked list. The *DescriptorCount* parameter is provided for additional information, and the DMA engine should use the linked list to access all of the DMA descriptors.

After the initial DMA transfer is started, the NetDMA interface can call the [**ProviderAppendDma**](https://msdn.microsoft.com/library/windows/hardware/ff570394) function to append additional descriptors to the transfer. For more information about appending descriptors to a DMA transfer, see [Appending DMA Descriptors to a DMA Channel](appending-dma-descriptors-to-a-dma-channel.md).

 

 





