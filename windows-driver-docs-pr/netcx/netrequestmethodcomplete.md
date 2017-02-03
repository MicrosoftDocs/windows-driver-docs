---
title: NetRequestMethodComplete method
description: .
ms.assetid: 5dd34173-b127-4f9e-bc38-7ce3fc7bf74c
keywords: ["NetRequestMethodComplete method Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- NetRequestMethodComplete
api_location:
- netrequest.h
api_type:
- HeaderDef
---

# NetRequestMethodComplete method


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Syntax
------

```ManagedCPlusPlus
VOID NetRequestMethodComplete(
  _In_ NETREQUEST Request,
  _In_ NTSTATUS   CompletionStatus,
  _In_ UINT       BytesRead,
  _In_ UINT       BytesWritten
);
```

Parameters
----------

*Request* \[in\]  
A handle to a network request object.

*CompletionStatus* \[in\]  

*BytesRead* \[in\]  

*BytesWritten* \[in\]  

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
<td align="left">Netrequest.h (include Netadaptercx.h)</td>
</tr>
<tr class="odd">
<td align="left"><p>IRQL</p></td>
<td align="left"><p>DISPATCH_LEVEL</p></td>
</tr>
</tbody>
</table>

 

 





