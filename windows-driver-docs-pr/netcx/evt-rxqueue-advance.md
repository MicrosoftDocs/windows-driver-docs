---
title: EVT\_RXQUEUE\_ADVANCE callback function
description: Implemented by the client driver to process receive packets provided by NetAdapterCx.
ms.assetid: 444e4845-b6fd-46a7-9d48-e99ff25cc113
keywords: ["EvtRxqueueAdvance callback function Network Drivers Starting with Windows Vista", "EVT_RXQUEUE_ADVANCE", "PFN_RXQUEUE_ADVANCE callback function pointer Network Drivers Starting with Windows Vista"]
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
<td align="left">[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</td>
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20EVT_RXQUEUE_ADVANCE%20callback%20function%20%20RELEASE:%20%281/19/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





