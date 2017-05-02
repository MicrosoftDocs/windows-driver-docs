---
title: EVT_RXQUEUE_SET_NOTIFICATION_ENABLED callback function
topic_type:
- apiref
api_name:
- PFN_RXQUEUE_SET_NOTIFICATION_ENABLED
api_location:
- netrxqueue.h
api_type:
- UserDefined
---

# EVT_RXQUEUE_SET_NOTIFICATION_ENABLED callback function


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Implemented by the client driver to enable receive queue notification for the associated device.

Syntax
------

```cpp
EVT_RXQUEUE_SET_NOTIFICATION_ENABLED EvtRxqueueSetNotificationEnabled;

NTSTATUS EvtRxqueueSetNotificationEnabled(
  _In_ NETRXQUEUE RxQueue,
  _In_ BOOLEAN    NotificationEnabled
)
{ ... }

typedef EVT_RXQUEUE_SET_NOTIFICATION_ENABLED PFN_RXQUEUE_SET_NOTIFICATION_ENABLED;
```

Register this callback function in [**NET_RXQUEUE_CONFIG_INIT**](net-rxqueue-config-init.md) before calling [**NetRxQueueCreate**](netrxqueuecreate.md).

Parameters
----------

*RxQueue* [in]  
A handle to a net receive queue.

*NotificationEnabled* [in]  
A value of **TRUE** requests that the client enable receive queue notification.  A value of **FALSE** requests that the client disable receive queue notification.

Return value
------------

If the operation is successful, the callback function returns STATUS_SUCCESS. Otherwise, return an appropriate [NTSTATUS](https://msdn.microsoft.com/library/windows/hardware/ff557697) error code.

Remarks
-------

For a PCI NIC, enabling receive queue notification typically means enabling the receive queue's hardware interrupt.  When the hardware interrupt fires, the client calls [**NetRxQueueNotifyMoreReceivedPacketsAvailable**](netrxqueuenotifymorereceivedpacketsavailable.md) from its DPC.

For example:
```cpp
NTSTATUS
EvtRxQueueSetNotificationEnabled(
    _In_ NETRXQUEUE rxQueue,
    _In_ BOOLEAN notificationEnabled)
{
    // optional: retrieve queue's WDF context
    MY_RX_QUEUE_CONTEXT *rxContext = GetRxQueueContext(RxQueue);

    // Enable receive queue's hardware interrupt
    ...
}

void
EvtInterruptDpc(
    _In_ WDFINTERRUPT interrupt,
    _In_ WDFOBJECT associatedObject)
{
    MY_INTERRUPT_CONTEXT *interruptContext = GetInterruptContext(interrupt);

    NetRxQueueNotifyMoreReceivedPacketsAvailable(interruptContext->RxQueue);
}
```

For a USB device, or any other queue with a software receive completion mechanism, the client driver should track in its own context whether the queue's notification is enabled.  From the completion routine (triggered for example when a message becomes available in the USB continuous reader), call [**NetRxQueueNotifyMoreReceivedPacketsAvailable**](netrxqueuenotifymorereceivedpacketsavailable.md) if the notification is enabled.  The following example shows how you might do this.

```cpp
VOID
UsbEvtReaderCompletionRoutine(
    _In_ WDFUSBPIPE pipe,
    _In_ WDFMEMORY buffer,
    _In_ size_t numBytesTransferred,
    _In_ WDFCONTEXT context)
{
    UNREFERENCED_PARAMETER(pipe);

    PUSB_RCB_POOL pRcbPool = *((PUSB_RCB_POOL*) context);
    PUSB_RCB pRcb = (PUSB_RCB) WdfMemoryGetBuffer(buffer, NULL);

    pRcb->DataOffsetCurrent = 0;
    pRcb->DataWdfMemory = buffer;
    pRcb->DataValidSize = numBytesTransferred;

    WdfObjectReference(pRcb->DataWdfMemory);

    ExInterlockedInsertTailList(&amp;pRcbPool->ListHead,
                                &amp;pRcb->Link,
                                &amp;pRcbPool->ListSpinLock);

    if (InterlockedExchange(&amp;pRcbPool->NotificationEnabled, FALSE) == TRUE)
    {
        NetRxQueueNotifyMoreReceivedPacketsAvailable(pRcbPool->RxQueue);
    }

}
```

NetAdapterCx serializes this callback function along with the receive queue's [*EVT_RXQUEUE_ADVANCE*](evt-rxqueue-advance.md) and [*EVT_RXQUEUE_CANCEL*](evt-rxqueue-cancel.md) callback functions.

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

## See also


[*EVT_RXQUEUE_ADVANCE*](evt-rxqueue-advance.md)

[**NetRxQueueNotifyMoreReceivedPacketsAvailable**](netrxqueuenotifymorereceivedpacketsavailable.md)

 

 






