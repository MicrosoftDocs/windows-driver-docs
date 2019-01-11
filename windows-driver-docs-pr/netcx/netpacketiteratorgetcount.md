---
title: NetPacketIteratorGetCount function
description: The NetPacketIteratorGetCount method gets the count of packets that a client driver owns in the packet ring.
ms.assetid: 7751D323-C654-4650-BE54-75561290DA5D
keywords:
- NetAdapterCx NetPacketIteratorGetCount, NetCx NetPacketIteratorGetCount
ms.date: 01/10/2019
ms.localizationpriority: medium
---

# NetPacketIteratorGetCount function

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

The **NetPacketIteratorGetCount** method gets the count of packets that a client driver owns in the packet ring.

## Syntax

```cpp
UINT32 NetPacketIteratorGetCount(
    NET_RING_PACKET_ITERATOR const * Iterator
);
```

## Parameters

`Iterator`

A pointer to a [**NET_RING_PACKET_ITERATOR**](net-ring-packet-iterator.md) structure.

## Return Value

Returns the number of packets between this packet iterator's current **Index** and **EndIndex - 1** inclusive. For example, if the iterator's **Index** is **1** and its **End** index is **5**, the client driver owns **4** packets: **1**, **2**, **3**, and **4**.

## Requirements

|  |  |
| --- | --- |
| Target Platform | Universal |
| Header | netringiterator.h |
| IRQL | Any level as long as target memory is resident |

## See Also

[Net rings and net ring iterators](net-rings-and-net-ring-iterators.md)

[**NET_RING_PACKET_ITERATOR**](net-ring-packet-iterator.md)