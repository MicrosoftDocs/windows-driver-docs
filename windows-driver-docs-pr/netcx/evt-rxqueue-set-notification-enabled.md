---
title: EVT_RXQUEUE_SET_NOTIFICATION_ENABLED callback function
description: Implemented by the client driver to perform client-specific processing when there are new packets received in the specified queue.
ms.assetid: b85f88bd-0e8a-4fb7-af59-5b107e7d5ae5
keywords: ["EvtRxqueueSetNotificationEnabled callback function Network Drivers Starting with Windows Vista", "EVT_RXQUEUE_SET_NOTIFICATION_ENABLED", "PFN_RXQUEUE_SET_NOTIFICATION_ENABLED callback function pointer Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- PFN_RXQUEUE_SET_NOTIFICATION_ENABLED
api_location:
- netrxqueue.h
api_type:
- UserDefined
---

# EVT\_RXQUEUE\_SET\_NOTIFICATION\_ENABLED callback function


\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

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

Register your implementation of this callback function by setting the appropriate member of [**NET\_RXQUEUE\_CONFIG**](net-rxqueue-config.md) and then calling [**NetRxQueueCreate**](netrxqueuecreate.md).

Parameters
----------

*RxQueue* \[in\]  
A handle to a net receive queue object.

*NotificationEnabled* \[in\]  
A Boolean value which, if TRUE, indicates that the driver's EVT\_RXQUEUE\_ADVANCE callback will not be called until either a higher level application finishes processing previously indicated data, or the driver calls [**NetRxQueueNotifyMoreReceivedPacketsAvailable**](netrxqueuenotifymorereceivedpacketsavailable.md). See Remarks for more info.

Return value
------------

If the operation is successful, the callback function must return STATUS\_SUCCESS, or another status value for which NT\_SUCCESS(status) equals TRUE. Otherwise, an appropriate [NTSTATUS](https://msdn.microsoft.com/library/windows/hardware/ff557697) error code.

Remarks
-------

If *NotificationEnabled* is TRUE, NetAdapterCx waits to call [*EVT\_RXQUEUE\_ADVANCE*](evt-rxqueue-advance.md) until after the client driver has called [**NetRxQueueNotifyMoreReceivedPacketsAvailable**](netrxqueuenotifymorereceivedpacketsavailable.md).

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
<td align="left">[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</td>
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


[*EVT\_RXQUEUE\_ADVANCE*](evt-rxqueue-advance.md)

[**NetRxQueueNotifyMoreReceivedPacketsAvailable**](netrxqueuenotifymorereceivedpacketsavailable.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20EVT_RXQUEUE_SET_NOTIFICATION_ENABLED%20callback%20function%20%20RELEASE:%20%281/19/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





