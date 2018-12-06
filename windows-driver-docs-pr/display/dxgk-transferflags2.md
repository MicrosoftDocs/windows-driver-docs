---
title: \_DXGK\_TRANSFERFLAGS2 structure
description: The DXGK\_TRANSFERFLAGS2 structure is reserved for system use. Do not use it in your driver.
ms.assetid: 5bc690c4-d95a-4048-b716-fb2b12a22a86
keywords: ["_DXGK_TRANSFERFLAGS2 structure Display Devices", "DXGK_TRANSFERFLAGS2 structure Display Devices"]
topic_type:
- apiref
api_name:
- DXGK_TRANSFERFLAGS2
api_location:
- d3dkmddi.h
api_type:
- HeaderDef
ms.date: 01/05/2018
ms.localizationpriority: medium
---

# \_DXGK\_TRANSFERFLAGS2 structure


The DXGK\_TRANSFERFLAGS2 structure is reserved for system use. Do not use it in your driver.

Syntax
------

```ManagedCPlusPlus
typedef struct _DXGK_TRANSFERFLAGS2 {
  union {
    struct {
      UINT Swizzle  :1;
      UINT Unswizzle  :1;
      UINT AllocationIsIdle  :1;
      UINT SwizzlingRange  :1;
      UINT Reserved  :28;
    };
    UINT Value;
  };
} DXGK_TRANSFERFLAGS2;
```

Members
-------

**Swizzle**
Reserved for system use.

**Unswizzle**
Reserved for system use.

**AllocationIsIdle**
Reserved for system use.

**SwizzlingRange**
Reserved for system use.

**Reserved**
Reserved for system use.

**Value**
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

 

 





