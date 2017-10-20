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

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20Planning%20your%20APN%20database%20submission%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")