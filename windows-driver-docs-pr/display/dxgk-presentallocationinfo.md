---
title: DXGK\_PRESENTALLOCATIONINFO structure
description: The DXGK\_PRESENTALLOCATIONINFO structure is reserved for system use. Do not use it in your driver.
ms.assetid: 8a7f25cf-c08c-4f65-bbf4-ba129d88ff6a
keywords: ["DXGK_PRESENTALLOCATIONINFO structure Display Devices"]
topic_type:
- apiref
api_name:
- DXGK_PRESENTALLOCATIONINFO
api_location:
- d3dkmddi.h
api_type:
- HeaderDef
ms.date: 01/05/2018
ms.localizationpriority: medium
---

# DXGK\_PRESENTALLOCATIONINFO structure


The DXGK\_PRESENTALLOCATIONINFO structure is reserved for system use. Do not use it in your driver.

Syntax
------

```ManagedCPlusPlus
typedef struct _DXGK_PRESENTALLOCATIONINFO {
  HANDLE                 hDeviceSpecificAllocation;
  D3DGPU_VIRTUAL_ADDRESS AllocationVirtualAddress;
  PHYSICAL_ADDRESS       PhysicalAddress;
  WORD                   SegmentId;
  WORD                   PhysicalAdapterIndex;
} DXGK_PRESENTALLOCATIONINFO;
```

Members
-------

**hDeviceSpecificAllocation**
Reserved for system use.

**AllocationVirtualAddress**
Reserved for system use.

**PhysicalAddress**
Reserved for system use.

**SegmentId**
Reserved for system use.

**PhysicalAdapterIndex**
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

 

 





