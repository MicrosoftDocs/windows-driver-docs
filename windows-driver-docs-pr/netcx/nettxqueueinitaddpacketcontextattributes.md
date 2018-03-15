---
title: NetTxQueueInitAddPacketContextAttributes method
description: NetTxQueueInitAddPacketContextAttributes method
ms.assetid: 1B340C8E-0A9A-4C06-BC0C-A956E8745DBE
keywords:
- WDF Network Adapter Class Extension NetTxQueueInitAddPacketContextAttributes, NetAdapterCx NetTxQueueInitAddPacketContextAttributes, NetCx NetTxQueueInitAddPacketContextAttributes
ms.author: windowsdriverdev
ms.date: 09/06/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# NetTxQueueInitAddPacketContextAttributes method

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

The **NetTxQueueInitAddPacketContextAttributes** method adds an initialized [NET_PACKET_CONTEXT_ATTRIBUTES](net-packet-context-attributes.md) structure to a transmit queue's packet context space.

## Syntax

```cpp
NTSTATUS FORCEINLINE NetTxQueueInitAddPacketContextAttributes(
    _Inout_ PNETTXQUEUE_INIT                NetTxQueueInit,
    _In_    PNET_PACKET_CONTEXT_ATTRIBUTES  PacketContextAttributes
);
```

## Parameters

*NetTxQueueInit* [in, out]  
A pointer to the **NETTXQUEUE_INIT** structure that the client driver received in [*EVT_NET_ADAPTER_CREATE_TXQUEUE*](evt-net-adapter-create-txqueue.md).

*PacketContextAttributes* [in]  
A pointer to an initialized [NET_PACKET_CONTEXT_ATTRIBUTES](net-packet-context-attributes.md) structure that represents attributes for the context space of each [NET_PACKET](net-packet.md) in this queue.

## Return value

If the operation is successful, this method must return STATUS_SUCCESS, or another status value for which NT_SUCCESS(status) equals TRUE. Otherwise, an appropriate [NTSTATUS](https://msdn.microsoft.com/library/windows/hardware/ff557697) error code.

## Remarks

The NETTXQUEUE_INIT structure is an opaque structure that is defined and allocated by NetAdapterCx, similar to WDFDEVICE_INIT. The client driver receives a pointer to the NETTXQUEUE_INIT object in its [*EVT_NET_ADAPTER_CREATE_TXQUEUE*](evt-net-adapter-create-txqueue.md) callback function, where this method is called to add context attributes to the queue for each packet context the driver has created.

## Requirements

|     |     |
| --- | --- |
| Target platform | Universal |
| Minimum KMDF version | 1.23 |
| Minimum NetAdapterCx version | 1.1 |
| Header | Nettxqueue.h (include NetAdapterCx.h) |
| IRQL | PASSIVE_LEVEL |

