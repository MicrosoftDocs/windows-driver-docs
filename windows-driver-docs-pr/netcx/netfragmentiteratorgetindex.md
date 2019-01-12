---
title: NetFragmentIteratorGetIndex method
description: The NetFragmentIteratorGetIndex method gets the current Index of a fragment iterator in the fragment ring.
ms.assetid: 2BB8D16F-F8C2-4D6E-B092-A307813311C7
keywords:
- NetAdapterCx NetFragmentIteratorGetIndex, NetCx NetFragmentIteratorGetIndex
ms.date: 01/11/2019
ms.localizationpriority: medium
---

# NetFragmentIteratorGetIndex method

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

The **NetFragmentIteratorGetIndex** method gets the current **Index** of a fragment iterator in the fragment ring.

## Syntax

```cpp
UINT32 NetFragmentIteratorGetIndex(
    NET_RING_FRAGMENT_ITERATOR const * Iterator
);
```

## Parameters

`Iterator`

A pointer to a [**NET_RING_FRAGMENT_ITERATOR**](net-ring-fragment-iterator.md) structure.

## Return Value

Returns the fragment iterator's current **Index**.

## Requirements

|  |  |
| --- | --- |
| Target Platform | Universal |
| Header | netringiterator.h |
| IRQL | Any level as long as target memory is resident |

## See Also

[Net rings and net ring iterators](net-rings-and-net-ring-iterators.md)

[**NET_RING_FRAGMENT_ITERATOR**](net-ring-fragment-iterator.md)