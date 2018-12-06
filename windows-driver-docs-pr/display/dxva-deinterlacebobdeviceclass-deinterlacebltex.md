---
title: DXVA\_DeinterlaceBobDeviceClass DeinterlaceBltEx method
description: The sample DeinterlaceBltEx function performs deinterlace or frame-rate conversion, combines the deinterlaced or frame-rate converted video with supplied video substreams, and writes the combined output to a destination surface.
ms.assetid: 12a0e467-54f8-4cca-8ec0-aa8d04480ab6
keywords: ["DeinterlaceBltEx method Display Devices", "DeinterlaceBltEx method Display Devices , DXVA_DeinterlaceBobDeviceClass interface", "DXVA_DeinterlaceBobDeviceClass interface Display Devices , DeinterlaceBltEx method"]
topic_type:
- apiref
api_name:
- DXVA_DeinterlaceBobDeviceClass.DeinterlaceBltEx
api_type:
- COM
ms.date: 01/05/2018
ms.localizationpriority: medium
---

# DXVA\_DeinterlaceBobDeviceClass::DeinterlaceBltEx method


The sample **DeinterlaceBltEx** function performs deinterlace or frame-rate conversion, combines the deinterlaced or frame-rate converted video with supplied video substreams, and writes the combined output to a destination surface.

Syntax
------

```ManagedCPlusPlus
HRESULT DeinterlaceBltEx(
  [in] REFERENCE_TIME      rtTargetFrame,
  [in] LPRECT              lprcTargetRect,
  [in] DXVA_AYUVsample2    BackgroundColor,
  [in] DWORD               dwDestinationFormat,
  [in] DWORD               dwDestinationFlags,
  [in] LPDDSURFACE         lpDDSDstSurface,
  [in] LPDXVA_VideoSample2 lpDDSrcSurfaces,
  [in] DWORD               dwNumSurfaces,
  [in] FLOAT               fAlpha
);
```

Parameters
----------

*rtTargetFrame* \[in\]
Supplies the location of the output frame within the sequence of input frames. If pure deinterlacing is performed, the target time should coincide with one of the **rtStart** times or midpoint times (that is, (**rtStart**+**rtEnd**)/2) of a sample, as defined in the [**DXVA\_VideoSample2**](https://msdn.microsoft.com/library/windows/hardware/ff564092) structure.

If a frame-rate conversion is requested, the *rtTargetFrame* time might be different from any of the **rtStart** times or midpoint times of the samples.

*lprcTargetRect* \[in\]
Supplies a pointer to a [**RECT**](https://msdn.microsoft.com/library/windows/hardware/ff569234) structure that describes the location within the destination surface to which **DeinterlaceBltEx** must write. The driver uses *lprcTargetRect* to determine which pixels to write to. Note that the output image is restricted to the pixels within the rectangle at *lprcTargetRect*. That is, every pixel within the rectangle at *lprcTargetRect* must be written to, and pixels outside the rectangle at *lprcTargetRect* must not be modified.

*BackgroundColor* \[in\]
Supplies a [**DXVA\_AYUVsample2**](https://msdn.microsoft.com/library/windows/hardware/ff563116) structure that identifies the color and opacity level of the background upon which all video stream and substreams are composed. For Microsoft Windows Server 2003 SP1 and Windows XP SP2, the opacity level is not used and should be ignored by the driver.

*dwDestinationFormat* \[in\]
Supplies format information for the destination surface that is specified in the pointer at *lpDDSDstSurface*. For Windows Server 2003 SP1 and Windows XP SP2, this parameter is set to 0.

*dwDestinationFlags* \[in\]
Supplies a collection of flags that indicate changes in the current destination surface from the previous destination surface. This parameter is a bitwise-OR of one or more of the flags in the [**DXVA\_DestinationFlags**](https://msdn.microsoft.com/library/windows/hardware/ff563963) enumeration type. You can use these flags to optimize your driver code. In other words, your code is not required to perform operations on the current destination surface if no changes have occurred from the previous destination surface.

*lpDDSDstSurface* \[in\]
Supplies a pointer to the destination surface. The destination surface is an offscreen-plain surface located in video memory. The pixel format of the destination surface is specified in the **d3dOutputFormat** member of the [**DXVA\_DeinterlaceCaps**](https://msdn.microsoft.com/library/windows/hardware/ff563939) structure. The pixel format must be in the YUV color space.

*lpDDSrcSurfaces* \[in\]
Supplies a pointer to an array of DXVA\_VideoSample2 structures that describe the video source reference samples and substream samples that are required for the bit-block transfer.

*dwNumSurfaces* \[in\]
Supplies the number of samples in the *lpDDSrcSurfaces* array.

*fAlpha* \[in\]
Supplies the planar-transparency value that the driver should apply to the output destination surface image, which is a composite of background color, video stream, and video substreams. For Windows Server 2003 SP1 and Windows XP SP2, this value is always 1.0F, which indicates that the overall image is opaque and that no alpha blending on the overall image is required.

Return value
------------

Returns 0 (S\_OK or DD\_OK) if successful; otherwise, returns an error code. Refer to *ddraw.h* for a complete list of error codes.

Remarks
-------

The **DeinterlaceBltEx** function performs the deinterlace or frame-rate conversion operation and simultaneously combines supplied video substreams with the deinterlaced or frame-rate converted video. The **DeinterlaceBltEx** function then writes the output to the destination surface. Note that **DeinterlaceBltEx** can be called with a progressive video sample, in which case the driver should not perform a deinterlace operation. The driver should combine the video with the supplied video substreams and convert each stream as indicated by the *lprcTargetRect* and *BackgroundColor* paramters and the **rcSrc** and **rcDst** members of the [**DXVA\_VideoSample2**](https://msdn.microsoft.com/library/windows/hardware/ff564092) structures in the array that is passed in the *pDDSrcSurfaces* parameter.

If a deinterlace mode that requires multiple reference streams is used with progressive video, the multiple frames are still sent to the driver even though those frames are not necessary to produce the output. For more information, see example 5 of [Input Buffer Order](https://msdn.microsoft.com/library/windows/hardware/ff567695).

For the reference video samples in the array that is passed in the *pDDSrcSurfaces* parameter, the **rtStart** and **rtEnd** members of the DXVA\_VideoSample2 structure for the samples indicate the temporal location of the samples. For each video substream sample in the array, the **rtStart** and **rtEnd** members of the DXVA\_VideoSample2 structure for each sample are cleared to 0.

Only video substreams with the AI44, IA44, and AYUV [*FOURCC*](https://msdn.microsoft.com/library/windows/hardware/ff556280#wdkgloss-fourcc) pixel formats can be supplied to the driver. For more information, see [Supplying Video Substream and Destination Surfaces](https://msdn.microsoft.com/library/windows/hardware/ff569751).

For palletized video substream pixel formats, the **Palette** member of the [**DXVA\_VideoSample2**](https://msdn.microsoft.com/library/windows/hardware/ff564092) structure for each video substream contains an array of 16 palette entries that the driver should use when compositing the substream sample. For nonpalletized pixel formats, the palette entries are cleared to zero and can be ignored.

The **SampleFlags** member of the [**DXVA\_VideoSample2**](https://msdn.microsoft.com/library/windows/hardware/ff564092) structure for each input sample contains a collection of flags that indicate changes in the current sample from the previous sample. The flags reflect changes to the palette, color data, source rectangle, and destination rectangle of the sample. You can use these flags to optimize your driver code. In other words, your code is not required to perform operations on the current sample frame if no changes have occurred from the previous sample frame.

The *dwNumSurfaces* parameter indicates the number of elements in the *lpDDSrcSurface* array. The video reference samples are first in the array, followed by the video substreams in Z-order. For more information, see [Input Buffer Order](https://msdn.microsoft.com/library/windows/hardware/ff567695). The number of video substreams that the driver receives can range from 0 to 15. When **DeinterlaceBltEx** is called, the driver will typically receive 0 or 1 video substreams. However, the driver must be implemented so that it can process multiple video substreams.

The **DeinterlaceBltEx** function maps directly to a call to the **RenderMoComp** member of the [**DD\_MOTIONCOMPCALLBACKS**](https://msdn.microsoft.com/library/windows/hardware/ff551660) structure. The **RenderMoComp** member points to a display driver-supplied function that references the [**DD\_RENDERMOCOMPDATA**](https://msdn.microsoft.com/library/windows/hardware/ff551693) structure. The DD\_RENDERMOCOMPDATA structure is filled as follows.

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
<td align="left"><p>Indicates the number of entries in the array pointed to by <strong>lpBufferInfo</strong>. This number is 1 plus the number of source samples.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>lpBufferInfo</strong></p></td>
<td align="left"><p>Points to an array of <a href="https://msdn.microsoft.com/library/windows/hardware/ff549652" data-raw-source="[&lt;strong&gt;DDMOCOMPBUFFERINFO&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549652)"><strong>DDMOCOMPBUFFERINFO</strong></a> structures, one for each input reference source sample or substream sample, and one for the destination sample. The destination sample is the first element of the array.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>dwFunction</strong></p></td>
<td align="left"><p>Indicates the <strong>DXVA_DeinterlaceBltExFnCode</strong> constant defined in <em>dxva.h</em>.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>lpInputData</strong></p></td>
<td align="left"><p>Points to a filled <a href="https://msdn.microsoft.com/library/windows/hardware/ff563915" data-raw-source="[&lt;strong&gt;DXVA_DeinterlaceBltEx&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff563915)"><strong>DXVA_DeinterlaceBltEx</strong></a> structure.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>lpOutputData</strong></p></td>
<td align="left"><p>Set to <strong>NULL</strong>, not currently used.</p></td>
</tr>
</tbody>
</table>

 

For the DirectX VA device used for deinterlacing, the driver-supplied callback pointed to by **RenderMoComp** is called without calling the display driver-supplied **BeginMoCompFrame** or **EndMoCompFrame** function.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Target platform</p></td>
<td align="left">Desktop</td>
</tr>
<tr class="even">
<td align="left"><p>Version</p></td>
<td align="left"><p>Versions:Windows Server 2003 SP1 and later and Windows XP SP2 and later versions only.</p></td>
</tr>
</tbody>
</table>

## <span id="see_also"></span>See also


[**DXVA\_AYUVsample2**](https://msdn.microsoft.com/library/windows/hardware/ff563116)

[**DXVA\_DeinterlaceBltEx**](https://msdn.microsoft.com/library/windows/hardware/ff563915)

[**DXVA\_DeinterlaceCaps**](https://msdn.microsoft.com/library/windows/hardware/ff563939)

[**DXVA\_DestinationFlags**](https://msdn.microsoft.com/library/windows/hardware/ff563963)

[**DXVA\_VideoSample2**](https://msdn.microsoft.com/library/windows/hardware/ff564092)

[**DDMOCOMPBUFFERINFO**](https://msdn.microsoft.com/library/windows/hardware/ff549652)

[**DD\_MOTIONCOMPCALLBACKS**](https://msdn.microsoft.com/library/windows/hardware/ff551660)

[**DD\_RENDERMOCOMPDATA**](https://msdn.microsoft.com/library/windows/hardware/ff551693)

 

 






