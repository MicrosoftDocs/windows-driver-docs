---
title: PFND3DKMT\_CHECKMULTIPLANEOVERLAYSUPPORT callback function
description: Reserved for system use. Do not use in your driver.
ms.assetid: CD354937-4383-4418-9BF8-34D78FCFC118
keywords: ["D3DKMTCheckMultiPlaneOverlaySupport callback function Display Devices", "PFND3DKMT_CHECKMULTIPLANEOVERLAYSUPPORT"]
topic_type:
- apiref
api_name:
- D3DKMTCheckMultiPlaneOverlaySupport
api_location:
- D3dkmthk.h
api_type:
- UserDefined
ms.date: 01/05/2018
ms.localizationpriority: medium
---

# PFND3DKMT\_CHECKMULTIPLANEOVERLAYSUPPORT callback function


Reserved for system use. Do not use in your driver.

Syntax
------

```ManagedCPlusPlus
PFND3DKMT_CHECKMULTIPLANEOVERLAYSUPPORT D3DKMTCheckMultiPlaneOverlaySupport;

EXTERN_C _Check_return_ NTSTATUS APIENTRY* D3DKMTCheckMultiPlaneOverlaySupport(
  _Inout_ const D3DKMT_CHECKMULTIPLANEOVERLAYSUPPORT *pMPOSupport
)
{ ... }
```

Parameters
----------

*pMPOSupport* \[in, out\]

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
<td align="left"><p>Windows 8.1</p></td>
</tr>
<tr class="even">
<td align="left"><p>Minimum supported server</p></td>
<td align="left"><p>Windows Server 2012 R2</p></td>
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

 

 





