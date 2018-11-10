---
title: NetRingSetTxPostPacketIterator function
description: The NetRingSetTxPostPacketIterator method advances the beginning of the post section for a transmit (Tx) queue's packet ring to the current index of the ring's post packet iterator.
ms.assetid: 8B86626F-CE3F-4806-A1B8-B0C6BC3E95F4
keywords:
- NetAdapterCx NetRingSetTxPostPacketIterator, NetCx NetRingSetTxPostPacketIterator
ms.date: 11/08/2018
ms.localizationpriority: medium
---

# NetRingSetTxPostPacketIterator function

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

The **NetRingSetTxPostPacketIterator** method advances the beginning of the post section for a transmit (Tx) queue's packet ring to the current index of the ring's post packet iterator.

## Syntax

```cpp
void NetRingSetTxPostPacketIterator(
    NET_RING_PACKET_ITERATOR const * Iterator
);
```

## Parameters

`Iterator`

A pointer to the net packet ring's post [**NET_RING_PACKET_ITERATOR**](net-ring-packet-iterator.md) that the driver previously acquired through a call to [**NetRingGetTxPostPacketIterator**](netringgettxpostpacketiterator.md).

## Return Value

None.

## Remarks

Client drivers call **NetRingSetTxPostPacketIterator** to complete the process of posting packets for Tx.

After calling **NetRingSetTxPostPacketIterator**, the packet ring's **NextIndex** advances to the [**NET_RING_PACKET_ITERATOR**](net-ring-packet-iterator.md)'s current position in the ring. Therefore, the packets between the old value of **NextIndex** and the iterator's **Index - 1** inclusive have had their fragments posted to hardware and are transferred to the drain section of the ring.

For an animation and code example of posting hardware, see [Using net rings and net ring iterators](using-net-rings-and-net-ring-iterators.md).

## Requirements

|  |  |
| --- | --- |
| Target Platform | Universal |
| Header | netringiterator.h |
| IRQL | Any level as long as target memory is resident |

## See Also

[Using net rings and net ring iterators](using-net-rings-and-net-ring-iterators.md)

[**NET_RING_PACKET_ITERATOR**](net-ring-packet-iterator.md)

[**NetRingGetTxPostPacketIterator**](netringgettxpostpacketiterator.md)