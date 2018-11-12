---
title: NetRingFragmentIteratorGetCount function
description: The NetRingFragmentIteratorGetCount method gets the count of fragments between a fragment iterator's current Index inclusive and its End index.
ms.assetid: 745B6680-C07B-460B-BE95-4E263EFE2355
keywords:
- NetAdapterCx NetRingFragmentIteratorGetCount, NetCx NetRingFragmentIteratorGetCount
ms.date: 11/09/2018
ms.localizationpriority: medium
---

# NetRingFragmentIteratorGetCount function

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

The **NetRingFragmentIteratorGetCount** method gets the count of fragments between a fragment iterator's current **Index** inclusive and its **End** index.

## Syntax

```cpp
UINT32 NetRingFragmentIteratorGetCount(
    NET_RING_FRAGMENT_ITERATOR const * Iterator
);
```

## Parameters

`Iterator`

A pointer to a [**NET_RING_FRAGMENT_ITERATOR**](net-ring-fragment-iterator.md).

## Return Value

Returns the number of fragments between this packet iterator's current index inclusive and its **End** index. For example, if the iterator's **Index** is **1** and its **End** index is **5**, the iterator currently covers **4** fragments: **1**, **2**, **3**, and **4**.

## Requirements

|  |  |
| --- | --- |
| Target Platform | Universal |
| Header | netringiterator.h |
| IRQL | Any level as long as target memory is resident |

## See Also

[Using net rings and net ring iterators](using-net-rings-and-net-ring-iterators.md)

[**NET_RING_FRAGMENT_ITERATOR**](net-ring-fragment-iterator.md)