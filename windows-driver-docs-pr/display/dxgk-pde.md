---
title: \_DXGK\_PDE structure
description: The DXGK\_PDE structure is reserved for system use. Do not use it in your driver.
ms.assetid: e2cd4541-beda-4c61-bdba-a86ae3888501
keywords: ["_DXGK_PDE structure Display Devices", "DXGK_PDE structure Display Devices"]
topic_type:
- apiref
api_name:
- DXGK_PDE
api_location:
- d3dkmddi.h
api_type:
- HeaderDef
ms.date: 01/05/2018
ms.localizationpriority: medium
---

# \_DXGK\_PDE structure


The DXGK\_PDE structure is reserved for system use. Do not use it in your driver.

Syntax
------

```ManagedCPlusPlus
typedef struct _DXGK_PDE {
  union {
    struct {
      ULONGLONG Valid  :1;
      ULONGLONG Segment  :5;
      ULONGLONG Reserved  :6;
      ULONGLONG PageTableAddress  :52;
    };
    ULONGLONG Value;
  };
  UINT PageTableSizeInPages;
} DXGK_PDE;
```

Members
-------

**Valid**
Reserved for system use.

**Segment**
Reserved for system use.

**Reserved**
Reserved for system use.

**PageTableAddress**
Reserved for system use.

**Value**
Reserved for system use.

**PageTableSizeInPages**
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

 

 





