---
title: NetPacketIteratorAdvance function
description: The NetPacketIteratorAdvance method advances the Index of a packet iterator by one.
ms.assetid: 517C20D6-78BC-4104-B70A-A2CB99813EB3
keywords:
- NetAdapterCx NetPacketIteratorAdvance, NetCx NetPacketIteratorAdvance
ms.date: 01/10/2019
ms.localizationpriority: medium
---

# NetPacketIteratorAdvance function

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

The NetPacketIteratorAdvance method advances the **Index** of a packet iterator by one.

## Syntax

```cpp
void NetPacketIteratorAdvance(
    NET_RING_PACKET_ITERATOR * Iterator
);
```

## Parameters

`Iterator`

A pointer to a [**NET_RING_PACKET_ITERATOR**](net-ring-packet-iterator.md) structure.

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