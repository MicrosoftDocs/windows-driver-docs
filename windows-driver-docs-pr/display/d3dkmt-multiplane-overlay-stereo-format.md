---
title: D3DKMT\_MULTIPLANE\_OVERLAY\_STEREO\_FORMAT enumeration
description: Reserved for system use. Do not use in your driver.
ms.assetid: dd26ac4b-ecef-4b4d-a050-d3e429ff0542
keywords: ["D3DKMT_MULTIPLANE_OVERLAY_STEREO_FORMAT enumeration Display Devices"]
topic_type:
- apiref
api_name:
- D3DKMT_MULTIPLANE_OVERLAY_STEREO_FORMAT
api_location:
- D3dkmthk.h
api_type:
- HeaderDef
ms.author: windowsdriverdev
ms.date: 01/05/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# D3DKMT\_MULTIPLANE\_OVERLAY\_STEREO\_FORMAT enumeration


Reserved for system use. Do not use in your driver.

Syntax
------

```ManagedCPlusPlus
typedef enum D3DKMT_MULTIPLANE_OVERLAY_STEREO_FORMAT {
  DXGKMT_MULTIPLANE_OVERLAY_STEREO_FORMAT_MONO                = 0,
  D3DKMT_MULTIPLANE_OVERLAY_STEREO_FORMAT_HORIZONTAL          = 1,
  D3DKMT_MULTIPLANE_OVERLAY_STEREO_FORMAT_VERTICAL            = 2,
  DXGKMT_MULTIPLANE_OVERLAY_STEREO_FORMAT_SEPARATE            = 3,
  DXGKMT_MULTIPLANE_OVERLAY_STEREO_FORMAT_MONO_OFFSET         = 4,
  DXGKMT_MULTIPLANE_OVERLAY_STEREO_FORMAT_ROW_INTERLEAVED     = 5,
  DXGKMT_MULTIPLANE_OVERLAY_STEREO_FORMAT_COLUMN_INTERLEAVED  = 6,
  DXGKMT_MULTIPLANE_OVERLAY_STEREO_FORMAT_CHECKERBOARD        = 7
} D3DKMT_MULTIPLANE_OVERLAY_STEREO_FORMAT;
```

Constants
---------

<span id="DXGKMT_MULTIPLANE_OVERLAY_STEREO_FORMAT_MONO"></span><span id="dxgkmt_multiplane_overlay_stereo_format_mono"></span>**DXGKMT\_MULTIPLANE\_OVERLAY\_STEREO\_FORMAT\_MONO**

<span id="D3DKMT_MULTIPLANE_OVERLAY_STEREO_FORMAT_HORIZONTAL"></span><span id="d3dkmt_multiplane_overlay_stereo_format_horizontal"></span>**D3DKMT\_MULTIPLANE\_OVERLAY\_STEREO\_FORMAT\_HORIZONTAL**

<span id="D3DKMT_MULTIPLANE_OVERLAY_STEREO_FORMAT_VERTICAL"></span><span id="d3dkmt_multiplane_overlay_stereo_format_vertical"></span>**D3DKMT\_MULTIPLANE\_OVERLAY\_STEREO\_FORMAT\_VERTICAL**

<span id="DXGKMT_MULTIPLANE_OVERLAY_STEREO_FORMAT_SEPARATE"></span><span id="dxgkmt_multiplane_overlay_stereo_format_separate"></span>**DXGKMT\_MULTIPLANE\_OVERLAY\_STEREO\_FORMAT\_SEPARATE**

<span id="DXGKMT_MULTIPLANE_OVERLAY_STEREO_FORMAT_MONO_OFFSET"></span><span id="dxgkmt_multiplane_overlay_stereo_format_mono_offset"></span>**DXGKMT\_MULTIPLANE\_OVERLAY\_STEREO\_FORMAT\_MONO\_OFFSET**

<span id="DXGKMT_MULTIPLANE_OVERLAY_STEREO_FORMAT_ROW_INTERLEAVED"></span><span id="dxgkmt_multiplane_overlay_stereo_format_row_interleaved"></span>**DXGKMT\_MULTIPLANE\_OVERLAY\_STEREO\_FORMAT\_ROW\_INTERLEAVED**

<span id="DXGKMT_MULTIPLANE_OVERLAY_STEREO_FORMAT_COLUMN_INTERLEAVED"></span><span id="dxgkmt_multiplane_overlay_stereo_format_column_interleaved"></span>**DXGKMT\_MULTIPLANE\_OVERLAY\_STEREO\_FORMAT\_COLUMN\_INTERLEAVED**

<span id="DXGKMT_MULTIPLANE_OVERLAY_STEREO_FORMAT_CHECKERBOARD"></span><span id="dxgkmt_multiplane_overlay_stereo_format_checkerboard"></span>**DXGKMT\_MULTIPLANE\_OVERLAY\_STEREO\_FORMAT\_CHECKERBOARD**

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
<td align="left">D3dkmthk.h</td>
</tr>
</tbody>
</table>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20D3DKMT_MULTIPLANE_OVERLAY_STEREO_FORMAT%20enumeration%20%20RELEASE:%20%281/4/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




