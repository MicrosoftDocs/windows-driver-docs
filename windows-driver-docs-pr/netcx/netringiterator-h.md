---
title: Netringiterator.h
description: Netringiterator.h
ms.assetid: E83EF182-24C5-4B35-9E0E-93C53211C199
keywords:
- NetAdapterCx net ring iterator reference, net ring iterator api reference, netringiterator.h
ms.date: 10/30/2018
ms.localizationpriority: medium
---

# Netringiterator.h

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

This header is used by NetAdapterCx. For more information, see:

- [Using net rings and net ring iterators](using-net-rings-and-net-ring-iterators.md)

Netringiterator.h contains the following programming interfaces:

## Functions

| Title | Description |
| --- | --- |
| [NetRingIteratorGetFragment](netringiteratorgetfragment.md) | The NetRingIteratorGetFragment method gets the NET_FRAGMENT structure pointed to by a NET_RING_FRAGMENT_ITERATOR. |
| [NetRingIteratorGetPacket](netringiteratorgetpacket.md) | The NetRingIteratorGetPacket method gets the NET_PACKET structure pointed to by a NET_RING_PACKET_ITERATOR. |
| [NetRingGetRxPostFragmentIterator](netringgetrxpostfragmentiterator.md) | The NetRingGetRxPostFragmentIterator method gets a fragment iterator for the current post section of a receive queue's fragment ring. |
| [NetRingSetRxPostFragmentIterator](netringsetrxpostfragmentiterator.md) | The NetRingSetRxPostFragmentIterator method advances the beginning of the post section for a receive queue's net fragment ring to the current index of the ring's post fragment iterator. |
| [NetRingGetRxDrainFragmentIterator](netringgetrxdrainfragmentiterator.md) | The NetRingGetRxPostFragmentIterator method gets a fragment iterator for the current drain section of a receive queue's fragment ring. |
| [NetRingSetRxDrainFragmentIterator](netringsetrxdrainfragmentiterator.md) | The NetRingSetRxDrainFragmentIterator method advances the beginning of the drain section for a receive queue's fragment ring to the current index of the ring's drain fragment iterator. |
| [NetRingGetRxDrainPacketIterator](netringgetrxdrainpacketiterator.md) | The NetRingGetRxDrainPacketIterator method gets a packet iterator for the current drain section of a receive queue's packet ring. |
| [NetRingSetRxDrainPacketIterator](netringsetrxdrainpacketiterator.md) | The NetRingSetRxDrainPacketIterator method advances the beginning of the drain section for a receive queue's packet ring to the current index of the ring's drain packet iterator. |
| [NetRingGetTxPostPacketIterator](netringgettxpostpacketiterator.md) | x |
| [NetRingSetTxPostPacketIterator](netringsettxpostpacketiterator.md) | x |
| [NetRingGetTxDrainPacketIterator](netringgettxdrainpacketiterator.md) | x |
| [NetRingSetTxDrainPacketIterator](netringsettxdrainpacketiterator.md) | x |
| [NetRingGetTxPostPacketFragmentIterator](netringgettxpostpacketfragmentiterator.md) | x |
| [NetRingSetTxPostFragmentIterator](netringsettxpostfragmentiterator.md) | x |
| [NetRingGetTxDrainPacketFragmentIterator](netringgettxdrainpacketfragmentiterator.md) | x |
| [NetRingSetTxDrainFragmentIterator](netringsettxdrainfragmentiterator.md) | x |
| [NetRingGetAllFragmentIterator](netringgetallfragmentiterator.md) | x |
| [NetRingSetAllFragmentIterator](netringsetallfragmentiterator.md) | x |
| [NetRingGetAllPacketIterator](netringgetallpacketiterator.md) | x |
| [NetRingSetAllPacketIterator](netringsetallpacketiterator.md) | x |
| [NetRingAdvancePacketIterator](netringadvancepacketiterator.md) | x |
| [NetRingAdvanceFragmentIterator](netringadvancefragmentiterator.md) | x |
| [NetRingAdvanceEndPacketIterator](netringadvanceendpacketiterator.md) | x |
| [NetRingAdvanceEndFragmentIterator](netringadvanceendfragmentiterator.md) | x |
| [NetRingPacketIteratorGetCount](netringpacketiteratorgetcount.md) | x |
| [NetRingFragmentIteratorGetCount](netringfragmentiteratorgetcount.md) | x |
| [NetRingIteratorGetIndex](netringiteratorgetindex.md) | x |
| [NetRingIteratorAny](netringiteratorany.md) | x |

## Structures

| Title | Description |
| --- | --- |
| [NET_RING_ITERATOR](net-ring-iterator.md) | A NET_RING_ITERATOR is a small structure that contains references to the post and drain indices of a NET_RING to which it belongs. |
| [NET_RING_PACKET_ITERATOR](net-ring-packet-iterator.md) | A NET_RING_PACKET_ITERATOR is a wrapper around a NET_RING_ITERATOR. The NET_RING_PACKET_ITERATOR is constrained to packet rings. |
| [NET_RING_FRAGMENT_ITERATOR](net-ring-fragment-iterator.md) | A NET_RING_FRAGMENT_ITERATOR is a wrapper around a NET_RING_ITERATOR. The NET_RING_FRAGMENT_ITERATOR is constrained to fragment rings. |