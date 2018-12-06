---
title: DXVA\_DeinterlaceContainerDeviceClass DeinterlaceQueryModeCaps method
description: The sample DeinterlaceQueryModeCaps function queries the driver to determine the input capabilities of a particular deinterlace mode and any additional video processing that might be supported on that mode.
ms.assetid: 49070e57-2a93-447e-98d5-b98cded78b9c
keywords: ["DeinterlaceQueryModeCaps method Display Devices", "DeinterlaceQueryModeCaps method Display Devices , DXVA_DeinterlaceContainerDeviceClass interface", "DXVA_DeinterlaceContainerDeviceClass interface Display Devices , DeinterlaceQueryModeCaps method"]
topic_type:
- apiref
api_name:
- DXVA_DeinterlaceContainerDeviceClass.DeinterlaceQueryModeCaps
api_location:
- N/A
api_type:
- COM
ms.date: 01/05/2018
ms.localizationpriority: medium
---

# DXVA\_DeinterlaceContainerDeviceClass::DeinterlaceQueryModeCaps method


The sample **DeinterlaceQueryModeCaps** function queries the driver to determine the input capabilities of a particular deinterlace mode and any additional video processing that might be supported on that mode.

Syntax
------

```ManagedCPlusPlus
HRESULT DeinterlaceQueryModeCaps(
  [in]  LPGUID               pGuidDeinterlaceMode,
  [in]  LPDXVA_VideoDesc     lpVideoDescription,
  [out] DXVA_DeinterlaceCaps *lpDeinterlaceCaps
);
```

Parameters
----------

*pGuidDeinterlaceMode* \[in\]
Supplies a pointer to the GUID used to specify the deinterlace mode.

*lpVideoDescription* \[in\]
Supplies a pointer to a [**DXVA\_VideoDesc**](https://msdn.microsoft.com/library/windows/hardware/ff564070) structure that defines the type of video to be deinterlaced or rate-converted.

*lpDeinterlaceCaps* \[out\]
Receives a pointer to a [**DXVA\_DeinterlaceCaps**](https://msdn.microsoft.com/library/windows/hardware/ff563939) structure that contains the capabilities of the deinterlace mode.

Return value
------------

Returns zero (S\_OK or DD\_OK) if successful; otherwise, returns an error code. Refer to *ddraw.h* for a complete list of error codes.

Remarks
-------

The driver is queried by the [*VMR*](https://msdn.microsoft.com/library/windows/hardware/ff556344#wdkgloss-vmr) for the capabilities of a deinterlace mode after the VMR has determined the deinterlace modes available for a particular video format. The driver returns available modes from a call to its [**DeinterlaceQueryAvailableModes**](dxva-deinterlacecontainerdeviceclass-deinterlacequeryavailablemodes.md) function.

The **DeinterlaceQueryModeCaps** function reports the capabilities for a given mode in the [**DXVA\_DeinterlaceCaps**](https://msdn.microsoft.com/library/windows/hardware/ff563939) structure.

The *lpVideoDescription* parameter is passed to the driver so that the driver can support the resolution and format of the source video. For example, the driver might be able to perform a three-field adaptive deinterlace of 480i content, but it might only be able to bob 1080i content. For more information, see [Video Content for Deinterlace and Frame-Rate Conversion](https://msdn.microsoft.com/library/windows/hardware/ff570502).

All drivers should be able to support the bob mode using the existing [*bit-block transfer*](https://msdn.microsoft.com/library/windows/hardware/ff556272#wdkgloss-bit-block-transfer) hardware.

**Mapping RenderMoComp to *DeinterlaceQueryModeCaps***

The **DeinterlaceQueryModeCaps** function maps directly to a call to the **RenderMoComp** member of the [**DD\_MOTIONCOMPCALLBACKS**](https://msdn.microsoft.com/library/windows/hardware/ff551660) structure. The **RenderMoComp** member points to a display driver-supplied function that references the [**DD\_RENDERMOCOMPDATA**](https://msdn.microsoft.com/library/windows/hardware/ff551693) structure.

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
<td align="left"><p>Pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff563956" data-raw-source="[&lt;strong&gt;DXVA_DeinterlaceQueryModeCaps&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff563956)"><strong>DXVA_DeinterlaceQueryModeCaps</strong></a> structure.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>lpOutputData</strong></p></td>
<td align="left"><p>Pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff563939" data-raw-source="[&lt;strong&gt;DXVA_DeinterlaceCaps&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff563939)"><strong>DXVA_DeinterlaceCaps</strong></a> structure.</p></td>
</tr>
</tbody>
</table>

 

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
<td align="left"><p>Header</p></td>
<td align="left">N/A (Declared in a driver-supplied header file)</td>
</tr>
</tbody>
</table>

## <span id="see_also"></span>See also


[**DD\_MOTIONCOMPCALLBACKS**](https://msdn.microsoft.com/library/windows/hardware/ff551660)

[**DD\_RENDERMOCOMPDATA**](https://msdn.microsoft.com/library/windows/hardware/ff551693)

[**DeinterlaceQueryAvailableModes**](dxva-deinterlacecontainerdeviceclass-deinterlacequeryavailablemodes.md)

[**DXVA\_DeinterlaceQueryModeCaps**](https://msdn.microsoft.com/library/windows/hardware/ff563956)

[**DXVA\_DeinterlaceCaps**](https://msdn.microsoft.com/library/windows/hardware/ff563939)

[**DXVA\_VideoDesc**](https://msdn.microsoft.com/library/windows/hardware/ff564070)

 

 






