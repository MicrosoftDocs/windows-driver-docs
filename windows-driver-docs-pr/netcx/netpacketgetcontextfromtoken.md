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

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20Planning%20your%20APN%20database%20submission%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")