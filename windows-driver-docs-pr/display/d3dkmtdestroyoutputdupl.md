---
title: D3DKMTDestroyOutputDupl function
description: Reserved for system use. Do not use in your driver.
ms.assetid: 3818ff85-779c-445d-ad48-70e3efe42b67
keywords: ["D3DKMTDestroyOutputDupl function Display Devices", "PFND3DKMT_DESTROYOUTPUTDUPL"]
topic_type:
- apiref
api_name:
- D3DKMTDestroyOutputDupl
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

# D3DKMTDestroyOutputDupl function


Reserved for system use. Do not use in your driver.

Syntax
------

```ManagedCPlusPlus
EXTERN_C NTSTATUS APIENTRY D3DKMTDestroyOutputDupl(
  _In_ const D3DKMT_DESTROY_OUTPUTDUPL *pData
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

 

 





