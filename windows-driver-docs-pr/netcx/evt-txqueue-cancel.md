---
title: EVT_TXQUEUE_CANCEL callback function
topic_type:
- apiref
api_name:
- PFN_TXQUEUE_CANCEL
api_location:
- nettxqueue.h
api_type:
- UserDefined
---

# EVT_TXQUEUE_CANCEL callback function


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Implemented by the client driver to handle operations that must be performed before a transmit queue is deleted.

Syntax
------

```cpp
EVT_TXQUEUE_CANCEL EvtTxqueueCancel;

void EvtTxQueueCancel(
  _In_ NETTXQUEUE TxQueue
)
{ ... }

typedef EVT_TXQUEUE_CANCEL PFN_TXQUEUE_CANCEL;
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

EvtTxQueueCancel is called to request that the adapter terminate any outstanding transmit operations. The device driver should attempt to stop any outstanding transmit operations, but it is not required since the OS can drain the remaining transmits via the queue's `EvtTxQueueAdvance` like usual. For more information on operating the ring buffer in general, see [**EvtTxQueueAdvance**](evt-txqueue-advance.md).

If the hardware supports cancelling in-flight transmits, the adapter should advance BeginIndex past all cancelled packets, as well. If the hardware does not support cancellation, this callback can be a no-op.

`EvtTxQueueCancel` is serialized with the queue's [**EvtTxQueueAdvance**](evt-txqueue-advance.md) and [**EvtTxQueueSetNotificationEnabled**](evt-txqueue-set-notification-enabled.md) callbacks.

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
<td align="left"><p>PASSIVE_LEVEL</p></td>
</tr>
</tbody>
</table>

 

 





