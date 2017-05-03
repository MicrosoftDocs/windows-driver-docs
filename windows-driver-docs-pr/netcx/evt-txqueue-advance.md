---
title: EVT_TXQUEUE_ADVANCE callback function
topic_type:
- apiref
api_name:
- PFN_TXQUEUE_ADVANCE
api_location:
- nettxqueue.h
api_type:
- UserDefined
---

# EVT_TXQUEUE_ADVANCE callback function

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Implemented by the client driver to process transmit packets provided by NetAdapterCx.

Syntax
------

```cpp
EVT_TXQUEUE_ADVANCE EvtTxQueueAdvance;

void EvtTxQueueAdvance(
  _In_ NETTXQUEUE TxQueue
)
{ ... }

typedef EVT_TXQUEUE_ADVANCE PFN_TXQUEUE_ADVANCE;
```

Register this callback function in [**NET_TXQUEUE_CONFIG_INIT**](net-txqueue-config-init.md) before calling [**NetTxQueueCreate**](nettxqueuecreate.md).

Parameters
----------

*TxQueue* [in]  
A handle to a net transmit queue.

Return value
------------

This callback function does not return a value.

Remarks
-------
In this callback, the client retrieves packets from the queue, programs the hardware to send the data, and returns any completed packets.

To return packets, call [**NetRingBufferIncrementIndex**](NetRingBufferIncrementIndex.md), or use a helper macro such as [**NetRingBufferReturnCompletedPackets method**](netringbufferreturncompletedpackets.md).

The following example retrieves incoming transmit packets from the queue and immediately completes them.

```cpp
VOID
EvtTxQueueAdvance(NETTXQUEUE TxQueue)
{
    NET_RING_BUFFER *ringBuffer = NetTxQueueGetRingBuffer(TxQueue);
    NET_PACKET *netPacket;

    // Retrieve pointer to packet at the NextIndex value of the ring buffer

    while ((netPacket = NetRingBufferGetNextPacket(ringBuffer)) != nullptr)
    {
        
        // Transmit the data
        
        netPacket->Data.Completed = TRUE;

        // Increment NextIndex
        
        NetRingBufferAdvanceNextPacket(ringBuffer);
    }

    NetRingBufferReturnCompletedPackets(ringBuffer);
}
```

NetAdapterCx serializes this callback function along with the queue's [*EVT_TXQUEUE_CANCEL*](evt-txqueue-cancel.md) and [*EVT_TXQUEUE_SET_NOTIFICATION_ENABLED*](evt-txqueue-set-notification-enabled.md) callback functions.

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
<td align="left">NetTxQueue.h</td>
</tr>
<tr class="odd">
<td align="left"><p>IRQL</p></td>
<td align="left"><p>&lt;=DISPATCH_LEVEL</p></td>
</tr>
</tbody>
</table>

## See also


[**NetTxQueueGetRingBuffer**](nettxqueuegetringbuffer.md)

 

 






