---
title: \_DXGK\_DMABUFFERCAPS structure
description: The DXGK\_DMABUFFERCAPS structure is reserved for system use. Do not use it in your driver.
ms.assetid: 57ccc0e6-eacf-48a2-a9a1-cb7e43850caa
keywords: ["_DXGK_DMABUFFERCAPS structure Display Devices", "DXGK_DMABUFFERCAPS structure Display Devices"]
topic_type:
- apiref
api_name:
- DXGK_DMABUFFERCAPS
api_location:
- d3dkmddi.h
api_type:
- HeaderDef
ms.date: 01/05/2018
ms.localizationpriority: medium
---

# \_DXGK\_DMABUFFERCAPS structure


The DXGK\_DMABUFFERCAPS structure is reserved for system use. Do not use it in your driver.

Syntax
------

```ManagedCPlusPlus
typedef struct _DXGK_DMABUFFERCAPS {
  struct {
    UINT Size;
    UINT PrivateDriverDataSize;
    UINT SegmentId;
    UINT AllocationGroup;
    UINT Reserved[16];
  } PresentDmaBuffer;
  struct {
    UINT Size;
    UINT PrivateDriverDataSize;
    UINT SegmentId;
    UINT AllocationGroup;
    UINT Reserved[16];
  } PagingDmaBuffer;
} DXGK_DMABUFFERCAPS;
```

Members
-------

**PresentDmaBuffer**

**PagingDmaBuffer**

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

 

 





