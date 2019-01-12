---
title: NetPacketIteratorHasAny function
description: The NetPacketIteratorHasAny method determines whether a packet iterator has any valid elements to process in the packet ring.
ms.assetid: BEEC7527-26A6-48EA-A603-CF35F978D48E
keywords:
- NetAdapterCx NetPacketIteratorHasAny, NetCx NetPacketIteratorHasAny
ms.date: 01/10/2019
ms.localizationpriority: medium
---

# NetPacketIteratorHasAny function

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

The **NetPacketIteratorHasAny** method determines whether a packet iterator has any valid elements to process in the packet ring.

## Syntax

```cpp
BOOLEAN NetPacketIteratorHasAny(
    NET_RING_PACKET_ITERATOR const * Iterator
);
```

## Parameters

`Iterator`

A pointer to a [**NET_RING_PACKET_ITERATOR**](net-ring-packet-iterator.md) structure.

## Return Value

Returns **TRUE** if the iterator's **Index** does not equal its **End** index. In other words, the iterator has a packet to process. Otherwise, returns **FALSE**.

## Remarks

Client drivers can call **NetPacketIteratorHasAny** to test if the iterator has any valid elements to process. This method can be used to verify a packet before processing it, or it can be used as a test condition for a loop when the driver is processing multiple packets in a batch.

## Requirements

|  |  |
| --- | --- |
| Target Platform | Universal |
| Header | netringiterator.h |
| IRQL | Any level as long as target memory is resident |

## See Also

[Net rings and net ring iterators](net-rings-and-net-ring-iterators.md)

[**NET_RING_PACKET_ITERATOR**](net-ring-packet-iterator.md)