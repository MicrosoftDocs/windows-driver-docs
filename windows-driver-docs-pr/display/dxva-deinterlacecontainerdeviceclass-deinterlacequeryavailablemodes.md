---
title: DXVA\_DeinterlaceContainerDeviceClass DeinterlaceQueryAvailableModes method
description: The sample DeinterlaceQueryAvailableModes function queries for available deinterlacing or frame-rate conversion modes for a particular input video format.
ms.assetid: be721bde-3c72-4942-9f33-5ea1bf2d187c
keywords: ["DeinterlaceQueryAvailableModes method Display Devices", "DeinterlaceQueryAvailableModes method Display Devices , DXVA_DeinterlaceContainerDeviceClass interface", "DXVA_DeinterlaceContainerDeviceClass interface Display Devices , DeinterlaceQueryAvailableModes method"]
topic_type:
- apiref
api_name:
- DXVA_DeinterlaceContainerDeviceClass.DeinterlaceQueryAvailableModes
api_type:
- COM
ms.date: 01/05/2018
ms.localizationpriority: medium
---

# DXVA\_DeinterlaceContainerDeviceClass::DeinterlaceQueryAvailableModes method


The sample *DeinterlaceQueryAvailableModes* function queries for available deinterlacing or frame-rate conversion modes for a particular input video format.

Syntax
------

```ManagedCPlusPlus
HRESULT DeinterlaceQueryAvailableModes(
  [in]      LPDXVA_VideoDesc lpVideoDescription,
  [in, out] LPDWORD          lpdwNumModesSupported,
  [in, out] LPGUID           pGuidsDeinterlaceModes
);
```

Parameters
----------

*lpVideoDescription* \[in\]
Supplies a pointer to a [**DXVA\_VideoDesc**](https://msdn.microsoft.com/library/windows/hardware/ff564070) structure that contains a description of the video stream for the deinterlacing or frame-rate conversion to be performed.

*lpdwNumModesSupported* \[in, out\]
Receives a pointer to the number of deinterlace or frame-rate conversion modes that are returned in the array at *pGuidsDeinterlaceModes*.

*pGuidsDeinterlaceModes* \[in, out\]
Receives a pointer to an array of GUIDs that represent the deinterlace or frame-rate conversion modes that are supported by the driver.

Return value
------------

Returns zero (S\_OK or DD\_OK) if successful; otherwise, returns an error code. Refer to *ddraw.h* for a complete list of error codes.

Remarks
-------

The *lpVideoDescription* parameter is passed to the driver so that the driver can support the resolution and format of the source video. For example, the driver might be able to perform a three-field adaptive deinterlace of 480i content, but it might only be able to bob 1080i content. For more information, see [Video Content for Deinterlace and Frame-Rate Conversion](https://msdn.microsoft.com/library/windows/hardware/ff570502).

The GUIDs returned by the *pGuidsDeinterlaceModes* parameter should be returned in order of descending quality (that is, the highest quality mode should occupy the first element of the GUID array returned).

All drivers should be able to support the bob mode using the existing [*bit-block transfer*](https://msdn.microsoft.com/library/windows/hardware/ff556272#wdkgloss-bit-block-transfer) (blt) hardware. For more information about modes, see the [Deinterlace Modes](https://msdn.microsoft.com/library/windows/hardware/ff552704) and [Frame-Rate Conversion Modes](https://msdn.microsoft.com/library/windows/hardware/ff566449) topics.

The driver returns the GUIDs (modes) that it supports in response to a request from the [*VMR*](https://msdn.microsoft.com/library/windows/hardware/ff556344#wdkgloss-video-mixer-renderer--vmr-). The driver responds to a call to its [*DdMoCompRender*](https://msdn.microsoft.com/library/windows/hardware/ff550248) callback function. The driver returns the GUIDs through the **lpOutputData** member of the [**DD\_RENDERMOCOMPDATA**](https://msdn.microsoft.com/library/windows/hardware/ff551693) structure to which the *lpRenderData* parameter of *DdMoCompRender* points. The **lpOutputData** member points to the [**DXVA\_DeinterlaceQueryAvailableModes**](https://msdn.microsoft.com/library/windows/hardware/ff563951) structure, which contains the array of GUIDs in the **Guids** member.

**Mapping RenderMoComp to** ***DeinterlaceQueryAvailableModes***

The sample *DeinterlaceQueryAvailableModes* function maps directly to a call to the **RenderMoComp** member of the [**DD\_MOTIONCOMPCALLBACKS**](https://msdn.microsoft.com/library/windows/hardware/ff551660) structure. The **RenderMoComp** member points to a display driver-supplied function that references the [**DD\_RENDERMOCOMPDATA**](https://msdn.microsoft.com/library/windows/hardware/ff551693) structure.

The **RenderMoComp** callback is called without the display driver-supplied **BeginMoCompFrame** or **EndMoCompFrame** function being called first.

The DD\_RENDERMOCOMPDATA structure is filled as follows.

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
<td align="left"><p>Zero.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>lpBufferInfo</strong></p></td>
<td align="left"><p>NULL.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>dwFunction</strong></p></td>
<td align="left"><p><strong>DXVA_DeinterlaceQueryAvailableModesFnCode</strong> constant (defined in <em>dxva.h</em>).</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>lpInputData</strong></p></td>
<td align="left"><p>Pointer to a filled <a href="https://msdn.microsoft.com/library/windows/hardware/ff564070" data-raw-source="[&lt;strong&gt;DXVA_VideoDesc&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564070)"><strong>DXVA_VideoDesc</strong></a> structure.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>lpOutputData</strong></p></td>
<td align="left"><p>Pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff563951" data-raw-source="[&lt;strong&gt;DXVA_DeinterlaceQueryAvailableModes&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff563951)"><strong>DXVA_DeinterlaceQueryAvailableModes</strong></a> structure.</p></td>
</tr>
</tbody>
</table>

 

After the [*VMR*](https://msdn.microsoft.com/library/windows/hardware/ff556344#wdkgloss-video-mixer-renderer--vmr-) has determined the deinterlace or frame conversion modes available for a particular video format, the VMR queries the driver to obtain detailed information about the input requirements of a particular deinterlace mode and any additional video processing that might be supported on that mode. The driver returns this information from a call to its [**DeinterlaceQueryModeCaps**](dxva-deinterlacecontainerdeviceclass-deinterlacequerymodecaps.md) function.

## <span id="see_also"></span>See also


[**DD\_MOTIONCOMPCALLBACKS**](https://msdn.microsoft.com/library/windows/hardware/ff551660)

[**DD\_RENDERMOCOMPDATA**](https://msdn.microsoft.com/library/windows/hardware/ff551693)

[**DeinterlaceQueryModeCaps**](dxva-deinterlacecontainerdeviceclass-deinterlacequerymodecaps.md)

[**DXVA\_VideoDesc**](https://msdn.microsoft.com/library/windows/hardware/ff564070)

[**DXVA\_SampleFormat**](https://msdn.microsoft.com/library/windows/hardware/ff564045)

 

 






