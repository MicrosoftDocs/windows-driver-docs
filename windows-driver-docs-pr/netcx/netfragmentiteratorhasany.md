---
title: NetFragmentIteratorHasAny function
description: The NetFragmentIteratorHasAny method determines whether a fragment iterator has any valid elements to process in the fragment ring.
ms.assetid: BCD79C0E-DEC1-4DEE-B937-2357A3CBD30D
keywords:
- NetAdapterCx NetFragmentIteratorHasAny, NetCx NetFragmentIteratorHasAny
ms.date: 01/11/2019
ms.localizationpriority: medium
---

# NetFragmentIteratorHasAny function

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

The **NetFragmentIteratorHasAny** method determines whether a fragment iterator has any valid elements to process in the fragment ring.

## Syntax

```cpp
BOOLEAN NetFragmentIteratorHasAny(
    NET_RING_FRAGMENT_ITERATOR const * Iterator
);
```

## Parameters

`Iterator`

A pointer to a [**NET_RING_FRAGMENT_ITERATOR**](net-ring-fragment-iterator.md) structure.

## Return Value

Returns **TRUE** if the iterator's **Index** does not equal its **End** index. In other words, the iterator has a fragment to process. Otherwise, returns **FALSE**.

## Remarks

Client drivers can call **NetFragmentIteratorHasAny** to test if the iterator has any valid elements to process. This method can be used to verify a fragment before processing it, or it can be used as a test condition for a loop when the driver is processing multiple fragments in a batch.

## Requirements

|  |  |
| --- | --- |
| Target Platform | Universal |
| Header | netringiterator.h |
| IRQL | Any level as long as target memory is resident |

## See Also

[Net rings and net ring iterators](net-rings-and-net-ring-iterators.md)

[**NET_RING_FRAGMENT_ITERATOR**](net-ring-fragment-iterator.md)