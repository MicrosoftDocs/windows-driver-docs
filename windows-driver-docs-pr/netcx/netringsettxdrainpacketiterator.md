---
title: NetRingSetTxDrainPacketIterator function
description: The NetRingSetTxDrainPacketIterator method advances the beginning of the drain section for a transmit (Tx) queue's packet ring to the current index of the ring's drain packet iterator.
ms.assetid: 7A26E7A0-6E61-44FE-83D0-CE1581733C2D
keywords:
- NetAdapterCx NetRingSetTxDrainPacketIterator, NetCx NetRingSetTxDrainPacketIterator
ms.date: 11/08/2018
ms.localizationpriority: medium
---

# NetRingSetTxDrainPacketIterator function

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

The **NetRingSetTxDrainPacketIterator** method advances the beginning of the drain section for a transmit (Tx) queue's packet ring to the current index of the ring's drain packet iterator.

## Syntax

```cpp
void NetRingSetTxDrainPacketIterator(
    NET_RING_PACKET_ITERATOR const * Iterator
);
```

## Parameters

`Iterator`

A pointer to the net packet ring's drain [**NET_RING_PACKET_ITERATOR**](net-ring-packet-iterator.md) that the driver previously acquired through a call to [**NetRingGetTxDrainPacketIterator**](netringgettxdrainpacketiterator.md).

## Return Value

None.

## Remarks

Client drivers call **NetRingSetRxDrainPacketIterator** to complete the process of draining transmit packets from the packet ring to the OS.

After calling this method, the packet ring's **BeginIndex** advances to the [**NET_RING_PACKET_ITERATOR**](net-ring-packet-iterator.md)'s current position in the ring. Therefore, the packets between the old value of **BeginIndex** and the iterator's **Index - 1** inclusive are drained from the ring and ownership of them is transferred to the OS. This is how client drivers return completed transmit packets to the system.

For an animation and code example of draining packets back to the OS, see [Net rings and net ring iterators](net-rings-and-net-ring-iterators.md).

## Requirements

|  |  |
| --- | --- |
| Target Platform | Universal |
| Header | netringiterator.h |
| IRQL | Any level as long as target memory is resident |

## See Also

[Net rings and net ring iterators](net-rings-and-net-ring-iterators.md)

[**NET_RING_PACKET_ITERATOR**](net-ring-packet-iterator.md)

[**NetRingGetTxDrainPacketIterator**](netringgettxdrainpacketiterator.md)