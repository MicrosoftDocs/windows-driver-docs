---
title: NetRingAdvanceEndFragmentIterator function
description: The NetRingAdvanceEndFragmentIterator method advances the current index of a NET_RING_FRAGMENT_ITERATOR to the iterator's End index.
ms.assetid: D1D7BDF5-219B-406B-9CDE-92FC67C4D148
keywords:
- NetAdapterCx NetRingAdvanceEndFragmentIterator, NetCx NetRingAdvanceEndFragmentIterator
ms.date: 11/09/2018
ms.localizationpriority: medium
---

# NetRingAdvanceEndFragmentIterator function

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

The **NetRingAdvanceEndFragmentIterator** method advances the current index of a [**NET_RING_FRAGMENT_ITERATOR**](net-ring-fragment-iterator.md) to the iterator's **End** index.

## Syntax

```cpp
void NetRingAdvanceEndFragmentIterator(
    NET_RING_FRAGMENT_ITERATOR * Iterator
);
```

## Parameters

`Iterator`

A pointer to a [**NET_RING_FRAGMENT_ITERATOR**](net-ring-fragment-iterator.md).

## Return Value

None.

## Remarks

After calling **NetRingAdvanceEndFragmentIterator**, the fragment iterator's current **Index** advances to the iterator's **End** index. Therefore, the fragments between the old value of iterator's **Index** and the iterator's **End - 1** inclusive are transferred to the OS.

Client drivers typically call **NetRingAdvanceEndFragmentIterator** to either process a batch of fragments in a range or cancel all fragments in the ring.

For a code example of using this method, see [Net rings and net ring iterators](net-rings-and-net-ring-iterators.md).

## Requirements

|  |  |
| --- | --- |
| Target Platform | Universal |
| Header | netringiterator.h |
| IRQL | Any level as long as target memory is resident |

## See Also

[Net rings and net ring iterators](net-rings-and-net-ring-iterators.md)

[**NET_RING_FRAGMENT_ITERATOR**](net-ring-fragment-iterator.md)