---
title: NetRingGetAllPacketIterator function
description: The NetRingGetAllPacketIterator method gets a packet iterator for the entire range in a packet ring that a client driver owns.
ms.assetid: AD14CCD5-AB95-4130-88B8-D5B8E8176B50
keywords:
- NetAdapterCx NetRingGetAllPacketIterator, NetCx NetRingGetAllPacketIterator
ms.date: 11/08/2018
ms.localizationpriority: medium
---

# NetRingGetAllPacketIterator function

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

The **NetRingGetAllPacketIterator** method gets a packet iterator for the entire range in a packet ring that a client driver owns.

## Syntax

```cpp
NET_RING_PACKET_ITERATOR NetRingGetAllPacketIterator(
    NET_RING_COLLECTION const * Rings
);
```

## Parameters

`Rings`

A pointer to the **NET_RING_COLLECTION** struture that describes the packet queue's net rings.

## Return Value

Returns a [**NET_RING_PACKET_ITERATOR**](net-ring-packet-iterator.md) that begins at the packet ring's **BeginIndex** and ends at the packet ring's **EndIndex**. In other words, the iterator covers both the ring's post section and its drain section, or all packets in the ring that the driver currently owns. 

## Remarks

Client drivers typically call **NetRingGetAllPacketIterator** to begin performing operations on all packets that they own in a packet ring. This might include processing a batch of receives that span all available packets in the ring, or draining the ring during data path cancelation.

To cancel and drain all packets from the ring back to the OS, a client driver calls these three methods in order:

1. **NetRingGetAllPacketIterator**
2. [**NetRingAdvanceEndPacketIterator**](netringadvanceendpacketiterator.md)
3. [**NetRingSetAllPacketIterator**](netringsetallpacketiterator.md)

For a code example of using this method, see [Using net rings and net ring iterators](using-net-rings-and-net-ring-iterators.md).

## Requirements

|  |  |
| --- | --- |
| Target Platform | Universal |
| Header | netringiterator.h |
| IRQL | Any level as long as target memory is resident |

## See Also

[Using net rings and net ring iterators](using-net-rings-and-net-ring-iterators.md)

**NET_RING_COLLECTION**

[**NET_RING_PACKET_ITERATOR**](net-ring-packet-iterator.md)

[**NetRingAdvanceEndPacketIterator**](netringadvanceendpacketiterator.md)

[**NetRingSetAllPacketIterator**](netringsetallpacketiterator.md)