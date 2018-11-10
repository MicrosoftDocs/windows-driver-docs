---
title: NetRingGetTxPostPacketIterator function
description: The NetRingGetTxPostPacketIterator method gets a packet iterator for the current post section of a transmit (Tx) queue's packet ring.
ms.assetid: AFF6B47D-02C4-4038-97DE-99CC5A56DB3F
keywords:
- NetAdapterCx NetRingGetTxPostPacketIterator, NetCx NetRingGetTxPostPacketIterator
ms.date: 11/08/2018
ms.localizationpriority: medium
---

# NetRingGetTxPostPacketIterator function

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

The **NetRingGetTxPostPacketIterator** method gets a packet iterator for the current post section of a transmit (Tx) queue's packet ring.

## Syntax

```cpp
NET_RING_PACKET_ITERATOR NetRingGetTxPostPacketIterator(
    NET_RING_COLLECTION const * Rings
);
```

## Parameters

`Rings`

A pointer to the **NET_RING_COLLECTION** struture that describes the transmit queue's net rings.

## Return Value

Returns a [**NET_RING_PACKET_ITERATOR**](net-ring-packet-iterator.md) that begins at the packet ring's **NextIndex** and ends at the packet ring's **EndIndex**. In other words, the iterator covers the packet ring's current post section. 

## Remarks

Client drivers typically call this method to begin the process of posting packets for Tx. Drivers later complete this process by calling [**NetRingSetTxPostPacketIterator**](netringsettxpostpacketiterator.md).

For an animation and code example of posting packets, see [Using net rings and net ring iterators](using-net-rings-and-net-ring-iterators.md).

## Requirements

|  |  |
| --- | --- |
| Target Platform | Universal |
| Header | netringiterator.h |
| IRQL | Any level as long as target memory is resident |

## See Also

[Using net rings and net ring iterators](using-net-rings-and-net-ring-iterators.md)

[**NET_RING_PACKET_ITERATOR**](net-ring-packet-iterator.md)

[**NetRingSetTxPostPacketIterator**](netringsettxpostpacketiterator.md)