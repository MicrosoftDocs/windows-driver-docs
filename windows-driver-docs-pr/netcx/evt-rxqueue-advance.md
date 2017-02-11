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

# EVT\_RXQUEUE\_ADVANCE callback function


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Implemented by the client driver to process receive packets provided by NetAdapterCx.

Syntax
------

```ManagedCPlusPlus
EVT_RXQUEUE_ADVANCE EvtRxqueueAdvance;

void EvtRxqueueAdvance(
  _In_ NETRXQUEUE RxQueue
)
{ ... }

typedef EVT_RXQUEUE_ADVANCE PFN_RXQUEUE_ADVANCE;
```

Register your implementation of this callback function by setting the appropriate member of [**NET\_RXQUEUE\_CONFIG**](net-rxqueue-config.md) and then calling [**NetRxQueueCreate**](netrxqueuecreate.md).

Parameters
----------

*RxQueue* \[in\]  
A handle to a net receive queue object.

Return value
------------

This callback function does not return a value.

Remarks
-------

In this callback function, the client driver typically performs the following steps:

1.  Call [**NetRxQueueGetRingBuffer**](netrxqueuegetringbuffer.md) to retrieve the ring buffer associated with the *RxQueue* handle.
2.  Iterate on the packets in the ring buffer.
    1.  Call [**NetRingBufferGetNextPacket**](netringbuffergetnextpacket.md). (If **NetRingBufferGetNextPacket** returns NULL, there are no more new packets available.)
    2.  Program that packet to receive. (Insert this NET\_PACKET in the driver's available to receive list).
    3.  Call [**NetRingBufferAdvanceNextPacket**](netringbufferadvancenextpacket.md)

3.  Return completed packets to the OS. The client driver can track asynchronous completion of individual packets using a flag on the packet. For packets that have been completed (have new receive data), advance the **BeginIndex** value of the ring buffer.
    ```
        UINT32 numOfElments =
            NetRingBufferGetNumberOfElementsInRange(RingBuffer,
                                                    RingBuffer->BeginIndex,
                                                    RingBuffer->NextIndex);
        PNET_PACKET pPacket = NULL;

        while (numOfElments > 0)
        {
            pPacket = (PNET_PACKET) NetRingBufferGetElementAtIndex(RingBuffer, RingBuffer->BeginIndex);

            if (!pPacket->Data.Scratch)
                break;

            RingBuffer->BeginIndex = NetRingBufferIncrementIndex(RingBuffer,
                                                                 RingBuffer->BeginIndex);

            numOfElments--;
        }
    ```

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
<td align="left">Netrxqueue.h</td>
</tr>
<tr class="odd">
<td align="left"><p>IRQL</p></td>
<td align="left"><p>DISPATCH_LEVEL</p></td>
</tr>
</tbody>
</table>

## See also


[**NetRxQueueGetRingBuffer**](netrxqueuegetringbuffer.md)

 

 






