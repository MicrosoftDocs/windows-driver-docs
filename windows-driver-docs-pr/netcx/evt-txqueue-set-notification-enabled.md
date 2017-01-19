---
title: EVT\_TXQUEUE\_SET\_NOTIFICATION\_ENABLED callback function
description: Implemented by the client driver to perform client-specific processing when there are new packets received in the specified queue's ring buffer.
ms.assetid: c2b26585-3949-4d18-b25a-7aa1ac99e2a6
keywords: ["EvtTxqueueSetNotificationEnabled callback function Network Drivers Starting with Windows Vista", "EVT_TXQUEUE_SET_NOTIFICATION_ENABLED", "PFN_TXQUEUE_SET_NOTIFICATION_ENABLED callback function pointer Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- PFN_TXQUEUE_SET_NOTIFICATION_ENABLED
api_location:
- nettxqueue.h
api_type:
- UserDefined
---

# EVT\_TXQUEUE\_SET\_NOTIFICATION\_ENABLED callback function


\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

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

Register your implementation of this callback function by setting the appropriate member of [**NET\_TXQUEUE\_CONFIG**](net-txqueue-config.md) and then calling [**NetTxQueueCreate**](nettxqueuecreate.md).

Parameters
----------

*TxQueue* \[in\]  
A handle to a net transmit queue object.

*NotificationEnabled* \[in\]  
A Boolean value which, if TRUE, indicates that execution of this queue is paused. See Remarks for more info.

Return value
------------

If the operation is successful, the callback function must return STATUS\_SUCCESS, or another status value for which NT\_SUCCESS(status) equals TRUE. Otherwise, an appropriate [NTSTATUS](https://msdn.microsoft.com/library/windows/hardware/ff557697) error code.

Remarks
-------

If *NotificationEnabled* is TRUE, NetAdapterCx waits to call [*EVT\_TXQUEUE\_ADVANCE*](evt-txqueue-advance.md) until after the client driver has called [**NetTxQueueNotifyMoreCompletedPacketsAvailable**](nettxqueuenotifymorecompletedpacketsavailable.md).

For more information, see [*EVT\_RXQUEUE\_SET\_NOTIFICATION\_ENABLED*](evt-rxqueue-set-notification-enabled.md).

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
<td align="left">Nettxqueue.h</td>
</tr>
<tr class="odd">
<td align="left"><p>IRQL</p></td>
<td align="left"><p>PASSIVE_LEVEL</p></td>
</tr>
</tbody>
</table>

## See also


[*EVT\_TXQUEUE\_ADVANCE*](evt-txqueue-advance.md)

[**NetTxQueueNotifyMoreCompletedPacketsAvailable**](nettxqueuenotifymorecompletedpacketsavailable.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20EVT_TXQUEUE_SET_NOTIFICATION_ENABLED%20callback%20function%20%20RELEASE:%20%281/19/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





