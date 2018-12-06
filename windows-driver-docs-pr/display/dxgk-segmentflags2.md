---
title: DXGK\_SEGMENTFLAGS2 structure
description: The DXGK\_SEGMENTFLAGS2 structure is reserved for system use. Do not use it in your driver.
ms.assetid: 9e6f96a2-d32f-4ef8-aaad-dc0cbd053222
keywords: ["DXGK_SEGMENTFLAGS2 structure Display Devices"]
topic_type:
- apiref
api_name:
- DXGK_SEGMENTFLAGS2
api_location:
- d3dkmddi.h
api_type:
- HeaderDef
ms.date: 01/05/2018
ms.localizationpriority: medium
---

# DXGK\_SEGMENTFLAGS2 structure


The DXGK\_SEGMENTFLAGS2 structure is reserved for system use. Do not use it in your driver.

Syntax
------

```ManagedCPlusPlus
typedef struct _DXGK_SEGMENTFLAGS2 {
  union {
    struct {
      UINT Aperture  :1;
      UINT PopulatedFromSystemMemory  :1;
      UINT SystemMemoryReservedByBios  :1;
      UINT CpuVisible  :1;
      UINT Reserved  :28;
    };
    UINT Value;
  };
} DXGK_SEGMENTFLAGS2;
```

Members
-------

**Aperture**
Reserved for system use.

**PopulatedFromSystemMemory**
Reserved for system use.

**SystemMemoryReservedByBios**
Reserved for system use.

**CpuVisible**
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

 

 





