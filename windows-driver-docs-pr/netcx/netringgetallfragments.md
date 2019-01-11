---
title: NetRingGetAllFragments function
description: The NetRingGetAllFragments method gets a fragment iterator for the entire range in a fragment ring that a client driver owns.
ms.assetid: 42CB8047-8213-4E24-8B00-EF78DDF76049
keywords:
- NetAdapterCx NetRingGetAllFragments, NetCx NetRingGetAllFragments
ms.date: 01/10/2019
ms.localizationpriority: medium
---

# NetRingGetAllFragments function

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

The **NetRingGetAllFragments** method gets a fragment iterator for the entire range in a fragment ring that a client driver owns.

## Syntax

```cpp
NET_RING_FRAGMENT_ITERATOR NetRingGetAllFragments(
    NET_RING_COLLECTION const * Rings
);
```

## Parameters

`Rings`

A pointer to the **NET_RING_COLLECTION** struture that describes the packet queue's net rings.

## Return Value

Returns a [**NET_RING_FRAGMENT_ITERATOR**](net-ring-fragment-iterator.md) that begins at the fragment ring's **BeginIndex** and ends at the fragment ring's **EndIndex**. In other words, the iterator covers both the ring's post subsection and its drain subsection, or all fragments in the ring that the driver currently owns. 

## Remarks

Client drivers typically call **NetRingGetAllFragments** to begin performing operations on all fragments that they own in a fragment ring. This might include processing a batch of receives that span all available fragments in the ring, or draining the ring during data path cancelation.

For a code example of using this method, see [Net rings and net ring iterators](net-rings-and-net-ring-iterators.md).

## Requirements

|  |  |
| --- | --- |
| Target Platform | Universal |
| Header | netringiterator.h |
| IRQL | Any level as long as target memory is resident |

## See Also

[Net rings and net ring iterators](net-rings-and-net-ring-iterators.md)

**NET_RING_COLLECTION**

[**NET_RING_FRAGMENT_ITERATOR**](net-ring-fragment-iterator.md)