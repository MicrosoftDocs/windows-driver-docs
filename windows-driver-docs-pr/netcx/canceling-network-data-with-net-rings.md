---
title: Canceling network data using net rings
description: This topic describes how NetAdapterCx client drivers use net rings and net ring iterators to cancel network data.
ms.assetid: 009CC1D7-5168-4D7B-9284-04F922D37434
keywords:
- NetAdapterCx Net rings and net ring iterators cancel, NetAdapterCx cancel packet queue
ms.date: 01/24/2019
ms.localizationpriority: medium
ms.custom: 19H1
---

# Canceling network data with net rings

NetAdapterCx client drivers cancel network data when the framework invokes their [*EvtPacketQueueCancel*](https://docs.microsoft.com/windows-hardware/drivers/ddi/netpacketqueue/nc-netpacketqueue-evt_packet_queue_cancel) callback function for a packet queue. This callback is where client drivers perform any processing needed before the framework deletes the packet queues.

### Canceling a transmit queue

In your *EvtPacketQueueCancel* callback function for a transmit queue, you have an opportunity to complete any outstanding transmit packets. Unlike with a receive queue, you not required to do so. If you leave outstanding packets, NetAdapterCx calls your [*EvtPacketQueueAdvance*](https://docs.microsoft.com/windows-hardware/drivers/ddi/netpacketqueue/nc-netpacketqueue-evt_packet_queue_advance) for the transmit queue, where you process them as part of your regular operation.

If your hardware supports canceling in-flight transmits, you should also advance the net ring's post packet iterator past all canceled packets. This might look like the following example:

```C++
void
MyEvtTxQueueCancel(
    NETPACKETQUEUE TxQueue
)
{
    // Get the transmit queue's context to retrieve the net ring collection
    PMY_TX_QUEUE_CONTEXT txQueueContext = MyGetTxQueueContext(TxQueue);
    NET_RING_COLLECTION const * rings = txQueueContext->Rings;

    NET_RING_PACKET_ITERATOR packetIterator = NetRingGetPostPackets(rings);
    while (NetPacketIteratorHasAny(&packetIterator))
    {
        // Mark this packet as canceled with the scratch field, then move past it
        NetPacketIteratorGetPacket(&packetIterator)->Scratch = 1;
        NetPacketIteratorAdvance(&packetIterator);
    }
    NetPacketIteratorSet(&packetIterator);
}
```

If your hardware does not support cancellation, this callback can return without taking action.

### Canceling a receive queue

In your *EvtPacketQueueCancel* callback function for a receive queue, you must complete any outstanding receive packets. If you do not return all packets, the operating system does not delete the queue, and NetAdapterCx stops calling your callbacks for the queue. 

To return packets, you should first attempt to indicate any receives that might have been indicated while the receive path was being disabled, then set all packets to be ignored and return all fragments to the OS. This might look like the following code example.

> [!NOTE]
> This example leaves out details for indicating receives. For a code sample of receiving data, see [Receiving network data with net rings](receiving-network-data-with-net-rings.md).

```C++
void
MyEvtRxQueueCancel(
    NETPACKETQUEUE RxQueue
)
{
    // Get the receive queue's context to retrieve the net ring collection
    PMY_RX_QUEUE_CONTEXT rxQueueContext = MyGetRxQueueContext(RxQueue);
    NET_RING_COLLECTION const * rings = rxQueueContext->Rings;

    // Set hardware register for cancellation
    ...
    //

    // Indicate receives
    ...
    //

    // Get all packets and mark them for ignoring
    NET_RING_PACKET_ITERATOR packetIterator = NetRingGetAllPackets(rings);
    while(NetPacketIteratorHasAny(&packetIterator))
    {
        NetPacketIteratorGetPacket(&packetIterator)->Ignore = 1;
        NetPacketIteratorAdvance(&packetIterator);
    }
    NetPacketIteratorSet(&packetIterator);

    // Return all fragments to the OS
    NET_RING_FRAGMENT_ITERATOR fragmentIterator = NetRingGetAllFragments(rings);
    NetFragmentIteratorAdvanceToTheEnd(&fragmentIterator);
    NetFragmentIteratorSet(&fragmentIterator);
}
```
