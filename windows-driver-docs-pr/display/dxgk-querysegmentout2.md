---
title: DXGK_QUERYSEGMENTOUT2 Structure
description: The DXGK\_QUERYSEGMENTOUT2 structure is reserved for system use. Do not use it in your driver.
keywords: ["DXGK_QUERYSEGMENTOUT2 structure Display Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- DXGK_QUERYSEGMENTOUT2
api_location:
- d3dkmddi.h
api_type:
- HeaderDef
ms.date: 01/05/2018
---

# DXGK\_QUERYSEGMENTOUT2 structure


The DXGK\_QUERYSEGMENTOUT2 structure is reserved for system use. Do not use it in your driver.

## Syntax

```ManagedCPlusPlus
typedef struct _DXGK_QUERYSEGMENTOUT2 {
  UINT                    SegmentCount;
  DXGK_SEGMENTDESCRIPTOR2 *pSegmentDescriptor;
} DXGK_QUERYSEGMENTOUT2;
```

## Members

**SegmentCount**
Reserved for system use.

**pSegmentDescriptor**
Reserved for system use.

## Requirements

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

 

 





