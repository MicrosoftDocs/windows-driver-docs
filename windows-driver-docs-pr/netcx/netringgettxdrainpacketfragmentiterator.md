---
title: NetRingGetTxDrainPacketFragmentIterator function
description: For a packet in the drain section of a transmit (Tx) queue's packet ring, the NetRingGetTxPostPacketFragmentIterator method gets the drain fragment iterator for that packet's fragments.
ms.assetid: F9A722E3-C532-4930-B0D4-154991313F79
keywords:
- NetAdapterCx NetRingGetTxDrainPacketFragmentIterator, NetCx NetRingGetTxDrainPacketFragmentIterator
ms.date: 11/08/2018
ms.localizationpriority: medium
---

# NetRingGetTxDrainPacketFragmentIterator function

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

For a packet in the drain section of a transmit (Tx) queue's packet ring, the **NetRingGetTxDrainPacketFragmentIterator** method gets the drain fragment iterator for that packet's fragments.

## Syntax

```cpp
NET_RING_FRAGMENT_ITERATOR NetRingGetTxDrainPacketFragmentIterator(
    NET_RING_PACKET_ITERATOR const * Iterator
);
```

## Parameters

`Iterator`

A pointer to a [**NET_RING_PACKET_ITERATOR**](net-ring-packet-iterator.md) that is currently pointing to a packet in the drain section of the transmit queue's packet ring.

## Return Value

Returns a [**NET_RING_FRAGMENT_ITERATOR**](net-ring-fragment-iterator.md) that begins at the first fragment belonging to this packet and ends at the last fragment belonging to this packet.

## Remarks

Client drivers typically call **NetRingGetTxDrainPacketFragmentIterator** to begin the process of draining transmitted fragments from the fragment ring to the OS. Drivers later complete this process by calling [**NetRingSetTxDrainFragmentIterator**](netringsettxdrainfragmentiterator.md).

For an animation and code example of draining fragments from the fragment ring to the OS for Tx, see [Using net rings and net ring iterators](using-net-rings-and-net-ring-iterators.md).

## Requirements

|  |  |
| --- | --- |
| Target Platform | Universal |
| Header | netringiterator.h |
| IRQL | PASSIVE_LEVEL |

## See Also

[Using net rings and net ring iterators](using-net-rings-and-net-ring-iterators.md)

[**NET_RING_PACKET_ITERATOR**](net-ring-packet-iterator.md)

[**NET_RING_FRAGMENT_ITERATOR**](net-ring-fragment-iterator.md)

[**NetRingSetTxDrainFragmentIterator**](netringsettxdrainfragmentiterator.md)