---
title: Sending network data using net rings
description: This topic describes how NetAdapterCx client drivers use net rings and net ring iterators to send network data.
ms.assetid: 2F3DA1A5-D0C1-4928-80B2-AF41F949FF14
keywords:
- NetAdapterCx Net rings and net ring iterators, NetCx Net rings and net ring iterators, NetAdapterCx PCI devices net ring, NetAdapterCx asynchronous I/O
ms.date: 03/21/2019
ms.localizationpriority: medium
ms.custom: 19H1
---

# Sending network data with net rings

NetAdapterCx client drivers send network data when the framework invokes their [*EvtPacketQueueAdvance*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netpacketqueue/nc-netpacketqueue-evt_packet_queue_advance) callback function for a transmit queue. During this callback, client drivers post buffers from the queue's fragment ring to hardware, then drain completed packets and fragments back to the OS.

## Transmit (Tx) post and drain operation overview

The following animation illustrates how a client driver for a simple PCI network interface card (NIC) performs post and drain operations for a transmit (Tx) queue.  

![Net ring post and drain operations for transmit (Tx)](images/net_ring_post_and_drain_operations_tx.gif "Net ring post and drain operations for transmit (Tx)")

In this animation, the packets owned by the client driver are highlighted in light blue and dark blue, and fragments owned by the client driver are highlighted in yellow and orange. The lighter colors represent the *drain* subsection of the elements the driver owns, while the darker colors represent the *post* subsection of the elements the driver owns.

## Sending data in order

Here is a typical post and drain sequence for a driver whose device transmits data in order, such as a simple PCI NIC.

1. Call **NetTxQueueGetRingCollection** to retrieve the transmit queue's ring collection structure. You can store this in the queue's context space to reduce calls out of the driver. 
2. Post data to hardware:    
    1. Use the ring collection to retrieve the post iterator for the transmit queue's packet ring by calling [**NetRingGetPostPackets**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netringiterator/nf-netringiterator-netringgetpostpackets).
    2. Do the following in a loop:
        1. Get a packet by calling [**NetPacketIteratorGetPacket**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netringiterator/nf-netringiterator-netpacketiteratorgetpacket) with the packet iterator.
        2. Check if this packet should be ignored. If it should be ignored, skip to step 6 of this loop. If not, continue.
        3. Get a fragment iterator for this packet's fragments by calling [**NetPacketIteratorGetFragments**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netringiterator/nf-netringiterator-netpacketiteratorgetfragments).
        4. Do the doing the following in a loop:
            1. Call [**NetFragmentIteratorGetFragment**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netringiterator/nf-netringiterator-netfragmentiteratorgetfragment) with the fragment iterator to get a fragment.
            2. Translate the **NET_FRAGMENT** descriptor into the associated hardware fragment descriptor.
            3. Call [**NetFragmentIteratorAdvance**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netringiterator/nf-netringiterator-netfragmentiteratoradvance) to move to the next fragment for this packet.
        5. Update the fragment ring's **Next** index to match the fragment iterator's current **Index**, which indicates that posting to hardware is complete.
        6. Call [**NetPacketIteratorAdvance**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netringiterator/nf-netringiterator-netpacketiteratoradvance) to move to the next packet.
    3. Call [**NetPacketIteratorSet**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netringiterator/nf-netringiterator-netpacketiteratorset) to finalize posting packets to hardware.
3. Drain completed transmit packets to the OS:
    1. Use the ring collection to retrieve the drain iterator for the transmit queue's packet ring by calling [**NetRingGetDrainPackets**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netringiterator/nf-netringiterator-netringgetdrainpackets).
    2. Do the following in a loop:
        1. Get a packet by calling [**NetPacketIteratorGetPacket**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netringiterator/nf-netringiterator-netpacketiteratorgetpacket).
        2. Check if the packet has finished transmitting. If it has not, break out of the loop.
        2. Call [**NetPacketIteratorAdvance**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netringiterator/nf-netringiterator-netpacketiteratoradvance) to move to the next packet.
    3. Call [**NetPacketIteratorSet**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netringiterator/nf-netringiterator-netpacketiteratorset) to finalize draining packets to the OS.

These steps might look like this in code. Note that hardware-specific details such as how to post descriptors to hardware or flushing a successful post transaction are left out for clarity.

```cpp
void
MyEvtTxQueueAdvance(
    NETPACKETQUEUE TxQueue
)
{
    // Get the transmit queue's context to retrieve the net ring collection
    PMY_TX_QUEUE_CONTEXT txQueueContext = MyGetTxQueueContext(TxQueue);
    NET_RING_COLLECTION const * Rings = txQueueContext->Rings;

    //
    // Post data to hardware
    //
    NET_RING_PACKET_ITERATOR packetIterator = NetRingGetPostPackets(Rings);
    while(NetPacketIteratorHasAny(&packetIterator))
    {
        NET_PACKET* packet = NetPacketIteratorGetPacket(&packetIterator);        
        if(!packet->Ignore)
        {
            NET_FRAGMENT_ITERATOR fragmentIterator = NetPacketIteratorGetFragments(&packetIterator);
            UINT32 packetIndex = NetPacketIteratorGetIndex(&packetIterator);
            
            for(txQueueContext->PacketTransmitControlBlocks[packetIndex]->numTxDescriptors = 0; 
                NetFragmentIteratorHasAny(&fragmentIterator); 
                txQueueContext->PacketTransmitControlBlocks[packetIndex]->numTxDescriptors++)
            {
                NET_FRAGMENT* fragment = NetFragmentIteratorGetFragment(&fragmentIterator);

                // Post fragment descriptor to hardware
                ...
                //

                NetFragmentIteratorAdvance(&fragmentIterator);
            }

            //
            // Update the fragment ring's Next index to indicate that posting is complete and prepare for draining
            //
            fragmentIterator.Iterator.Rings->Rings[NET_RING_TYPE_FRAGMENT]->NextIndex = NetFragmentIteratorGetIndex(&fragmentIterator);
        }
        NetPacketIteratorAdvance(&packetIterator);
    }
    NetPacketIteratorSet(&packetIterator);

    //
    // Drain packets if completed
    //
    packetIterator = NetRingGetDrainPackets(Rings);
    while(NetPacketIteratorHasAny(&packetIterator))
    {        
        NET_PACKET* packet = NetPacketIteratorGetPacket(&packetIterator);
        
        // Test packet for transmit completion by checking hardware ownership flags in the packet's last fragment
        ..
        //
        
        NetPacketIteratorAdvance(&packetIterator);
    }
    NetPacketIteratorSet(&packetIterator);
}
```

## Sending data out of order

For drivers whose devices might complete transmissions out of order, the primary difference from in-order devices lies in who allocates the transmit buffers and how the driver handles the test for transmission completion. For in-order transmissions with a PCI NIC that is DMA-capable, the OS typically allocates, attaches, and ultimately owns the fragment buffers. Then, in order, the client driver can test each fragment's corresponding hardware ownership flag during *EvtPacketQueueAdvance*.

In contrast to this model, consider a typical USB-based NIC. In this situation, the USB stack owns the memory buffers for transmission and those buffers might be located elsewhere in system memory. The USB stack indicates completions to the client driver out of order, so the client driver needs to record a packet's completion status separately during its completion callback routine. To do so, the client driver can either use the packet's **Scratch** field, or it can use some other method like storing information in its queue context space. Then, in the call to [*EvtPacketQueueAdvance*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netpacketqueue/nc-netpacketqueue-evt_packet_queue_advance), the client driver checks this information for packet completion testing. 
