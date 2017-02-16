---
title: NetTxQueueGetRingBuffer method
topic_type:
- apiref
api_name:
- NetTxQueueGetRingBuffer
api_location:
- nettxqueue.h
api_type:
- HeaderDef
---

# NetTxQueueGetRingBuffer method

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Retrieves the net ring buffer for a specified net transmit queue structure.

Syntax
------

```ManagedCPlusPlus
PNET_RING_BUFFER NetTxQueueGetRingBuffer(
  _In_ NETTXQUEUE NetTxQueue
);
```

Parameters
----------

*NetTxQueue* [in]  
A handle to a net transmit queue object.

Return value
------------

The method returns STATUS_SUCCESS if the operation succeeds. Otherwise, this method may return an appropriate NTSTATUS error code.

Return value
------------

Returns a pointer to the [NET_RING_BUFFER](net-ring-buffer.md) structure associated with a net transmit queue structure.

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
<td align="left">Nettxqueue.h (include Netadaptercx.h)</td>
</tr>
<tr class="odd">
<td align="left"><p>IRQL</p></td>
<td align="left"><p>PASSIVE_LEVEL</p></td>
</tr>
</tbody>
</table>

 

 





