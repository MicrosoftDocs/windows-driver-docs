---
title: NetRingIteratorGetFragment function
description: The NetRingIteratorGetFragment method gets the NET_FRAGMENT structure pointed to by a NET_RING_FRAGMENT_ITERATOR.
ms.assetid: B6F2FEE8-7571-4B00-8D73-352D554F2F45
keywords:
- NetAdapterCx NetRingIteratorGetFragment, NetCx NetRingIteratorGetFragment
ms.date: 10/30/2018
ms.localizationpriority: medium
---

# NetRingIteratorGetFragment function

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

The **NetRingIteratorGetFragment** method gets the **NET_FRAGMENT** structure pointed to by a [**NET_RING_FRAGMENT_ITERATOR**](net-ring-fragment-iterator.md).

## Syntax

```cpp
NET_FRAGMENT* NetRingIteratorGetFragment(
    NET_RING_FRAGMENT_ITERATOR const * Iterator
);
```

## Parameters

`Iterator`

A pointer to a [**NET_RING_FRAGMENT_ITERATOR**](net-ring-fragment-iterator.md) structure.

## Return Value

Returns a pointer to the **NET_FRAGMENT** pointed to by the **NET_RING_FRAGMENT_ITERATOR**.

## Requirements

|  |  |
| --- | --- |
| Target Platform | Universal |
| Header | netringiterator.h |
| IRQL | PASSIVE_LEVEL |

## See Also

[Using net rings and net ring iterators](using-net-rings-and-net-ring-iterators.md)