---
title: NetRingAdvancePacketIterator function
description: The NetRingAdvancePacketIterator method advances the index of a NET_RING_PACKET_ITERATOR by one.
ms.assetid: 517C20D6-78BC-4104-B70A-A2CB99813EB3
keywords:
- NetAdapterCx NetRingAdvancePacketIterator, NetCx NetRingAdvancePacketIterator
ms.date: 11/09/2018
ms.localizationpriority: medium
---

# NetRingAdvancePacketIterator function

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

The NetRingAdvancePacketIterator method advances the index of a [**NET_RING_PACKET_ITERATOR**](net-ring-packet-iterator.md) by one.

## Syntax

```cpp
void NetRingAdvancePacketIterator(
    NET_RING_PACKET_ITERATOR * Iterator
);
```

## Parameters

`Iterator`

A pointer to a [**NET_RING_PACKET_ITERATOR**](net-ring-packet-iterator.md).

## Return Value

None.

## Requirements

|  |  |
| --- | --- |
| Target Platform | Universal |
| Header | netringiterator.h |
| IRQL | Any level as long as target memory is resident |

## See Also

[Net rings and net ring iterators](net-rings-and-net-ring-iterators.md)

[**NET_RING_PACKET_ITERATOR**](net-ring-packet-iterator.md)