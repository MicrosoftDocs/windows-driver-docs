---
title: Sending network data using net rings
description: This topic describes how NetAdapterCx client drivers use net rings and net ring iterators to send network data.
keywords:
- NetAdapterCx Net rings and net ring iterators, NetCx Net rings and net ring iterators, NetAdapterCx PCI devices net ring, NetAdapterCx asynchronous I/O
ms.date: 11/01/2019
ms.localizationpriority: medium
ms.custom: Vib
---

# Sending network data with net rings

NetAdapterCx client drivers send network data when the framework invokes their [*EvtPacketQueueAdvance*](/windows-hardware/drivers/ddi/netpacketqueue/nc-netpacketqueue-evt_packet_queue_advance) callback function for a transmit queue. During this callback, client drivers post buffers from the queue's fragment ring to hardware, then drain completed packets and fragments back to the OS.

## Transmit (Tx) post and drain operation overview

The following animation illustrates how a client driver for a simple PCI network interface card (NIC) performs post and drain operations for a transmit (Tx) queue.  

![Net ring post and drain operations for transmit (Tx).](images/net_ring_post_and_drain_operations_tx.gif "Net ring post and drain operations for transmit (Tx)")

In this animation, the packets owned by the client driver are highlighted in light blue and dark blue, and fragments owned by the client driver are highlighted in yellow and orange. The lighter colors represent the *drain* subsection of the elements the driver owns, while the darker colors represent the *post* subsection of the elements the driver owns.

## Sending data in order

Here is a typical post and drain sequence for a driver whose device transmits data in order, such as a simple PCI NIC.

1. Call [**NetTxQueueGetRingCollection**](/windows-hardware/drivers/ddi/nettxqueue/nf-nettxqueue-nettxqueuegetringcollection) to retrieve the transmit queue's ring collection structure. You can store this in the queue's context space to reduce calls out of the driver. Use the ring collection to retrieve the transmit queue's packet ring.
2. Post data to hardware:        
    1. Allocate a UINT32 variable for the packet index and set it to the packet ring's **NextIndex**, which is the start of the post subsection of the ring.
    2. Do the following in a loop:
        1. Get a packet by calling [**NetRingGetPacketAtIndex**](/windows-hardware/drivers/ddi/ring/nf-ring-netringgetpacketatindex) with the packet index.
        2. Check if this packet should be ignored. If it should be ignored, skip to step 6 of this loop. If not, continue.
        3. Get this packet's fragments. Retrieve the transmit queue's fragment ring from the ring collection, retrieve the beginning of the packet's fragments from the packet's **FragmentIndex** member, then retrieve the end of the packet's fragments by calling [**NetRingIncrementIndex**](/windows-hardware/drivers/ddi/ring/nf-ring-netringincrementindex) with the packet's **FragmentCount**.
        4. Do the doing the following in a loop:
            1. Call [**NetRingGetFragmentAtIndex**](/windows-hardware/drivers/ddi/ring/nf-ring-netringgetpacketatindex) to get a fragment.
            2. Translate the **NET_FRAGMENT** descriptor into the associated hardware fragment descriptor.
            3. Advance the fragment index by calling  [**NetRingIncrementIndex**](/windows-hardware/drivers/ddi/ring/nf-ring-netringincrementindex).
        5. Update the fragment ring's **Next** index to match the fragment iterator's current **Index**, which indicates that posting to hardware is complete.
        6. Advance the packet index by calling  [**NetRingIncrementIndex**](/windows-hardware/drivers/ddi/ring/nf-ring-netringincrementindex).
    3. Update the packet ring's **NextIndex** to the packet index to finalize posting packets to hardware.
3. Drain completed transmit packets to the OS:
    1. Set the packet index to the packet ring's **BeginIndex**, which is the start of the drain subsection of the ring.
    2. Do the following in a loop:
        1. Get a packet by calling [**NetRingGetPacketAtIndex**](/windows-hardware/drivers/ddi/ring/nf-ring-netringgetpacketatindex) with the packet index.
        2. Check if the packet has finished transmitting. If it has not, break out of the loop.
        3. Advance the packet index by calling  [**NetRingIncrementIndex**](/windows-hardware/drivers/ddi/ring/nf-ring-netringincrementindex).
    3. Update the packet ring's **BeginIndex** to the packet index to finalize posting packets to hardware.

These steps might look like this in code. Note that hardware-specific details such as how to post descriptors to hardware or flushing a successful post transaction are left out for clarity.

```cpp
void
MyEvtTxQueueAdvance(
    NETPACKETQUEUE TxQueue
)
{
    //
    // Retrieve the transmit queue's ring collection and packet ring. 
    // This example stores the Tx queue's ring collection in its queue context space.
    //
    PMY_TX_QUEUE_CONTEXT txQueueContext = MyGetTxQueueContext(TxQueue);
    NET_RING_COLLECTION const * ringCollection = txQueueContext->RingCollection;
    NET_RING * packetRing = ringCollection->Rings[NET_RING_TYPE_PACKET];
    UINT32 currentPacketIndex = 0;

    //
    // Post data to hardware
    //      
    currentPacketIndex = packetRing->NextIndex;
    while(currentPacketIndex != packetRing->EndIndex)
    {
        NET_PACKET * packet = NetRingGetPacketAtIndex(packetRing, currentPacketIndex);        
        if(!packet->Ignore)
        {
            NET_RING * fragmentRing = ringCollection->Rings[NET_RING_TYPE_FRAGMENT];
            UINT32 currentFragmentIndex = packet->FragmentIndex;
            UINT32 fragmentEndIndex = NetRingIncrementIndex(fragmentRing, currentFragmentIndex + packet->FragmentCount - 1);
            
            for(txQueueContext->PacketTransmitControlBlocks[packetIndex]->numTxDescriptors = 0; 
                currentFragmentIndex != fragmentEndIndex; 
                txQueueContext->PacketTransmitControlBlocks[packetIndex]->numTxDescriptors++)
            {
                NET_FRAGMENT * fragment = NetRingGetFragmentAtIndex(fragmentRing, currentFragmentIndex);

                // Post fragment descriptor to hardware
                ...
                //

                currentFragmentIndex = NetRingIncrementIndex(fragmentRing, currentFragmentIndex);
            }

            //
            // Update the fragment ring's Next index to indicate that posting is complete and prepare for draining
            //
            fragmentRing->NextIndex = currentFragmentIndex;
        }
        currentPacketIndex = NetRingIncrementIndex(packetRing, currentPacketIndex);
    }
    packetRing->NextIndex = currentPacketIndex;

    //
    // Drain packets if completed
    //
    currentPacketIndex = packetRing->BeginIndex;
    while(currentPacketIndex != packetRing->NextIndex)
    {        
        NET_PACKET * packet = NetRingGetPacketAtIndex(packetRing, currentPacketIndex); 
        
        // Test packet for transmit completion by checking hardware ownership flags in the packet's last fragment
        // Break if transmit is not complete
        ...
        //
        
        currentPacketIndex = NetRingIncrementIndex(packetRing, currentPacketIndex);
    }
    packetRing->BeginIndex = currentPacketIndex;
}
```

## Sending data out of order

For drivers whose devices might complete transmissions out of order, the primary difference from in-order devices lies in who allocates the transmit buffers and how the driver handles the test for transmission completion. For in-order transmissions with a PCI NIC that is DMA-capable, the OS typically allocates, attaches, and ultimately owns the fragment buffers. Then, in order, the client driver can test each fragment's corresponding hardware ownership flag during *EvtPacketQueueAdvance*.

In contrast to this model, consider a typical USB-based NIC. In this situation, the USB stack owns the memory buffers for transmission and those buffers might be located elsewhere in system memory. The USB stack indicates completions to the client driver out of order, so the client driver needs to record a packet's completion status separately during its completion callback routine. To do so, the client driver can either use the packet's **Scratch** field, or it can use some other method like storing information in its queue context space. Then, in the call to [*EvtPacketQueueAdvance*](/windows-hardware/drivers/ddi/netpacketqueue/nc-netpacketqueue-evt_packet_queue_advance), the client driver checks this information for packet completion testing.
