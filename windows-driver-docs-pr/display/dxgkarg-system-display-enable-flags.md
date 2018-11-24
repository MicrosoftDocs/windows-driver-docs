---
title: DXGKARG\_SYSTEM\_DISPLAY\_ENABLE\_FLAGS structure
description: Reserved for system use. Do not use it in your driver.
ms.assetid: f23d6692-4c9d-48eb-8d7f-ef70334494b1
keywords: ["DXGKARG_SYSTEM_DISPLAY_ENABLE_FLAGS structure Display Devices", "PDXGKARG_SYSTEM_DISPLAY_ENABLE_FLAGS structure pointer Display Devices"]
topic_type:
- apiref
api_name:
- DXGKARG_SYSTEM_DISPLAY_ENABLE_FLAGS
api_location:
- Dispmprt.h
api_type:
- HeaderDef
ms.date: 01/05/2018
ms.localizationpriority: medium
---

# DXGKARG\_SYSTEM\_DISPLAY\_ENABLE\_FLAGS structure


Reserved for system use. Do not use it in your driver.

Syntax
------

```ManagedCPlusPlus
typedef struct _DXGKARG_SYSTEM_DISPLAY_ENABLE_FLAGS {
  union {
    struct {
      UINT Reserved  :32;
    };
    UINT   Value;
  };
} DXGKARG_SYSTEM_DISPLAY_ENABLE_FLAGS, *PDXGKARG_SYSTEM_DISPLAY_ENABLE_FLAGS;
```

Members
-------

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
<td align="left"><p>Minimum supported client</p></td>
<td align="left"><p>Windows 8</p></td>
</tr>
<tr class="even">
<td align="left"><p>Minimum supported server</p></td>
<td align="left"><p>Windows Server 2012</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Header</p></td>
<td align="left">Dispmprt.h</td>
</tr>
</tbody>
</table>

 

 





