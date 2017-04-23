---
title: EVT_RXQUEUE_ADVANCE callback function
topic_type:
- apiref
api_name:
- PFN_RXQUEUE_ADVANCE
api_location:
- netrxqueue.h
api_type:
- UserDefined
---

# EVT_RXQUEUE_ADVANCE callback function


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Implemented by the client driver to process receive packets provided by NetAdapterCx.

Syntax
------

```cpp
EVT_RXQUEUE_ADVANCE EvtRxqueueAdvance;

void EvtRxqueueAdvance(
  _In_ NETRXQUEUE RxQueue
)
{ ... }

typedef EVT_RXQUEUE_ADVANCE PFN_RXQUEUE_ADVANCE;
```

Register this callback function in [**NET_RXQUEUE_CONFIG_INIT**](net-rxqueue-config-init.md) before calling [**NetRxQueueCreate**](netrxqueuecreate.md).

Parameters
----------

*RxQueue* [in]  
A handle to a net receive queue.

Return value
------------

This callback function does not return a value.

Remarks
-------

In this callback function, the client driver typically performs the following steps:

1.  Retrieve the receive queue's WDF context.
2.  Call [**NetRxQueueGetRingBuffer**](netrxqueuegetringbuffer.md) to retrieve the ring buffer handle associated with the *RxQueue* handle.
3.  Program packets returned by the OS to hardware. The returned packet window is all packets between NextIndex and EndIndex.
    1.  Iterate until NextIndex matches EndIndex, or the hardware will not accept any new packets.
    2.  Call [**NetRingBufferGetPacketAtIndex**](netringbuffergetpacketatindex.md) to retrieve the packet at NextIndex.
    3.  Free any resources associated with the packet that may have been allocated the last time the descriptor was handed to the OS.
    4.  Program the packet to the associated hardware receive queue.
    5.  Advance NextIndex by calling [**NetRingBufferIncrementIndex**](NetRingBufferIncrementIndex.md). `NetRingBufferIncrementIndex` will handle ring buffer wrap around.

```cpp
VOID
EvtRxQueueAdvance(NETRXQUEUE RxQueue)
{
    // optional: retrieve queue's WDF context
    MY_RX_QUEUE_CONTEXT *rxContext = GetRxQueueContext(RxQueue);

    // tip: store a reference to RingBuffer in the receive context to reduce
    // calls out of driver.
    NET_RING_BUFFER *ringBuffer = NetRxQueueGetRingBuffer(RxQueue);

    // move returned packet descriptors back to the hardware queue
    while (ringBuffer->NextIndex != ringBuffer->EndIndex)
    {
        NET_PACKET *netPacket =
            NetRingBufferGetPacketAtIndex(ringBuffer, ringBuffer->NextIndex);

        // optional: retrieve queue's packet context
        MY_RX_PACKET_CONTEXT *packetContext = GetRxPacketContext(netPacket);

        // free resources associated with the packet
        ...

        // program netPacket to hardware
        ...

        // return the packet to the available descriptor queue
        RingBuffer->NextIndex =
            NetRingBufferIncrementIndex(ringBuffer, ringBuffer->NextIndex);
    }

    // Indicate received packets (see below)
    ...
}
```

4.  Indicate received packets to the OS by advancing `BeginIndex` past each descriptor that the hardware indicates has received packets. If the driver completes packets asynchronously in software (e.g. a USB bus completes receive requests asynchronously), then use the `Completed` flag on the packet's [**NET_PACKET_FRAGMENT**](net-packet-fragment.md) to track completion.

```cpp
    while (ringBuffer->BeginIndex != ringBuffer->NextIndex)
    {
        NET_PACKET *netPacket =
            NetRingBufferGetPacketAtIndex(ringBuffer, ringBuffer->BeginIndex);
        
        // optional: retrieve queue's packet context
        MY_RX_PACKET_CONTEXT *packetContext = GetRxPacketContext(netPacket);

        // Optional: For asynchronous completions, use the Completed flag to 
        // detect completion of the packet.
        if (!netPacket->Data.Completed)
            break;

        RingBuffer->BeginIndex =
            NetRingBufferIncrementIndex(RingBuffer, RingBuffer->BeginIndex);
    }
```

`EvtRxQueueAdvance` is serialized with the queue's [**EvtRxQueueCancel**](evt-rxqueue-cancel.md) and [**EvtRxQueueSetNotificationEnabled**](evt-rxqueue-set-notification-enabled.md) callbacks.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Target platform</p></td>
<td align="left">Universal</td>
</tr>
<tr class="even">
<td align="left"><p>Minimum KMDF version</p></td>
<td align="left"><p>1.21</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Minimum NetAdapterCx version</p></td>
<td align="left"><p>1.0</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">NetRxQueue.h</td>
</tr>
<tr class="odd">
<td align="left"><p>IRQL</p></td>
<td align="left"><p>DISPATCH_LEVEL</p></td>
</tr>
</tbody>
</table>

## See also


[**NetRxQueueGetRingBuffer**](netrxqueuegetringbuffer.md)

 

 






