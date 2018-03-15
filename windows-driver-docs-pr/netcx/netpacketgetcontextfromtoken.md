---
title: NetPacketGetContextFromToken method
description: NetPacketGetContextFromToken method
ms.assetid: 518EEEB6-9667-4EE9-BD2E-D3B3D88B7AF2
keywords:
- WDF Network Adapter Class Extension NetPacketGetContextFromToken, NetAdapterCx NetPacketGetContextFromToken, NetCx NetPacketGetContextFromToken
ms.author: windowsdriverdev
ms.date: 09/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# NetPacketGetContextFromToken method

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

The **NetPacketGetContextFromToken** method retrieves a [NET_PACKET](net-packet.md) context based on a [NET_PACKET_CONTEXT_TOKEN](net-packet-context-token.md).

> [!WARNING]
> This method is reserved for NetAdapterCx. Client drivers must not call this method directly. Instead, they should call an accessor method created by a call to [NET_PACKET_DECLARE_CONTEXT_TYPE_WITH_NAME](net-packet-declare-context-type-with-name.md).

## Syntax

```cpp
PVOID FORCEINLINE NetPacketGetContextFromToken(
    _In_    NET_PACKET*                 NetPacket,
    _In_    PNET_PACKET_CONTEXT_TOKEN   Token
);
```

## Requirements

|     |     |
| --- | --- |
| Target platform | Universal |
| Minimum KMDF version | 1.23 |
| Minimum NetAdapterCx version | 1.1 |
| Header | Netadapterpacket.h (include NetAdapterCx.h) |
| IRQL | DISPATCH_LEVEL |

