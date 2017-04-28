---
title: NetTxQueueNotifyMoreCompletedPacketsAvailable method
topic_type:
- apiref
api_name:
- NetTxQueueNotifyMoreCompletedPacketsAvailable
api_location:
- nettxqueue.h
api_type:
- HeaderDef
---

# NetTxQueueNotifyMoreCompletedPacketsAvailable method


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

The client driver calls **NetTxQueueNotifyMoreCompletedPacketsAvailable** to resume queue operations after NetAdapterCx calls the client's [*EVT_TXQUEUE_SET_NOTIFICATION_ENABLED*](evt-txqueue-set-notification-enabled.md) event callback routine.

Syntax
------

```cpp
void NetTxQueueNotifyMoreCompletedPacketsAvailable(
  _In_ NETTXQUEUE TxQueue
);
```

Parameters
----------

*TxQueue* [in]  
A handle to a net transmit queue.

Return value
------------

This method does not return a value.

Remarks
-------

After NetAdapterCx enables a transmit queue's notification via its [*EVT_TXQUEUE_SET_NOTIFICATION_ENABLED*](evt-txqueue-set-notification-enabled.md) event callback routine, the client may call **NetTxQueueNotifyMoreCompletedPacketsAvailable** when the queue's notification fires. Typically, the client does this in its [*EVT_WDF_INTERRUPT_DPC*](https://msdn.microsoft.com/library/windows/hardware/ff541721) callback function, after it completes a pending [**NET_PACKET**](net-packet.md) in the transmit queue’s [**NET_RING_BUFFER**](net-ring-buffer.md).

The client may notify the queue no more than once per enabling of the notification. If the notification is disabled, the client must not call **NetTxQueueNotifyMoreCompletedPacketsAvailable**.

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
<td align="left">Nettxqueue.h (include Netadaptercx.h)</td>
</tr>
<tr class="odd">
<td align="left"><p>IRQL</p></td>
<td align="left"><p>HIGH_LEVEL</p></td>
</tr>
</tbody>
</table>

## See also


[*EVT_TXQUEUE_ADVANCE*](evt-txqueue-advance.md)

[*EVT_TXQUEUE_SET_NOTIFICATION_ENABLED*](evt-txqueue-set-notification-enabled.md)

 

 






