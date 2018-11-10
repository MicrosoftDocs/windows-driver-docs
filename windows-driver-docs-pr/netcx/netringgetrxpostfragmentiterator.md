---
title: NetRingGetRxPostFragmentIterator function
description: The NetRingGetRxPostFragmentIterator method gets a fragment iterator for the current post section of a receive (Rx) queue's fragment ring.
ms.assetid: 81CD9EB1-B1EE-4170-B4DD-89A8C80881A3
keywords:
- NetAdapterCx NetRingGetRxPostFragmentIterator, NetCx NetRingGetRxPostFragmentIterator
ms.date: 10/30/2018
ms.localizationpriority: medium
---

# NetRingGetRxPostFragmentIterator function

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

The **NetRingGetRxPostFragmentIterator** method gets a fragment iterator for the current post section of a receive (Rx) queue's fragment ring.

## Syntax

```cpp
NET_RING_FRAGMENT_ITERATOR NetRingGetRxPostFragmentIterator(
    NET_RING_COLLECTION const * Rings
);
```

## Parameters

`Rings`

A pointer to the **NET_RING_COLLECTION** struture that describes the receive queue's net rings.

## Return Value

Returns a [**NET_RING_FRAGMENT_ITERATOR**](net-ring-fragment-iterator.md) that begins at the fragment ring's **NextIndex** and ends at the fragment ring's **EndIndex**. In other words, the iterator covers the fragment ring's current post section. 

## Remarks

Client drivers typically call **NetRingGetRxPostFragmentIterator** to begin the process of posting fragments to hardware for Rx. Drivers later complete this process by calling [**NetRingSetRxPostFragmentIterator**](netringsetrxpostfragmentiterator.md).

For an animation and code example of posting fragments to hardware for Rx, see [Using net rings and net ring iterators](using-net-rings-and-net-ring-iterators.md).

## Requirements

|  |  |
| --- | --- |
| Target Platform | Universal |
| Header | netringiterator.h |
| IRQL | Any level as long as target memory is resident |

## See Also

[Using net rings and net ring iterators](using-net-rings-and-net-ring-iterators.md)

[**NET_RING_FRAGMENT_ITERATOR**](net-ring-fragment-iterator.md)

**NET_RING_COLLECTION**

[**NetRingSetRxPostFragmentIterator**](netringsetrxpostfragmentiterator.md)