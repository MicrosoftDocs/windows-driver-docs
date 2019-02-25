---
title: \_DXGKARG\_UPDATEPAGETABLE structure
description: The DXGKARG\_UPDATEPAGETABLE structure is reserved for system use. Do not use it in your driver.
ms.assetid: abd5a200-5f10-4b5d-98e5-f75bc045aff8
keywords: ["_DXGKARG_UPDATEPAGETABLE structure Display Devices", "DXGKARG_UPDATEPAGETABLE structure Display Devices"]
topic_type:
- apiref
api_name:
- DXGKARG_UPDATEPAGETABLE
api_location:
- d3dkmddi.h
api_type:
- HeaderDef
ms.date: 01/05/2018
ms.localizationpriority: medium
---

# \_DXGKARG\_UPDATEPAGETABLE structure


The DXGKARG\_UPDATEPAGETABLE structure is reserved for system use. Do not use it in your driver.

Syntax
------

```ManagedCPlusPlus
typedef struct _DXGKARG_UPDATEPAGETABLE {
  PVOID                        pPageTable;
  UINT                         SizeOfPageTableInPages;
  UINT                         StartIndex;
  UINT                         PageCount;
  const DXGK_PTE               *PTEArray;
  HANDLE                       hAllocation;
  UINT                         PageOffset;
  DXGKARG_UPDATEPAGETABLEFLAGS Flags;
} DXGKARG_UPDATEPAGETABLE;
```

Members
-------

**pPageTable**
Reserved for system use.

**SizeOfPageTableInPages**
Reserved for system use.

**StartIndex**
Reserved for system use.

**PageCount**
Reserved for system use.

**PTEArray**
Reserved for system use.

**hAllocation**
Reserved for system use.

**PageOffset**
Reserved for system use.

**Flags**
Reserved for system use.

Requirements
------------

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

 

 





