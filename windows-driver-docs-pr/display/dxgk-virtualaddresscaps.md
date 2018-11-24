---
title: \_DXGK\_VIRTUALADDRESSCAPS structure
description: The DXGK\_VIRTUALADDRESSCAPS structure is reserved for system use. Do not use it in your driver.
ms.assetid: 45a33031-26ca-4477-9be0-2066927506cf
keywords: ["_DXGK_VIRTUALADDRESSCAPS structure Display Devices", "DXGK_VIRTUALADDRESSCAPS structure Display Devices"]
topic_type:
- apiref
api_name:
- DXGK_VIRTUALADDRESSCAPS
api_location:
- d3dkmddi.h
api_type:
- HeaderDef
ms.date: 01/05/2018
ms.localizationpriority: medium
---

# \_DXGK\_VIRTUALADDRESSCAPS structure


The DXGK\_VIRTUALADDRESSCAPS structure is reserved for system use. Do not use it in your driver.

Syntax
------

```ManagedCPlusPlus
typedef struct _DXGK_VIRTUALADDRESSCAPS {
  union {
    struct {
      UINT PrivilegedMemorySupported  :1;
      UINT ReadOnlyMemorySupported  :1;
      UINT Reserved  :30;
    };
    UINT Value;
  };
  UINT VirtualAddressBitCount;
  UINT PageTableCoverageBitCount;
  UINT PageDirectoryEntrySize;
  UINT PageDirectorySegment;
  UINT PageTableSegment;
  UINT IdealGPUPageSize;
} DXGK_VIRTUALADDRESSCAPS;
```

Members
-------

**PrivilegedMemorySupported**
Reserved for system use.

**ReadOnlyMemorySupported**
Reserved for system use.

**Reserved**
Reserved for system use.

**Value**
Reserved for system use.

**VirtualAddressBitCount**
Reserved for system use.

**PageTableCoverageBitCount**
Reserved for system use.

**PageDirectoryEntrySize**
Reserved for system use.

**PageDirectorySegment**
Reserved for system use.

**PageTableSegment**
Reserved for system use.

**IdealGPUPageSize**
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

 

 





