---
title: NetRingSetTxDrainFragmentIterator function
description: The NetRingSetTxDrainFragmentIterator method advances the beginning of the drain section for a transmit (Tx) queue's fragment ring to the current index of a drain fragment iterator.
ms.assetid: C1A992BC-E531-4B40-AD6A-AAFAE322BEC5
keywords:
- NetAdapterCx NetRingSetTxDrainFragmentIterator, NetCx NetRingSetTxDrainFragmentIterator
ms.date: 11/08/2018
ms.localizationpriority: medium
---

# NetRingSetTxDrainFragmentIterator function

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

The **NetRingSetTxDrainFragmentIterator** method advances the beginning of the drain section for a transmit (Tx) queue's fragment ring to the current index of a drain fragment iterator.

## Syntax

```cpp
void NetRingSetTxDrainFragmentIterator(
    NET_RING_FRAGMENT_ITERATOR const * Iterator
);
```

## Parameters

`Iterator`

A pointer to a drain [**NET_RING_FRAGMENT_ITERATOR**](net-ring-fragment-iterator.md) that the driver previously acquired through a call to [**NetRingGetTxDrainPacketFragmentIterator**](netringgettxdrainpacketfragmentiterator.md).

## Return Value

None. 

## Remarks

Client drivers call **NetRingSetTxDrainFragmentIterator** to complete the process of draining a packet's transmitted fragments to the OS.

After calling **NetRingSetTxDrainFragmentIterator**, the fragment ring's **NextIndex** advances to the [**NET_RING_FRAGMENT_ITERATOR**](net-ring-fragment-iterator.md)'s current position in the ring. Therefore, the fragments between the old value of **NextIndex** and the iterator's **Index - 1** inclusive are drained from the ring and ownership of them is transferred to the OS. This is how client drivers return completed transmit buffers.

For an animation and code example of draining transmitted fragments to the OS, see [Using net rings and net ring iterators](using-net-rings-and-net-ring-iterators.md).

## Requirements

|  |  |
| --- | --- |
| Target Platform | Universal |
| Header | netringiterator.h |
| IRQL | PASSIVE_LEVEL |

## See Also

[Using net rings and net ring iterators](using-net-rings-and-net-ring-iterators.md)

[**NET_RING_FRAGMENT_ITERATOR**](net-ring-fragment-iterator.md)

[**NetRingGetTxDrainPacketFragmentIterator**](netringgettxdrainpacketfragmentiterator.md)