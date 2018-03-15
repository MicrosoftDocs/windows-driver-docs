---
title: NetTxRueueGetPacketContextToken method
description: NetRxQueueGetPacketContextToken method
ms.assetid: 4FFA09AB-425E-4D33-803A-7804F67312B3
keywords:
- WDF Network Adapter Class Extension NetRxQueueGetPacketContextToken, NetAdapterCx NetRxQueueGetPacketContextToken, NetCx NetRxQueueGetPacketContextToken
ms.author: windowsdriverdev
ms.date: 09/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# NetRxQueueGetPacketContextToken method

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

The **NetRxQueueGetPacketContextToken** method retrieves a [NET_PACKET_CONTEXT_TOKEN](net-packet-context-token.md) for a [NET_PACKET](net-packet.md) context on a transmit queue.

> [!WARNING]
> This method is reserved for NetAdapterCx. Client drivers must not call this method directly. Instead, they should call [NET_RXQUEUE_GET_PACKET_CONTEXT_TOKEN](net-rxqueue-get-packet-context-token.md).

## Syntax

```cpp
PNET_PACKET_CONTEXT_TOKEN FORCEINLINE NetRxQueueGetPacketContextToken(
    _In_    NETRXQUEUE              NetRxQueue,
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

