---
title: DxgkDdiMovePageDirectory function
description: The DxgkDdiMovePageDirectory function is reserved for system use. Do not implement it in your driver.
ms.assetid: 25972570-174d-40dc-bfbc-e9eb395dcb0e
keywords: ["DxgkDdiMovePageDirectory function Display Devices"]
topic_type:
- apiref
api_name:
- DxgkDdiMovePageDirectory
api_location:
- Dispmprt.h
api_type:
- HeaderDef
ms.date: 01/05/2018
ms.localizationpriority: medium
---

# DxgkDdiMovePageDirectory function


\[Reserved for system use.\]

The *DxgkDdiMovePageDirectory* function is reserved for system use. Do not implement it in your driver.

Syntax
------

```ManagedCPlusPlus
NTSTATUS APIENTRY DxgkDdiMovePageDirectory(
  _In_    CONST HANDLE              hContext,
  _Inout_ DXGKARG_MOVEPAGEDIRECTORY *pMovePageDirectory
);
```

Parameters
----------

*hContext* \[in\]
This parameter is reserved for system use.

*pMovePageDirectory* \[in, out\]
This parameter is reserved for system use.

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
<td align="left">Desktop</td>
</tr>
<tr class="even">
<td align="left"><p>Version</p></td>
<td align="left"><p>Available in Windows 7 and later versions of the Windows operating systems.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Header</p></td>
<td align="left">Dispmprt.h (include Dispmprt.h)</td>
</tr>
<tr class="even">
<td align="left"><p>IRQL</p></td>
<td align="left"><p>PASSIVE_LEVEL</p></td>
</tr>
</tbody>
</table>

 

 





