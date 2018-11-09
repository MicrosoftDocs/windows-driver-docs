---
title: NetRingSetRxPostFragmentIterator function
description: The NetRingSetRxPostFragmentIterator method advances the beginning of the post section for a receive (Rx) queue's fragment ring to the current index of the ring's post fragment iterator.
ms.assetid: DBDFD3F8-CA1F-444C-84FB-DE9DBF4FC354
keywords:
- NetAdapterCx NetRingSetRxPostFragmentIterator, NetCx NetRingSetRxPostFragmentIterator
ms.date: 10/30/2018
ms.localizationpriority: medium
---

# NetRingSetRxPostFragmentIterator function

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

The **NetRingSetRxPostFragmentIterator** method advances the beginning of the post section for a receive (Rx) queue's fragment ring to the current index of the ring's post fragment iterator.

## Syntax

```cpp
void NetRingSetRxPostFragmentIterator(
    NET_RING_FRAGMENT_ITERATOR const * Iterator
);
```

## Parameters

`Iterator`

A pointer to the net fragment ring's post [**NET_RING_FRAGMENT_ITERATOR**](net-ring-fragment-iterator.md) that the driver previously acquired through a call to [**NetRingGetRxPostFragmentIterator**](netringgetrxpostfragmentiterator.md).

## Return Value

None.

## Remarks

Client drivers call **NetRingSetRxPostFragmentIterator** to complete the process of posting fragments to hardware for Rx.

After calling **NetRingSetRxPostFragmentIterator**, the fragment ring's **NextIndex** advances to the [**NET_RING_FRAGMENT_ITERATOR**](net-ring-fragment-iterator.md)'s current position in the ring. Therefore, the fragments between the old value of **NextIndex** and the iterator's **Index - 1** inclusive are posted to hardware and are transferred to the drain section of the ring.

For an animation and code example of posting fragments to hardware, see [Using net rings and net ring iterators](using-net-rings-and-net-ring-iterators.md).

## Requirements

|  |  |
| --- | --- |
| Target Platform | Universal |
| Header | netringiterator.h |
| IRQL | PASSIVE_LEVEL |

## See Also

[Using net rings and net ring iterators](using-net-rings-and-net-ring-iterators.md)

[**NET_RING_FRAGMENT_ITERATOR**](net-ring-fragment-iterator.md)

[**NetRingGetRxPostFragmentIterator**](netringgetrxpostfragmentiterator.md)