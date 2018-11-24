---
title: NetDMA Provider Services
description: NetDMA Provider Services
ms.assetid: f93eef62-3a6b-4bee-99b9-fca2c02142d1
keywords:
- NetDMA provider drivers WDK networking , services
- NetDMA provider services WDK networking
- memory-to-memory data transfers WDK NetDMA , provider services
- data transfers WDK NetDMA , provider services
- transferring data WDK NetDMA , provider service
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# NetDMA Provider Services


**Note**  The NetDMA interface is not supported in Windows 8 and later.

 




The NetDMA interface requires *ProviderXxx* functions that the NetDMA provider driver supplies to service NetDMA requests. The *ProviderXxx* function entry points are defined in the [**NET\_DMA\_PROVIDER\_CHARACTERISTICS**](https://msdn.microsoft.com/library/windows/hardware/ff568738) structure that the NetDMA provider driver passes to the [**NetDmaRegisterProvider**](https://msdn.microsoft.com/library/windows/hardware/ff568336) function.

The NetDMA interface does not use the NetDMA provider services until after the NetDMA provider is started. For more information about starting a NetDMA provider, see [Starting a NetDMA Provider](starting-a-netdma-provider.md).

The following *ProviderXxx* functions are mandatory:

[**ProviderAllocateDmaChannel**](https://msdn.microsoft.com/library/windows/hardware/ff570393)

[**ProviderFreeDmaChannel**](https://msdn.microsoft.com/library/windows/hardware/ff570398)

[**ProviderStartDma**](https://msdn.microsoft.com/library/windows/hardware/ff570404)

[**ProviderAppendDma**](https://msdn.microsoft.com/library/windows/hardware/ff570394)

The following *ProviderXxx* functions are optional:

[**ProviderSuspendDma**](https://msdn.microsoft.com/library/windows/hardware/ff570405)

[**ProviderResumeDma**](https://msdn.microsoft.com/library/windows/hardware/ff570401)

[**ProviderAbortDma**](https://msdn.microsoft.com/library/windows/hardware/ff570392)

[**ProviderResetChannel**](https://msdn.microsoft.com/library/windows/hardware/ff570400)

If the NetDMA provider driver does not support an optional *ProviderXxx* function, the driver sets the entry point for that function to **NULL**.

The following topics describe the NetDMA provider services and the preceding *ProviderXxx* functions:

[Allocating a NetDMA Channel](allocating-a-netdma-channel.md)

[Freeing a NetDMA Channel](freeing-a-netdma-channel.md)

[Starting a DMA Transfer](starting-a-dma-transfer.md)

[Appending DMA Descriptors to a DMA Channel](appending-dma-descriptors-to-a-dma-channel.md)

[Completing a DMA Transfer](completing-a-dma-transfer.md)

[Supporting NULL DMA Transfers](supporting-null-dma-transfers.md)

[Suspending and Resuming a DMA Transfer](suspending-and-resuming-a-dma-transfer.md)

[Aborting a DMA Transfer](aborting-a-dma-transfer.md)

[Resetting a DMA Channel](resetting-a-dma-channel.md)

 

 





