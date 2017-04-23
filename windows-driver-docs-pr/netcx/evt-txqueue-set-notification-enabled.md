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
`TRUE` requests that the client enable its transmit queue's notification. `FALSE` requests the client disable its transmit queue's notification.

Return value
------------

If the operation is successful, the callback function must return `STATUS_SUCCESS`, or another status value for which `NT_SUCCESS(status)` is true. Otherwise, an appropriate [NTSTATUS](https://msdn.microsoft.com/library/windows/hardware/ff557697) error code.

Remarks
-------

If *NotificationEnabled* is `TRUE`, the client should enable its transmit queue's notification. If *NotificationEnabled* is `FALSE`, the client should disable its transmit queue's notification.

For a PCI NIC this typically means to enable the transmit queue's hardware interrupt. When the hardware interrupt fires, it should call [**NetTxQueueNotifyMoreCompletedPacketsAvailable**](nettxqueuenotifymorecompletedpacketsavailable.md) from its DPC.

For example:
```cpp
NTSTATUS
EvtTxQueueSetNotificationEnabled(
    _In_ NETRXQUEUE rxQueue,
    _In_ BOOLEAN notificationEnabled)
{
    // optional: retrieve queue's WDF context
    MY_TX_QUEUE_CONTEXT *rxContext = GetTxQueueContext(RxQueue);

    // Enable transmit queue's hardware interrupt
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

`EvtTxQueueSetNotificationEnabled` is serialized with the queue's [**EvtTxQueueAdvance**](evt-txqueue-advance.md) and [**EvtTxQueueCancel**](evt-txqueue-cancel.md) callbacks.

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

 

 






