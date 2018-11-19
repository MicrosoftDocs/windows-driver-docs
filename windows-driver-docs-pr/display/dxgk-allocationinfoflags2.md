---
title: \_DXGK\_ALLOCATIONINFOFLAGS2 structure
description: The DXGK\_ALLOCATIONINFOFLAGS2 structure is reserved for system use. Do not use in your driver.
ms.assetid: 67c27f53-29f0-4639-a360-0dbf7f3b3849
keywords: ["_DXGK_ALLOCATIONINFOFLAGS2 structure Display Devices", "DXGK_ALLOCATIONINFOFLAGS2 structure Display Devices"]
topic_type:
- apiref
api_name:
- DXGK_ALLOCATIONINFOFLAGS2
api_location:
- d3dkmddi.h
api_type:
- HeaderDef
ms.date: 01/05/2018
ms.localizationpriority: medium
---

# \_DXGK\_ALLOCATIONINFOFLAGS2 structure


The DXGK\_ALLOCATIONINFOFLAGS2 structure is reserved for system use. Do not use in your driver.

Syntax
------

```ManagedCPlusPlus
typedef struct _DXGK_ALLOCATIONINFOFLAGS2 {
  union {
    struct {
      UINT CpuVisible;
      UINT ReadOnly;
      UINT PermanentSysMem;
      UINT Cached;
      UINT ExistingSysMem;
      UINT ExistingKernelSysMem;
      UINT Swizzled;
      UINT Overlay;
      UINT Capture;
      UINT SynchronousPaging;
      UINT LinkMirrored;
      UINT LinkInstanced;
      UINT HistoryBuffer  :1;
      UINT Reserved  :2;
      UINT DXGK_ALLOC_RESERVED16  :1;
      UINT DXGK_ALLOC_RESERVED15  :1;
      UINT DXGK_ALLOC_RESERVED14  :1;
      UINT DXGK_ALLOC_RESERVED13  :1;
      UINT DXGK_ALLOC_RESERVED12  :1;
      UINT DXGK_ALLOC_RESERVED11  :1;
      UINT DXGK_ALLOC_RESERVED9  :1;
      UINT DXGK_ALLOC_RESERVED8  :1;
      UINT DXGK_ALLOC_RESERVED7  :1;
      UINT DXGK_ALLOC_RESERVED6  :1;
      UINT DXGK_ALLOC_RESERVED5  :1;
      UINT DXGK_ALLOC_RESERVED4  :1;
      UINT DXGK_ALLOC_RESERVED3  :1;
      UINT DXGK_ALLOC_RESERVED2  :1;
      UINT DXGK_ALLOC_RESERVED1  :1;
      UINT DXGK_ALLOC_RESERVED0  :1;
    };
    UINT Value;
  };
} DXGK_ALLOCATIONINFOFLAGS2;
```

Members
-------

**CpuVisible**

**ReadOnly**

**PermanentSysMem**

**Cached**

**ExistingSysMem**

**ExistingKernelSysMem**

**Swizzled**

**Overlay**

**Capture**

**SynchronousPaging**

**LinkMirrored**

**LinkInstanced**

**HistoryBuffer**

**Reserved**

**DXGK\_ALLOC\_RESERVED16**

**DXGK\_ALLOC\_RESERVED15**

**DXGK\_ALLOC\_RESERVED14**

**DXGK\_ALLOC\_RESERVED13**

**DXGK\_ALLOC\_RESERVED12**

**DXGK\_ALLOC\_RESERVED11**

**DXGK\_ALLOC\_RESERVED9**

**DXGK\_ALLOC\_RESERVED8**

**DXGK\_ALLOC\_RESERVED7**

**DXGK\_ALLOC\_RESERVED6**

**DXGK\_ALLOC\_RESERVED5**

**DXGK\_ALLOC\_RESERVED4**

**DXGK\_ALLOC\_RESERVED3**

**DXGK\_ALLOC\_RESERVED2**

**DXGK\_ALLOC\_RESERVED1**

**DXGK\_ALLOC\_RESERVED0**

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
<td align="left"><p>Version</p></td>
<td align="left"><p>Available in Windows 7 and later versions of the Windows operating systems. Updated in Windows 8.1.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">D3dkmddi.h (include D3dkmddi.h)</td>
</tr>
</tbody>
</table>

 

 





