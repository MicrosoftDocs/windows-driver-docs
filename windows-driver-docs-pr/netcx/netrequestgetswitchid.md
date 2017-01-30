---
title: NetRequestGetSwitchId method
description: .
ms.assetid: b325b9f8-5134-4463-890e-abe85b86bcd9
keywords: ["NetRequestGetSwitchId method Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- NetRequestGetSwitchId
api_location:
- netrequest.h
api_type:
- HeaderDef
---

# NetRequestGetSwitchId method


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Syntax
------

```ManagedCPlusPlus
NDIS_NIC_SWITCH_ID NetRequestGetSwitchId(
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
<td align="left">Netrequest.h (include Netadaptercx.h)</td>
</tr>
<tr class="odd">
<td align="left"><p>IRQL</p></td>
<td align="left"><p>DISPATCH_LEVEL</p></td>
</tr>
</tbody>
</table>

 

 





