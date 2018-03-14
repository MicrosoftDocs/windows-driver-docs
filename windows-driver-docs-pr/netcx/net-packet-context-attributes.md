---
title: NET_PACKET_CONTEXT_ATTRIBUTES structure
description: NET_PACKET_CONTEXT_ATTRIBUTES structure
ms.assetid: 16543429-9BD5-472F-A5AC-72FB2EE50267
keywords:
- WDF Network Adapter Class Extension NET_PACKET_CONTEXT_ATTRIBUTES, NetAdapterCx NET_PACKET_CONTEXT_ATTRIBUTES, NetCx NET_PACKET_CONTEXT_ATTRIBUTES
ms.author: windowsdriverdev
ms.date: 09/05/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# NET_PACKET_CONTEXT_ATTRIBUTES structure

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

The NET_PACKET_CONTEXT_ATTRIBUTES structure represents attributes for a [NET_PACKET](net-packet.md) context space.

## Syntax

```cpp
typedef struct _NET_PACKET_CONTEXT_ATTRIBUTES{
    ULONG                   Size;
    size_t                  ContextSizeOverride;
    PCNET_CONTEXT_TYPE_INFO ContextTypeInfo;
} NET_PACKET_CONTEXT_ATTRIBUTES, *PNET_PACKET_CONTEXT_ATTRIBUTES;
```

## Members

**Size**  
The size of this structure, in bytes.

**ContextSizeOverride**  
If this member is not set to zero, it represents the context size to use when allocating the packet context.

**ContextTypeInfo**  
A pointer to a [**WDF_OBJECT_CONTEXT_TYPE_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff552407) structure.

## Remarks

Initialize this structure with a context type by calling [NET_PACKET_CONTEXT_ATTRIBUTES_INIT_TYPE](net-packet-context-attributes-init-type.md).

## Requirements

|     |     |
| --- | --- |
| Minimum KMDF version | 1.23 |
| Minimum NetAdapterCx version | 1.1 |
| Header | Netrxqueue.h (include NetAdapterCx.h) |

