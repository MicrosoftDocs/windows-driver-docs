---
title: D3DKMTSetStereoEnabled function
description: Retrieves a Boolean value that indicates whether the operating system's stereoscopic 3-D display behavior is enabled.
ms.assetid: 03aa74bb-0999-41d3-b67f-a58cfe17043e
keywords: ["D3DKMTSetStereoEnabled function Display Devices"]
topic_type:
- apiref
api_name:
- D3DKMTSetStereoEnabled
api_location:
- GDI32.dll
- API-MS-Win-dx-d3dkmt-l1-1-0.dll
- API-MS-Win-dx-d3dkmt-l1-1-1.dll
- API-MS-Win-DX-D3DKMT-L1-1-2.dll
api_type:
- DllExport
ms.date: 01/05/2018
ms.localizationpriority: medium
---

# D3DKMTSetStereoEnabled function


Retrieves a Boolean value that indicates whether the operating system's stereoscopic 3-D display behavior is enabled.

Syntax
------

```ManagedCPlusPlus
_Check_return_ NTSTATUS APIENTRY D3DKMTSetStereoEnabled(
  _In_ BOOL bStereoEnabled
);
```

Parameters
----------

*bStereoEnabled* \[in\]
**TRUE** if the operating system's stereoscopic 3-D display behavior is enabled; **FALSE** otherwise.

Return value
------------

Returns one of the following values:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Return code</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><strong>STATUS_SUCCESS</strong></td>
<td align="left"><p>The function completed successfully.</p></td>
</tr>
</tbody>
</table>

 

This function might also return other NTSTATUS values.

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
<td align="left">GDI32.lib</td>
</tr>
<tr class="even">
<td align="left"><p>DLL</p></td>
<td align="left">GDI32.dll</td>
</tr>
</tbody>
</table>

 

 





