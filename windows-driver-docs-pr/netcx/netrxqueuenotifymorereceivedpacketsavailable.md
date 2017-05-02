---
title: NetRxQueueNotifyMoreReceivedPacketsAvailable method
topic_type:
- apiref
api_name:
- NetRxQueueNotifyMoreReceivedPacketsAvailable
api_location:
- netrxqueue.h
api_type:
- HeaderDef
---

# NetRxQueueNotifyMoreReceivedPacketsAvailable method


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

The client driver calls **NetRxQueueNotifyMoreReceivedPacketsAvailable** to resume queue operations after NetAdapterCx calls the client's [*EVT_RXQUEUE_SET_NOTIFICATION_ENABLED*](evt-rxqueue-set-notification-enabled.md) event callback routine.

Syntax
------

```cpp
void NetRxQueueNotifyMoreReceivedPacketsAvailable(
  _In_ NETRXQUEUE RxQueue
);
```

Parameters
----------

*RxQueue* [in]  
A handle to a net receive queue object.

Return value
------------

This method does not return a value.

Remarks
-------

After NetAdapterCx calls a client driver's [*EVT_RXQUEUE_SET_NOTIFICATION_ENABLED*](evt-rxqueue-set-notification-enabled.md) event callback routine with *NotificationEnabled* set to **TRUE**, the client enables the queue's hardware interrupt.  When the device generates a hardware interrupt, the client typically calls **NetRxQueueNotifyMoreReceivedPacketsAvailable** from its [*EVT_WDF_INTERRUPT_DPC*](https://msdn.microsoft.com/library/windows/hardware/ff541721) callback function, after it completes a pending [**NET_PACKET**](net-packet.md) in the receive queue's [**NET_RING_BUFFER**](net-ring-buffer.md).

The client should only call **NetRxQueueNotifyMoreReceivedPacketsAvailable** once per enabling of the notification.  Do not call **NetRxQueueNotifyMoreReceivedPacketsAvailable** if NetAdapterCx calls [*EVT_RXQUEUE_SET_NOTIFICATION_ENABLED*](evt-rxqueue-set-notification-enabled.md) with *NotificationEnabled* set to **FALSE**.

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
<td align="left">Netrxqueue.h (include Netadaptercx.h)</td>
</tr>
<tr class="odd">
<td align="left"><p>IRQL</p></td>
<td align="left"><p>HIGH_LEVEL</p></td>
</tr>
</tbody>
</table>

## See also


[*EVT_RXQUEUE_ADVANCE*](evt-rxqueue-advance.md)

[*EVT_RXQUEUE_SET_NOTIFICATION_ENABLED*](evt-rxqueue-set-notification-enabled.md)

 

 






