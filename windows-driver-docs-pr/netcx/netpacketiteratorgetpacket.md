---
title: NetPacketIteratorGetPacket function
description: The NetPacketIteratorGetPacket method gets the NET_PACKET structure at a NET_RING_PACKET_ITERATOR's current Index.
ms.assetid: 572FC3F5-241B-40ED-A3F1-AE6A21C3EAD7
keywords:
- NetAdapterCx NetPacketIteratorGetPacket, NetCx NetPacketIteratorGetPacket
ms.date: 12/21/2018
ms.localizationpriority: medium
---

# NetPacketIteratorGetPacket function

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

The **NetPacketIteratorGetPacket** method gets the [**NET_PACKET**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netpacket/ns-netpacket-_net_packet) structure at a [**NET_RING_PACKET_ITERATOR**](net-ring-packet-iterator.md)'s current **Index**.

## Syntax

```cpp
NET_PACKET* NetPacketIteratorGetPacket(
    NET_RING_PACKET_ITERATOR const * Iterator
);
```

## Parameters

`Iterator`

A pointer to a [**NET_RING_PACKET_ITERATOR**](net-ring-packet-iterator.md) structure.

## Return Value

Returns a pointer to the **NET_PACKET** structure at the **NET_RING_PACKET_ITERATOR**'s current **Index**.

## Requirements

|  |  |
| --- | --- |
| Target Platform | Universal |
| Header | netringiterator.h |
| IRQL | Any level as long as target memory is resident |

## See Also

[Net rings and net ring iterators](net-rings-and-net-ring-iterators.md)

[**NET_PACKET**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netpacket/ns-netpacket-_net_packet)

[**NET_RING_PACKET_ITERATOR**](net-ring-packet-iterator.md)