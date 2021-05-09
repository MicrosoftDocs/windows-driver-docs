---
title: DeinterlaceQueryModeCaps method
description: The sample DXVA\_DeinterlaceContainerDeviceClass::DeinterlaceQueryModeCaps function queries the driver to determine the input capabilities of a particular deinterlace mode and any additional video processing that might be supported on that mode.
keywords: ["DeinterlaceQueryModeCaps method Display Devices", "DeinterlaceQueryModeCaps method Display Devices , DXVA_DeinterlaceContainerDeviceClass interface", "DXVA_DeinterlaceContainerDeviceClass interface Display Devices , DeinterlaceQueryModeCaps method"]
topic_type:
- apiref
api_name:
- DXVA_DeinterlaceContainerDeviceClass.DeinterlaceQueryModeCaps
api_location:
- N/A
api_type:
- COM
ms.date: 12/06/2018
ms.localizationpriority: medium
ms.custom: seodec18
---

# DXVA\_DeinterlaceContainerDeviceClass::DeinterlaceQueryModeCaps method


The sample **DeinterlaceQueryModeCaps** function queries the driver to determine the input capabilities of a particular deinterlace mode and any additional video processing that might be supported on that mode.

## Syntax

```cpp
HRESULT DeinterlaceQueryModeCaps(
  [in]  LPGUID               pGuidDeinterlaceMode,
  [in]  LPDXVA_VideoDesc     lpVideoDescription,
  [out] DXVA_DeinterlaceCaps *lpDeinterlaceCaps
);
```

## Parameters

*pGuidDeinterlaceMode* \[in\]
Supplies a pointer to the GUID used to specify the deinterlace mode.

*lpVideoDescription* \[in\]
Supplies a pointer to a [**DXVA\_VideoDesc**](/windows-hardware/drivers/ddi/dxva/ns-dxva-_dxva_videodesc) structure that defines the type of video to be deinterlaced or rate-converted.

*lpDeinterlaceCaps* \[out\]
Receives a pointer to a [**DXVA\_DeinterlaceCaps**](/windows-hardware/drivers/ddi/dxva/ns-dxva-_dxva_deinterlacecaps) structure that contains the capabilities of the deinterlace mode.

## Return value

Returns zero (S\_OK or DD\_OK) if successful; otherwise, returns an error code. Refer to *ddraw.h* for a complete list of error codes.

## Remarks

The driver is queried by the *VMR* for the capabilities of a deinterlace mode after the VMR has determined the deinterlace modes available for a particular video format. The driver returns available modes from a call to its [**DeinterlaceQueryAvailableModes**](dxva-deinterlacecontainerdeviceclass-deinterlacequeryavailablemodes.md) function.

The **DeinterlaceQueryModeCaps** function reports the capabilities for a given mode in the [**DXVA\_DeinterlaceCaps**](/windows-hardware/drivers/ddi/dxva/ns-dxva-_dxva_deinterlacecaps) structure.

The *lpVideoDescription* parameter is passed to the driver so that the driver can support the resolution and format of the source video. For example, the driver might be able to perform a three-field adaptive deinterlace of 480i content, but it might only be able to bob 1080i content. For more information, see [Video Content for Deinterlace and Frame-Rate Conversion](./video-content-for-deinterlace-and-frame-rate-conversion.md).

All drivers should be able to support the bob mode using the existing *bit-block transfer* hardware.

**Mapping RenderMoComp to *DeinterlaceQueryModeCaps***

The **DeinterlaceQueryModeCaps** function maps directly to a call to the **RenderMoComp** member of the [**DD\_MOTIONCOMPCALLBACKS**](/windows/win32/api/ddrawint/ns-ddrawint-dd_motioncompcallbacks) structure. The **RenderMoComp** member points to a display driver-supplied function that references the [**DD\_RENDERMOCOMPDATA**](/windows/win32/api/ddrawint/ns-ddrawint-dd_rendermocompdata) structure.

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
<td align="left"><p>Pointer to a <a href="/windows-hardware/drivers/ddi/dxva/ns-dxva-_dxva_deinterlacequerymodecaps" data-raw-source="[&lt;strong&gt;DXVA_DeinterlaceQueryModeCaps&lt;/strong&gt;](/windows-hardware/drivers/ddi/dxva/ns-dxva-_dxva_deinterlacequerymodecaps)"><strong>DXVA_DeinterlaceQueryModeCaps</strong></a> structure.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>lpOutputData</strong></p></td>
<td align="left"><p>Pointer to a <a href="/windows-hardware/drivers/ddi/dxva/ns-dxva-_dxva_deinterlacecaps" data-raw-source="[&lt;strong&gt;DXVA_DeinterlaceCaps&lt;/strong&gt;](/windows-hardware/drivers/ddi/dxva/ns-dxva-_dxva_deinterlacecaps)"><strong>DXVA_DeinterlaceCaps</strong></a> structure.</p></td>
</tr>
</tbody>
</table>

 

## Requirements

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
<td align="left"><p>Header</p></td>
<td align="left">N/A (Declared in a driver-supplied header file)</td>
</tr>
</tbody>
</table>

## <span id="see_also"></span>See also


[**DD\_MOTIONCOMPCALLBACKS**](/windows/win32/api/ddrawint/ns-ddrawint-dd_motioncompcallbacks)

[**DD\_RENDERMOCOMPDATA**](/windows/win32/api/ddrawint/ns-ddrawint-dd_rendermocompdata)

[**DeinterlaceQueryAvailableModes**](dxva-deinterlacecontainerdeviceclass-deinterlacequeryavailablemodes.md)

[**DXVA\_DeinterlaceQueryModeCaps**](/windows-hardware/drivers/ddi/dxva/ns-dxva-_dxva_deinterlacequerymodecaps)

[**DXVA\_DeinterlaceCaps**](/windows-hardware/drivers/ddi/dxva/ns-dxva-_dxva_deinterlacecaps)

[**DXVA\_VideoDesc**](/windows-hardware/drivers/ddi/dxva/ns-dxva-_dxva_videodesc)

