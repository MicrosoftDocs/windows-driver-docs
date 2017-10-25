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

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20Planning%20your%20APN%20database%20submission%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")