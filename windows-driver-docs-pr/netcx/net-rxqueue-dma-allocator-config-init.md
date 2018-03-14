---
title: NET_RXQUEUE_DMA_ALLOCATOR_CONFIG_INIT method
description: NET_RXQUEUE_DMA_ALLOCATOR_CONFIG_INIT method
ms.assetid: 4A88673C-9652-476E-B564-30220F0D1370
keywords:
- WDF Network Adapter Class Extension NET_RXQUEUE_DMA_ALLOCATOR_CONFIG_INIT, NetAdapterCx NET_RXQUEUE_DMA_ALLOCATOR_CONFIG_INIT, NetCx NET_RXQUEUE_DMA_ALLOCATOR_CONFIG_INIT
ms.author: windowsdriverdev
ms.date: 09/01/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# NET_RXQUEUE_DMA_ALLOCATOR_CONFIG_INIT method

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

The NET_RXQUEUE_DMA_ALLOCATOR_CONFIG_INIT method initializes a [NET_RXQUEUE_DMA_ALLOCATOR_CONFIG](net-rxqueue-dma-allocator-config.md) structure.

## Syntax

```cpp
VOID FORCEINLINE NET_RXQUEUE_DMA_ALLOCATOR_CONFIG_INIT(
    _Out_   PNET_RXQUEUE_DMA_ALLOCATOR_CONFIG   DmaAllocatorConfig,
    _In_    WDFDMAENABLER                       DmaEnabler
);
```

## Parameters

*DmaAllocatorConfig* [out]  
The NET_RXQUEUE_DMA_ALLOCATOR_CONFIG structure to be initialized.

*DmaEnabler* [in]  
A handle to a DMA enabler object that the client driver obtained from a previous call to [WdfDmaEnablerCreate](https://msdn.microsoft.com/library/windows/hardware/ff546983). 

## Return value

This method does not return a value.

## Remarks

NET_RXQUEUE_DMA_ALLOCATOR_CONFIG_INIT is used to initialize a [NET_RXQUEUE_DMA_ALLOCATOR_CONFIG](net-rxqueue-dma-allocator-config.md) structure, which is passed as an input parameter to [NetRxQueueInitSetDmaAllocatorConfig](netrxqueueinitsetdmaallocatorconfig.md).

## Requirements

|     |     |
| --- | --- |
| Minimum supported client | Windows 10, version 1709 |
| Minimum supported server | Windows Server 2016 |
| Header | Netrxqueue.h (include NetAdapterCx.h) |
| IRQL | PASSIVE_LEVEL |

