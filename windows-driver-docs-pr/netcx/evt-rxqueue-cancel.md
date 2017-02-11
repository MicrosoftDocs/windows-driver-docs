---
title: EVT_RXQUEUE_CANCEL callback function
topic_type:
- apiref
api_name:
- PFN_RXQUEUE_CANCEL
api_location:
- netrxqueue.h
api_type:
- UserDefined
---

# EVT_RXQUEUE_CANCEL callback function


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Implemented by the client driver to handle operations that must be performed before a receive queue is deleted.

Syntax
------

```ManagedCPlusPlus
EVT_RXQUEUE_CANCEL EvtRxqueueCancel;

void EvtRxqueueCancel(
  _In_ NETRXQUEUE RxQueue
)
{ ... }

typedef EVT_RXQUEUE_CANCEL PFN_RXQUEUE_CANCEL;
```

Register your implementation of this callback function by setting the appropriate member of [**NET_RXQUEUE_CONFIG**](net-rxqueue-config.md) and then calling [**NetRxQueueCreate**](netrxqueuecreate.md).

Parameters
----------

*RxQueue* \[in\]  
A NETRXQUEUE object.

Return value
------------

This callback function does not return a value.

Remarks
-------

NetAdapterCx calls this event callback function when the queue is being deleted. *EVT_RXQUEUE_CANCEL* is the final **EVT_RXQUEUE_*Xxx*** callback that NetAdapterCx calls before deleting the queue.

In this callback, the client typically completes pending packets and cleans up client specific context data associated with this NETRXQUEUE object.

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

 

 





