---
title: NetRxQueueInitSetDmaAllocatorConfig method
description: NetRxQueueInitSetDmaAllocatorConfig method
ms.assetid: A463532D-BE87-42DD-ABBB-2B541AF02B8D
keywords:
- WDF Network Adapter Class Extension NetRxQueueInitSetDmaAllocatorConfig, NetAdapterCx NetRxQueueInitSetDmaAllocatorConfig, NetCx NetRxQueueInitSetDmaAllocatorConfig
ms.author: windowsdriverdev
ms.date: 09/01/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# NetRxQueueInitSetDmaAllocatorConfig method

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

The NetRxQueueInitSetDmaAllocatorConfig method associates an initialized [NET_RXQUEUE_DMA_ALLOCATOR_CONFIG](net-rxqueue-dma-allocator-config.md) structure with a receive queue.

## Syntax

```cpp
VOID FORCEINLINE NetRxQueueInitSetDmaAllocatorConfig(
    _Inout_ PNETRXQUEUE_INIT                    NetRxQueueInit,
    _In_    PNET_RXQUEUE_DMA_ALLOCATOR_CONFIG   DmaAllocatorConfig
)
```

## Parameters

*NetRxQueueInit* [in, out]  
A pointer to the **NETRXQUEUE_INIT** structure that the client driver received in [*EVT_NET_ADAPTER_CREATE_RXQUEUE*](evt-net-adapter-create-rxqueue.md).

*DmaAllocatorConfig* [in]  
A pointer to a [NET_RXQUEUE_DMA_ALLOCATOR_CONFIG](net-rxqueue-dma-allocator-config.md) structure the driver initialized with a previous call to [NET_RXQUEUE_DMA_ALLOCATOR_CONFIG_INIT](net-rxqueue-dma-allocator-config-init.md).

## Return value

This method does not return a value.

## Remarks

The NETRXQUEUE_INIT structure is an opaque structure that is defined and allocated by NetAdapterCx, similar to WDFDEVICE_INIT.

In NetAdapterCx version 1.1, this method replaced the previous **NetRxQueueConfigureDmaAllocator** method as the way a client driver lets NetAdapterCx manage the receive buffer. To opt in, follow these steps in your [EVT_NET_ADAPTER_CREATE_RXQUEUE](evt-net-adapter-create-rxqueue.md) callback function:

  1. Set the **AllocationSize** and **AlignmentRequirement** members of [**NET_RXQUEUE_CONFIG**](net-rxqueue-config.md).
  2. Allocate a [NET_RXQUEUE_DMA_ALLOCATOR_CONFIG](net-rxqueue-dma-allocator-config.md) structure.
  3. Call [NET_RXQUEUE_DMA_ALLOCATOR_CONFIG_INIT](net-rxqueue-dma-allocator-config-init.md) with the NET_RXQUEUE_DMA_ALLOCATOR_CONFIG structure and a DMA enabler object retrieved from the NETADAPTER's context.
  4. Call **NetRxQueueInitSetDmaAllocatorConfig** with the initialized NET_RXQUEUE_DMA_ALLOCATOR_CONFIG structure.

NetAdapterCx then uses the queue's DMA enabler to allocate pre-mapped buffers for each packet in the queue's [**NET_RING_BUFFER**](net-ring-buffer.md) structure, and updates the **VirtualAddress** and **DmaLogicalAddress** members of each [**NET_PACKET_FRAGMENT**](net-packet-fragment.md) to point to each premapped buffer.

The client driver retrieves a pointer to the ring buffer by calling [**NetTxQueueGetRingBuffer**](nettxqueuegetringbuffer.md) or [**NetRxQueueGetRingBuffer**](netrxqueuegetringbuffer.md).

## Requirements

|     |     |
| --- | --- |
| Target platform | Universal |
| Minimum KMDF version | 1.23 |
| Minimum NetAdapterCx version | 1.1 |
| Header | Netrxqueue.h (include NetAdapterCx.h) |
| IRQL | PASSIVE_LEVEL |

