---
title: PFND3DKMT\_UNPINDIRECTFLIPRESOURCES callback function
description: Reserved for system use. Do not use in your driver.
ms.assetid: cfbcf6b4-b1e7-4565-856a-585d7d0d187d
keywords: ["D3DKMTUnpinDirectFlipResources callback function Display Devices", "PFND3DKMT_UNPINDIRECTFLIPRESOURCES"]
topic_type:
- apiref
api_name:
- D3DKMTUnpinDirectFlipResources
api_location:
- D3dkmthk.h
api_type:
- UserDefined
ms.date: 01/05/2018
ms.localizationpriority: medium
---

# PFND3DKMT\_UNPINDIRECTFLIPRESOURCES callback function


Reserved for system use. Do not use in your driver.

Syntax
------

```ManagedCPlusPlus
PFND3DKMT_UNPINDIRECTFLIPRESOURCES D3DKMTUnpinDirectFlipResources;

_Check_return_ NTSTATUS APIENTRY* D3DKMTUnpinDirectFlipResources(
  _In_ const D3DKMT_UNPINDIRECTFLIPRESOURCES *pResources
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

 

 





