---
title: NetRxQueueInitGetQueueId method
description: .
ms.assetid: 134512e5-5158-4f3a-8691-7780646fe480
keywords: ["NetRxQueueInitGetQueueId method Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- NetRxQueueInitGetQueueId
api_location:
- netrxqueue.h
api_type:
- HeaderDef
---

# NetRxQueueInitGetQueueId method


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Syntax
------

```ManagedCPlusPlus
ULONG NetRxQueueInitGetQueueId(
  _In_ PNETRXQUEUE_INIT NetRxQueueInit
);
```

Parameters
----------

*NetRxQueueInit* \[in\]  

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
<td align="left"><p>PASSIVE_LEVEL</p></td>
</tr>
</tbody>
</table>

 

 





