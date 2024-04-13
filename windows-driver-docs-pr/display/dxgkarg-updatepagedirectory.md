---
title: _DXGKARG_UPDATEPAGEDIRECTORY Structure
description: The DXGKARG\_UPDATEPAGEDIRECTORY structure is reserved for system use. Do not use it in your driver.
keywords: ["_DXGKARG_UPDATEPAGEDIRECTORY structure Display Devices", "DXGKARG_UPDATEPAGEDIRECTORY structure Display Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- DXGKARG_UPDATEPAGEDIRECTORY
api_location:
- d3dkmddi.h
api_type:
- HeaderDef
ms.date: 01/05/2018
---

# \_DXGKARG\_UPDATEPAGEDIRECTORY structure


The DXGKARG\_UPDATEPAGEDIRECTORY structure is reserved for system use. Do not use it in your driver.

## Syntax

```ManagedCPlusPlus
typedef struct _DXGKARG_UPDATEPAGEDIRECTORY {
  PVOID          pPageDirectory;
  UINT           StartIndex;
  UINT           PageTableCount;
  const DXGK_PDE *PDEArray;
} DXGKARG_UPDATEPAGEDIRECTORY;
```

## Members

**pPageDirectory**
Reserved for system use.

**StartIndex**
Reserved for system use.

**PageTableCount**
Reserved for system use.

**PDEArray**
Reserved for system use.

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Version</p></td>
<td align="left"><p>Available in Windows 7 and later versions of the Windows operating systems.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">D3dkmddi.h (include D3dkmddi.h)</td>
</tr>
</tbody>
</table>

 

 





