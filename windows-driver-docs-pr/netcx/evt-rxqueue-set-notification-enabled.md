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

Implemented by the client driver to perform client-specific processing when there are new packets received in the specified queue.

Syntax
------

```ManagedCPlusPlus
EVT_RXQUEUE_SET_NOTIFICATION_ENABLED EvtRxqueueSetNotificationEnabled;

NTSTATUS EvtRxqueueSetNotificationEnabled(
  _In_ NETRXQUEUE RxQueue,
  _In_ BOOLEAN    NotificationEnabled
)
{ ... }

typedef EVT_RXQUEUE_SET_NOTIFICATION_ENABLED PFN_RXQUEUE_SET_NOTIFICATION_ENABLED;
```

Register your implementation of this callback function by setting the appropriate member of [**NET_RXQUEUE_CONFIG**](net-rxqueue-config.md) and then calling [**NetRxQueueCreate**](netrxqueuecreate.md).

Parameters
----------

*RxQueue* \[in\]  
A handle to a net receive queue object.

*NotificationEnabled* \[in\]  
A Boolean value which, if TRUE, indicates that the driver's EVT_RXQUEUE_ADVANCE callback will not be called until either a higher level application finishes processing previously indicated data, or the driver calls [**NetRxQueueNotifyMoreReceivedPacketsAvailable**](netrxqueuenotifymorereceivedpacketsavailable.md). See Remarks for more info.

Return value
------------

If the operation is successful, the callback function must return STATUS_SUCCESS, or another status value for which NT_SUCCESS(status) equals TRUE. Otherwise, an appropriate [NTSTATUS](https://msdn.microsoft.com/library/windows/hardware/ff557697) error code.

Remarks
-------

If *NotificationEnabled* is TRUE, NetAdapterCx waits to call [*EVT_RXQUEUE_ADVANCE*](evt-rxqueue-advance.md) until after the client driver has called [**NetRxQueueNotifyMoreReceivedPacketsAvailable**](netrxqueuenotifymorereceivedpacketsavailable.md).

In this callback, a client driver for a PCI device typically enables the hardware’s receive interrupt. Then from its interrupt handler, the client driver calls [**NetRxQueueNotifyMoreReceivedPacketsAvailable**](netrxqueuenotifymorereceivedpacketsavailable.md).

For a USB device, the client driver might track a flag, for example on the queue context. When a message is available in the continuous reader of the USB bus, the client driver calls [**NetRxQueueNotifyMoreReceivedPacketsAvailable**](netrxqueuenotifymorereceivedpacketsavailable.md). The following example shows how you might do this.

```
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

 

 






