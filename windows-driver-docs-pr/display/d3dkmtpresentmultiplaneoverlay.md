---
title: D3DKMTPresentMultiPlaneOverlay function
description: Reserved for system use. Do not use in your driver.
ms.assetid: 62993166-9630-4395-8649-078f0de40647
keywords: ["D3DKMTPresentMultiPlaneOverlay function Display Devices"]
topic_type:
- apiref
api_name:
- D3DKMTPresentMultiPlaneOverlay
api_location:
- D3dkmthk.h
api_type:
- HeaderDef
ms.date: 01/05/2018
ms.localizationpriority: medium
---

# D3DKMTPresentMultiPlaneOverlay function


Reserved for system use. Do not use in your driver.

Syntax
------

```ManagedCPlusPlus
EXTERN_C _Check_return_ NTSTATUS APIENTRY D3DKMTPresentMultiPlaneOverlay(
  _In_ const D3DKMT_PRESENT_MULTIPLANE_OVERLAY *pPresent
);
```

Parameters
----------

*pPresent* \[in\]

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Minimum supported client</p></td>
<td align="left"><p>Windows 8</p></td>
</tr>
<tr class="even">
<td align="left"><p>Minimum supported server</p></td>
<td align="left"><p>Windows Server 2012</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Target platform</p></td>
<td align="left">Universal</td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">D3dkmthk.h</td>
</tr>
</tbody>
</table>

 

 





