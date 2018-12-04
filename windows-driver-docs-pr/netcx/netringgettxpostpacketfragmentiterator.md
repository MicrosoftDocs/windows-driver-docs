---
title: NetRingGetTxPostPacketFragmentIterator function
description: For a packet in the post section of a transmit (Tx) queue's packet ring, the NetRingGetTxPostPacketFragmentIterator method gets the post fragment iterator for that packet's fragments.
ms.assetid: 714D76A4-6321-4936-A31A-7E11D18F16BF
keywords:
- NetAdapterCx NetRingGetTxPostPacketFragmentIterator, NetCx NetRingGetTxPostPacketFragmentIterator
ms.date: 11/08/2018
ms.localizationpriority: medium
---

# NetRingGetTxPostPacketFragmentIterator function

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

For a packet in the post section of a transmit (Tx) queue's packet ring, the **NetRingGetTxPostPacketFragmentIterator** method gets the post fragment iterator for that packet's fragments.

## Syntax

```cpp
NET_RING_FRAGMENT_ITERATOR NetRingGetTxPostPacketFragmentIterator(
    NET_RING_PACKET_ITERATOR const * Iterator
);
```

## Parameters

`Iterator`

A pointer to a [**NET_RING_PACKET_ITERATOR**](net-ring-packet-iterator.md) that is currently pointing to a packet in the post section of the transmit queue's packet ring.

## Return Value

Returns a [**NET_RING_FRAGMENT_ITERATOR**](net-ring-fragment-iterator.md) that begins at the first fragment belonging to this packet and ends at the last fragment belonging to this packet.

## Remarks

Client drivers typically call **NetRingGetTxPostPacketFragmentIterator** to begin the process of posting fragments to hardware for Tx. Drivers later complete this process by calling [**NetRingSetTxPostFragmentIterator**](netringsettxpostfragmentiterator.md).

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

[**NetRingSetTxPostFragmentIterator**](netringsettxpostfragmentiterator.md)