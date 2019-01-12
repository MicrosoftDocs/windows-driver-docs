---
title: NetFragmentIteratorGetCount function
description: The NetFragmentIteratorGetCount method gets the count of fragments that a client driver owns in the fragment ring.
ms.assetid: 800F52E8-7D54-4B7A-9B9A-A0BCD955B353
keywords:
- NetAdapterCx NetFragmentIteratorGetCount, NetCx NetFragmentIteratorGetCount
ms.date: 01/11/2019
ms.localizationpriority: medium
---

# NetFragmentIteratorGetCount function

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

The **NetFragmentIteratorGetCount** method gets the count of fragments that a client driver owns in the fragment ring.

## Syntax

```cpp
UINT32 NetFragmentIteratorGetCount(
    NET_RING_FRAGMENT_ITERATOR const * Iterator
);
```

## Parameters

`Iterator`

A pointer to a [**NET_RING_FRAGMENT_ITERATOR**](net-ring-fragment-iterator.md) structure.

## Return Value

Returns the number of fragments between this fragment iterator's current **Index** and **EndIndex - 1** inclusive. For example, if the iterator's **Index** is **1** and its **End** index is **5**, the client driver owns **4** fragments: **1**, **2**, **3**, and **4**.

## Requirements

|  |  |
| --- | --- |
| Target Platform | Universal |
| Header | netringiterator.h |
| IRQL | Any level as long as target memory is resident |

## See Also

[Net rings and net ring iterators](net-rings-and-net-ring-iterators.md)

[**NET_RING_FRAGMENT_ITERATOR**](net-ring-fragment-iterator.md)