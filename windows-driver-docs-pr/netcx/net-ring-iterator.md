---
title: NET_RING_ITERATOR structure
description: A NET_RING_ITERATOR is a small structure that contains references to the indices of a NET_RING to which it belongs.
ms.assetid: 5F7B2428-0E71-44F9-82F1-A77F9C9A45DA
keywords:
- NetAdapterCx NET_RING_ITERATOR, NetCx NET_RING_ITERATOR
ms.date: 11/02/2018
ms.localizationpriority: medium
---

# NET_RING_ITERATOR structure

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

A **NET_RING_ITERATOR** is a small structure that contains references to the post and drain indices of a **NET_RING** to which it belongs.

## Syntax

```cpp
typedef struct _NET_RING_ITERATOR {
    NET_RING_COLLECTION const * Rings;
    UINT32                      Index;
    UINT32              const   End;
} NET_RING_ITERATOR;
```

## Members

`Rings`

A **NET_RING_COLLECTION** structure that describes the **NET_RING** structure to which this net ring iterator belongs.

`Index`

The current index in the **NET_RING** at which the iterator is currently pointing. This index is the beginning of the range of elements that are covered by this iterator.

`End`

The end of the range of elements covered by this iterator.

## Remarks

NetAdapterCx client drivers should not use the **NET_RING_ITERATOR** structure directly. Instead, they should either use a [**NET_RING_PACKET_ITERATOR**](net-ring-packet-iterator.md) for a packet ring or a [**NET_RING_FRAGMENT_ITERATOR**](net-ring-fragment-iterator.md) for a fragment ring. These wrapper structures are used in all Net Ring Iterator Interface API calls.

## Requirements

|  |  |
| --- | --- |
| Header | netringiterator.h |

## See Also

[Using net rings and net ring iterators](using-net-rings-and-net-ring-iterators.md)

[**NET_RING_PACKET_ITERATOR**](net-ring-packet-iterator.md)

[**NET_RING_FRAGMENT_ITERATOR**](net-ring-fragment-iterator.md)