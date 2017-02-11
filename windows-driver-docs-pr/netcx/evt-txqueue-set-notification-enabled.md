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

```ManagedCPlusPlus
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

*TxQueue* \[in\]  
A handle to a net transmit queue object.

*NotificationEnabled* \[in\]  
A Boolean value which, if TRUE, indicates that execution of this queue is paused. See Remarks for more info.

Return value
------------

If the operation is successful, the callback function must return STATUS_SUCCESS, or another status value for which NT_SUCCESS(status) equals TRUE. Otherwise, an appropriate [NTSTATUS](https://msdn.microsoft.com/library/windows/hardware/ff557697) error code.

Remarks
-------

If *NotificationEnabled* is TRUE, NetAdapterCx waits to call [*EVT_TXQUEUE_ADVANCE*](evt-txqueue-advance.md) until after the client driver has called [**NetTxQueueNotifyMoreCompletedPacketsAvailable**](nettxqueuenotifymorecompletedpacketsavailable.md).

For more information, see [*EVT_RXQUEUE_SET_NOTIFICATION_ENABLED*](evt-rxqueue-set-notification-enabled.md).

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
<td align="left"><p>PASSIVE_LEVEL</p></td>
</tr>
</tbody>
</table>

## See also


[*EVT_TXQUEUE_ADVANCE*](evt-txqueue-advance.md)

[**NetTxQueueNotifyMoreCompletedPacketsAvailable**](nettxqueuenotifymorecompletedpacketsavailable.md)

 

 






