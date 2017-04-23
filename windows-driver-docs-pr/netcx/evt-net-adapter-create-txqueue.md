---
title: EVT_NET_ADAPTER_CREATE_TXQUEUE callback function
topic_type:
- apiref
api_name:
- PFN_NET_ADAPTER_CREATE_TXQUEUE
api_location:
- netadapter.h
api_type:
- UserDefined
---

# EVT_NET_ADAPTER_CREATE_TXQUEUE callback function


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

The client driver's implementation of the *EVT_NET_ADAPTER_CREATE_TXQUEUE* event callback function that sets up a transmit queue.

Syntax
------

```cpp
EVT_NET_ADAPTER_CREATE_TXQUEUE EvtNetAdapterCreateTxqueue;

NTSTATUS EvtNetAdapterCreateTxqueue(
  _In_    NETADAPTER       Adapter,
  _Inout_ PNETTXQUEUE_INIT TxQueueInit
)
{ ... }

typedef EVT_NET_ADAPTER_CREATE_TXQUEUE PFN_NET_ADAPTER_CREATE_TXQUEUE;
```

Parameters
----------

*Adapter* [in]  
The NetAdapter object that was created by [**NetAdapterCreate**](netadaptercreate.md).

*TxQueueInit* [in, out]  
A pointer to a NetAdapterCx-allocated **NETTXQUEUE_INIT** structure. For more information, see the Remarks section.

Return value
------------

If the operation is successful, the callback function must return STATUS_SUCCESS, or another status value for which NT_SUCCESS(status) equals TRUE. Otherwise, an appropriate [NTSTATUS](https://msdn.microsoft.com/library/windows/hardware/ff557697) error code.

Remarks
-------

To register an *EVT_NET_ADAPTER_CREATE_TXQUEUE* callback function, the client driver must call [**NetAdapterCreate**](netadaptercreate.md).

The **NETTXQUEUE_INIT** structure is an opaque structure that is defined and allocated by NetAdapterCx, similar to [WDFDEVICE_INIT](https://msdn.microsoft.com/library/windows/hardware/ff546951).

In this callback, the client driver typically calls [**NetTxQueueInitGetQueueId**](nettxqueueinitgetqueueid.md) with *NetTxQueueInit* to retrieve the identifier of the transmit queue to set up.

The NetTxQueue's ring buffer is allocated in NetTxQueueCreate, so it can be retrieved via [**NetTxQueueGetRingBuffer**](nettxqueuegetringbuffer.md) after queue creation. You can use this as an opportunity to allocate any per-packet resources.

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
<td align="left">NetAdapter.h</td>
</tr>
<tr class="odd">
<td align="left"><p>IRQL</p></td>
<td align="left"><p>PASSIVE_LEVEL</p></td>
</tr>
</tbody>
</table>

 

 





