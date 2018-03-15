---
title: NET_RXQUEUE_DMA_ALLOCATOR_CONFIG structure
description: NET_RXQUEUE_DMA_ALLOCATOR_CONFIG structure
ms.assetid: B3C3C6AD-6853-4069-8090-601E120A77C6
keywords:
- WDF Network Adapter Class Extension NET_RXQUEUE_DMA_ALLOCATOR_CONFIG, NetAdapterCx NET_RXQUEUE_DMA_ALLOCATOR_CONFIG, NetCx NET_RXQUEUE_DMA_ALLOCATOR_CONFIG
ms.author: windowsdriverdev
ms.date: 09/01/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# NET_RXQUEUE_DMA_ALLOCATOR_CONFIG structure

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

The NET_RXQUEUE_DMA_ALLOCATOR_CONFIG structure describes the configuration options for a DMA allocator to be associated with a receive queue.

## Syntax

```cpp
typedef struct _NET_RXQUEUE_DMA_ALLOCATOR_CONFIG{
    ULONG               Size;
    WDFDMAENABLER       DmaEnabler;
    PHYSICAL_ADDRESS    MaximumPhysicalAddress;
    WDF_TRI_STATE       CacheEnabled;
    NODE_REQUIREMENT    PreferredNode;
} NET_RXQUEUE_DMA_ALLOCATOR_CONFIG, *PNET_RXQUEUE_DMA_ALLOCATOR_CONFIG;
```

## Members

**Size**  
The size of this structure, in bytes.

**DmaEnabler**  
The DMA enabler to use when allocating receive buffers.

**MaximumPhysicalAddress**  
The maximum logical address to use when allocating receive buffers. Set to **0** to indicate to NetAdapterCx that there is no maximum address.

**CacheEnabled**  
A [WDF_TRI_STATE](https://msdn.microsoft.com/library/windows/hardware/ff552533) value defining if the memory allocated should have cache enabled or not. A value of **WdfUseDefault** will enable cache only if the device is cache coherent.

**PreferredNode**  
The preferred NUMA node to use when allocating memory. If this member is set to MM_ANY_NODE_OK, NetAdapterCx will automatically determine the best node to use.

## Remarks

Call [NET_RXQUEUE_DMA_ALLOCATOR_CONFIG_INIT](net-rxqueue-dma-allocator-config-init.md) to initialize this structure.

The **NET_RXQUEUE_DMA_ALLOCATOR_CONFIG** structure is an input parameter to [NetRxQueueInitSetDmaAllocatorConfig](netrxqueueinitsetdmaallocatorconfig.md). The client must use [NET_RXQUEUE_DMA_ALLOCATOR_CONFIG_INIT](net-rxqueue-dma-allocator-config-init.md) to initialize this structure.

## Requirements

|     |     |
| --- | --- |
| Minimum KMDF version | 1.23 |
| Minimum NetAdapterCx version | 1.1 |
| Header | Netrxqueue.h (include NetAdapterCx.h) |

