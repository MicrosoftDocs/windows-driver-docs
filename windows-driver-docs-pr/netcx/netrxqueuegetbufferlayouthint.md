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

