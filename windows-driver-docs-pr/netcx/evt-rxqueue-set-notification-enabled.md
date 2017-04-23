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

Implemented by the client driver to enable device's receive queue notification.

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
`TRUE` requests that the client enable its receive queue's notification. `FALSE` requests the client disable its receive queue's notification.

Return value
------------

If the operation is successful, the callback function must return `STATUS_SUCCESS`, or another status value for which `NT_SUCCESS(status)` is true. Otherwise, an appropriate [NTSTATUS](https://msdn.microsoft.com/library/windows/hardware/ff557697) error code.

Remarks
-------

If *NotificationEnabled* is `TRUE`, the client should enable its receive queue's notification. If *NotificationEnabled* is `FALSE`, the client should disable its receive queue's notification.

For a PCI NIC this typically means to enable the receive queue's hardware interrupt. When the hardware interrupt fires, it should call [**NetRxQueueNotifyMoreReceivedPacketsAvailable**](netrxqueuenotifymorereceivedpacketsavailable.md) from its DPC.

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

For a USB device, or any other queue with a software receive completion mechanism, the client driver should track in its own context whether the queue's notification is enabled. When the completion routine is executed (e.g. a message becomes available in USB continuous reader), call [**NetRxQueueNotifyMoreReceivedPacketsAvailable**](netrxqueuenotifymorereceivedpacketsavailable.md) if the notification is enabled. The following example shows how you might do this.

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

`EvtRxQueueSetNotificationEnabled` is serialized with the queue's [**EvtRxQueueAdvance**](evt-rxqueue-advance.md) and [**EvtRxQueueCancel**](evt-rxqueue-cancel.md) callbacks.

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

 

 






