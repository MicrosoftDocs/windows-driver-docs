---
title: NET_PACKET_DECLARE_CASTING_FUNCTION_FROM_TOKEN macro
description: NET_PACKET_DECLARE_CASTING_FUNCTION_FROM_TOKEN macro
ms.assetid: 3C552958-F97C-4ADA-8E7D-A275C0DFF1CC
keywords:
- WDF Network Adapter Class Extension NET_PACKET_DECLARE_CASTING_FUNCTION_FROM_TOKEN, NetAdapterCx NET_PACKET_DECLARE_CASTING_FUNCTION_FROM_TOKEN, NetCx NET_PACKET_DECLARE_CASTING_FUNCTION_FROM_TOKEN
ms.author: windowsdriverdev
ms.date: 09/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# NET_PACKET_DECLARE_CASTING_FUNCTION_FROM_TOKEN macro

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

The **NET_PACKET_DECLARE_CASTING_FUNCTION_FROM_TOKEN** macro declares a casting function from a [NET_PACKET_CONTEXT_TOKEN](net-packet-context-token.md) for a [NET_PACKET](net-packet.md) context space. 

> [!WARNING]
> This macro is reserved for NetAdapterCx. Client drivers must not call this macro directly. Instead, they should call [NET_PACKET_DECLARE_CONTEXT_TYPE_WITH_NAME](net-packet-declare-context-type-with-name.md).

## Syntax

```cpp
void NET_PACKET_DECLARE_CASTING_FUNCTION_FROM_TOKEN(
    _contexttype,
    _castingfunction
);
```

## Requirements

|     |     |
| --- | --- |
| Target platform | Universal |
| Minimum KMDF version | 1.23 |
| Minimum NetAdapterCx version | 1.1 |
| Header | NetAdapterPacket.h (include NetAdapterCx.h) |

