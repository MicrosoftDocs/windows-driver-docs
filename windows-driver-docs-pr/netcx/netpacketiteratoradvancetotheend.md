---
title: NetPacketIteratorAdvanceToTheEnd function
description: The NetPacketIteratorAdvanceToTheEnd method advances the current Index of a packet iterator to its End index.
ms.assetid: 11C49184-273D-4B12-BC7D-ECCF7FE0DEAF
keywords:
- NetAdapterCx NetPacketIteratorAdvanceToTheEnd, NetCx NetPacketIteratorAdvanceToTheEnd
ms.date: 01/10/2019
ms.localizationpriority: medium
---

# NetPacketIteratorAdvanceToTheEnd function

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

The **NetPacketIteratorAdvanceToTheEnd** method advances the current **Index** of a packet iterator to its **End** index.

## Syntax

```cpp
void NetPacketIteratorAdvanceToTheEnd(
    NET_RING_PACKET_ITERATOR * Iterator
);
```

## Parameters

`Iterator`

A pointer to a [**NET_RING_PACKET_ITERATOR**](net-ring-packet-iterator.md).

## Return Value

None.

## Remarks

After calling **NetPacketIteratorAdvanceToTheEnd**, the packet iterator's current **Index** advances to the iterator's **End** index. Therefore, the packets between the old value of iterator's **Index** and the iterator's **End - 1** inclusive are transferred to the OS.

Client drivers typically call **NetPacketIteratorAdvanceToTheEnd** to cancel all packets in the ring or perform other operations that drain all the ring's packets.

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