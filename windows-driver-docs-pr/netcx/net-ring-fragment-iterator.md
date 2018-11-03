---
title: NET_RING_FRAGMENT_ITERATOR structure
description: A NET_RING_FRAGMENT_ITERATOR is a wrapper around a NET_RING_ITERATOR. The NET_RING_FRAGMENT_ITERATOR is constrained to fragment rings.
ms.assetid: F8DCB2AF-2014-4512-AF54-64D4DD26B2A7
keywords:
- NetAdapterCx NET_RING_FRAGMENT_ITERATOR, NetCx NET_RING_FRAGMENT_ITERATOR
ms.date: 10/30/2018
ms.localizationpriority: medium
---

# NET_RING_FRAGMENT_ITERATOR structure

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

A NET_RING_FRAGMENT_ITERATOR is a wrapper around a NET_RING_ITERATOR. The NET_RING_FRAGMENT_ITERATOR is constrained to fragment rings.

## Syntax

```cpp
typedef struct _NET_RING_FRAGMENT_ITERATOR {
    NET_RING_ITERATOR   Iterator;
} NET_RING_FRAGMENT_ITERATOR;
```

## Members

`Iterator`

The [**NET_RING_ITERATOR**](net-ring-iterator.md) structure around which this structure wraps.

## Remarks

For working with fragment rings, client drivers must use a **NET_RING_FRAGMENT_ITERATOR** instead of using a [**NET_RING_ITERATOR**](net-ring-iterator.md) directly.

## Requirements

|  |  |
| --- | --- |
| Header | netringiterator.h |

## See Also

[Using net rings and net ring iterators](using-net-rings-and-net-ring-iterators.md)

[Netringiterator.h](netringiterator-h.md)

[**NET_RING_ITERATOR**](net-ring-iterator.md)

[**NET_RING_PACKET_ITERATOR**](net-ring-packet-iterator.md)