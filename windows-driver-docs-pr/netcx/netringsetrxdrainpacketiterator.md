---
title: NetRingSetRxDrainPacketIterator function
description: The NetRingSetRxDrainPacketIterator method advances the beginning of the drain section for a receive (Rx) queue's packet ring to the current index of the ring's drain packet iterator.
ms.assetid: DE28AAFC-BDD9-4025-B0A5-3778CA4581DB
keywords:
- NetAdapterCx NetRingSetRxDrainPacketIterator, NetCx NetRingSetRxDrainPacketIterator
ms.date: 11/08/2018
ms.localizationpriority: medium
---

# NetRingSetRxDrainPacketIterator function

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

The **NetRingSetRxDrainPacketIterator** method advances the beginning of the drain section for a receive (Rx) queue's packet ring to the current index of the ring's drain packet iterator.

## Syntax

```cpp
void NetRingSetRxDrainPacketIterator(
    NET_RING_PACKET_ITERATOR const * Iterator
);
```

## Parameters

`Iterator`

A pointer to the net packet ring's drain [**NET_RING_PACKET_ITERATOR**](net-ring-packet-iterator.md) that the driver previously acquired through a call to [**NetRingGetRxDrainPacketIterator**](netringgetrxdrainpacketiterator.md).

## Return Value

None.

## Remarks

Client drivers call **NetRingSetRxDrainPacketIterator** to complete the process of draining receive packets from the packet ring to the OS.

After calling this method, the packet ring's **BeginIndex** advances to the [**NET_RING_PACKET_ITERATOR**](net-ring-packet-iterator.md)'s current position in the ring. Therefore, the packets between the old value of **BeginIndex** and the iterator's **Index - 1** inclusive are drained from the ring and ownership of them is transferred to the OS. This is how client drivers indicate receives to the system.

For an animation and code example of draining packets back to the OS, see [Using net rings and net ring iterators](using-net-rings-and-net-ring-iterators.md).

## Requirements

|  |  |
| --- | --- |
| Target Platform | Universal |
| Header | netringiterator.h |
| IRQL | PASSIVE_LEVEL |

## See Also

[Using net rings and net ring iterators](using-net-rings-and-net-ring-iterators.md)

[**NET_RING_PACKET_ITERATOR**](net-ring-packet-iterator.md)

[**NetRingGetRxDrainPacketIterator**](netringgetrxdrainpacketiterator.md)