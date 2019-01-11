---
title: NetRingGetDrainFragments function
description: The NetRingGetDrainFragments method gets a fragment iterator for the current drain subsection of a fragment ring.
ms.assetid: DBDFD3F8-CA1F-444C-84FB-DE9DBF4FC354
keywords:
- NetAdapterCx NetRingGetDrainFragments, NetCx NetRingGetDrainFragments
ms.date: 01/10/2019
ms.localizationpriority: medium
---

# NetRingGetDrainFragments function

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

The **NetRingGetDrainFragments** method gets a fragment iterator for the current drain subsection of a fragment ring.

## Syntax

```cpp
NET_RING_FRAGMENT_ITERATOR NetRingGetDrainFragments(
    NET_RING_COLLECTION const * Rings
);
```

## Parameters

`Rings`

A pointer to the **NET_RING_COLLECTION** struture that describes the packet queue's net rings.

## Return Value

Returns a [**NET_RING_FRAGMENT_ITERATOR**](net-ring-fragment-iterator.md) that begins at the fragment ring's **BeginIndex** and ends at the fragment ring's **NextIndex**. In other words, the iterator covers the fragment ring's current drain section. 

## Remarks

Client drivers call **NetRingGetDrainFragments** to begin the process of draining receive (Rx) fragments from the ring to the OS. 

For an animation and code example of draining fragments from the ring back to the OS, see [Net rings and net ring iterators](net-rings-and-net-ring-iterators.md).

## Requirements

|  |  |
| --- | --- |
| Target Platform | Universal |
| Header | netringiterator.h |
| IRQL | Any level as long as target memory is resident |

## See Also

[Net rings and net ring iterators](net-rings-and-net-ring-iterators.md)

[**NET_RING_FRAGMENT_ITERATOR**](net-ring-fragment-iterator.md)

**NET_RING_COLLECTION**