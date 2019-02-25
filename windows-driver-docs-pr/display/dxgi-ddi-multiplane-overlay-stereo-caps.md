---
title: DXGI\_DDI\_MULTIPLANE\_OVERLAY\_STEREO\_CAPS enumeration
description: Reserved for system use. Do not use it in your driver.
ms.assetid: 28017595-06d5-48ff-91d7-0e084d1e92de
keywords: ["DXGI_DDI_MULTIPLANE_OVERLAY_STEREO_CAPS enumeration Display Devices"]
topic_type:
- apiref
api_name:
- DXGI_DDI_MULTIPLANE_OVERLAY_STEREO_CAPS
api_location:
- Dxgiddi.h
api_type:
- HeaderDef
ms.date: 01/05/2018
ms.localizationpriority: medium
---

# DXGI\_DDI\_MULTIPLANE\_OVERLAY\_STEREO\_CAPS enumeration


Reserved for system use. Do not use it in your driver.

Syntax
------

```ManagedCPlusPlus
typedef enum DXGI_DDI_MULTIPLANE_OVERLAY_STEREO_CAPS {
  DXGI_DDI_MULTIPLANE_OVERLAY_STEREO_CAPS_SEPARATE            = 0x1,
  DXGI_DDI_MULTIPLANE_OVERLAY_STEREO_CAPS_ROW_INTERLEAVED     = 0x4,
  DXGI_DDI_MULTIPLANE_OVERLAY_STEREO_CAPS_COLUMN_INTERLEAVED  = 0x8,
  DXGI_DDI_MULTIPLANE_OVERLAY_STEREO_CAPS_CHECKERBOARD        = 0x10,
  DXGI_DDI_MULTIPLANE_OVERLAY_STEREO_CAPS_FLIP_MODE           = 0x20
} DXGI_DDI_MULTIPLANE_OVERLAY_STEREO_CAPS;
```

Constants
---------

<span id="DXGI_DDI_MULTIPLANE_OVERLAY_STEREO_CAPS_SEPARATE"></span><span id="dxgi_ddi_multiplane_overlay_stereo_caps_separate"></span>**DXGI\_DDI\_MULTIPLANE\_OVERLAY\_STEREO\_CAPS\_SEPARATE**

<span id="DXGI_DDI_MULTIPLANE_OVERLAY_STEREO_CAPS_ROW_INTERLEAVED"></span><span id="dxgi_ddi_multiplane_overlay_stereo_caps_row_interleaved"></span>**DXGI\_DDI\_MULTIPLANE\_OVERLAY\_STEREO\_CAPS\_ROW\_INTERLEAVED**

<span id="DXGI_DDI_MULTIPLANE_OVERLAY_STEREO_CAPS_COLUMN_INTERLEAVED"></span><span id="dxgi_ddi_multiplane_overlay_stereo_caps_column_interleaved"></span>**DXGI\_DDI\_MULTIPLANE\_OVERLAY\_STEREO\_CAPS\_COLUMN\_INTERLEAVED**

<span id="DXGI_DDI_MULTIPLANE_OVERLAY_STEREO_CAPS_CHECKERBOARD"></span><span id="dxgi_ddi_multiplane_overlay_stereo_caps_checkerboard"></span>**DXGI\_DDI\_MULTIPLANE\_OVERLAY\_STEREO\_CAPS\_CHECKERBOARD**

<span id="DXGI_DDI_MULTIPLANE_OVERLAY_STEREO_CAPS_FLIP_MODE"></span><span id="dxgi_ddi_multiplane_overlay_stereo_caps_flip_mode"></span>**DXGI\_DDI\_MULTIPLANE\_OVERLAY\_STEREO\_CAPS\_FLIP\_MODE**

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
<td align="left">Dxgiddi.h</td>
</tr>
</tbody>
</table>

 

 





