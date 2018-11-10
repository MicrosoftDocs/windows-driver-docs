---
title: NetRingIteratorAny macro
description: The NetRingIteratorAny macro determines whether a net ring iterator has reached its End index or not.
ms.assetid: BEEC7527-26A6-48EA-A603-CF35F978D48E
keywords:
- NetAdapterCx NetRingIteratorAny, NetCx NetRingIteratorAny
ms.date: 11/09/2018
ms.localizationpriority: medium
---

# NetRingIteratorAny macro

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

The **NetRingIteratorAny** macro determines whether a net ring iterator has reached its **End** index or not.

## Syntax

```cpp
bool NetRingIteratorAny(
    i
);
```

## Parameters

`i`

Either a [**NET_RING_PACKET_ITERATOR**](net-ring-packet-iterator.md) or a [**NET_RING_FRAGMENT_ITERATOR**](net-ring-fragment-iterator.md).

## Return Value

Returns **TRUE** if the iterator has not reached its **End** index, false otherwise.

## Remarks

Client drivers can call **NetRingIteratorAny** to test whether the iterator has a valid element to process. This macro can be used to verify a packet or fragment before processing it, or it can be used as a test condition for a loop when the driver is processing multiple fragments or packets in a batch.

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