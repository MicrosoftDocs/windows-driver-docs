---
title: NetRingIteratorGetPacket function
description: The NetRingIteratorGetPacket method gets the NET_PACKET structure pointed to by a NET_RING_PACKET_ITERATOR.
ms.assetid: 572FC3F5-241B-40ED-A3F1-AE6A21C3EAD7
keywords:
- NetAdapterCx NetRingIteratorGetPacket, NetCx NetRingIteratorGetPacket
ms.date: 10/30/2018
ms.localizationpriority: medium
---

# NetRingIteratorGetPacket function

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

The NetRingIteratorGetPacket method gets the [**NET_PACKET**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netpacket/ns-netpacket-_net_packet) structure pointed to by a [[**NET_RING_PACKET_ITERATOR**](net-ring-packet-iterator.md).

## Syntax

```cpp
NET_PACKET* NetRingIteratorGetPacket(
    NET_RING_PACKET_ITERATOR const * Iterator
);
```

## Parameters

`Iterator`

A pointer to a [**NET_RING_PACKET_ITERATOR**](net-ring-packet-iterator.md) structure.

## Return Value

Returns a pointer to the **NET_PACKET** structure pointed to by the **NET_RING_PACKET_ITERATOR**.

## Requirements

|  |  |
| --- | --- |
| Target Platform | Universal |
| Header | netringiterator.h (include netadaptercx.h) |
| Library | NetAdapterCxStub.lib |
| IRQL | PASSIVE_LEVEL |

[Net rings and net ring iterators](net-rings-and-net-ring-iterators.md)