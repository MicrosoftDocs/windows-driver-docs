---
title: NetPacketIteratorGetFragments function
description: The NetPacketIteratorGetFragments method gets the fragments associated with a packet.
ms.assetid: 714D76A4-6321-4936-A31A-7E11D18F16BF
keywords:
- NetAdapterCx NetPacketIteratorGetFragments, NetCx NetPacketIteratorGetFragments
ms.date: 01/10/2019
ms.localizationpriority: medium
---

# NetPacketIteratorGetFragments function

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

The **NetPacketIteratorGetFragments** method gets the fragments associated with a packet.

## Syntax

```cpp
NET_RING_FRAGMENT_ITERATOR NetPacketIteratorGetFragments(
    NET_RING_PACKET_ITERATOR const * Iterator
);
```

## Parameters

`Iterator`

A pointer to a [**NET_RING_PACKET_ITERATOR**](net-ring-packet-iterator.md) structure.

## Return Value

Returns a [**NET_RING_FRAGMENT_ITERATOR**](net-ring-fragment-iterator.md) that begins at the first fragment belonging to this packet and ends at the last fragment belonging to this packet.

## Remarks

Client drivers typically call **NetPacketIteratorGetFragments** to begin the process of posting fragments to hardware for transmitting (Tx). 

For an animation and code example of posting fragments to hardware for Tx, see [Net rings and net ring iterators](net-rings-and-net-ring-iterators.md).

## Requirements

|  |  |
| --- | --- |
| Target Platform | Universal |
| Header | netringiterator.h |
| IRQL | Any level as long as target memory is resident |

## See Also

[Net rings and net ring iterators](net-rings-and-net-ring-iterators.md)

[**NET_RING_PACKET_ITERATOR**](net-ring-packet-iterator.md)

[**NET_RING_FRAGMENT_ITERATOR**](net-ring-fragment-iterator.md)