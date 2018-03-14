---
title: NET_RXQUEUE_BUFFER_LAYOUT_HINT structure
description: NET_RXQUEUE_BUFFER_LAYOUT_HINT structure
ms.assetid: 5EFAEB36-9B39-41A7-9140-16DB225801E2
keywords:
- WDF Network Adapter Class Extension NET_RXQUEUE_BUFFER_LAYOUT_HINT, NetAdapterCx NET_RXQUEUE_BUFFER_LAYOUT_HINT, NetCx NET_RXQUEUE_BUFFER_LAYOUT_HINT
ms.author: windowsdriverdev
ms.date: 09/01/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# NET_RXQUEUE_BUFFER_LAYOUT_HINT structure

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

The NET_RXQUEUE_BUFFER_LAYOUT_HINT structure represents receive buffer layout hints returned to a client driver from the upper layer.

## Syntax

```cpp
typedef struct _NET_RXQUEUE_BUFFER_LAYOUT_HINT{
    ULONG   MinimumBackfillSize;
    ULONG   L3HeaderAlignment;
} NET_RXQUEUE_BUFFER_LAYOUT_HINT, *PNET_RXQUEUE_BUFFER_LAYOUT_HINT;
```

## Members

**MinimumBackfillSize**  
The minimum space that should be unused in the beginning of the first fragment of the ring buffer.

**L3HeaderAlignment**  
The ideal alignment for the start of the L3 header. This member's value is in the form *N-1*, where *N* is the alignment. For example, TCP/IP performance is optimized with a 4-byte alignment boundary, so this member would be set to **3** in that case.
You can use the **FILE_XXX_ALIGNMENT** constants, like **FILE_QUAD_ALIGNMENT** to name a specific alignment.

## Remarks

The information in this structure is set by the upper layer and is retrieved by the client driver by calling [NetRxQueueGetBufferLayoutHint](netrxqueuegetbufferlayouthint.md).

## Requirements

|     |     |
| --- | --- |
| Minimum KMDF version | 1.23 |
| Minimum NetAdapterCx version | 1.1 |
| Header | Netrxqueue.h (include NetAdapterCx.h) |

