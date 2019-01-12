---
title: NetFragmentIteratorAdvance function
description: The NetFragmentIteratorAdvance method advances the Index of a fragment iterator by one.
ms.assetid: FE840A8B-2ECF-4E5B-9F1C-2C2CD4465FF3
keywords:
- NetAdapterCx NetFragmentIteratorAdvance, NetCx NetFragmentIteratorAdvance
ms.date: 01/11/2019
ms.localizationpriority: medium
---

# NetFragmentIteratorAdvance function

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

The **NetFragmentIteratorAdvance** method advances the **Index** of a fragment iterator by one.

## Syntax

```cpp
void NetFragmentIteratorAdvance(
    NET_RING_FRAGMENT_ITERATOR * Iterator
);
```

## Parameters

`Iterator`

A pointer to a [**NET_RING_FRAGMENT_ITERATOR**](net-ring-fragment-iterator.md) structure.

## Return Value

None.

## Requirements

|  |  |
| --- | --- |
| Target Platform | Universal |
| Header | netringiterator.h |
| IRQL | Any level as long as target memory is resident |

## See Also

[Net rings and net ring iterators](net-rings-and-net-ring-iterators.md)

[**NET_RING_FRAGMENT_ITERATOR**](net-ring-fragment-iterator.md)