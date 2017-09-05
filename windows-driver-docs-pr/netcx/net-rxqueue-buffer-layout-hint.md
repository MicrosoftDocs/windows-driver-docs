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
The ideal alignment for the start of the L3 header. This member's value is in the form *N-1*, where *N* is the alignment.

## Remarks

The information in this structure is set by the upper layer and is retrieved by the client driver by calling [NetRxQueueGetBufferLayoutHint](netrxqueuegetbufferlayouthint.md).

## Requirements

|     |     |
| --- | --- |
| Minimum KMDF version | 1.23 |
| Minimum NetAdapterCx version | 1.1 |
| Header | Netrxqueue.h (include NetAdapterCx.h) |

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20Planning%20your%20APN%20database%20submission%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")