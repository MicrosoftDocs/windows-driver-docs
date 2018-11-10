---
title: NetRingAdvanceFragmentIterator function
description: The NetRingAdvanceFragmentIterator method advances the index of a NET_RING_FRAGMENT_ITERATOR by one.
ms.assetid: EEC08D91-E121-4DCD-9925-DE78E30B5D4D
keywords:
- NetAdapterCx NetRingAdvanceFragmentIterator, NetCx NetRingAdvanceFragmentIterator
ms.date: 11/09/2018
ms.localizationpriority: medium
---

# NetRingAdvanceFragmentIterator function

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

The NetRingAdvanceFragmentIterator method advances the index of a [**NET_RING_FRAGMENT_ITERATOR**](net-ring-fragment-iterator.md) by one.

## Syntax

```cpp
void NetRingAdvanceFragmentIterator(
    NET_RING_FRAGMENT_ITERATOR * Iterator
);
```

## Parameters

`Iterator`

A pointer to a [**NET_RING_FRAGMENT_ITERATOR**](net-ring-fragment-iterator.md).

## Return Value

None.

## Requirements

|  |  |
| --- | --- |
| Target Platform | Universal |
| Header | netringiterator.h |
| IRQL | PASSIVE_LEVEL |

## See Also

[Using net rings and net ring iterators](using-net-rings-and-net-ring-iterators.md)

[**NET_RING_FRAGMENT_ITERATOR**](net-ring-fragment-iterator.md)