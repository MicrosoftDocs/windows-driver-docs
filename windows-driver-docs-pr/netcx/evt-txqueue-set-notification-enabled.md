---
title: EVT_TXQUEUE_SET_NOTIFICATION_ENABLED callback function
topic_type:
- apiref
api_name:
- PFN_TXQUEUE_SET_NOTIFICATION_ENABLED
api_location:
- nettxqueue.h
api_type:
- UserDefined
---

# EVT_TXQUEUE_SET_NOTIFICATION_ENABLED callback function


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Implemented by the client driver to perform client-specific processing when there are new packets received in the specified queue's ring buffer.

Syntax
------

```cpp
EVT_TXQUEUE_SET_NOTIFICATION_ENABLED EvtTxqueueSetNotificationEnabled;

NTSTATUS EvtTxqueueSetNotificationEnabled(
  _In_ NETTXQUEUE TxQueue,
  _In_ BOOLEAN    NotificationEnabled
)
{ ... }

typedef EVT_TXQUEUE_SET_NOTIFICATION_ENABLED PFN_TXQUEUE_SET_NOTIFICATION_ENABLED;
```

Register your implementation of this callback function by setting the appropriate member of [**NET_TXQUEUE_CONFIG**](net-txqueue-config.md) and then calling [**NetTxQueueCreate**](nettxqueuecreate.md).

Parameters
----------

*TxQueue* [in]  
A handle to a net transmit queue.

*NotificationEnabled* [in]  
A value of **TRUE** requests that the client enable transmit queue notification.  A value of **FALSE** requests that the client disable transmit queue notification.

Return value
------------

If the operation is successful, the callback function must return STATUS_SUCCESS. Otherwise, it should return an appropriate [NTSTATUS](https://msdn.microsoft.com/library/windows/hardware/ff557697) error code.

Remarks
-------

For a PCI NIC, enabling transmit queue notification typically means enabling the transmit queue's hardware interrupt.  When the hardware interrupt fires, the client calls [**NetTxQueueNotifyMoreCompletedPacketsAvailable**](nettxqueuenotifymorecompletedpacketsavailable.md) from its DPC.

NetAdapterCx calls *EVT_TXQUEUE_SET_NOTIFICATION_ENABLED* once with *NotificationEnabled* set to **TRUE**.  After the client calls [**NetTxQueueNotifyMoreCompletedPacketsAvailable**](nettxqueuenotifymorecompletedpacketsavailable.md), it should turn off whatever flag it uses to track the notification status.  If NetAdapterCx calls *EVT_TXQUEUE_SET_NOTIFICATION_ENABLED* with *NotificationEnabled* set to **FALSE**, the client must not call [**NetTxQueueNotifyMoreCompletedPacketsAvailable**](nettxqueuenotifymorecompletedpacketsavailable.md) until NetAdapterCx re-enables the notification.

For example:
```cpp
NTSTATUS
EvtTxQueueSetNotificationEnabled(
    _In_ NETTXQUEUE rxQueue,
    _In_ BOOLEAN notificationEnabled)
{
    // optional: retrieve queue's WDF context
    MY_TX_QUEUE_CONTEXT *txContext = GetTxQueueContext(TxQueue);

    // If notificationEnabled is TRUE, enable transmit queue's hardware interrupt
    ...
}

void
EvtInterruptDpc(
    _In_ WDFINTERRUPT interrupt,
    _In_ WDFOBJECT associatedObject)
{
    MY_INTERRUPT_CONTEXT *interruptContext = GetInterruptContext(interrupt);

    NetTxQueueNotifyMoreCompletedPacketsAvailable(interruptContext->TxQueue);
}
```

NetAdapterCx serializes this callback function along with the receive queue's [*EVT_TXQUEUE_ADVANCE*](evt-rxqueue-advance.md) and [*EVT_TXQUEUE_CANCEL*](evt-txqueue-cancel.md) callback functions.

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

## See also


[*EVT_TXQUEUE_ADVANCE*](evt-txqueue-advance.md)

[**NetTxQueueNotifyMoreCompletedPacketsAvailable**](nettxqueuenotifymorecompletedpacketsavailable.md)

 

 






