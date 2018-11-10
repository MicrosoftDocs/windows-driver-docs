---
title: NetRingAdvanceEndPacketIterator function
description: The NetRingAdvanceEndPacketIterator method advances the current index of a NET_RING_PACKET_ITERATOR to the iterator's End index.
ms.assetid: 11C49184-273D-4B12-BC7D-ECCF7FE0DEAF
keywords:
- NetAdapterCx NetRingAdvanceEndPacketIterator, NetCx NetRingAdvanceEndPacketIterator
ms.date: 11/09/2018
ms.localizationpriority: medium
---

# NetRingAdvanceEndPacketIterator function

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

The **NetRingAdvanceEndPacketIterator** method advances the current index of a [**NET_RING_PACKET_ITERATOR**](net-ring-packet-iterator.md) to the iterator's **End** index.

## Syntax

```cpp
void NetRingAdvanceEndPacketIterator(
    NET_RING_PACKET_ITERATOR * Iterator
);
```

## Parameters

`Iterator`

A pointer to a [**NET_RING_PACKET_ITERATOR**](net-ring-packet-iterator.md).

## Return Value

None.

## Remarks

After calling **NetRingAdvanceEndPacketIterator**, the packet iterator's current **Index** advances to the iterator's **End** index. Therefore, the packets between the old value of iterator's **Index** and the iterator's **End** - 1 inclusive are transferred to the OS.

Client drivers typically call **NetRingAdvanceEndPacketIterator** to cancel all packets in the ring.

For a code example of using this method, see [Using net rings and net ring iterators](using-net-rings-and-net-ring-iterators.md).

## Requirements

|  |  |
| --- | --- |
| Target Platform | Universal |
| Header | netringiterator.h |
| IRQL | PASSIVE_LEVEL |

## See Also

[Using net rings and net ring iterators](using-net-rings-and-net-ring-iterators.md)

[**NET_RING_PACKET_ITERATOR**](net-ring-packet-iterator.md)