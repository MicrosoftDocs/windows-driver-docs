---
title: \_DXGK\_ALLOCATIONINFO2 structure
description: The DXGK\_ALLOCATIONINFO2 structure is reserved for system use. Do not use it in your driver.
ms.assetid: af396dd1-6b47-4724-a481-c8f4646816e9
keywords: ["_DXGK_ALLOCATIONINFO2 structure Display Devices", "DXGK_ALLOCATIONINFO2 structure Display Devices"]
topic_type:
- apiref
api_name:
- DXGK_ALLOCATIONINFO2
api_location:
- d3dkmddi.h
api_type:
- HeaderDef
ms.date: 01/05/2018
ms.localizationpriority: medium
---

# \_DXGK\_ALLOCATIONINFO2 structure


The DXGK\_ALLOCATIONINFO2 structure is reserved for system use. Do not use it in your driver.

Syntax
------

```ManagedCPlusPlus
typedef struct _DXGK_ALLOCATIONINFO2 {
  VOID                      *pPrivateDriverData;
  UINT                      PrivateDriverDataSize;
  UINT                      Alignment;
  SIZE_T                    Size;
  DXGK_SEGMENTPREFERENCE    PreferredSegment;
  UINT                      SupportedSegmentSet;
  UINT                      MaximumRenamingListLength;
  HANDLE                    hAllocation;
  DXGK_ALLOCATIONINFOFLAGS2 Flags;
  DXGK_ALLOCATIONUSAGEHINT  *pAllocationUsageHint;
  UINT                      AllocationPriority;
  UINT                      AllocationGroup;
  UINT                      SwizzlingInvariantBlockSize;
  UINT                      Reserved[6];
} DXGK_ALLOCATIONINFO2;
```

Members
-------

**pPrivateDriverData**
Reserved for system use.

**PrivateDriverDataSize**
Reserved for system use.

**Alignment**
Reserved for system use.

**Size**
Reserved for system use.

**PreferredSegment**
Reserved for system use.

**SupportedSegmentSet**
Reserved for system use.

**MaximumRenamingListLength**
Reserved for system use.

**hAllocation**
Reserved for system use.

**Flags**
Reserved for system use.

**pAllocationUsageHint**
Reserved for system use.

**AllocationPriority**
Reserved for system use.

**AllocationGroup**
Reserved for system use.

**SwizzlingInvariantBlockSize**
Reserved for system use.

**Reserved**
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

 

 





