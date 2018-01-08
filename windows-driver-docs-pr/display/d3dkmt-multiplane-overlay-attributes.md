---
title: D3DKMT\_MULTIPLANE\_OVERLAY\_ATTRIBUTES structure
description: Reserved for system use. Do not use in your driver.
ms.assetid: 07abf207-62ab-42d1-84b0-74815d1d42b8
keywords: ["D3DKMT_MULTIPLANE_OVERLAY_ATTRIBUTES structure Display Devices"]
topic_type:
- apiref
api_name:
- D3DKMT_MULTIPLANE_OVERLAY_ATTRIBUTES
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

# D3DKMT\_MULTIPLANE\_OVERLAY\_ATTRIBUTES structure


Reserved for system use. Do not use in your driver.

Syntax
------

```ManagedCPlusPlus
typedef struct D3DKMT_MULTIPLANE_OVERLAY_ATTRIBUTES {
  UINT                                         Flags;
  RECT                                         SrcRect;
  RECT                                         DstRect;
#if (DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WDDM1_3)
  RECT                                         ClipRect;
#endif
  D3DDDI_ROTATION                              Rotation;
  D3DKMT_MULTIPLANE_OVERLAY_BLEND              Blend;
#if (DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WDDM1_3)
  UINT                                         DirtyRectCount;
  RECT                                         pDirtyRects;
#else
  UINT                                         NumFilters;
  void                                         *pFilters;
#endif
  D3DKMT_MULTIPLANE_OVERLAY_VIDEO_FRAME_FORMAT VideoFrameFormat;
  UINT                                         YCbCrFlags;
  D3DKMT_MULTIPLANE_OVERLAY_STEREO_FORMAT      StereoFormat;
  BOOL                                         StereoLeftViewFrame0;
  BOOL                                         StereoBaseViewFrame0;
  DXGKMT_MULTIPLANE_OVERLAY_STEREO_FLIP_MODE   StereoFlipMode;
#if (DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WDDM1_3)
  DXGKMT_MULTIPLANE_OVERLAY_STRETCH_QUALITY    StretchQuality;
#endif
} D3DKMT_MULTIPLANE_OVERLAY_ATTRIBUTES;
```

Members
-------

**Flags**

**SrcRect**

**DstRect**

**ClipRect**

**Rotation**

**Blend**

**DirtyRectCount**

**pDirtyRects**

**NumFilters**

**pFilters**

**VideoFrameFormat**

**YCbCrFlags**

**StereoFormat**

**StereoLeftViewFrame0**

**StereoBaseViewFrame0**

**StereoFlipMode**

**StretchQuality**

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20D3DKMT_MULTIPLANE_OVERLAY_ATTRIBUTES%20structure%20%20RELEASE:%20%281/4/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




