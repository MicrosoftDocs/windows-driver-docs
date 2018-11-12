---
title: NetRingPacketIteratorGetCount function
description: The NetRingPacketIteratorGetCount method gets the count of packets between a packet iterator's current Index inclusive and its End index.
ms.assetid: 7751D323-C654-4650-BE54-75561290DA5D
keywords:
- NetAdapterCx NetRingPacketIteratorGetCount, NetCx NetRingPacketIteratorGetCount
ms.date: 11/09/2018
ms.localizationpriority: medium
---

# NetRingPacketIteratorGetCount function

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

The **NetRingPacketIteratorGetCount** method gets the count of packets between a packet iterator's current **Index** inclusive and its **End** index.

## Syntax

```cpp
UINT32 NetRingPacketIteratorGetCount(
    NET_RING_PACKET_ITERATOR const * Iterator
);
```

## Parameters

`Iterator`

A pointer to a [**NET_PACKET_ITERATOR**](net-packet-iterator.md).

## Return Value

Returns the number of packets between this packet iterator's current index inclusive and its **End** index. For example, if the iterator's **Index** is **1** and its **End** index is **5**, the iterator currently covers **4** packets: **1**, **2**, **3**, and **4**.

## Requirements

|  |  |
| --- | --- |
| Target Platform | Universal |
| Header | netringiterator.h |
| IRQL | Any level as long as target memory is resident |

## See Also

[Using net rings and net ring iterators](using-net-rings-and-net-ring-iterators.md)

[**NET_PACKET_ITERATOR**](net-packet-iterator.md)