---
title: NetRingGetPostFragments function
description: The NetRingGetPostFragments method The NetRingGetPostFragments method gets a fragment iterator for the current post subsection of a fragment ring.
ms.assetid: 81CD9EB1-B1EE-4170-B4DD-89A8C80881A3
keywords:
- NetAdapterCx NetRingGetPostFragments, NetCx NetRingGetPostFragments
ms.date: 01/10/2019
ms.localizationpriority: medium
---

# NetRingGetPostFragments function

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

The **NetRingGetPostFragments** method The NetRingGetPostFragments method gets a fragment iterator for the current post subsection of a fragment ring.

## Syntax

```cpp
NET_RING_FRAGMENT_ITERATOR NetRingGetPostFragments(
    NET_RING_COLLECTION const * Rings
);
```

## Parameters

`Rings`

A pointer to the **NET_RING_COLLECTION** struture that describes the packet queue's net rings.

## Return Value

Returns a [**NET_RING_FRAGMENT_ITERATOR**](net-ring-fragment-iterator.md) that begins at the fragment ring's **NextIndex** and ends at the fragment ring's **EndIndex**. In other words, the iterator covers the fragment ring's current post section. 

## Remarks

Client drivers typically call **NetRingGetPostFragments** to begin the process of posting fragments to hardware for receiving (Rx). Drivers later complete this process by calling [**NetFragmentIteratorSet**](netfragmentiteratorset.md).

For an animation and code example of posting fragments to hardware for Rx, see [Net rings and net ring iterators](net-rings-and-net-ring-iterators.md).

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

[**NetFragmentIteratorSet**](netfragmentiteratorset.md)