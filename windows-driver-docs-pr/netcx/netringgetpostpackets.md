---
title: NetRingGetPostPackets function
description: The NetRingGetPostPackets method gets a packet iterator for the post subsection of a packet ring.
ms.assetid: AFF6B47D-02C4-4038-97DE-99CC5A56DB3F
keywords:
- NetAdapterCx NetRingGetPostPackets, NetCx NetRingGetPostPackets
ms.date: 12/18/2018
ms.localizationpriority: medium
---

# NetRingGetPostPackets function

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

The **NetRingGetPostPackets** method gets a packet iterator for the post subsection of a packet ring.

## Syntax

```cpp
NET_RING_PACKET_ITERATOR NetRingGetPostPackets(
    NET_RING_COLLECTION const * Rings
);
```

## Parameters

`Rings`

A pointer to the **NET_RING_COLLECTION** struture that describes this packet queue's net rings.

## Return Value

Returns a [**NET_RING_PACKET_ITERATOR**](net-ring-packet-iterator.md) that begins at the packet ring's **NextIndex** and ends at the packet ring's **EndIndex**. In other words, the iterator covers the packet ring's current post section. 

## Remarks

Client drivers typically call this method to begin the process of posting packets. Drivers later complete this process by calling [**NetPacketIteratorSet**](netpacketiteratorset.md).

For an animation and code example of posting packets, see [Net rings and net ring iterators](net-rings-and-net-ring-iterators.md).

## Requirements

|  |  |
| --- | --- |
| Target Platform | Universal |
| Header | netringiterator.h |
| IRQL | Any level as long as target memory is resident |

## See Also

[Net rings and net ring iterators](net-rings-and-net-ring-iterators.md)

[**NET_RING_PACKET_ITERATOR**](net-ring-packet-iterator.md)

[**NetPacketIteratorSet**](netpacketiteratorset.md)