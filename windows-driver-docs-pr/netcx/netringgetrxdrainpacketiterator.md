---
title: NetRingGetRxDrainPacketIterator function
description: The NetRingGetRxDrainPacketIterator method gets a packet iterator for the current drain section of a receive (Rx) queue's packet ring.
ms.assetid: 121A80A2-7FCC-453E-93C6-D66B7AA70C1F
keywords:
- NetAdapterCx NetRingGetRxDrainPacketIterator, NetCx NetRingGetRxDrainPacketIterator
ms.date: 11/08/2018
ms.localizationpriority: medium
---

# NetRingGetRxDrainPacketIterator function

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

The **NetRingGetRxDrainPacketIterator** method gets a packet iterator for the current drain section of a receive (Rx) queue's packet ring.

## Syntax

```cpp
NET_RING_PACKET_ITERATOR NetRingGetRxDrainPacketIterator(
    NET_RING_COLLECTION const * Rings
);
```

## Parameters

`Rings`

A pointer to the **NET_RING_COLLECTION** struture that describes the receive queue's net rings.

## Return Value

Returns a [**NET_RING_PACKET_ITERATOR**](net-ring-packet-iterator.md) that begins at the packet ring's **BeginIndex** and ends at the packet ring's **EndIndex**. In other words, the iterator covers the packet ring's current drain section. 

## Remarks

Client drivers typically call this method to begin the process of draining receive packets from the packet ring to the OS. Drivers later complete this process by calling [**NetRingSetRxDrainPacketIterator**](netringsetrxdrainpacketiterator.md).

For an animation and code example of draining packets from the ring back to the OS, see [Net rings and net ring iterators](net-rings-and-net-ring-iterators.md).

## Requirements

|  |  |
| --- | --- |
| Target Platform | Universal |
| Header | netringiterator.h |
| IRQL | Any level as long as target memory is resident |

## See Also

[Net rings and net ring iterators](net-rings-and-net-ring-iterators.md)

[**NET_RING_PACKET_ITERATOR**](net-ring-packet-iterator.md)

**NET_RING_COLLECTION**

[**NetRingSetRxDrainPacketIterator**](netringsetrxdrainpacketiterator.md)