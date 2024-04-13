---
title: D3DKMT_SCATTERBLTS Structure
description: Learn about the D3DKMT\_SCATTERBLTS structure, which is reserved for system use. Do not use in your driver.
keywords: ["D3DKMT_SCATTERBLTS structure Display Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- D3DKMT_SCATTERBLTS
api_location:
- D3dkmthk.h
api_type:
- HeaderDef
ms.date: 01/05/2018
---

# D3DKMT\_SCATTERBLTS structure


Reserved for system use. Do not use in your driver.

## Syntax

```ManagedCPlusPlus
typedef struct _D3DKMT_SCATTERBLTS {
  UINT              NumBlts;
  D3DKMT_SCATTERBLT Blts[D3DKMT_MAX_PRESENT_HISTORY_SCATTERBLTS];
} D3DKMT_SCATTERBLTS;
```

## Members

**NumBlts**

**Blts**

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

 

 





