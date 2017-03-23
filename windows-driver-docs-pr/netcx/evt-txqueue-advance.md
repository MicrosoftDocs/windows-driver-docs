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
EVT_TXQUEUE_ADVANCE EvtTxqueueAdvance;

void EvtTxqueueAdvance(
  _In_ NETTXQUEUE TxQueue
)
{ ... }

typedef EVT_TXQUEUE_ADVANCE PFN_TXQUEUE_ADVANCE;
```

Register your implementation of this callback function by setting the appropriate member of [**NET_TXQUEUE_CONFIG**](net-txqueue-config.md) and then calling [**NetTxQueueCreate**](nettxqueuecreate.md).

Parameters
----------

*TxQueue* [in]  
A handle to a net transmit queue object.

Return value
------------

This callback function does not return a value.

Remarks
-------
In this callback, the client retrieves packets from the queue, programs the hardware to send the data, and then completes the packets.

To retrieve packets, the client can either update the ring buffer's **BeginIndex** manually, or it can call helper macros such as [**NetRingBufferReturnCompletedPackets method**](netringbufferreturncompletedpackets.md).

The following example retrieves incoming transmit packets from the queue and then immediately completes them.

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

For more info, see [*EVT_RXQUEUE_ADVANCE*](evt-rxqueue-advance.md).

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
<td align="left">Nettxqueue.h</td>
</tr>
<tr class="odd">
<td align="left"><p>IRQL</p></td>
<td align="left"><p>DISPATCH_LEVEL</p></td>
</tr>
</tbody>
</table>

## See also


[**NetTxQueueGetRingBuffer**](nettxqueuegetringbuffer.md)

 

 






