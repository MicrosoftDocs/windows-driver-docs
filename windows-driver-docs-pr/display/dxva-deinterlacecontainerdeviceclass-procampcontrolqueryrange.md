---
title: DXVA\_DeinterlaceContainerDeviceClass ProcAmpControlQueryRange method
description: The sample ProcAmpControlQueryRange function allows the VMR to query the driver to determine the minimum, maximum, step size, and default value for each ProcAmp property.
ms.assetid: 13fd5d4b-f753-4a2c-80e0-c9614d7ebd3d
keywords: ["ProcAmpControlQueryRange method Display Devices", "ProcAmpControlQueryRange method Display Devices , DXVA_DeinterlaceContainerDeviceClass interface", "DXVA_DeinterlaceContainerDeviceClass interface Display Devices , ProcAmpControlQueryRange method"]
topic_type:
- apiref
api_name:
- DXVA_DeinterlaceContainerDeviceClass.ProcAmpControlQueryRange
api_location:
- N/A
api_type:
- COM
ms.date: 01/05/2018
ms.localizationpriority: medium
---

# DXVA\_DeinterlaceContainerDeviceClass::ProcAmpControlQueryRange method


The sample **ProcAmpControlQueryRange** function allows the [*VMR*](https://msdn.microsoft.com/library/windows/hardware/ff556344#wdkgloss-vmr) to query the driver to determine the minimum, maximum, step size, and default value for each ProcAmp property.

Syntax
------

```ManagedCPlusPlus
HRESULT ProcAmpControlQueryRange(
  [in]  DWORD                   VideoProperty,
  [in]  DXVA_VideoDes           *lpVideoDescription,
  [out] DXVA_VideoPropertyRange *lpPropRange
);
```

Parameters
----------

*VideoProperty* \[in\]
Identifies the ProcAmp control property for which the driver should return information. The following are possible values for this parameter.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Value</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>DXVA_ProcAmp_Brightness</p></td>
<td align="left"><p>Returns brightness information.</p></td>
</tr>
<tr class="even">
<td align="left"><p>DXVA_ProcAmp_Contrast</p></td>
<td align="left"><p>Returns contrast information.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>DXVA_ProcAmp_Hue</p></td>
<td align="left"><p>Returns hue information.</p></td>
</tr>
<tr class="even">
<td align="left"><p>DXVA_ProcAmp_Saturation</p></td>
<td align="left"><p>Returns saturation information.</p></td>
</tr>
</tbody>
</table>

 

*lpVideoDescription* \[in\]
Supplies a pointer to a [**DXVA\_VideoDesc**](https://msdn.microsoft.com/library/windows/hardware/ff564070) structure. This structure provides the driver with a description of the video to which the ProcAmp adjustment will be applied. Drivers can adjust their ProcAmp support for particular video streams.

*lpPropRange* \[out\]
Receives a pointer to a [**DXVA\_VideoPropertyRange**](https://msdn.microsoft.com/library/windows/hardware/ff564083) structure that specifies the range, step size, and default value for the ProcAmp.

Return value
------------

Returns zero (S\_OK or DD\_OK) if successful; otherwise, returns an error code (for example, E\_NOTIMPL). Refer to *ddraw.h* for a complete list of error codes.

Remarks
-------

For each ProcAmp property, the VMR queries the driver to determine the minimum, maximum, step size, and default value. If the hardware does not support a particular ProcAmp control property, the driver should return E\_NOTIMPL from the **ProcAmpControlQueryRange** function.

For more information regarding ProcAmp properties, see [ProcAmp Properties](https://msdn.microsoft.com/library/windows/hardware/ff569189).

The sample **ProcAmpControlQueryRange** function maps directly to a call to the **RenderMoComp** member of the [**DD\_MOTIONCOMPCALLBACKS**](https://msdn.microsoft.com/library/windows/hardware/ff551660) structure. The **RenderMoComp** member points to the driver-supplied [**DdMoCompRender**](https://msdn.microsoft.com/library/windows/hardware/ff550248) callback that references the [**DD\_RENDERMOCOMPDATA**](https://msdn.microsoft.com/library/windows/hardware/ff551693) structure. The DD\_RENDERMOCOMPDATA structure is filled as follows.

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
<td align="left"><p>dwNumBuffers</p></td>
<td align="left"><p>Zero.</p></td>
</tr>
<tr class="even">
<td align="left"><p>lpBufferInfo</p></td>
<td align="left"><p>NULL.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>dwFunction</p></td>
<td align="left"><p><strong>DXVA_ProcAmpControlQueryRangeFnCode</strong> constant (defined in <em>dxva.h</em>).</p></td>
</tr>
<tr class="even">
<td align="left"><p>lpInputData</p></td>
<td align="left"><p>Pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff564032" data-raw-source="[&lt;strong&gt;DXVA_ProcAmpControlQueryRange&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564032)"><strong>DXVA_ProcAmpControlQueryRange</strong></a> structure.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>lpOutputData</p></td>
<td align="left"><p>Pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff564083" data-raw-source="[&lt;strong&gt;DXVA_VideoPropertyRange&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564083)"><strong>DXVA_VideoPropertyRange</strong></a> structure.</p></td>
</tr>
</tbody>
</table>

 

Note that the RenderMoComp function will be called without the display driver-supplied BeginMoCompFrame or EndMoCompFrame function being called first.

**Example Code**

The following code provides an example of how you can implement your *ProcAmpControlQueryRange* function:

```cpp
HRESULT
DXVA_DeinterlaceContainerDeviceClass::ProcAmpControlQueryRange(
    DWORD VideoProperty,
    LPDXVA_VideoDesc lpVideoDesc,
    DXVA_VideoPropertyRange* lpPropRange
    )
{
    // only the YUY2 and YV12 formats can be operated on
    if (lpVideoDesc->d3dFormat != &#39;2YUY&#39; &amp;&amp;
        lpVideoDesc->d3dFormat != &#39;21VY&#39;) {
        return E_INVALIDARG;
    }
    // the following are the recommended settings for each property
    switch (VideoProperty) {
    case DXVA_ProcAmp_Brightness:
        lpPropRange->MinValue = -100.F;
        lpPropRange->MaxValue = 100.F;
        lpPropRange->DefaultValue = 0.0F;
        lpPropRange->StepSize = 0.1F;
        break;
    case DXVA_ProcAmp_Contrast:
        lpPropRange->MinValue = 0.F;
        lpPropRange->MaxValue = 10.F;
        lpPropRange->DefaultValue = 1.0F;
        lpPropRange->StepSize = 0.01F;
        break;
    case DXVA_ProcAmp_Hue:
        lpPropRange->MinValue = -180.0F;
        lpPropRange->MaxValue =  180.0F;
        lpPropRange->DefaultValue = 0.0F;
        lpPropRange->StepSize = 0.1F;
        break;
    case DXVA_ProcAmp_Saturation:
        lpPropRange->MinValue = 0.F;
        lpPropRange->MaxValue = 10.F;
        lpPropRange->DefaultValue = 1.0F;
        lpPropRange->StepSize = 0.01F;
        break;
    }
    return S_OK;
}
```

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
<td align="left">N/A (Declared in a driver-supplied header file.)</td>
</tr>
</tbody>
</table>

## <span id="see_also"></span>See also


[**DXVA\_ProcAmpControlQueryRange**](https://msdn.microsoft.com/library/windows/hardware/ff564032)

[**DXVA\_VideoDesc**](https://msdn.microsoft.com/library/windows/hardware/ff564070)

[**DXVA\_VideoPropertyRange**](https://msdn.microsoft.com/library/windows/hardware/ff564083)

 

 






