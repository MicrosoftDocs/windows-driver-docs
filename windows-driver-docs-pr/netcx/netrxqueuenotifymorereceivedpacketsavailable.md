---
title: NetRxQueueNotifyMoreReceivedPacketsAvailable method
description: The client driver calls NetRxQueueNotifyMoreReceivedPacketsAvailable to resume queue operations after NetAdapterCx calls the client's EVT\_RXQUEUE\_SET\_NOTIFICATION\_ENABLED event callback routine.
ms.assetid: 6a02b5e2-946a-428c-8640-1a5371725c41
keywords: ["NetRxQueueNotifyMoreReceivedPacketsAvailable method Network Drivers Starting with Windows Vista"]
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

The client driver calls **NetRxQueueNotifyMoreReceivedPacketsAvailable** to resume queue operations after NetAdapterCx calls the client's [*EVT\_RXQUEUE\_SET\_NOTIFICATION\_ENABLED*](evt-rxqueue-set-notification-enabled.md) event callback routine.

Syntax
------

```ManagedCPlusPlus
void NetRxQueueNotifyMoreReceivedPacketsAvailable(
  _In_ NETRXQUEUE RxQueue
);
```

Parameters
----------

*RxQueue* \[in\]  
A handle to a net receive queue object.

Return value
------------

This method does not return a value.

Remarks
-------

After NetAdapterCx calls a client driver's [*EVT\_RXQUEUE\_SET\_NOTIFICATION\_ENABLED*](evt-rxqueue-set-notification-enabled.md) event callback routine, the client must call **NetRxQueueNotifyMoreReceivedPacketsAvailable** to resume queue operations. Typically, the client does this after it completes a pending NET\_PACKET in the receive queue’s [**NET\_RING\_BUFFER**](net-ring-buffer.md).

When the client driver calls **NetRxQueueNotifyMoreReceivedPacketsAvailable**, NetAdapterCx reclaims the NET\_PACKET previously used for receive and may subsequently call the client’s [*EVT\_RXQUEUE\_ADVANCE*](evt-rxqueue-advance.md) callback function.

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
<td align="left">Netrxqueue.h (include Netadaptercx.h)</td>
</tr>
<tr class="odd">
<td align="left"><p>IRQL</p></td>
<td align="left"><p>HIGH_LEVEL</p></td>
</tr>
</tbody>
</table>

## See also


[*EVT\_RXQUEUE\_ADVANCE*](evt-rxqueue-advance.md)

[*EVT\_RXQUEUE\_SET\_NOTIFICATION\_ENABLED*](evt-rxqueue-set-notification-enabled.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NetRxQueueNotifyMoreReceivedPacketsAvailable%20method%20%20RELEASE:%20%281/19/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





