---
title: NetRingIteratorGetIndex macro
description: The NetRingIteratorGetIndex macro gets the current Index of a net ring iterator.
ms.assetid: D9239E11-A366-44B8-B1A4-A58C986FBDFE
keywords:
- NetAdapterCx NetRingIteratorGetIndex, NetCx NetRingIteratorGetIndex
ms.date: 11/09/2018
ms.localizationpriority: medium
---

# NetRingIteratorGetIndex macro

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

The **NetRingIteratorGetIndex** macro gets the current **Index** of a net ring iterator.

## Syntax

```cpp
UINT32 NetRingIteratorGetIndex(
    i
);
```

## Parameters

`i`

Either a [**NET_RING_PACKET_ITERATOR**](net-ring-packet-iterator.md) or a [**NET_RING_FRAGMENT_ITERATOR**](net-ring-fragment-iterator.md).

## Return Value

Returns the iterator's current **Index**.

## Requirements

|  |  |
| --- | --- |
| Target Platform | Universal |
| Header | netringiterator.h |
| IRQL | Any level as long as target memory is resident |

## See Also

[Using net rings and net ring iterators](using-net-rings-and-net-ring-iterators.md)

[**NET_RING_PACKET_ITERATOR**](net-ring-packet-iterator.md)

[**NET_RING_FRAGMENT_ITERATOR**](net-ring-fragment-iterator.md)