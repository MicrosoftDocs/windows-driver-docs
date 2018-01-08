---
title: DXVA\_DeinterlaceBobDeviceClass DeinterlaceBlt method
description: The sample DeinterlaceBlt function performs deinterlace or frame-rate conversion by writing the output to a destination surface.
ms.assetid: 0aa68d0c-8c2b-41fe-9e46-a41b157fbd98
keywords: ["DeinterlaceBlt method Display Devices", "DeinterlaceBlt method Display Devices , DXVA_DeinterlaceBobDeviceClass interface", "DXVA_DeinterlaceBobDeviceClass interface Display Devices , DeinterlaceBlt method"]
topic_type:
- apiref
api_name:
- DXVA_DeinterlaceBobDeviceClass.DeinterlaceBlt
api_type:
- COM
ms.author: windowsdriverdev
ms.date: 01/05/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# DXVA\_DeinterlaceBobDeviceClass::DeinterlaceBlt method


The sample *DeinterlaceBlt* function performs deinterlace or frame-rate conversion by writing the output to a destination surface.

Syntax
------

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

Parameters
----------

*rtTargetFrame* \[in\]
Identifies the location of the output frame within the sequence of input frames. If only deinterlacing is performed, the target time should coincide with either the starting display time of a reference sample, as defined in the [**DXVA\_VideoSample**](https://msdn.microsoft.com/library/windows/hardware/ff564085) structure, or the midpoint between the starting display time and the ending display time. For more information, see the [**DXVA\_DeinterlaceBlt**](https://msdn.microsoft.com/library/windows/hardware/ff563912) structure.

If a frame rate conversion is requested, the **rtTarget** time can be different from any of the **rtStart** times of the reference samples.

*lprcDstRect* \[in\]
Supplies a pointer to a [**RECT**](https://msdn.microsoft.com/library/windows/hardware/ff569234) structure that describes the upper left and lower right points of a rectangle on the destination surface. These points define the area in which the bit-block transfer should occur and its position on the destination surface.

*lpDDSDstSurface* \[in\]
Supplies a pointer to the destination surface. The destination surface can be a D3D render target, a D3D texture, or a D3D texture that is also a render target. The destination surface is always allocated in local video memory.

The pixel format of the destination surface is the one indicated in the [**DXVA\_DeinterlaceCaps**](https://msdn.microsoft.com/library/windows/hardware/ff563939) structure unless a YUV-to-RGB color space conversion is being performed as part of the deinterlace procedure. In this case, the destination surface format is an RGB format with at least 8 bits of precision for each color component.

*lprcSrcRect* \[in\]
Supplies a pointer to a RECT structure that describes the upper left and lower right points of a rectangle on the source surface. These points define the area of the source data for the bit-block transfer and its position on the source surface.

*lpDDSrcSurfaces* \[in\]
Supplies a pointer to an array of video source samples.

*dwNumSurfaces* \[in\]
Indicates the number of surfaces in the **lpDDSrcSurfaces** array.

*fAlpha* \[in\]
Indicates the alpha value for the surface. A value of 0.0F indicates a transparent surface. A value of 1.0F indicates an opaque surface.

Return value
------------

Returns zero (S\_OK or DD\_OK) if successful; otherwise, returns an error code. Refer to *ddraw.h* for a complete list of error codes.

Remarks
-------

The *DeinterlaceBlt* function maps directly to a call to the **RenderMoComp** member of the [**DD\_MOTIONCOMPCALLBACKS**](https://msdn.microsoft.com/library/windows/hardware/ff551660) structure. The **RenderMoComp** member points to a display driver-supplied function that references the [**DD\_RENDERMOCOMPDATA**](https://msdn.microsoft.com/library/windows/hardware/ff551693) structure. The DD\_RENDERMOCOMPDATA structure is filled as follows.

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
<td align="left"><p>Points to an array of [<strong>DDMOCOMPBUFFERINFO</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549652) structures, one for each input reference sample and one for the destination sample. The destination sample is the first element of the array.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>dwFunction</strong></p></td>
<td align="left"><p>Indicates the <strong>DXVA_DeinterlaceBltFnCode</strong> constant defined in <em>dxva.h</em>.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>lpInputData</strong></p></td>
<td align="left"><p>Points to a filled [<strong>DXVA_DeinterlaceBlt</strong>](https://msdn.microsoft.com/library/windows/hardware/ff563912) structure.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>lpOutputData</strong></p></td>
<td align="left"><p>Set to <strong>NULL</strong>, not currently used.</p></td>
</tr>
</tbody>
</table>

 

For the DirectX VA device used for deinterlacing, the driver-supplied callback pointed to by **RenderMoComp** is called without calling the display driver-supplied **BeginMoCompFrame** or **EndMoCompFrame** function.

## <span id="see_also"></span>See also


[**DD\_MOTIONCOMPCALLBACKS**](https://msdn.microsoft.com/library/windows/hardware/ff551660)

[**DD\_RENDERMOCOMPDATA**](https://msdn.microsoft.com/library/windows/hardware/ff551693)

[**DXVA\_DeinterlaceBlt**](https://msdn.microsoft.com/library/windows/hardware/ff563912)

[**DXVA\_DeinterlaceCaps**](https://msdn.microsoft.com/library/windows/hardware/ff563939)

[**DXVA\_VideoSample**](https://msdn.microsoft.com/library/windows/hardware/ff564085)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20DXVA_DeinterlaceBobDeviceClass::DeinterlaceBlt%20method%20%20RELEASE:%20%281/4/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





