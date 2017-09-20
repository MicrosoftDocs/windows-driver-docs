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

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20Planning%20your%20APN%20database%20submission%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")