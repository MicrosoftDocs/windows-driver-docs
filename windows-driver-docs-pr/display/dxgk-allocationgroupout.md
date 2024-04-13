---
title: _DXGK_ALLOCATIONGROUPOUT Structure
description: The DXGK\_ALLOCATIONGROUPOUT structure is reserved for system use. Do not use it in your driver.
keywords: ["_DXGK_ALLOCATIONGROUPOUT structure Display Devices", "DXGK_ALLOCATIONGROUPOUT structure Display Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- DXGK_ALLOCATIONGROUPOUT
api_location:
- d3dkmddi.h
api_type:
- HeaderDef
ms.date: 01/05/2018
---

# \_DXGK\_ALLOCATIONGROUPOUT structure


The DXGK\_ALLOCATIONGROUPOUT structure is reserved for system use. Do not use it in your driver.

## Syntax

```ManagedCPlusPlus
typedef struct _DXGK_ALLOCATIONGROUPOUT {
  UINT                           NbAllocationGroup;
  DXGK_ALLOCATIONGROUPDESCRIPTOR *pAllocationGroupDescriptor;
} DXGK_ALLOCATIONGROUPOUT;
```

## Members

**NbAllocationGroup**
Reserved for system use.

**pAllocationGroupDescriptor**
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

 

 





