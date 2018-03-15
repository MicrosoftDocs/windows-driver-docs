---
title: NET_RXQUEUE_GET_PACKET_CONTEXT_TOKEN macro
description: NET_RXQUEUE_GET_PACKET_CONTEXT_TOKEN macro
ms.assetid: 342DD39C-28FF-4CBC-9A30-07FB45777572
keywords:
- WDF Network Adapter Class Extension NET_RXQUEUE_GET_PACKET_CONTEXT_TOKEN, NetAdapterCx NET_RXQUEUE_GET_PACKET_CONTEXT_TOKEN, NetCx NET_RXQUEUE_GET_PACKET_CONTEXT_TOKEN
ms.author: windowsdriverdev
ms.date: 09/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# NET_RXQUEUE_GET_PACKET_CONTEXT_TOKEN macro

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

The **NET_RXQUEUE_GET_PACKET_CONTEXT_TOKEN** macro 

## Syntax

```cpp
void NET_RXQUEUE_GET_PACKET_CONTEXT_TOKEN(
    _rxqueue,
    _contexttype
);
```

## Parameters

*_rxqueue*  
A handle to the NETRXQUEUE object.

*_contexttype*  
The structure type name of a driver-defined structure that describes the contents of the packet's context space.

## Return value

This macro does not return a value.

## Remarks

In NetAdapterCx 1.1, the ability to add more than one packet context was introduced, meaning queues with more than one packet per context now require a [NET_PACKET_CONTEXT_TOKEN](net-packet-context-token.md) to identify and retrieve each context. Call NET_RXQUEUE_GET_PACKET_CONTEXT_TOKEN to retrieve the token for a context type if your receive queue uses more than one context per packet.

For an example of how to use this macro to retrieve a packet context token, see [NET_PACKET_DECLARE_CONTEXT_TYPE_WITH_NAME](net-packet-declare-context-type-with-name.md).

## Requirements

|     |     |
| --- | --- |
| Target platform | Universal |
| Minimum KMDF version | 1.23 |
| Minimum NetAdapterCx version | 1.1 |
| Header | NetRxQueue.h (include NetAdapterCx.h) |

