---
title: \_DXGKARG\_MOVEPAGEDIRECTORY structure
description: The DXGKARG\_MOVEPAGEDIRECTORY structure is reserved for system use. Do not use it in your driver.
keywords: ["_DXGKARG_MOVEPAGEDIRECTORY structure Display Devices", "DXGKARG_MOVEPAGEDIRECTORY structure Display Devices"]
topic_type:
- apiref
api_name:
- DXGKARG_MOVEPAGEDIRECTORY
api_location:
- d3dkmddi.h
api_type:
- HeaderDef
ms.date: 01/05/2018
ms.localizationpriority: medium
---

# \_DXGKARG\_MOVEPAGEDIRECTORY structure


The DXGKARG\_MOVEPAGEDIRECTORY structure is reserved for system use. Do not use it in your driver.

## Syntax

```ManagedCPlusPlus
typedef struct _DXGKARG_MOVEPAGEDIRECTORY {
  PVOID            pPageDirectory;
  PHYSICAL_ADDRESS PhysicalAddress;
  UINT             Segment;
  UINT             SizeInPages;
} DXGKARG_MOVEPAGEDIRECTORY;
```

## Members

**pPageDirectory**
Reserved for system use.

**PhysicalAddress**
Reserved for system use.

**Segment**
Reserved for system use.

**SizeInPages**
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

 

 





