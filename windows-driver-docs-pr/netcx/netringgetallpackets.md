---
title: NetRingGetAllPackets function
description: The NetRingGetAllPackets method gets a packet iterator for the entire range in a packet ring that a client driver owns.
ms.assetid: AD14CCD5-AB95-4130-88B8-D5B8E8176B50
keywords:
- NetAdapterCx NetRingGetAllPackets, NetCx NetRingGetAllPackets
ms.date: 12/21/2018
ms.localizationpriority: medium
---

# NetRingGetAllPackets function

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

The **NetRingGetAllPackets** method gets a packet iterator for the entire range in a packet ring that a client driver owns.

## Syntax

```cpp
NET_RING_PACKET_ITERATOR NetRingGetAllPackets(
    NET_RING_COLLECTION const * Rings
);
```

## Parameters

`Rings`

A pointer to the **NET_RING_COLLECTION** struture that describes this packet queue's net rings.

## Return Value

Returns a [**NET_RING_PACKET_ITERATOR**](net-ring-packet-iterator.md) that begins at the packet ring's **BeginIndex** and ends at the packet ring's **EndIndex**. In other words, the iterator covers all packets in the ring that the driver currently owns including the post subsection and the drain subsection. 

## Remarks

Client drivers typically call **NetRingGetAllPackets** to begin performing operations on all packets that they own in a packet ring. This might include processing a batch of receives that span all available packets in the ring, or draining the ring during data path cancellation.

For a code example of using this method, see [Net rings and net ring iterators](net-rings-and-net-ring-iterators.md).

## Requirements

|  |  |
| --- | --- |
| Target Platform | Universal |
| Header | netringiterator.h |
| IRQL | Any level as long as target memory is resident |

## See Also

[Net rings and net ring iterators](net-rings-and-net-ring-iterators.md)

**NET_RING_COLLECTION**

[**NET_RING_PACKET_ITERATOR**](net-ring-packet-iterator.md)