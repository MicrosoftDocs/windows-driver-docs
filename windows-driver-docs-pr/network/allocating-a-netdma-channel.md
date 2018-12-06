---
title: Allocating a NetDMA Channel
description: Allocating a NetDMA Channel
ms.assetid: f65c63a3-baf3-453e-a9f9-846a09afd10c
keywords:
- memory-to-memory data transfers WDK NetDMA , allocating channels
- data transfers WDK NetDMA , allocating channels
- transferring data WDK NetDMA , allocating channels
- DMA transfers WDK NetDMA , allocating channels
- NetDMA WDK networking , allocating c
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Allocating a NetDMA Channel


**Note**  The NetDMA interface is not supported in Windows 8 and later.

 




Before using a dynamic memory access (DMA) channel, the NetDMA interface calls the [**ProviderAllocateDmaChannel**](https://msdn.microsoft.com/library/windows/hardware/ff570393) function of the NetDMA provider driver to allocate and initialize the DMA channel.

The NetDMA interface supplies a[**NET\_DMA\_CHANNEL\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff568732) structure in the *ChannelParameters* parameter of *ProviderAllocateDmaChannel*. This parameters structure contains:

-   Information about the structure, including the revision number and size.

-   The virtual and physical address of the memory location that the NetDMA provider must use to write the completion status of a DMA operation on the DMA channel. These addresses are used if the NET\_DMA\_STATUS\_UPDATE\_ON\_COMPLETION flag in the [**NET\_DMA\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff568734) structure is set.

-   A bitmap that specifies the desired CPU affinities for the interrupt deferred procedure calls (DPCs) that are associated with DMA operations on the DMA channel.

-   The priority of the DMA channel.

If the NetDMA provider supports MSI-X and the CPU affinities of the interrupts that are associated with the DMA channels are set, the NetDMA provider driver attempts to allocate a DMA channel with an interrupt CPU affinity that matches a bit that is specified in the **ProcessorAffinityMask** member of the [**NET\_DMA\_CHANNEL\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff568732) structure. If MSI-X is not supported or MSI-X is supported but a DMA channel with a matching interrupt CPU affinity is not available, the NetDMA provider driver allocates any available DMA channel and calls the [**KeSetTargetProcessorDpc**](https://msdn.microsoft.com/library/windows/hardware/ff553278) routine to set the target CPU of the interrupt DPC of the DMA channel to match one of the specified affinity mask bits.

In any situation, the NetDMA provider driver returns the CPU number that it associated with the interrupt DPC for the DMA channel to the NetDMA interface in the **CpuNumber** member of the NET\_DMA\_CHANNEL\_PARAMETERS structure.

The NetDMA provider driver provides a pointer to a block of driver-allocated context information at the *pProviderChannelContext* parameter of [**ProviderAllocateDmaChannel**](https://msdn.microsoft.com/library/windows/hardware/ff570393). This context area stores information about the DMA channel. The NetDMA interface passes the context information in subsequent calls to *ProviderXxx* functions that require a DMA channel context.

When the NetDMA interface calls [**ProviderAllocateDmaChannel**](https://msdn.microsoft.com/library/windows/hardware/ff570393), the NetDMA interface provides a handle at the *NetDmaChannelHandle* parameter. The NetDMA provider driver uses this handle in subsequent calls to **NetDma*Xxx*** functions that are associated with the DMA channel.

If the NetDMA provider driver successfully allocates the DMA channel, the driver returns STATUS\_SUCCESS from [**ProviderAllocateDmaChannel**](https://msdn.microsoft.com/library/windows/hardware/ff570393). After a DMA channel allocation succeeds, the driver must be ready for the NetDMA interface to use the channel in DMA transfers.

If the allocation fails for any reason, the driver should release any resources that it allocated in *ProviderAllocateDmaChannel* and return an appropriate return value from *ProviderAllocateDmaChannel*.

The NetDMA interface calls the [**ProviderFreeDmaChannel**](https://msdn.microsoft.com/library/windows/hardware/ff570398) function to free a previously allocated DMA channel. For more information about freeing DMA channels, see [Freeing a NetDMA Channel](freeing-a-netdma-channel.md).

 

 





