---
title: NetRequestGetId method
description: .
ms.assetid: 56f5fea6-8018-4ceb-b9f5-988923cbe106
keywords: ["NetRequestGetId method Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- NetRequestGetId
api_location:
- netrequest.h
api_type:
- HeaderDef
---

# NetRequestGetId method


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Syntax
------

```ManagedCPlusPlus
NDIS_OID NetRequestGetId(
  _In_ NETREQUEST Request
);
```

Parameters
----------

*Request* \[in\]  

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

 

 





