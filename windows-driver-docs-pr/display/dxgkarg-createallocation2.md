---
title: _DXGKARG_CREATEALLOCATION2 Structure
description: The DXGKARG\_CREATEALLOCATION2 structure is reserved for system use. Do not use it in your driver.
keywords: ["_DXGKARG_CREATEALLOCATION2 structure Display Devices", "DXGKARG_CREATEALLOCATION2 structure Display Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- DXGKARG_CREATEALLOCATION2
api_location:
- d3dkmddi.h
api_type:
- HeaderDef
ms.date: 01/05/2018
---

# \_DXGKARG\_CREATEALLOCATION2 structure


The DXGKARG\_CREATEALLOCATION2 structure is reserved for system use. Do not use it in your driver.

## Syntax

```ManagedCPlusPlus
typedef struct _DXGKARG_CREATEALLOCATION2 {
  const VOID                  *pPrivateDriverData;
  UINT                        PrivateDriverDataSize;
  UINT                        NumAllocations;
  DXGK_ALLOCATIONINFO2        *pAllocationInfo;
  HANDLE                      hResource;
  DXGK_CREATEALLOCATIONFLAGS2 Flags;
} DXGKARG_CREATEALLOCATION2;
```

## Members

**pPrivateDriverData**
Reserved for system use.

**PrivateDriverDataSize**
Reserved for system use.

**NumAllocations**
Reserved for system use.

**pAllocationInfo**
Reserved for system use.

**hResource**
Reserved for system use.

**Flags**
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

 

 





