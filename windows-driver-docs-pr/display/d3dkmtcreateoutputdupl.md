---
title: D3DKMTCreateOutputDupl function
description: Reserved for system use. Do not use in your driver.
ms.assetid: 6667c881-ccee-4966-9cf0-989670074a0f
keywords: ["D3DKMTCreateOutputDupl function Display Devices", "PFND3DKMT_CREATEOUTPUTDUPL"]
topic_type:
- apiref
api_name:
- D3DKMTCreateOutputDupl
api_location:
- Gdi32.dll
- API-MS-Win-dx-d3dkmt-l1-1-0.dll
- API-MS-Win-dx-d3dkmt-l1-1-1.dll
- API-MS-Win-DX-D3DKMT-L1-1-2.dll
api_type:
- DllExport
ms.date: 01/05/2018
ms.localizationpriority: medium
---

# D3DKMTCreateOutputDupl function


Reserved for system use. Do not use in your driver.

Syntax
------

```ManagedCPlusPlus
EXTERN_C NTSTATUS APIENTRY D3DKMTCreateOutputDupl(
  _In_ const D3DKMT_CREATE_OUTPUTDUPL *pData
);
```

Parameters
----------

*pData* \[in\]

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
<tr class="odd">
<td align="left"><p>Library</p></td>
<td align="left">Gdi32.lib</td>
</tr>
<tr class="even">
<td align="left"><p>DLL</p></td>
<td align="left">Gdi32.dll</td>
</tr>
</tbody>
</table>

 

 





