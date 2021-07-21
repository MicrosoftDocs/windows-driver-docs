---
title: Receiving network data using net rings
description: This topic describes how NetAdapterCx client drivers use net rings and net ring iterators to receive network data.
keywords:
- NetAdapterCx Net rings and net ring iterators, NetCx Net rings and net ring iterators, NetAdapterCx PCI devices net ring, NetAdapterCx asynchronous I/O
ms.date: 11/04/2019
ms.localizationpriority: medium
ms.custom: Vib
---

# Receiving network data with net rings

NetAdapterCx client drivers receive network data when the framework invokes their [*EvtPacketQueueAdvance*](/windows-hardware/drivers/ddi/netpacketqueue/nc-netpacketqueue-evt_packet_queue_advance) callback function for a receive queue. During this callback, client drivers indicate receives by draining received fragments and packets to the OS, then post new buffers to hardware.

## Receive (Rx) post and drain operation overview

The following animation illustrates how a client driver for a simple PCI network interface card (NIC) performs post and drain operations for a receive (Rx) queue. Fragment buffers in this example scenario are allocated and attached to the fragment ring by the OS. This example assumes a one-to-one relationship between the hardware receive queue and the OS receive queue.

![Net ring post and drain operations for receive (Rx).](images/net_ring_post_and_drain_operations_rx.gif "Net ring post and drain operations for receive (Rx)")

In this animation, the packets owned by the client driver are highlighted in light blue and dark blue, and fragments owned by the client driver are highlighted in yellow and orange. The lighter colors represent the *drain* subsection of the elements the driver owns, while the darker colors represent the *post* subsection of the elements the driver owns.

## Receiving data in order

Here is a typical sequence for a driver that receives data in order, with one fragment per packet.

1. Call [**NetRxQueueGetRingCollection**](/windows-hardware/drivers/ddi/netrxqueue/nf-netrxqueue-netrxqueuegetringcollection) to retrieve the receive queue's ring collection structure. You can store this in the queue's context space to reduce calls out of the driver. Use the ring collection to retrieve the drain iterator for the receive queue's fragment ring and packet ring.
2. Indicate received data to the OS by draining the net rings:
    1. Allocate UINT32 variables for tracking the fragment ring's current index and packet ring's current index. Set these variables to the **BeginIndex** of their respective net rings, which is the beginning of the drain subsection of the ring. Allocate a UINT32 variable for the end of the fragment ring's drain section by setting it to the fragment ring's **NextIndex**.
    2. Do the following in a loop:
        1. Check if the fragment has been received by the hardware. If not, break out of the loop.
        2. Call [**NetRingGetFragmentAtIndex**](/windows-hardware/drivers/ddi/ring/nf-ring-netringgetpacketatindex) to get a fragment.
        3. Fill in the fragment's information, such as its **ValidLength**, based on its matching hardware descriptor.
        4. Get a packet for this fragment by calling [**NetRingGetPacketAtIndex**](/windows-hardware/drivers/ddi/ring/nf-ring-netringgetpacketatindex).
        5. Bind the fragment to the packet by setting the packet's **FragmentIndex** to the fragment's current index in the fragment ring and setting the number of fragments appropriately (in this example, it is set to **1**). 
        6. Optionally, fill in any other packet information such as checksum info.
        7. Advance the fragment index by calling  [**NetRingIncrementIndex**](/windows-hardware/drivers/ddi/ring/nf-ring-netringincrementindex).
        7. Advance the packet index by calling  [**NetRingIncrementIndex**](/windows-hardware/drivers/ddi/ring/nf-ring-netringincrementindex).
    3. Update the fragment ring's **BeginIndex** to the current fragment index variable and update the packet ring's **BeginIndex** to the current packet index to finalize indicating received packets and their fragments to the OS.
3. Post fragment buffers to hardware for the next receives:    
    1. Set the current fragment index to the fragment ring's **NextIndex**, which is the beginning of the post subsection of the ring. Set the fragment end index to the fragment ring's **EndIndex**.
    2. Do the following in a loop:
        1. Post the fragment's information to the matching hardware descriptor.
        2. Advance the fragment index by calling  [**NetRingIncrementIndex**](/windows-hardware/drivers/ddi/ring/nf-ring-netringincrementindex).
    3. Update the fragment ring's **NextIndex** to the current fragment index variable to finalize posting fragments to hardware.

These steps might look like this in code:

```cpp
void
MyEvtRxQueueAdvance(
    NETPACKETQUEUE RxQueue
)
{
    //
    // Retrieve the receive queue's ring collection and net rings. 
    // This example stores the Rx queue's ring collection in its queue context space.
    //
    PMY_RX_QUEUE_CONTEXT rxQueueContext = MyGetRxQueueContext(RxQueue);
    NET_RING_COLLECTION const * ringCollection = rxQueueContext->RingCollection;
    NET_RING * packetRing = ringCollection->Rings[NET_RING_TYPE_PACKET];
    NET_RING * fragmentRing = ringCollection->Rings[NET_RING_TYPE_FRAGMENT];
    UINT32 currentPacketIndex = 0;
    UINT32 currentFragmentIndex = 0;
    UINT32 fragmentEndIndex = 0;

    //
    // Indicate receives by draining the rings
    //
    currentPacketIndex = packetRing->BeginIndex;
    currentFragmentIndex = fragmentRing->BeginIndex;
    fragmentEndIndex = fragmentRing->NextIndex;
    while(currentFragmentIndex != fragmentEndIndex)
    {
        // Test for fragment reception. Break if fragment has not been received.
        ...
        //

        NET_FRAGMENT * fragment = NetRingGetFragmentAtIndex(fragmentRing, currentFragmentIndex);
        fragment->ValidLength = ... ;
        NET_PACKET * packet = NetRingGetPacketAtIndex(packetRing, currentPacketIndex);
        packet->FragmentIndex = currentFragmentIndex;
        packet->FragmentCount = 1;

        if(rxQueueContext->IsChecksumExtensionEnabled)
        {
            // Fill in checksum info
            ...
            //
        }        

        currentFragmentIndex = NetRingIncrementIndex(fragmentRing, currentFragmentIndex);
        currentPacketIndex = NetRingIncrementIndex(packetRing, currentPacketIndex);
    }
    fragmentRing->BeginIndex = currentFragmentIndex;
    packetRing->BeginIndex = currentPacketIndex;

    //
    // Post fragment buffers to hardware
    //
    currentFragmentIndex = fragmentRing->NextIndex;
    fragmentEndIndex = fragmentRing->EndIndex;
    while(currentFragmentIndex != fragmentEndIndex)
    {
        // Post fragment information to hardware descriptor
        ...
        //

        currentFragmentIndex = NetRingIncrementIndex(fragmentRing, currentFragmentIndex);
    }
    fragmentRing->NextIndex = currentFragmentIndex;
}
```

## Receiving data out of order

Unlike a [Tx](sending-network-data-with-net-rings.md) queue, client drivers don't typically receive data out of order if they have one OS receive queue per hardware receive queue. This is regardless of the type of the client driver's NIC. Whether the device is PCI-based and the OS allocates and owns the receive buffers, or whether the device is USB-based and the USB stack owns the receive buffers, the client driver initializes a packet for each fragment received and indicates it to the OS. The order is not important in this case.

If your hardware supports more than one OS receive queue per hardware receive queue, you must synchronize access to the receive buffers. The scope of doing so is outside of this topic and is dependent on your hardware's design.
