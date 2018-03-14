---
title: NET_PACKET_DECLARE_CASTING_FUNCTION macro
description: NET_PACKET_DECLARE_CASTING_FUNCTION macro
ms.assetid: 0E369C3A-3889-4BA2-B0E3-78A363F7218B
keywords:
- WDF Network Adapter Class Extension NET_PACKET_DECLARE_CASTING_FUNCTION, NetAdapterCx NET_PACKET_DECLARE_CASTING_FUNCTION, NetCx NET_PACKET_DECLARE_CASTING_FUNCTION
ms.author: windowsdriverdev
ms.date: 09/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# NET_PACKET_DECLARE_CASTING_FUNCTION macro

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

The **NET_PACKET_DECLARE_CASTING_FUNCTION** macro declares a casting function for a [NET_PACKET](net-packet.md) context space. 

> [!WARNING]
> This macro is reserved for NetAdapterCx. Client drivers must not call this macro directly. Instead, they should call [NET_PACKET_DECLARE_CONTEXT_TYPE_WITH_NAME](net-packet-declare-context-type-with-name.md).

## Syntax

```cpp
void NET_PACKET_DECLARE_CASTING_FUNCTION(
    _contexttype,
    _castingfunction
);
```

## Requirements

|     |     |
| --- | --- |
| Target platform | Universal |
| Minimum KMDF version | 1.21 |
| Minimum NetAdapterCx version | 1.0 |
| Header | NetAdapterPacket.h (include NetAdapterCx.h) |

