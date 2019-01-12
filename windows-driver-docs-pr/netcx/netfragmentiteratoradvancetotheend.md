---
title: NetFragmentIteratorAdvanceToTheEnd function
description: The NetFragmentIteratorAdvanceToTheEnd method advances the current Index of a fragment iterator to its End index.
ms.assetid: 0D0FA90C-E820-4C0A-9228-F49F9812FA49
keywords:
- NetAdapterCx NetFragmentIteratorAdvanceToTheEnd, NetCx NetFragmentIteratorAdvanceToTheEnd
ms.date: 01/10/2019
ms.localizationpriority: medium
---

# NetFragmentIteratorAdvanceToTheEnd function

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

The **NetFragmentIteratorAdvanceToTheEnd** method advances the current **Index** of a fragment iterator to its **End** index.

## Syntax

```cpp
void NetFragmentIteratorAdvanceToTheEnd(
    NET_RING_FRAGMENT_ITERATOR * Iterator
);
```

## Parameters

`Iterator`

A pointer to a [**NET_RING_FRAGMENT_ITERATOR**](net-ring-fragment-iterator.md).

## Return Value

None.

## Remarks

After calling **NetFragmentIteratorAdvanceToTheEnd**, the fragment iterator's current **Index** advances to the iterator's **End** index. Therefore, the fragments between the old value of iterator's **Index** and the iterator's **End - 1** inclusive are transferred to the OS.

Client drivers typically call **NetFragmentIteratorAdvanceToTheEnd** to cancel all fragments in the ring or perform other operations that drain all the ring's fragments.

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