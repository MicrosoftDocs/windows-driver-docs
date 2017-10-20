---
title: NetRxQueueGetBufferLayoutHint method
description: NetRxQueueGetBufferLayoutHint method
ms.assetid: 2C1C8385-F4CF-4EDF-87B8-3BF9412518B6
keywords:
- WDF Network Adapter Class Extension NetRxQueueGetBufferLayoutHint, NetAdapterCx NetRxQueueGetBufferLayoutHint, NetCx NetRxQueueGetBufferLayoutHint
ms.author: windowsdriverdev
ms.date: 09/01/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# NetRxQueueGetBufferLayoutHint method

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

The NetRxQueueGetBufferLayoutHint method queries buffer layout hints that a NetAdapterCx client driver's receive queue can use to calculate how much padding its receive buffers should have.

## Syntax

```cpp
VOID FORCEINLINE NetRxQueueGetBufferLayoutHint(
    _In_    NETRXQUEUE                      NetRxQueue,
    _Out_   PNET_RXQUEUE_BUFFER_LAYOUT_HINT BufferLayoutHint
);
```

## Parameters

*NetRxQueue* [in]  
A handle to a NETRXQUEUE object created in a prior call to [NetRxQueueCreate](netrxqueuecreate.md).

*BufferLayoutHint* [out]  
A [NET_RXQUEUE_BUFFER_LAYOUT_HINT](net-rxqueue-buffer-layout-hint.md) structure that represents the buffer layout hints returned from the upper layer.

## Return value

This method does not return a value.

## Remarks

Call this method to obtain buffer layout hints from the upper layer, formatted as a NET_RXQUEUE_BUFFER_LAYOUT_HINT structure. While this method is optional for client drivers to call, it can help improve receive queue performance by ensuring that protocol headers are naturally aligned.

## Requirements

|     |     |
| --- | --- |
| Target platform | Universal |
| Minimum KMDF version | 1.23 |
| Minimum NetAdapterCx version | 1.1 |
| Header | Netrxqueue.h (include NetAdapterCx.h) |
| IRQL | PASSIVE_LEVEL |

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20Planning%20your%20APN%20database%20submission%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")