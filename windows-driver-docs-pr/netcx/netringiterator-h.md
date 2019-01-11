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

- [Net rings and net ring iterators](net-rings-and-net-ring-iterators.md)

Netringiterator.h contains the following programming interfaces:

## Functions

| Title | Description |
| --- | --- |
| [NetRingGetPostPackets](netringgetpostpackets.md) | The NetRingGetPostPackets method gets a packet iterator for the post subsection of a packet ring. |
| [NetRingGetDrainPackets](netringgetdrainpackets.md) | The NetRingGetDrainPackets method gets a packet iterator for the drain subsection of a packet ring. |
| [NetRingGetAllPackets](netringgetallpackets.md) | The NetRingGetAllPackets method gets a packet iterator for the entire range in a packet ring that a client driver owns. |
| [NetPacketIteratorGetPacket](netpacketiteratorgetpacket.md) | The NetPacketIteratorGetPacket method gets the NET_PACKET structure at a packet iterator's Index. |
| [NetPacketIteratorGetIndex](netpacketiteratorgetindex.md) | The NetPacketIteratorGetIndex method gets the current Index of a packet iterator. |
| [NetPacketIteratorHasAny](netpacketiteratorhasany.md) | The NetPacketIteratorHasAny method determines whether a packet iterator iterator has any valid elements to process in the packet ring. |
| [NetPacketIteratorGetCount](netpacketiteratorgetcount.md) | The NetPacketIteratorGetCount method gets the count of packets that a client driver owns in the packet ring. |
| [NetPacketIteratorAdvance](netpacketiteratoradvance.md) | The NetPacketIteratorAdvance method advances the Index of a packet iterator by one. |
| [NetPacketIteratorAdvanceToTheEnd](netpacketiteratoradvancetotheend.md) | The NetPacketIteratorAdvanceToTheEnd method advances the current Index of a packet iterator to its End index. |
| [NetPacketIteratorSet](netpacketiteratorset.md) | The NetPacketIteratorSet method completes a client driver's post or drain operation on the packet ring. |
| [NetPacketIteratorGetFragments](netpacketiteratorgetfragments.md) | The NetPacketIteratorGetFragments method gets the fragments associated with a packet. |
| [NetRingGetPostFragments](netringgetpostfragments.md) | The NetRingGetPostFragments method gets a fragment iterator for the current post subsection of a fragment ring. |
| [NetRingGetDrainFragments](netringgetdrainfragments.md) | The NetRingGetDrainFragments method gets a fragment iterator for the current drain subsection of a fragment ring. |
| [NetRingGetAllFragments](netringgetallfragments.md) | The NetRingGetAllFragments method gets a fragment iterator for the entire range in a fragment ring that a client driver owns. |
| [NetRingIteratorGetFragment](netringiteratorgetfragment.md) | The NetRingIteratorGetFragment method gets the NET_FRAGMENT structure at a fragment iterator's Index. |

| [NetRingSetRxPostFragmentIterator](netringsetrxpostfragmentiterator.md) | The NetRingSetRxPostFragmentIterator method advances the beginning of the post section for a receive (Rx) queue's net fragment ring to the current index of the ring's post fragment iterator. |
| [NetRingSetRxDrainFragmentIterator](netringsetrxdrainfragmentiterator.md) | The NetRingSetRxDrainFragmentIterator method advances the beginning of the drain section for a receive (Rx) queue's fragment ring to the current index of the ring's drain fragment iterator. |


| [NetRingSetTxPostPacketIterator](netringsettxpostpacketiterator.md) | The NetRingSetTxPostPacketIterator method advances the beginning of the post section for a transmit (Tx) queue's packet ring to the current index of the ring's post packet iterator. |
| [NetRingGetTxDrainPacketIterator](netringgettxdrainpacketiterator.md) | The NetRingGetTxDrainPacketIterator method gets a packet iterator for the current drain section of a transmit (Tx) queue's packet ring. |
| [NetRingSetTxDrainPacketIterator](netringsettxdrainpacketiterator.md) | The NetRingSetTxDrainPacketIterator method advances the beginning of the drain section for a transmit (Tx) queue's packet ring to the current index of the ring's drain packet iterator. |
| [NetRingSetTxPostFragmentIterator](netringsettxpostfragmentiterator.md) | The NetRingSetTxPostFragmentIterator method advances the beginning of the post section for a transmit (Tx) queue's fragment ring to the current index of a post fragment iterator. |
| [NetRingGetTxDrainPacketFragmentIterator](netringgettxdrainpacketfragmentiterator.md) | For a packet in the drain section of a transmit (Tx) queue's packet ring, the NetRingGetTxPostPacketFragmentIterator method gets the drain fragment iterator for that packet's fragments. |
| [NetRingSetTxDrainFragmentIterator](netringsettxdrainfragmentiterator.md) | The NetRingSetTxDrainFragmentIterator method advances the beginning of the drain section for a transmit (Tx) queue's fragment ring to the current index of a drain fragment iterator. |
| [NetRingSetAllFragmentIterator](netringsetallfragmentiterator.md) | The NetRingSetAllFragmentIterator method advances the beginning of the section of a fragment ring that a client driver owns to the current index of a fragment iterator. |
| [NetRingSetAllPacketIterator](netringsetallpacketiterator.md) | The NetRingSetAllPacketIterator method advances the beginning of the section of a packet ring that a client driver owns to the current index of a packet iterator. |
| [NetRingAdvanceFragmentIterator](netringadvancefragmentiterator.md) | The NetRingAdvanceFragmentIterator method advances the index of a NET_RING_FRAGMENT_ITERATOR by one. |
| [NetRingAdvanceEndFragmentIterator](netringadvanceendfragmentiterator.md) | The NetRingAdvanceEndFragmentIterator method advances the current index of a NET_RING_FRAGMENT_ITERATOR to the iterator's End index. |
| [NetRingFragmentIteratorGetCount](netringfragmentiteratorgetcount.md) | The NetRingFragmentIteratorGetCount method gets the count of fragments between a fragment iterator's current Index inclusive and its End index. |


## Structures

| Title | Description |
| --- | --- |
| [NET_RING_ITERATOR](net-ring-iterator.md) | A NET_RING_ITERATOR is a small structure that contains references to the post and drain indices of a NET_RING to which it belongs. |
| [NET_RING_PACKET_ITERATOR](net-ring-packet-iterator.md) | A NET_RING_PACKET_ITERATOR is a wrapper around a NET_RING_ITERATOR. The NET_RING_PACKET_ITERATOR is constrained to packet rings. |
| [NET_RING_FRAGMENT_ITERATOR](net-ring-fragment-iterator.md) | A NET_RING_FRAGMENT_ITERATOR is a wrapper around a NET_RING_ITERATOR. The NET_RING_FRAGMENT_ITERATOR is constrained to fragment rings. |