---
title: EVT_RXQUEUE_CANCEL callback function
topic_type:
- apiref
api_name:
- PFN_RXQUEUE_CANCEL
api_location:
- netrxqueue.h
api_type:
- UserDefined
---

# EVT_RXQUEUE_CANCEL callback function


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Implemented by the client driver to handle operations that must be performed before a receive queue is deleted.

Syntax
------

```cpp
EVT_RXQUEUE_CANCEL EvtRxQueueCancel;

void EvtRxQueueCancel(
  _In_ NETRXQUEUE RxQueue
)
{ ... }

typedef EVT_RXQUEUE_CANCEL PFN_RXQUEUE_CANCEL;
```

Register this callback function in [**NET_RXQUEUE_CONFIG_INIT**](net-rxqueue-config-init.md) before calling [**NetRxQueueCreate**](netrxqueuecreate.md).

Parameters
----------

*RxQueue* [in]  
A handle to a net receive queue.

Return value
------------

This callback function does not return a value.

Example
-----

In its *EVT_RXQUEUE_CANCEL* callback function, the client must complete any outstanding receive packets.  If the client does not return all packets, the operating system does not delete the queue, and NetAdapterCx stops calling the client's callbacks for the queue.  To return packets, the client advances the ring buffer's **BeginIndex** and **NextIndex** indices to **EndIndex**.

```cpp
VOID
EvtRxQueueCancel(NETRXQUEUE RxQueue)
{
    NET_RING_BUFFER *ringBuffer = NetRxQueueGetRingBuffer(RxQueue);

    ringBuffer->BeginIndex = ringBuffer->NextIndex = ringBuffer->EndIndex;
}
```

For additional example code demonstrating ring buffer usage, see [*EVT_RXQUEUE_ADVANCE*](evt-rxqueue-advance.md).

Remarks
-------

NetAdapterCx serializes this callback function along with the receive queue's [*EVT_RXQUEUE_ADVANCE*](evt-rxqueue-advance.md) and [*EVT_RXQUEUE_SET_NOTIFICATION_ENABLED*](evt-rxqueue-set-notification-enabled.md) callback functions.

For more info, see [Transferring Network Data](transferring-network-data.md).

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
<td align="left"><p>PASSIVE_LEVEL</p></td>
</tr>
</tbody>
</table>
