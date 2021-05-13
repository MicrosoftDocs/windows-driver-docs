---
title: D3DKMT\_OUTDUPL\_POINTER\_SHAPE\_INFO structure
description: Learn about the D3DKMT\_OUTDUPL\_POINTER\_SHAPE\_INFO structure, which is reserved for system use. Do not use in your driver.
keywords: ["D3DKMT_OUTDUPL_POINTER_SHAPE_INFO structure Display Devices"]
topic_type:
- apiref
api_name:
- D3DKMT_OUTDUPL_POINTER_SHAPE_INFO
api_location:
- D3dkmthk.h
api_type:
- HeaderDef
ms.date: 01/05/2018
ms.localizationpriority: medium
---

# D3DKMT\_OUTDUPL\_POINTER\_SHAPE\_INFO structure


Reserved for system use. Do not use in your driver.

## Syntax

```ManagedCPlusPlus
typedef struct _D3DKMT_OUTDUPL_POINTER_SHAPE_INFO {
  D3DKMT_OUTDUPL_POINTER_SHAPE_TYPE Type;
  UINT                              Width;
  UINT                              Height;
  UINT                              Pitch;
  POINT                             HotSpot;
} D3DKMT_OUTDUPL_POINTER_SHAPE_INFO;
```

## Members

**Type**

**Width**

**Height**

**Pitch**

**HotSpot**

## Requirements

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
<td align="left"><p>Header</p></td>
<td align="left">D3dkmthk.h (include D3dkmthk.h)</td>
</tr>
</tbody>
</table>

 

 





