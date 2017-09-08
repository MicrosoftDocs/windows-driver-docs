---
title: NetRxQueueInitAddPacketContextAttributes method
description: NetRxQueueInitAddPacketContextAttributes method
ms.assetid: ED6DC974-6110-4651-973D-4AAF2A148E9B
keywords:
- WDF Network Adapter Class Extension NetRxQueueInitAddPacketContextAttributes, NetAdapterCx NetRxQueueInitAddPacketContextAttributes, NetCx NetRxQueueInitAddPacketContextAttributes
ms.author: windowsdriverdev
ms.date: 09/06/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# NetRxQueueInitAddPacketContextAttributes method

The **NetRxQueueInitAddPacketContextAttributes** method adds an initialized [NET_PACKET_CONTEXT_ATTRIBUTES](net-packet-context-attributes.md) structure to a receive queue's packet context space.

## Syntax

```cpp
NTSTATUS FORCEINLINE NetRxQueueInitAddPacketContextAttributes(
    _Inout_ PNETRXQUEUE_INIT                NetRxQueueInit,
    _In_    PNET_PACKET_CONTEXT_ATTRIBUTES  PacketContextAttributes
);
```

## Parameters

*NetRxQueueInit* [in, out]  
A pointer to the **NETRXQUEUE_INIT** structure that the client driver received in [*EVT_NET_ADAPTER_CREATE_RXQUEUE*](evt-net-adapter-create-rxqueue.md).

*PacketContextAttributes* [in]  
A pointer to an initialized [NET_PACKET_CONTEXT_ATTRIBUTES](net-packet-context-attributes.md) structure that represents attributes for the context space of each [NET_PACKET](net-packet.md) in this queue.

## Return value

If the operation is successful, theis method must return STATUS_SUCCESS, or another status value for which NT_SUCCESS(status) equals TRUE. Otherwise, an appropriate [NTSTATUS](https://msdn.microsoft.com/library/windows/hardware/ff557697) error code.

## Remarks

The NETRXQUEUE_INIT structure is an opaque structure that is defined and allocated by NetAdapterCx, similar to WDFDEVICE_INIT. The client driver receives a pointer to the NETRXQUEUE_INIT object in its [*EVT_NET_ADAPTER_CREATE_RXQUEUE*](evt-net-adapter-create-rxqueue.md) callback function, where this method can be optionally called to add additional information to the receive queue's packet context space.

## Requirements

|     |     |
| --- | --- |
| Target platform | Universal |
| Minimum KMDF version | 1.23 |
| Minimum NetAdapterCx version | 1.1 |
| Header | Netrxqueue.h (include NetAdapterCx.h) |
| IRQL | PASSIVE_LEVEL |

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20Planning%20your%20APN%20database%20submission%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")