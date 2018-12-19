---
title: NET_RING_ITERATOR structure
description: A NET_RING_ITERATOR is a small structure that contains references to the indices of a NET_RING to which it belongs.
ms.assetid: 5F7B2428-0E71-44F9-82F1-A77F9C9A45DA
keywords:
- NetAdapterCx NET_RING_ITERATOR, NetCx NET_RING_ITERATOR
ms.date: 12/18/2018
ms.localizationpriority: medium
---

# NET_RING_ITERATOR structure

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

A **NET_RING_ITERATOR** is a small structure that contains references to the post and drain indices of a **NET_RING** to which it belongs.

## Syntax

```cpp
typedef struct _NET_RING_ITERATOR {
    NET_RING_COLLECTION const * Rings;
    UINT32*             const   IndexToSet;
    UINT32                      Index;
    UINT32              const   End;
} NET_RING_ITERATOR;
```

## Members

`Rings`

A **NET_RING_COLLECTION** structure that describes the **NET_RING** structure to which this net ring iterator belongs.

`IndexToSet`

The beginning of the range of elements that are covered by this iterator. This index does not move until after the client driver has finished processing elements in the ring and *sets* the iterator, which advances **IndexToSet** to **Index**.

Client drivers call [**NetPacketIteratorSet**](netpacketiteratorset.md) to set a packet iterator, or [**NetFragmentIteratorSet**](netfragmentiteratorset.md) to set a fragment iterator.

`Index`

The iterator's current index in the **NET_RING**. This index is advanced as the client driver processes elements in the ring.

Client drivers call [**NetPacketIteratorAdvance**](netpacketiteratoradvance.md) to advance a packet iterator, or [**NetFragmentIteratorAdvance**](netfragmentiteratoradvance.md) to advance a fragment iterator.

`End`

The end of the range of elements covered by this iterator.

## Remarks

NetAdapterCx client drivers should not use the **NET_RING_ITERATOR** structure directly. Instead, they should either use a [**NET_RING_PACKET_ITERATOR**](net-ring-packet-iterator.md) for a packet ring or a [**NET_RING_FRAGMENT_ITERATOR**](net-ring-fragment-iterator.md) for a fragment ring. These wrapper structures are used in all Net Ring Iterator Interface API calls.

## Requirements

|  |  |
| --- | --- |
| Header | netringiterator.h |

## See Also

[Net rings and net ring iterators](net-rings-and-net-ring-iterators.md)

[**NET_RING_PACKET_ITERATOR**](net-ring-packet-iterator.md)

[**NET_RING_FRAGMENT_ITERATOR**](net-ring-fragment-iterator.md)