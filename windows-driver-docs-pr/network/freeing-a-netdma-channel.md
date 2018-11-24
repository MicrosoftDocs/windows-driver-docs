---
title: Freeing a NetDMA Channel
description: Freeing a NetDMA Channel
ms.assetid: 71d563d4-c0be-4fc3-a0c6-6bf139cd3ba3
keywords:
- memory-to-memory data transfers WDK NetDMA , freeing channels
- data transfers WDK NetDMA , freeing channels
- transferring data WDK NetDMA , freeing channels
- DMA transfers WDK NetDMA , freeing channels
- NetDMA WDK networking , freeing channels
- channe
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Freeing a NetDMA Channel


**Note**  The NetDMA interface is not supported in Windows 8 and later.

 




The NetDMA interface calls a NetDMA provider driver's [**ProviderFreeDmaChannel**](https://msdn.microsoft.com/library/windows/hardware/ff570398) function to free a dynamic memory access (DMA) channel that was previously allocated in the [**ProviderAllocateDmaChannel**](https://msdn.microsoft.com/library/windows/hardware/ff570393) function. For more information about allocating DMA channels, see [Allocating a NetDMA Channel](allocating-a-netdma-channel.md).

Before the NetDMA interface calls *ProviderFreeDmaChannel*, it ensures that there are no outstanding DMA operations on the DMA channel that the interface will free.

After the NetDMA interface calls *ProviderFreeDmaChannel*, it will not call any *ProviderXxx* functions for the freed channel.

The NetDMA interface frees all of the allocated DMA channels before it returns from the [**NetDmaProviderStop**](https://msdn.microsoft.com/library/windows/hardware/ff568335) function. For more information about stopping a NetDMA provider, see [Stopping a NetDMA Provider](stopping-a-netdma-provider.md).

 

 





