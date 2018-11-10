---
title: NetRingAdvanceEndFragmentIterator function
description: The NetRingAdvanceEndFragmentIterator method advances the index of a NET_RING_FRAGMENT_ITERATOR to the end index of the range in a fragment ring that a client driver owns.
ms.assetid: D1D7BDF5-219B-406B-9CDE-92FC67C4D148
keywords:
- NetAdapterCx NetRingAdvanceEndFragmentIterator, NetCx NetRingAdvanceEndFragmentIterator
ms.date: 11/09/2018
ms.localizationpriority: medium
---

# NetRingAdvanceEndFragmentIterator function

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

The **NetRingAdvanceEndFragmentIterator** method advances the index of a [**NET_RING_FRAGMENT_ITERATOR**](net-ring-fragment-iterator.md) to the end index of the range in a fragment ring that a client driver owns.

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

After calling **NetRingAdvanceEndFragmentIterator**, the fragment iterator's index advances to the fragment ring's **EndIndex**. Therefore, the fragments between the old value of iterator's **Index** and the ring's **EndIndex** inclusive are transferred to the OS. This means the client driver no longer owns any fragments.

Client drivers typically call **NetRingAdvanceEndFragmentIterator** to either process a batch of fragments in a range or cancel all fragments in the ring.

For a code example of using this method, see [Using net rings and net ring iterators](using-net-rings-and-net-ring-iterators.md).

## Requirements

|  |  |
| --- | --- |
| Target Platform | Universal |
| Header | netringiterator.h |
| IRQL | Any level as long as target memory is resident |

## See Also

[Using net rings and net ring iterators](using-net-rings-and-net-ring-iterators.md)

[**NET_RING_FRAGMENT_ITERATOR**](net-ring-fragment-iterator.md)