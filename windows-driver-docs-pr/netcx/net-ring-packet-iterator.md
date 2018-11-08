---
title: NET_RING_PACKET_ITERATOR structure
description: A NET_RING_PACKET_ITERATOR is a wrapper around a NET_RING_ITERATOR. The NET_RING_PACKET_ITERATOR is constrained to packet rings.
ms.assetid: F7B2DB14-028A-433B-AC10-5E4BECC70438
keywords:
- NetAdapterCx NET_RING_PACKET_ITERATOR, NetCx NET_RING_PACKET_ITERATOR
ms.date: 11/02/2018
ms.localizationpriority: medium
---

# NET_RING_PACKET_ITERATOR structure

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

A **NET_RING_PACKET_ITERATOR** is a wrapper around a [**NET_RING_ITERATOR**](net-ring-iterator.md) that client drivers use for net packet rings.

## Syntax

```cpp
typedef struct _NET_RING_PACKET_ITERATOR {
    NET_RING_ITERATOR   Iterator;
} NET_RING_PACKET_ITERATOR;
```

## Members

`Iterator`

The [**NET_RING_ITERATOR**](net-ring-iterator.md) structure around which this structure wraps.

## Remarks

For packet rings, client drivers must use a **NET_RING_PACKET_ITERATOR** instead of using a [**NET_RING_ITERATOR**](net-ring-iterator.md) directly.

## Requirements

|  |  |
| --- | --- |
| Header | netringiterator.h |

## See Also

[Using net rings and net ring iterators](using-net-rings-and-net-ring-iterators.md)

[**NET_RING_ITERATOR**](net-ring-iterator.md)

[**NET_RING_FRAGMENT_ITERATOR**](net-ring-fragment-iterator.md)