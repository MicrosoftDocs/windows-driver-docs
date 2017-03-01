---
title: EVT_TXQUEUE_CANCEL callback function
topic_type:
- apiref
api_name:
- PFN_TXQUEUE_CANCEL
api_location:
- nettxqueue.h
api_type:
- UserDefined
---

# EVT_TXQUEUE_CANCEL callback function


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Implemented by the client driver to handle operations that must be performed before a transmit queue is deleted.

Syntax
------

```cpp
EVT_TXQUEUE_CANCEL EvtTxqueueCancel;

void EvtTxqueueCancel(
  _In_ NETTXQUEUE TxQueue
)
{ ... }

typedef EVT_TXQUEUE_CANCEL PFN_TXQUEUE_CANCEL;
```

Register your implementation of this callback function by setting the appropriate member of [**NET_TXQUEUE_CONFIG**](net-txqueue-config.md) and then calling [**NetTxQueueCreate**](nettxqueuecreate.md).

Parameters
----------

*TxQueue* [in]  
A NETTXQUEUE object.

Return value
------------

This callback function does not return a value.

Remarks
-------

NetAdapterCx calls this event callback function when the queue is being deleted. *EVT_TXQUEUE_CANCEL* is the final **EVT_TXQUEUE_*Xxx*** callback that NetAdapterCx calls.

In this callback, the client typically completes pending packets and cleans up client specific context data associated with this NETTXQUEUE object.

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
<td align="left">Nettxqueue.h</td>
</tr>
<tr class="odd">
<td align="left"><p>IRQL</p></td>
<td align="left"><p>PASSIVE_LEVEL</p></td>
</tr>
</tbody>
</table>

 

 





