---
title: NetRingGetTxDrainPacketIterator function
description: The NetRingGetTxDrainPacketIterator method gets a packet iterator for the current drain section of a transmit (Tx) queue's packet ring.
ms.assetid: E5A311A1-1DD6-4393-B32D-5BAE29D87824
keywords:
- NetAdapterCx NetRingGetTxDrainPacketIterator, NetCx NetRingGetTxDrainPacketIterator
ms.date: 11/08/2018
ms.localizationpriority: medium
---

# NetRingGetTxDrainPacketIterator function

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

The **NetRingGetTxDrainPacketIterator** method gets a packet iterator for the current drain section of a transmit (Tx) queue's packet ring.

## Syntax

```cpp
NET_RING_PACKET_ITERATOR NetRingGetTxDrainPacketIterator(
    NET_RING_COLLECTION const * Rings
);
```

## Parameters

`Rings`

A pointer to the **NET_RING_COLLECTION** struture that describes the transmit queue's net rings.

## Return Value

Returns a [**NET_RING_PACKET_ITERATOR**](net-ring-packet-iterator.md) that begins at the packet ring's **BeginIndex** and ends at the packet ring's **NextIndex**. In other words, the iterator covers the packet ring's current drain section. 

## Remarks

Client drivers typically call this method to begin the process of draining transmitted packets from the packet ring to the OS. Drivers later complete this process by calling [**NetRingSetTxDrainPacketIterator**](netringsettxdrainpacketiterator.md).

For an animation and code example of draining packets from the ring back to the OS, see [Using net rings and net ring iterators](using-net-rings-and-net-ring-iterators.md).

## Requirements

|  |  |
| --- | --- |
| Target Platform | Universal |
| Header | netringiterator.h |
| IRQL | Any level as long as target memory is resident |

## See Also

[Using net rings and net ring iterators](using-net-rings-and-net-ring-iterators.md)

[**NET_RING_PACKET_ITERATOR**](net-ring-packet-iterator.md)

**NET_RING_COLLECTION**

[**NetRingSetTxDrainPacketIterator**](netringsettxdrainpacketiterator.md)