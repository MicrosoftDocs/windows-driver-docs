---
title: NetRingSetAllPacketIterator function
description: The NetRingSetAllPacketIterator method advances the beginning of the section of a packet ring that a client driver owns to the current index of a packet iterator.
ms.assetid: 2A3011C1-14B0-4C28-94BB-FB2A0A1F4CFB
keywords:
- NetAdapterCx NetRingSetAllPacketIterator, NetCx NetRingSetAllPacketIterator
ms.date: 11/09/2018
ms.localizationpriority: medium
---

# NetRingSetAllPacketIterator function

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

The **NetRingSetAllPacketIterator** method advances the beginning of the section of a packet ring that a client driver owns to the current index of a packet iterator.

## Syntax

```cpp
void NetRingSetAllPacketIterator(
    NET_RING_PACKET_ITERATOR const * Iterator
);
```

## Parameters

`Iterator`

A pointer to a [**NET_RING_PACKET_ITERATOR**](net-ring-packet-iterator.md).

## Return Value

None.

## Remarks

Client drivers can acquire the [**NET_RING_PACKET_ITERATOR**](net-ring-packet-iterator.md) through a call to [**NetRingGetAllPacketIterator**](netringgetallpacketiterator.md), though this is not required.

After calling **NetRingSetAllPacketIterator**, the packet ring's **BeginIndex** advances to the **NET_RING_PACKET_ITERATOR**'s current index. Therefore, the packets between the old value of **BeginIndex** and the iterator's **Index - 1** inclusive are transferred to the OS. If the iterator's **Index** equals the packet ring's **EndIndex**, this means the client driver no longer owns any packets.

Client drivers typically call **NetRingSetAllPacketIterator** to finish performing operations on all packets that they own in a packet ring. This might include processing a batch of receives that span all available packets in the ring, or draining the ring during data path cancelation. 

To cancel and drain all packets from the ring back to the OS, a client driver calls these three methods in order:

1. [**NetRingGetAllPacketIterator**](netringgetallpacketiterator.md)
2. [**NetRingAdvanceEndPacketIterator**](netringadvanceendpacketiterator.md)
3. **NetRingSetAllPacketIterator**

For a code example of using this method, see [Net rings and net ring iterators](net-rings-and-net-ring-iterators.md).

## Requirements

|  |  |
| --- | --- |
| Target Platform | Universal |
| Header | netringiterator.h |
| IRQL | Any level as long as target memory is resident |

## See Also

[Net rings and net ring iterators](net-rings-and-net-ring-iterators.md)

[**NET_RING_PACKET_ITERATOR**](net-ring-packet-iterator.md)

[**NetRingGetAllPacketIterator**](netringgetallpacketiterator.md)

[**NetRingAdvanceEndPacketIterator**](netringadvanceendpacketiterator.md)