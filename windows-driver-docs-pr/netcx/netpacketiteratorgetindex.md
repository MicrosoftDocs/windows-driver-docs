---
title: NetPacketIteratorGetIndex method
description: The NetPacketIteratorGetIndex method gets the current Index of a packet iterator in the packet ring.
ms.assetid: D9239E11-A366-44B8-B1A4-A58C986FBDFE
keywords:
- NetAdapterCx NetPacketIteratorGetIndex, NetCx NetPacketIteratorGetIndex
ms.date: 12/21/2018
ms.localizationpriority: medium
---

# NetPacketIteratorGetIndex method

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

The **NetPacketIteratorGetIndex** method gets the current **Index** of a packet iterator in the packet ring.

## Syntax

```cpp
UINT32 NetPacketIteratorGetIndex(
    NET_RING_PACKET_ITERATOR const * Iterator
);
```

## Parameters

`Iterator`

A pointer to a [**NET_RING_PACKET_ITERATOR**](net-ring-packet-iterator.md) structure.

## Return Value

Returns the packet iterator's current **Index**.

## Requirements

|  |  |
| --- | --- |
| Target Platform | Universal |
| Header | netringiterator.h |
| IRQL | Any level as long as target memory is resident |

## See Also

[Net rings and net ring iterators](net-rings-and-net-ring-iterators.md)

[**NET_RING_PACKET_ITERATOR**](net-ring-packet-iterator.md)