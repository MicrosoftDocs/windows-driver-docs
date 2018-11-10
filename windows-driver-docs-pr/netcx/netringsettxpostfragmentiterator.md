---
title: NetRingSetTxPostFragmentIterator function
description: The NetRingSetTxPostFragmentIterator method advances the beginning of the post section for a transmit (Tx) queue's fragment ring to the current index of a post fragment iterator.
ms.assetid: 0C5EC7C3-5633-4D85-87B1-B9AA1006AB94
keywords:
- NetAdapterCx NetRingSetTxPostFragmentIterator, NetCx NetRingSetTxPostFragmentIterator
ms.date: 11/08/2018
ms.localizationpriority: medium
---

# NetRingSetTxPostFragmentIterator function

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

The **NetRingSetTxPostFragmentIterator** method advances the beginning of the post section for a transmit (Tx) queue's fragment ring to the current index of a post fragment iterator.

## Syntax

```cpp
void NetRingSetTxPostFragmentIterator(
    NET_RING_FRAGMENT_ITERATOR const * Iterator
);
```

## Parameters

`Iterator`

A pointer to a post [**NET_RING_FRAGMENT_ITERATOR**](net-ring-fragment-iterator.md) that the driver previously acquired through a call to [**NetRingGetTxPostPacketFragmentIterator**](netringgettxpostpacketfragmentiterator.md).

## Return Value

None.

## Remarks

Client drivers call **NetRingSetTxPostFragmentIterator** to complete the process of posting a packet's fragments to hardware for Tx.

After calling **NetRingSetTxPostFragmentIterator**, the fragment ring's **NextIndex** advances to the [**NET_RING_FRAGMENT_ITERATOR**](net-ring-fragment-iterator.md)'s current position in the ring. Therefore, the fragments between the old value of **NextIndex** and the iterator's **Index - 1** inclusive are posted to hardware and are transferred to the drain section of the ring.

For an animation and code example of posting fragments to hardware for Tx, see [Using net rings and net ring iterators](using-net-rings-and-net-ring-iterators.md).

## Requirements

|  |  |
| --- | --- |
| Target Platform | Universal |
| Header | netringiterator.h |
| IRQL | Any level as long as target memory is resident |

## See Also

[Using net rings and net ring iterators](using-net-rings-and-net-ring-iterators.md)

[**NET_RING_FRAGMENT_ITERATOR**](net-ring-fragment-iterator.md)

[**NetRingGetTxPostPacketFragmentIterator**](netringgettxpostpacketfragmentiterator.md)