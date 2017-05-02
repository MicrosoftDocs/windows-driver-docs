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

In its *EVT_TXQUEUE_CANCEL* callback function, the client has an opportunity to complete any outstanding transmit packets.  Unlike with [*EVT_RXQUEUE_CANCEL*](evt-rxqueue-cancel.md), the client is not required to do so.  If the client leaves outstanding packets, NetAdapterCx calls the client's [*EVT_TXQUEUE_ADVANCE*](evt-txqueue-advance.md), where the client processes them as part of its regular operation.

If the hardware supports cancelling in-flight transmits, the client should also advance the ring buffer's **BeginIndex** past all cancelled packets.  If the hardware does not support cancellation, this callback can return without taking action.

NetAdapterCx serializes this callback function along with the receive queue's [*EVT_TXQUEUE_ADVANCE*](evt-rxqueue-advance.md) and [*EVT_TXQUEUE_SET_NOTIFICATION_ENABLED*](evt-txqueue-set-notification-enabled.md) callback functions.

For more info about ring buffer usage, see [*EVT_TXQUEUE_ADVANCE*](evt-txqueue-advance.md) and [Transferring Network Data](transferring-network-data.md).

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

 

 





