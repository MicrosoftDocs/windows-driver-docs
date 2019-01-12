---
title: NetFragmentIteratorGetFragment function
description: The NetFragmentIteratorGetFragment method gets the NET_FRAGMENT structure at a fragment iterator's current Index in the fragment ring.
ms.assetid: B6F2FEE8-7571-4B00-8D73-352D554F2F45
keywords:
- NetAdapterCx NetFragmentIteratorGetFragment, NetCx NetFragmentIteratorGetFragment
ms.date: 01/11/2019
ms.localizationpriority: medium
---

# NetFragmentIteratorGetFragment function

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

The **NetFragmentIteratorGetFragment** method gets the **NET_FRAGMENT** structure at a fragment iterator's current **Index** in the fragment ring.

## Syntax

```cpp
NET_FRAGMENT* NetFragmentIteratorGetFragment(
    NET_RING_FRAGMENT_ITERATOR const * Iterator
);
```

## Parameters

`Iterator`

A pointer to a [**NET_RING_FRAGMENT_ITERATOR**](net-ring-fragment-iterator.md) structure.

## Return Value

Returns a pointer to the **NET_FRAGMENT** structure at the fragment iterator's **Index**.

## Requirements

|  |  |
| --- | --- |
| Target Platform | Universal |
| Header | netringiterator.h |
| IRQL | Any level as long as target memory is resident |

## See Also

[Net rings and net ring iterators](net-rings-and-net-ring-iterators.md)

**NET_FRAGMENT**

[**NET_RING_FRAGMENT_ITERATOR**](net-ring-fragment-iterator.md)