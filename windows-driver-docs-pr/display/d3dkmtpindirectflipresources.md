---
title: PFND3DKMT\_PINDIRECTFLIPRESOURCES callback function
description: Reserved for system use. Do not use in your driver.
ms.assetid: fc497f21-a9da-4d81-ba39-6e3058942d3e
keywords: ["D3DKMTPinDirectFlipResources callback function Display Devices", "PFND3DKMT_PINDIRECTFLIPRESOURCES"]
topic_type:
- apiref
api_name:
- D3DKMTPinDirectFlipResources
api_location:
- D3dkmthk.h
api_type:
- UserDefined
ms.date: 01/05/2018
ms.localizationpriority: medium
---

# PFND3DKMT\_PINDIRECTFLIPRESOURCES callback function


Reserved for system use. Do not use in your driver.

Syntax
------

```ManagedCPlusPlus
PFND3DKMT_PINDIRECTFLIPRESOURCES D3DKMTPinDirectFlipResources;

_Check_return_ NTSTATUS APIENTRY* D3DKMTPinDirectFlipResources(
  _In_ const D3DKMT_PINDIRECTFLIPRESOURCES *pResources
)
{ ... }
```

Parameters
----------

*pResources* \[in\]

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
<td align="left">D3dkmthk.h (include D3dkmthk.h)</td>
</tr>
</tbody>
</table>

 

 





