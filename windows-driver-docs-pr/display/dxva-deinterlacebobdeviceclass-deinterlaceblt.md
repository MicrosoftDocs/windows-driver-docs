---
title: DXVA_DeinterlaceBobDeviceClass DeinterlaceBlt method
description: The sample DeinterlaceBlt function performs deinterlace or frame-rate conversion by writing the output to a destination surface.
keywords: ["DeinterlaceBlt method Display Devices", "DeinterlaceBlt method Display Devices , DXVA_DeinterlaceBobDeviceClass interface", "DXVA_DeinterlaceBobDeviceClass interface Display Devices , DeinterlaceBlt method"]
topic_type:
- apiref
api_name:
- DXVA_DeinterlaceBobDeviceClass.DeinterlaceBlt
api_type:
- COM
ms.date: 01/05/2018
ms.localizationpriority: medium
---

# DXVA_DeinterlaceBobDeviceClass::DeinterlaceBlt method


The sample *DeinterlaceBlt* function performs deinterlace or frame-rate conversion by writing the output to a destination surface.

## Syntax

```ManagedCPlusPlus
HRESULT DeinterlaceBlt(
  [in] REFERENCE_TIME     rtTargetFrame,
  [in] LPRECT             lprcDstRect,
  [in] LPDDSURFACE        lpDDSDstSurface,
  [in] LPRECT             lprcSrcRect,
  [in] LPDXVA_VideoSample lpDDSrcSurfaces,
  [in] DWORD              dwNumSurfaces,
  [in] FLOAT              fAlpha
);
```

## Parameters

*rtTargetFrame* \[in\]
Identifies the location of the output frame within the sequence of input frames. If only deinterlacing is performed, the target time should coincide with either the starting display time of a reference sample, as defined in the [**DXVA_VideoSample**](/windows-hardware/drivers/ddi/dxva/ns-dxva-_dxva_videosample) structure, or the midpoint between the starting display time and the ending display time. For more information, see the [**DXVA_DeinterlaceBlt**](/windows-hardware/drivers/ddi/dxva/ns-dxva-_dxva_deinterlaceblt) structure.

If a frame rate conversion is requested, the **rtTarget** time can be different from any of the **rtStart** times of the reference samples.

*lprcDstRect* \[in\]
Supplies a pointer to a [**RECT**](/windows/win32/api/windef/ns-windef-rect) structure that describes the upper left and lower right points of a rectangle on the destination surface. These points define the area in which the bit-block transfer should occur and its position on the destination surface.

*lpDDSDstSurface* \[in\]
Supplies a pointer to the destination surface. The destination surface can be a D3D render target, a D3D texture, or a D3D texture that is also a render target. The destination surface is always allocated in local video memory.

The pixel format of the destination surface is the one indicated in the [**DXVA_DeinterlaceCaps**](/windows-hardware/drivers/ddi/dxva/ns-dxva-_dxva_deinterlacecaps) structure unless a YUV-to-RGB color space conversion is being performed as part of the deinterlace procedure. In this case, the destination surface format is an RGB format with at least 8 bits of precision for each color component.

*lprcSrcRect* \[in\]
Supplies a pointer to a RECT structure that describes the upper left and lower right points of a rectangle on the source surface. These points define the area of the source data for the bit-block transfer and its position on the source surface.

*lpDDSrcSurfaces* \[in\]
Supplies a pointer to an array of video source samples.

*dwNumSurfaces* \[in\]
Indicates the number of surfaces in the **lpDDSrcSurfaces** array.

*fAlpha* \[in\]
Indicates the alpha value for the surface. A value of 0.0F indicates a transparent surface. A value of 1.0F indicates an opaque surface.

## Return value

Returns zero (S_OK or DD_OK) if successful; otherwise, returns an error code. Refer to *ddraw.h* for a complete list of error codes.

## Remarks

The *DeinterlaceBlt* function maps directly to a call to the **RenderMoComp** member of the [**DD_MOTIONCOMPCALLBACKS**](/windows/win32/api/ddrawint/ns-ddrawint-dd_motioncompcallbacks) structure. The **RenderMoComp** member points to a display driver-supplied function that references the [**DD_RENDERMOCOMPDATA**](/windows/win32/api/ddrawint/ns-ddrawint-dd_rendermocompdata) structure. The DD_RENDERMOCOMPDATA structure is filled as follows.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Member</th>
<th align="left">Value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>dwNumBuffers</strong></p></td>
<td align="left"><p>Indicates the number of entries in the array pointed to by <strong>lpBufferInfo</strong>.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>lpBufferInfo</strong></p></td>
<td align="left"><p>Points to an array of <a href="/windows/win32/api/ddrawint/ns-ddrawint-ddmocompbufferinfo" data-raw-source="[&lt;strong&gt;DDMOCOMPBUFFERINFO&lt;/strong&gt;](/windows/win32/api/ddrawint/ns-ddrawint-_ddmocompbufferinfo)"><strong>DDMOCOMPBUFFERINFO</strong></a> structures, one for each input reference sample and one for the destination sample. The destination sample is the first element of the array.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>dwFunction</strong></p></td>
<td align="left"><p>Indicates the <strong>DXVA_DeinterlaceBltFnCode</strong> constant defined in <em>dxva.h</em>.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>lpInputData</strong></p></td>
<td align="left"><p>Points to a filled <a href="/windows-hardware/drivers/ddi/dxva/ns-dxva-_dxva_deinterlaceblt" data-raw-source="[&lt;strong&gt;DXVA_DeinterlaceBlt&lt;/strong&gt;](/windows-hardware/drivers/ddi/dxva/ns-dxva-_dxva_deinterlaceblt)"><strong>DXVA_DeinterlaceBlt</strong></a> structure.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>lpOutputData</strong></p></td>
<td align="left"><p>Set to <strong>NULL</strong>, not currently used.</p></td>
</tr>
</tbody>
</table>

For the DirectX VA device used for deinterlacing, the driver-supplied callback pointed to by **RenderMoComp** is called without calling the display driver-supplied **BeginMoCompFrame** or **EndMoCompFrame** function.

## See also

[**DD_MOTIONCOMPCALLBACKS**](/windows/win32/api/ddrawint/ns-ddrawint-dd_motioncompcallbacks)

[**DD_RENDERMOCOMPDATA**](/windows/win32/api/ddrawint/ns-ddrawint-dd_rendermocompdata)

[**DXVA_DeinterlaceBlt**](/windows-hardware/drivers/ddi/dxva/ns-dxva-_dxva_deinterlaceblt)

[**DXVA_DeinterlaceCaps**](/windows-hardware/drivers/ddi/dxva/ns-dxva-_dxva_deinterlacecaps)

[**DXVA_VideoSample**](/windows-hardware/drivers/ddi/dxva/ns-dxva-_dxva_videosample)
