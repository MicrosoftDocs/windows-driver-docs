---
title: NetTxQueueGetPacketContextToken method
description: NetTxQueueGetPacketContextToken method
ms.assetid: 6661EE60-8171-4D40-8EEE-A04D18CF9BF5
keywords:
- WDF Network Adapter Class Extension NetTxQueueGetPacketContextToken, NetAdapterCx NetTxQueueGetPacketContextToken, NetCx NetTxQueueGetPacketContextToken
ms.author: windowsdriverdev
ms.date: 09/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# NetTxQueueGetPacketContextToken method

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

The **NetTxQueueGetPacketContextToken** method retrieves a [NET_PACKET_CONTEXT_TOKEN](net-packet-context-token.md) for a [NET_PACKET](net-packet.md) context on a transmit queue.

> [!WARNING]
> This method is reserved for NetAdapterCx. Client drivers must not call this method directly. Instead, they should call [NET_TXQUEUE_GET_PACKET_CONTEXT_TOKEN](net-txqueue-get-packet-context-token.md).

## Syntax

```cpp
PNET_PACKET_CONTEXT_TOKEN FORCEINLINE NetTxQueueGetPacketContextToken(
    _In_    NETTXQUEUE              NetTxQueue,
    _In_    PCNET_CONTEXT_TYPE_INFO ContextTypeInfo
);
```

## Requirements

|     |     |
| --- | --- |
| Target platform | Universal |
| Minimum KMDF version | 1.23 |
| Minimum NetAdapterCx version | 1.1 |
| Header | Nettxqueue.h (include NetAdapterCx.h) |
| IRQL | PASSIVE_LEVEL |

