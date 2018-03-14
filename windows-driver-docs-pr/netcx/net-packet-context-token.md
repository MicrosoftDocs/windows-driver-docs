---
title: NET_PACKET_CONTEXT_TOKEN structure
description: NET_PACKET_CONTEXT_TOKEN structure
ms.assetid: 84B44373-FE17-4A21-9B01-E4389F9C38CC
keywords:
- WDF Network Adapter Class Extension NET_PACKET_CONTEXT_TOKEN, NetAdapterCx NET_PACKET_CONTEXT_TOKEN, NetCx NET_PACKET_CONTEXT_TOKEN
ms.author: windowsdriverdev
ms.date: 08/30/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# NET_PACKET_CONTEXT_TOKEN structure

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

The NET_PACKET_CONTEXT_TOKEN structure represents an identifier token for a [NET_PACKET](net-packet.md) context.

## Syntax

```cpp
typedef struct NET_PACKET_CONTEXT_TOKEN *PNET_PACKET_CONTEXT_TOKEN;
```

## Members

This structure has no members.

## Remarks

To retrieve a token for a packet context, call either [NET_TXQUEUE_GET_PACKET_CONTEXT_TOKEN](net-txqueue-get-packet-context-token.md) or [NET_RXQUEUE_GET_PACKET_CONTEXT_TOKEN](net-rxqueue-get-packet-context-token.md) depending on the type of queue on which you are operating.

## Requirements

|     |     |
| --- | --- |
| Minimum KMDF version | 1.23 |
| Minimum NetAdapterCx version | 1.1 |
| Header | Netadapterpacket.h (include NetAdapterCx.h) |

