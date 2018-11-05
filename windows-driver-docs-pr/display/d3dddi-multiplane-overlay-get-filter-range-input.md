---
title: D3DDDI\_MULTIPLANE\_OVERLAY\_GET\_FILTER\_RANGE\_INPUT structure
description: Reserved for system use. Do not use it in your driver.Note  This structure is available only in the D3dumddi.h header provided with Windows Driver Kit (WDK) Version 8 that shipped with Windows 8. It has been removed from later versions of the header. .
ms.assetid: 1a1c345c-f59e-47fc-8846-27dd7490c1f7
keywords: ["D3DDDI_MULTIPLANE_OVERLAY_GET_FILTER_RANGE_INPUT structure Display Devices"]
topic_type:
- apiref
api_name:
- D3DDDI_MULTIPLANE_OVERLAY_GET_FILTER_RANGE_INPUT
api_location:
- D3dumddi.h
api_type:
- HeaderDef
ms.date: 01/05/2018
ms.localizationpriority: medium
---

# D3DDDI\_MULTIPLANE\_OVERLAY\_GET\_FILTER\_RANGE\_INPUT structure


Reserved for system use. Do not use it in your driver.

&gt; \[!Note\]
&gt;  This structure is available only in the D3dumddi.h header provided with Windows Driver Kit (WDK) Version 8 that shipped with Windows 8. It has been removed from later versions of the header.

 

Syntax
------

```ManagedCPlusPlus
typedef struct D3DDDI_MULTIPLANE_OVERLAY_GET_FILTER_RANGE_INPUT {
  D3DDDI_VIDEO_PRESENT_SOURCE_ID        VidPnSourceId;
  D3DDDI_MULTIPLANE_OVERLAY_FILTER_TYPE FilterType;
} D3DDDI_MULTIPLANE_OVERLAY_GET_FILTER_RANGE_INPUT;
```

Members
-------

**VidPnSourceId**

**FilterType**

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
<td align="left"><p>Windows 8</p></td>
</tr>
<tr class="even">
<td align="left"><p>Minimum supported server</p></td>
<td align="left"><p>Windows Server 2012</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Header</p></td>
<td align="left">D3dumddi.h</td>
</tr>
</tbody>
</table>

 

 





