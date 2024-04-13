---
title: _DXGK_MULTIPLANE_OVERLAY_FILTER Structure
description: Reserved for system use. Do not use it in your driver.Note  This structure is available only in the D3dkmddi.h header provided with Windows Driver Kit (WDK) Version 8 that shipped with Windows 8. It has been removed from later versions of the header. .
keywords: ["_DXGK_MULTIPLANE_OVERLAY_FILTER structure Display Devices", "DXGK_MULTIPLANE_OVERLAY_FILTER structure Display Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- DXGK_MULTIPLANE_OVERLAY_FILTER
api_location:
- D3dkmddi.h
api_type:
- HeaderDef
ms.date: 01/05/2018
---

# \_DXGK\_MULTIPLANE\_OVERLAY\_FILTER structure


Reserved for system use. Do not use it in your driver.

> [!NOTE]
>  This structure is available only in the D3dkmddi.h header provided with Windows Driver Kit (WDK) Version 8 that shipped with Windows 8. It has been removed from later versions of the header.

 

## Syntax

```ManagedCPlusPlus
typedef struct _DXGK_MULITPLANE_OVERLAY_FILTER {
  DXGK_MULTIPLANE_OVERLAY_FILTER_TYPE FilterType;
  BOOL                                Enabled;
  INT                                 Value;
} DXGK_MULTIPLANE_OVERLAY_FILTER;
```

## Members

**FilterType**

**Enabled**

**Value**

## Requirements

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
<td align="left">D3dkmddi.h</td>
</tr>
</tbody>
</table>

 

 





