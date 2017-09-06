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

The NET_PACKET_CONTEXT_ATTRIBUTES structure represents attributes for a [NET_PACKET](net-packet.md) structure's context space.

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

## Requirements

|     |     |
| --- | --- |
| Minimum KMDF version | 1.23 |
| Minimum NetAdapterCx version | 1.1 |
| Header | Netrxqueue.h (include NetAdapterCx.h) |

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20Planning%20your%20APN%20database%20submission%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")