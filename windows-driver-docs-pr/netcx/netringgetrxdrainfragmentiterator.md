---
title: NetRingGetRxDrainFragmentIterator function
description: The NetRingGetRxDrainFragmentIterator method gets a fragment iterator for the current drain section of a receive queue's fragment ring.
ms.assetid: DBDFD3F8-CA1F-444C-84FB-DE9DBF4FC354
keywords:
- NetAdapterCx NetRingGetRxDrainFragmentIterator, NetCx NetRingGetRxDrainFragmentIterator
ms.date: 11/05/2018
ms.localizationpriority: medium
---

# NetRingGetRxDrainFragmentIterator function

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

The **NetRingGetRxDrainFragmentIterator** method gets a fragment iterator for the current drain section of a receive queue's fragment ring.

## Syntax

```cpp
NET_RING_FRAGMENT_ITERATOR NetRingGetRxDrainFragmentIterator(
    NET_RING_COLLECTION const * Rings
);
```

## Parameters

`Rings`

A pointer to the **NET_RING_COLLECTION** struture that describes the receive queue's net rings.

## Return Value

Returns a [**NET_RING_FRAGMENT_ITERATOR**](net-ring-fragment-iterator.md) that begins at the fragment ring's **BeginIndex** and ends at the fragment ring's **NextIndex**. In other words, the iterator covers the fragment ring's current drain section. 

## Remarks

Client drivers typically call this method to begin the process of draining fragments from the ring to the OS.

For an animation and code example of draining fragments from the ring back to the OS, see [Using net rings and net ring iterators](using-net-rings-and-net-ring-iterators.md).

## Requirements

|  |  |
| --- | --- |
| Target Platform | Universal |
| Header | netringiterator.h |
| IRQL | PASSIVE_LEVEL |

## See Also

[Using net rings and net ring iterators](using-net-rings-and-net-ring-iterators.md)

[**NET_RING_FRAGMENT_ITERATOR**](net-ring-fragment-iterator.md)

**NET_RING_COLLECTION**