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

EvtRxQueueCancel is called to request that the adapter terminate any outstanding receive operations. Unlike for EvtTxQueueCancel, the receive queue *must* use this opportunity to return any outstanding buffers to the OS. For more information on operating the ring buffer, see [**EvtRxQueueAdvance**](evt-rxqueue-advance.md).

Typically, this involves advancing `BeginIndex` and `NextIndex` to `EndIndex`. If the receive queue does not return all packets in Cancel, this can result in a stuck queue.

```cpp
VOID
EvtRxQueueCancel(NETRXQUEUE RxQueue)
{
    NET_RING_BUFFER *ringBuffer = NetRxQueueGetRingBuffer(RxQueue);

    ringBuffer->BeginIndex = ringBuffer->NextIndex = ringBuffer->EndIndex;
}
```

Remarks
-------

`EvtRxQueueCancel` is called by the framework to wind down the receive queue. Use the cancel callback to return all packets to the OS so the OS can destroy the queue.

`EvtRxQueueCencel` is serialized with the queue's [**EvtRxQueueAdvance**](evt-rxqueue-advance.md) and [**EvtRxQueueSetNotificationEnabled**](evt-rxqueue-set-notification-enabled.md) callbacks.

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

 

 





