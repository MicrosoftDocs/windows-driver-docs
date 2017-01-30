---
title: NetTxQueueNotifyMoreCompletedPacketsAvailable method
description: The client driver calls NetTxQueueNotifyMoreCompletedPacketsAvailable to resume queue operations after NetAdapterCx calls the client's EVT\_TXQUEUE\_SET\_NOTIFICATION\_ENABLED event callback routine.
ms.assetid: 89949a53-d884-4e03-afc3-897920f97df2
keywords: ["NetTxQueueNotifyMoreCompletedPacketsAvailable method Network Drivers Starting with Windows Vista"]
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

The client driver calls **NetTxQueueNotifyMoreCompletedPacketsAvailable** to resume queue operations after NetAdapterCx calls the client's [*EVT\_TXQUEUE\_SET\_NOTIFICATION\_ENABLED*](evt-txqueue-set-notification-enabled.md) event callback routine.

Syntax
------

```ManagedCPlusPlus
void NetTxQueueNotifyMoreCompletedPacketsAvailable(
  _In_ NETTXQUEUE TxQueue
);
```

Parameters
----------

*TxQueue* \[in\]  
A handle to a net transmit queue object.

Return value
------------

This method does not return a value.

Remarks
-------

After NetAdapterCx calls a client driver's [*EVT\_TXQUEUE\_SET\_NOTIFICATION\_ENABLED*](evt-txqueue-set-notification-enabled.md) event callback routine, the client must call **NetTxQueueNotifyMoreCompletedPacketsAvailable** to resume queue operations. Typically, the client does this after it completes a pending NET\_PACKET in the transmit queue’s [**NET\_RING\_BUFFER**](net-ring-buffer.md).

Then NetAdapterCx reclaims the NET\_PACKET previously used for transmit and calls the client’s [*EVT\_TXQUEUE\_ADVANCE*](evt-txqueue-advance.md) callback function.

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
<td align="left">Nettxqueue.h (include Netadaptercx.h)</td>
</tr>
<tr class="odd">
<td align="left"><p>IRQL</p></td>
<td align="left"><p>HIGH_LEVEL</p></td>
</tr>
</tbody>
</table>

## See also


[*EVT\_TXQUEUE\_ADVANCE*](evt-txqueue-advance.md)

[*EVT\_TXQUEUE\_SET\_NOTIFICATION\_ENABLED*](evt-txqueue-set-notification-enabled.md)

 

 






