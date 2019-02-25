---
title: \_DXGK\_ALLOCATIONGROUPDESCRIPTOR structure
description: The DXGK\_ALLOCATIONGROUPDESCRIPTOR structure is reserved for system use. Do not use it in your driver.
ms.assetid: 74ca560d-b5ec-40f1-a064-4972c7908fc9
keywords: ["_DXGK_ALLOCATIONGROUPDESCRIPTOR structure Display Devices", "DXGK_ALLOCATIONGROUPDESCRIPTOR structure Display Devices"]
topic_type:
- apiref
api_name:
- DXGK_ALLOCATIONGROUPDESCRIPTOR
api_location:
- d3dkmddi.h
api_type:
- HeaderDef
ms.date: 01/05/2018
ms.localizationpriority: medium
---

# \_DXGK\_ALLOCATIONGROUPDESCRIPTOR structure


The DXGK\_ALLOCATIONGROUPDESCRIPTOR structure is reserved for system use. Do not use it in your driver.

Syntax
------

```ManagedCPlusPlus
typedef struct _DXGK_ALLOCATIONGROUPDESCRIPTOR {
  D3DGPU_VIRTUAL_ADDRESS MinimumVirtualAddress;
  D3DGPU_VIRTUAL_ADDRESS MaximumVirtualAddress;
} DXGK_ALLOCATIONGROUPDESCRIPTOR;
```

Members
-------

**MinimumVirtualAddress**
Reserved for system use.

**MaximumVirtualAddress**
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

 

 





