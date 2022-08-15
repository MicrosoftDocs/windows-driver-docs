---
title: Canceling network data using net rings
description: This topic describes how NetAdapterCx client drivers use net rings and net ring iterators to cancel network data.
keywords:
- NetAdapterCx Net rings and net ring iterators cancel, NetAdapterCx cancel packet queue
ms.date: 11/01/2019
ms.custom: Vib
---

# Canceling network data with net rings

NetAdapterCx client drivers cancel network data when the framework invokes their [*EvtPacketQueueCancel*](/windows-hardware/drivers/ddi/netpacketqueue/nc-netpacketqueue-evt_packet_queue_cancel) callback function for a packet queue. This callback is where client drivers perform any processing needed before the framework deletes the packet queues.

### Canceling a transmit queue

In your *EvtPacketQueueCancel* callback function for a transmit queue, you have an opportunity to complete any outstanding transmit packets. Unlike with a receive queue, you not required to do so. If you leave outstanding packets, NetAdapterCx calls your [*EvtPacketQueueAdvance*](/windows-hardware/drivers/ddi/netpacketqueue/nc-netpacketqueue-evt_packet_queue_advance) for the transmit queue, where you process them as part of your regular operation.

If your hardware supports canceling in-flight transmits, you should also advance the net ring's post packet iterator past all canceled packets. This might look like the following example:

```C++
void
MyEvtTxQueueCancel(
    NETPACKETQUEUE TxQueue
)
{
    // Get the transmit queue's context to retrieve the net ring collection
    PMY_TX_QUEUE_CONTEXT txQueueContext = MyGetTxQueueContext(TxQueue);
    NET_RING_COLLECTION const * ringCollection = txQueueContext->RingCollection;
    NET_RING * packetRing = ringCollection->Rings[NET_RING_TYPE_PACKET];
    UINT32 currentPacketIndex = packetRing->BeginIndex;
    UINT32 packetEndIndex = packetRing->EndIndex;

    while (currentPacketIndex != packetEndIndex)
    {
        // Mark this packet as canceled with the scratch field, then move past it
        NET_PACKET * packet = NetRingGetPacketAtIndex(packetRing, currentPacketIndex);
        packet->Scratch = 1;
        currentPacketIndex = NetRingIncrementIndex(packetRing, currentPacketIndex);
    }
    
    packetRing->BeginIndex = packetRing->EndIndex;
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
    NET_RING_COLLECTION const * ringCollection = rxQueueContext->RingCollection;
    NET_RING * packetRing = ringCollection->Rings[NET_RING_TYPE_PACKET];
    NET_RING * fragmentRing = ringCollection->Rings[NET_RING_TYPE_FRAGMENT];
    UINT32 currentPacketIndex = packetRing->BeginIndex;
    UINT32 packetEndIndex = packetRing->EndIndex;

    // Set hardware register for cancellation
    ...
    //

    // Indicate receives
    ...
    //

    // Get all packets and mark them for ignoring
    currentPacketIndex = packetRing->BeginIndex;
    while(currentPacketIndex != packetEndIndex)
    {
        NET_PACKET * packet = NetRingGetPacketAtIndex(packetRing, currentPacketIndex);
        packet->Ignore = 1;
        currentPacketIndex = NetRingIncrementIndex(packetRing, currentPacketIndex);
    }
    
    packetRing->BeginIndex = packetRing->EndIndex;

    // Return all fragments to the OS
    fragmentRing->BeginIndex = fragmentRing->EndIndex;
}
```
