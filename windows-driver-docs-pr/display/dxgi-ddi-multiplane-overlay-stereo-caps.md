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
ms.author: windowsdriverdev
ms.date: 01/05/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20DXGI_DDI_MULTIPLANE_OVERLAY_STEREO_CAPS%20enumeration%20%20RELEASE:%20%281/4/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




