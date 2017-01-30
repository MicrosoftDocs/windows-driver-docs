---
title: NetRxQueueGetRingBuffer method
description: .
ms.assetid: 8960e92a-cdce-4764-8ab5-2ff056e2d770
keywords: ["NetRxQueueGetRingBuffer method Network Drivers Starting with Windows Vista"]
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

Syntax
------

```ManagedCPlusPlus
PNET_RING_BUFFER NetRxQueueGetRingBuffer(
  _In_ NETRXQUEUE NetRxQueue
);
```

Parameters
----------

*NetRxQueue* \[in\]  

Return value
------------

(NTSTATUS) The method returns STATUS\_SUCCESS if the operation succeeds. Otherwise, this method may return an appropriate NTSTATUS error code.

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

 

 





