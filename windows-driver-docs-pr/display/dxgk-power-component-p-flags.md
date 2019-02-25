---
title: DXGK\_POWER\_COMPONENT\_P\_FLAGS structure
description: Reserved for system use. Do not use in your driver.
ms.assetid: 9A3C9821-7E98-4F9E-94EE-AF2C09C2A881
keywords: ["DXGK_POWER_COMPONENT_P_FLAGS structure Display Devices"]
topic_type:
- apiref
api_name:
- DXGK_POWER_COMPONENT_P_FLAGS
api_location:
- D3dkmddi.h
api_type:
- HeaderDef
ms.date: 01/05/2018
ms.localizationpriority: medium
---

# DXGK\_POWER\_COMPONENT\_P\_FLAGS structure


Reserved for system use. Do not use in your driver.

Syntax
------

```ManagedCPlusPlus
typedef struct _DXGK_POWER_COMPONENT_P_FLAGS {
  union {
    struct {
      UINT Reserved  :32;
    };
    UINT Value;
  };
} DXGK_POWER_COMPONENT_P_FLAGS;
```

Members
-------

**Reserved**

**Value**

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
<td align="left"><p>Windows 8.1</p></td>
</tr>
<tr class="even">
<td align="left"><p>Minimum supported server</p></td>
<td align="left"><p>Windows Server 2012 R2</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Header</p></td>
<td align="left">D3dkmddi.h (include D3dkmddi.h)</td>
</tr>
</tbody>
</table>

 

 





