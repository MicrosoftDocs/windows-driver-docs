---
title: D3DKMT\_MULTIPLANE\_OVERLAY\_YCbCr\_FLAGS enumeration
description: Reserved for system use. Do not use in your driver.
ms.assetid: 3bfcd424-961f-4efe-a928-2ee7fbd29f4a
keywords: ["D3DKMT_MULTIPLANE_OVERLAY_YCbCr_FLAGS enumeration Display Devices"]
topic_type:
- apiref
api_name:
- D3DKMT_MULTIPLANE_OVERLAY_YCbCr_FLAGS
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

# D3DKMT\_MULTIPLANE\_OVERLAY\_YCbCr\_FLAGS enumeration


Reserved for system use. Do not use in your driver.

Syntax
------

```ManagedCPlusPlus
typedef enum D3DKMT_MULTIPLANE_OVERLAY_YCbCr_FLAGS {
  D3DKMT_MULTIPLANE_OVERLAY_YCbCr_FLAG_NOMINAL_RANGE  = 0x1,
  D3DKMT_MULTIPLANE_OVERLAY_YCbCr_FLAG_BT709          = 0x2,
  D3DKMT_MULTIPLANE_OVERLAY_YCbCr_FLAG_xvYCC          = 0x4
} D3DKMT_MULTIPLANE_OVERLAY_YCbCr_FLAGS;
```

Constants
---------

<span id="D3DKMT_MULTIPLANE_OVERLAY_YCbCr_FLAG_NOMINAL_RANGE"></span><span id="d3dkmt_multiplane_overlay_ycbcr_flag_nominal_range"></span><span id="D3DKMT_MULTIPLANE_OVERLAY_YCBCR_FLAG_NOMINAL_RANGE"></span>**D3DKMT\_MULTIPLANE\_OVERLAY\_YCbCr\_FLAG\_NOMINAL\_RANGE**

<span id="D3DKMT_MULTIPLANE_OVERLAY_YCbCr_FLAG_BT709"></span><span id="d3dkmt_multiplane_overlay_ycbcr_flag_bt709"></span><span id="D3DKMT_MULTIPLANE_OVERLAY_YCBCR_FLAG_BT709"></span>**D3DKMT\_MULTIPLANE\_OVERLAY\_YCbCr\_FLAG\_BT709**

<span id="D3DKMT_MULTIPLANE_OVERLAY_YCbCr_FLAG_xvYCC"></span><span id="d3dkmt_multiplane_overlay_ycbcr_flag_xvycc"></span><span id="D3DKMT_MULTIPLANE_OVERLAY_YCBCR_FLAG_XVYCC"></span>**D3DKMT\_MULTIPLANE\_OVERLAY\_YCbCr\_FLAG\_xvYCC**

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20D3DKMT_MULTIPLANE_OVERLAY_YCbCr_FLAGS%20enumeration%20%20RELEASE:%20%281/4/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




