---
title: NetRingSetRxDrainFragmentIterator function
description: The NetRingSetRxDrainFragmentIterator method advances the beginning of the drain section for a receive queue's fragment ring to the current index of the ring's drain fragment iterator.
ms.assetid: D3040BA5-0EC7-402F-B8E1-B6E06D6255CF
keywords:
- NetAdapterCx NetRingSetRxDrainFragmentIterator, NetCx NetRingSetRxDrainFragmentIterator
ms.date: 11/05/2018
ms.localizationpriority: medium
---

# NetRingSetRxDrainFragmentIterator function

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

The **NetRingSetRxDrainFragmentIterator** method advances the beginning of the drain section for a receive queue's fragment ring to the current index of the ring's drain fragment iterator.

## Syntax

```cpp
void NetRingSetRxDrainFragmentIterator(
    NET_RING_FRAGMENT_ITERATOR const * Iterator
);
```

## Parameters

`Iterator`

A pointer to the net fragment ring's drain [**NET_RING_FRAGMENT_ITERATOR**](net-ring-fragment-iterator.md) that the driver previously acquired through a call to [**NetRingGetRxDrainFragmentIterator**](netringgetrxdrainfragmentiterator.md).

## Return Value

None.

## Remarks

Client drivers call **NetRingSetRxDrainFragmentIterator** to complete the process of draining receive fragments to the OS.

After calling this method, the fragment ring's **BeginIndex** advances to the [**NET_RING_FRAGMENT_ITERATOR**](net-ring-fragment-iterator.md)'s current position in the ring. Therefore, the fragments between the old value of **BeginIndex** and the iterator's **Index - 1** inclusive are drained from the ring and ownership of them is transferred to the OS. This is how client drivers indicate receives to the system.

For an animation and code example of draining fragments back to the OS, see [Using net rings and net ring iterators](using-net-rings-and-net-ring-iterators.md).

## Requirements

|  |  |
| --- | --- |
| Target Platform | Universal |
| Header | netringiterator.h |
| IRQL | PASSIVE_LEVEL |

## See Also

[Using net rings and net ring iterators](using-net-rings-and-net-ring-iterators.md)

[**NET_RING_FRAGMENT_ITERATOR**](net-ring-fragment-iterator.md)

[**NetRingGetRxDrainFragmentIterator**](netringgetrxdrainfragmentiterator.md)