---
title: D3DDDI_MULTIPLANE_OVERLAY_FILTER_TYPE Enumeration
description: Learn about the D3DDDI\_MULTIPLANE\_OVERLAY\_FILTER\_TYPE enumeration, which is reserved for system use. Do not use it in your driver.
keywords: ["D3DDDI_MULTIPLANE_OVERLAY_FILTER_TYPE enumeration Display Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- D3DDDI_MULTIPLANE_OVERLAY_FILTER_TYPE
api_location:
- D3dumddi.h
api_type:
- HeaderDef
ms.date: 01/05/2018
---

# D3DDDI\_MULTIPLANE\_OVERLAY\_FILTER\_TYPE enumeration


Reserved for system use. Do not use it in your driver.

> [!NOTE]
> This structure is available only in the D3dumddi.h header provided with Windows Driver Kit (WDK) Version 8 that shipped with Windows 8. It has been removed from later versions of the header.

 

## Syntax

```ManagedCPlusPlus
typedef enum _D3DDDI_MULTIPLANE_OVERLAY_FILTER_TYPE {
  D3DDDI_MULTIPLANE_OVERLAY_FILTER_CAPS_BRIGHTNESS       = 0x1,
  D3DDDI_MULTIPLANE_OVERLAY_FILTER_CAPS_CONTRAST         = 0x2,
  D3DDDI_MULTIPLANE_OVERLAY_FILTER_CAPS_HUE              = 0x4,
  D3DDDI_MULTIPLANE_OVERLAY_FILTER_CAPS_SATURATION       = 0x8,
  D3DDDI_MULTIPLANE_OVERLAY_FILTER_CAPS_STRETCH_QUALITY  = 0x10
} D3DDDI_MULTIPLANE_OVERLAY_FILTER_TYPE;
```

## Constants

<span id="D3DDDI_MULTIPLANE_OVERLAY_FILTER_CAPS_BRIGHTNESS"></span><span id="d3dddi_multiplane_overlay_filter_caps_brightness"></span>**D3DDDI\_MULTIPLANE\_OVERLAY\_FILTER\_CAPS\_BRIGHTNESS**

<span id="D3DDDI_MULTIPLANE_OVERLAY_FILTER_CAPS_CONTRAST"></span><span id="d3dddi_multiplane_overlay_filter_caps_contrast"></span>**D3DDDI\_MULTIPLANE\_OVERLAY\_FILTER\_CAPS\_CONTRAST**

<span id="D3DDDI_MULTIPLANE_OVERLAY_FILTER_CAPS_HUE"></span><span id="d3dddi_multiplane_overlay_filter_caps_hue"></span>**D3DDDI\_MULTIPLANE\_OVERLAY\_FILTER\_CAPS\_HUE**

<span id="D3DDDI_MULTIPLANE_OVERLAY_FILTER_CAPS_SATURATION"></span><span id="d3dddi_multiplane_overlay_filter_caps_saturation"></span>**D3DDDI\_MULTIPLANE\_OVERLAY\_FILTER\_CAPS\_SATURATION**

<span id="D3DDDI_MULTIPLANE_OVERLAY_FILTER_CAPS_STRETCH_QUALITY"></span><span id="d3dddi_multiplane_overlay_filter_caps_stretch_quality"></span>**D3DDDI\_MULTIPLANE\_OVERLAY\_FILTER\_CAPS\_STRETCH\_QUALITY**

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
<td align="left">D3dumddi.h</td>
</tr>
</tbody>
</table>

 

 





