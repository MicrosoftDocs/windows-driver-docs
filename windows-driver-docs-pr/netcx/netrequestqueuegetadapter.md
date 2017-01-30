---
title: NetRequestQueueGetAdapter method
description: .
ms.assetid: c82fe7de-4f18-4c2d-9f07-49184ed59ef2
keywords: ["NetRequestQueueGetAdapter method Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- NetRequestQueueGetAdapter
api_location:
- netrequestqueue.h
api_type:
- HeaderDef
---

# NetRequestQueueGetAdapter method


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Syntax
------

```ManagedCPlusPlus
NETADAPTER NetRequestQueueGetAdapter(
  _In_ NETREQUESTQUEUE NetRequestQueue
);
```

Parameters
----------

*NetRequestQueue* \[in\]  

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
<td align="left">Netrequestqueue.h (include Netadaptercx.h)</td>
</tr>
<tr class="odd">
<td align="left"><p>IRQL</p></td>
<td align="left"><p>DISPATCH_LEVEL</p></td>
</tr>
</tbody>
</table>

 

 





