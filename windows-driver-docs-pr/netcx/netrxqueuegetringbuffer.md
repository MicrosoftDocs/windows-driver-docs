---
title: NetRxQueueGetRingBuffer method
topic_type:
- apiref
api_name:
- NetRxQueueGetRingBuffer
api_location:
- netrxqueue.h
api_type:
- HeaderDef
---

# NetRxQueueGetRingBuffer method

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Retrieves the net ring buffer for a specified net receive queue structure.

Syntax
------

```cpp
PNET_RING_BUFFER NetRxQueueGetRingBuffer(
  _In_ NETRXQUEUE NetRxQueue
);
```

Parameters
----------

*NetRxQueue* [in]  
A handle to a net receive queue object.

Return value
------------

Returns a pointer to the [**NET_RING_BUFFER**](net-ring-buffer.md) structure associated with a net receive queue structure.

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
<td align="left">Netrxqueue.h (include Netadaptercx.h)</td>
</tr>
<tr class="odd">
<td align="left"><p>IRQL</p></td>
<td align="left"><p>PASSIVE_LEVEL</p></td>
</tr>
</tbody>
</table>

 

 





