---
title: NetObjectMarkCancelableEx method
description: .
ms.assetid: af9d02d1-c97f-4cfd-9e6d-0988db58edb4
keywords: ["NetObjectMarkCancelableEx method Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- NetObjectMarkCancelableEx
api_location:
- netobject.h
api_type:
- HeaderDef
---

# NetObjectMarkCancelableEx method


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Syntax
------

```ManagedCPlusPlus
NTSTATUS NetObjectMarkCancelableEx(
  _In_ WDFOBJECT             NetObject,
  _In_ PFN_NET_OBJECT_CANCEL EvtObjectCancel
);
```

Parameters
----------

*NetObject* \[in\]  

*EvtObjectCancel* \[in\]  

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
<td align="left">Netobject.h (include Netadaptercx.h)</td>
</tr>
<tr class="odd">
<td align="left"><p>IRQL</p></td>
<td align="left"><p>DISPATCH_LEVEL</p></td>
</tr>
</tbody>
</table>

 

 





