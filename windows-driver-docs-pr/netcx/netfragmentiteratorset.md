---
title: NetFragmentIteratorSet function
description: The NetFragmentIteratorSet method completes a client driver's post or drain operation on the fragment ring. 
ms.assetid: E19347A0-3F00-43AF-95E2-ACC8E16DF4E2
keywords:
- NetAdapterCx NetFragmentIteratorSet, NetCx NetFragmentIteratorSet
ms.date: 01/11/2019
ms.localizationpriority: medium
---

# NetFragmentIteratorSet function

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

The **NetFragmentIteratorSet** method completes a client driver's post or drain operation on the fragment ring. 

## Syntax

```cpp
void NetFragmentIteratorSet(
    NET_RING_FRAGMENT_ITERATOR const * Iterator
);
```

## Parameters

`Iterator`

A pointer to a [**NET_RING_FRAGMENT_ITERATOR**](net-ring-fragment-iterator.md) structure.

## Return Value

None.

## Remarks

**NetFragmentIteratorSet** sets the fragment iterator's **IndexToSet** to its **Index**, which indicates to the OS that the client driver has finished processing the fragments from **IndexToSet** to **Index - 1** inclusive. Client drivers call this method to finish posting fragments to hardware, or to finish draining completed fragments to the OS. 

For an animation and code example of draining fragments back to the OS, see [Net rings and net ring iterators](net-rings-and-net-ring-iterators.md).

## Requirements

|  |  |
| --- | --- |
| Target Platform | Universal |
| Header | netringiterator.h |
| IRQL | Any level as long as target memory is resident |

## See Also

[Net rings and net ring iterators](net-rings-and-net-ring-iterators.md)

[**NET_RING_FRAGMENT_ITERATOR**](net-ring-fragment-iterator.md)