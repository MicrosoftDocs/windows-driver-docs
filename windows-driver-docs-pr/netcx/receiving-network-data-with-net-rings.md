---
title: Receiving network data using net rings
description: This topic describes how NetAdapterCx client drivers use net rings and net ring iterators to receive network data.
ms.assetid: 78D202E2-4123-4F63-9B86-48400C2CCC38
keywords:
- NetAdapterCx Net rings and net ring iterators, NetCx Net rings and net ring iterators, NetAdapterCx PCI devices net ring, NetAdapterCx asynchronous I/O
ms.date: 03/21/2019
ms.localizationpriority: medium
ms.custom: 19H1
---

# Receiving network data with net rings

NetAdapterCx client drivers receive network data when the framework invokes their [*EvtPacketQueueAdvance*](https://docs.microsoft.com/windows-hardware/drivers/ddi/netpacketqueue/nc-netpacketqueue-evt_packet_queue_advance) callback function for a receive queue. During this callback, client drivers indicate receives by draining received fragments and packets to the OS, then post new buffers to hardware.

## Receive (Rx) post and drain operation overview

The following animation illustrates how a client driver for a simple PCI network interface card (NIC) performs post and drain operations for a receive (Rx) queue. Fragment buffers in this example scenario are allocated and attached to the fragment ring by the OS. This example assumes a one-to-one relationship between the hardware receive queue and the OS receive queue.

![Net ring post and drain operations for receive (Rx)](images/net_ring_post_and_drain_operations_rx.gif "Net ring post and drain operations for receive (Rx)")

In this animation, the packets owned by the client driver are highlighted in light blue and dark blue, and fragments owned by the client driver are highlighted in yellow and orange. The lighter colors represent the *drain* subsection of the elements the driver owns, while the darker colors represent the *post* subsection of the elements the driver owns.

## Receiving data in order

Here is a typical sequence for a driver that receives data in order, with one fragment per packet.

1. Call **NetRxQueueGetRingCollection** to retrieve the receive queue's ring collection structure. You can store this in the queue's context space to reduce calls out of the driver. 
2. Indicate received data to the OS by draining the net rings:
    1. Use the ring collection to retrieve the drain iterator for the receive queue's fragment ring through a call to [**NetRingGetDrainFragments**](https://docs.microsoft.com/windows-hardware/drivers/ddi/netringiterator/nf-netringiterator-netringgetdrainfragments).
    2. Get a packet iterator for all available packets in the packet ring by calling [**NetRingGetAllPackets**](https://docs.microsoft.com/windows-hardware/drivers/ddi/netringiterator/nf-netringiterator-netringgetallpackets).
    3. Do the following in a loop:
        1. Check if the fragment has been received by the hardware. If not, break out of the loop.
        2. Get the fragment iterator's current fragment by calling [**NetFragmentIteratorGetFragment**](https://docs.microsoft.com/windows-hardware/drivers/ddi/netringiterator/nf-netringiterator-netfragmentiteratorgetfragment).
        3. Fill in the fragment's information, such as its **ValidLength**, based on its matching hardware descriptor.
        4. Get a packet for this fragment by calling [**NetPacketIteratorGetPacket**](https://docs.microsoft.com/windows-hardware/drivers/ddi/netringiterator/nf-netringiterator-netpacketiteratorgetpacket).
        5. Bind the fragment to the packet by setting the packet's **FragmentIndex** to the fragment's current index in the fragment ring and setting the number of fragments appropriately (in this example, it is set to **1**). 
        6. Optionally, fill in any other packet information such as checksum info.
        7. Call [**NetFragmentIteratorAdvance**](https://docs.microsoft.com/windows-hardware/drivers/ddi/netringiterator/nf-netringiterator-netfragmentiteratoradvance) to move to the next fragment.
        7. Call [**NetPacketIteratorAdvance**](https://docs.microsoft.com/windows-hardware/drivers/ddi/netringiterator/nf-netringiterator-netpacketiteratoradvance) to move to the next packet.
    4. Call [**NetFragmentIteratorSet**](https://docs.microsoft.com/windows-hardware/drivers/ddi/netringiterator/nf-netringiterator-netfragmentiteratorset) and [**NetPacketIteratorSet**](https://docs.microsoft.com/windows-hardware/drivers/ddi/netringiterator/nf-netringiterator-netpacketiteratorset) to finalize indicating received packets and their fragments to the OS.
3. Post fragment buffers to hardware for the next receives:    
    1. Use the ring collection to retrieve the post iterator for the receive queue's fragment ring by calling [**NetRingGetPostFragments**](https://docs.microsoft.com/windows-hardware/drivers/ddi/netringiterator/nf-netringiterator-netringgetpostfragments).
    2. Do the following in a loop:
        1. Get the fragment iterator's current index by calling [**NetFragmentIteratorGetIndex**](https://docs.microsoft.com/windows-hardware/drivers/ddi/netringiterator/nf-netringiterator-netfragmentiteratorgetindex).
        2. Post the fragment's information to the matching hardware descriptor.
        3. Call [**NetFragmentIteratorAdvance**](https://docs.microsoft.com/windows-hardware/drivers/ddi/netringiterator/nf-netringiterator-netfragmentiteratoradvance) to move to the next fragment.
    3. Call [**NetFragmentIteratorSet**](https://docs.microsoft.com/windows-hardware/drivers/ddi/netringiterator/nf-netringiterator-netfragmentiteratorset) to finalize posting fragments to hardware.

These steps might look like this in code:

```cpp
void
MyEvtRxQueueAdvance(
    NETPACKETQUEUE RxQueue
)
{
    // Get the receive queue's context to retrieve the net ring collection
    PMY_RX_QUEUE_CONTEXT rxQueueContext = MyGetRxQueueContext(RxQueue);
    NET_RING_COLLECTION const * Rings = rxQueueContext->Rings;

    //
    // Indicate receives by draining the rings
    //
    NET_RING_FRAGMENT_ITERATOR fragmentIterator = NetRingGetDrainFragments(Rings);
    NET_RING_PACKET_ITERATOR packetIterator = NetRingGetAllPackets(Rings);
    while(NetFragmentIteratorHasAny(&fragmentIterator))
    {
        UINT32 currentFragmentIndex = NetFragmentIteratorGetIndex(&fragmentIterator);

        // Test for fragment reception
        ...
        //

        NET_FRAGMENT* fragment = NetFragmentIteratorGetFragment(&fragmentIterator);
        fragment->ValidLength = ... ;
        NET_PACKET* packet = NetPacketIteratorGetPacket(&packetIterator);
        packet->FragmentIndex = currentFragmentIndex;
        packet->FragmentCount = 1;

        if(rxQueueContext->IsChecksumExtensionEnabled)
        {
            // Fill in checksum info
            ...
            //
        }        

        NetFragmentIteratorAdvance(&fragmentIterator);
        NetPacketIteratorAdvance(&packetIterator);
    }
    NetFragmentIteratorSet(&fragmentIterator);
    NetFragmentIteratorSet(&packetIterator);

    //
    // Post fragment buffers to hardware
    //
    fragmentIterator = NetRingGetPostFragments(Rings);
    while(NetFragmentIteratorHasAny(&fragmentIterator))
    {
        UINT32 currentFragmentIndex = NetFragmentIteratorGetIndex(&fragmentIterator);

        // Post fragment information to hardware descriptor
        ...
        //

        NetFragmentIteratorAdvance(&fragmentIterator);
    }
    NetFragmentIteratorSet(&fragmentIterator);
}
```

## Receiving data out of order

Unlike a [Tx](sending-network-data-with-net-rings.md) queue, client drivers don't typically receive data out of order if they have one OS receive queue per hardware receive queue. This is regardless of the type of the client driver's NIC. Whether the device is PCI-based and the OS allocates and owns the receive buffers, or whether the device is USB-based and the USB stack owns the receive buffers, the client driver initializes a packet for each fragment received and indicates it to the OS. The order is not important in this case.

If your hardware supports more than one OS receive queue per hardware receive queue, you must synchronize access to the receive buffers. The scope of doing so is outside of this topic and is dependent on your hardware's design.
