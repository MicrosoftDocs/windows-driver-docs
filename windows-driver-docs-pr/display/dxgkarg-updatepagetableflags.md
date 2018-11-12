---
title: \_DXGKARG\_UPDATEPAGETABLEFLAGS structure
description: The DXGKARG\_UPDATEPAGETABLEFLAGS structure is reserved for system use. Do not use it in your driver.
ms.assetid: 59a3fb51-ba3e-420e-abf7-c3faacc25ebc
keywords: ["_DXGKARG_UPDATEPAGETABLEFLAGS structure Display Devices", "DXGKARG_UPDATEPAGETABLEFLAGS structure Display Devices"]
topic_type:
- apiref
api_name:
- DXGKARG_UPDATEPAGETABLEFLAGS
api_location:
- d3dkmddi.h
api_type:
- HeaderDef
ms.date: 01/05/2018
ms.localizationpriority: medium
---

# \_DXGKARG\_UPDATEPAGETABLEFLAGS structure


The DXGKARG\_UPDATEPAGETABLEFLAGS structure is reserved for system use. Do not use it in your driver.

Syntax
------

```ManagedCPlusPlus
typedef struct _DXGKARG_UPDATEPAGETABLEFLAGS {
  union {
    struct {
      UINT LinearAccess  :1;
      UINT Reserved  :31;
    };
    UINT Value;
  };
} DXGKARG_UPDATEPAGETABLEFLAGS;
```

Members
-------

**LinearAccess**
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

 

 





