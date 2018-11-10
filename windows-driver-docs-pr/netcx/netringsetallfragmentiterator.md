---
title: NetRingSetAllFragmentIterator function
description: The NetRingSetAllFragmentIterator method advances the beginning of the section of a fragment ring that a client driver owns to the current index of a fragment iterator.
ms.assetid: C5F06C02-ECD2-472E-8681-8D83544F8F91
keywords:
- NetAdapterCx NetRingSetAllFragmentIterator, NetCx NetRingSetAllFragmentIterator
ms.date: 10/30/2018
ms.localizationpriority: medium
---

# NetRingSetAllFragmentIterator function

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

The **NetRingSetAllFragmentIterator** method advances the beginning of the section of a fragment ring that a client driver owns to the current index of a fragment iterator.

## Syntax

```cpp
void NetRingSetAllFragmentIterator(
    NET_RING_FRAGMENT_ITERATOR const * Iterator
);
```

## Parameters

`Iterator`

A pointer to a [**NET_RING_FRAGMENT_ITERATOR**](net-ring-fragment-iterator.md).

## Return Value

None.

## Remarks

Client drivers can acquire the [**NET_RING_FRAGMENT_ITERATOR**](net-ring-fragment-iterator.md) through a call to [**NetRingGetAllFragmentIterator**](netringgetallfragmentiterator.md), though this is not required.

After calling **NetRingSetAllFragmentIterator**, the fragment ring's **BeginIndex** advances to the **NET_RING_FRAGMENT_ITERATOR**'s current index. Therefore, the fragments between the old value of **BeginIndex** and the iterator's **Index - 1** inclusive are transferred to the OS. If the iterator's **Index** equals the fragment ring's **EndIndex**, this means the client driver no longer owns any fragments.

Client drivers typically call **NetRingSetAllFragmentIterator** to finish performing operations on all fragments that they own in a fragment ring. This might include processing a batch of receives that span all available fragments in the ring, or draining the ring during data path cancelation.

For a code example of using this method, see [Using net rings and net ring iterators](using-net-rings-and-net-ring-iterators.md).

## Requirements

|  |  |
| --- | --- |
| Target Platform | Universal |
| Header | netringiterator.h |
| IRQL | Any level as long as target memory is resident |

## See Also

[Using net rings and net ring iterators](using-net-rings-and-net-ring-iterators.md)

[**NetRingGetAllFragmentIterator**](netringgetallfragmentiterator.md)

[**NET_RING_FRAGMENT_ITERATOR**](net-ring-fragment-iterator.md)