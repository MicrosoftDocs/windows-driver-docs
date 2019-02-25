---
title: \_DXGK\_CREATEALLOCATIONFLAGS2 structure
description: The DXGK\_CREATEALLOCATIONFLAGS2 structure is reserved for system use. Do not use it in your driver.
ms.assetid: c0d57a64-c509-4d72-81eb-7591bb0c1b9b
keywords: ["_DXGK_CREATEALLOCATIONFLAGS2 structure Display Devices", "DXGK_CREATEALLOCATIONFLAGS2 structure Display Devices"]
topic_type:
- apiref
api_name:
- DXGK_CREATEALLOCATIONFLAGS2
api_location:
- d3dkmddi.h
api_type:
- HeaderDef
ms.date: 01/05/2018
ms.localizationpriority: medium
---

# \_DXGK\_CREATEALLOCATIONFLAGS2 structure


The DXGK\_CREATEALLOCATIONFLAGS2 structure is reserved for system use. Do not use it in your driver.

Syntax
------

```ManagedCPlusPlus
typedef struct _DXGK_CREATEALLOCATIONFLAGS2 {
  union {
    struct {
      UINT Resource;
      UINT Reserved;
    };
    UINT Value;
  };
} DXGK_CREATEALLOCATIONFLAGS2;
```

Members
-------

**Resource**
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

 

 





