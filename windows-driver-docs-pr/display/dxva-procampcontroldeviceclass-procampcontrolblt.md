---
title: ProcAmpControlBlt Method
description: The sample DXVA\_ProcAmpControlDeviceClass::ProcAmpControlBlt function performs the ProcAmp adjustment operation by writing the output to the destination surface.
keywords: ["ProcAmpControlBlt method Display Devices", "ProcAmpControlBlt method Display Devices , DXVA_ProcAmpControlDeviceClass interface", "DXVA_ProcAmpControlDeviceClass interface Display Devices , ProcAmpControlBlt method"]
topic_type:
- apiref
ms.topic: reference
api_name:
- DXVA_ProcAmpControlDeviceClass.ProcAmpControlBlt
api_type:
- COM
ms.date: 01/05/2018
---

# DXVA\_ProcAmpControlDeviceClass::ProcAmpControlBlt method


The sample *ProcAmpControlBlt* function performs the ProcAmp adjustment operation by writing the output to the destination surface.

## Syntax

```cpp
HRESULT ProcAmpControlBlt(
  [in] LPDDSURFACE            lpDDSDstSurface,
  [in] LPDDSURFACE            lpDDSSrcSurface,
  [in] DXVA_ProcAmpControlBlt *ccBlt
);
```

## Parameters

*lpDDSDstSurface* \[in\]
Supplies a pointer to the destination surface.

*lpDDSSrcSurface* \[in\]
Supplies a pointer to the source surface.

*ccBlt* \[in\]
Supplies a pointer to a [**DXVA\_ProcAmpControlBlt**](/windows-hardware/drivers/ddi/dxva/ns-dxva-_dxva_procampcontrolblt) structure that specifies the ProcAmp adjustment data output to the destination surface.

## Return value

Returns zero (S\_OK or DD\_OK) if successful; otherwise, returns an error code. Refer to *ddraw.h* for a complete list of error codes.

## Remarks

The source and destination rectangles are required for either subrectangle ProcAmp adjustment or stretching. Support for stretching is optional and is reported by the **VideoProcessingCaps** member of the [**DXVA\_ProcAmpControlCaps**](/windows-hardware/drivers/ddi/dxva/ns-dxva-_dxva_procampcontrolcaps) structure. Support for subrectangles is also optional.

The destination surface can be an off-screen plane, a D3D render target, a D3D texture, or a D3D texture that is also a render target. The destination surface will always be allocated in local video memory. The pixel format of the destination surface will be the one indicated in the DXVA\_ProcAmpControlCaps structure, unless a YUV-to-RGB color space conversion is being performed as part of the ProcAmp adjustment procedure. In this case, the destination surface format will be an RGB format with at least 8 bits of precision for each color component.

The sample *ProcAmpControlBlt* function maps directly to a call to the **RenderMoComp** member of the [**DD\_MOTIONCOMPCALLBACKS**](/windows/win32/api/ddrawint/ns-ddrawint-dd_motioncompcallbacks) structure. The **RenderMoComp** member points to the driver-supplied *DdMoCompRender* callback that references the [**DD\_RENDERMOCOMPDATA**](/windows/win32/api/ddrawint/ns-ddrawint-dd_rendermocompdata) structure. The DD\_RENDERMOCOMPDATA structure is filled as follows.

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
<td align="left"><p>Number of buffers, which must be the value 2.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>lpBufferInfo</strong></p></td>
<td align="left"><p>Pointer to an array of two surfaces. The first element of the array is the destination surface; the second element of the array is the source surface.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>dwFunction</strong></p></td>
<td align="left"><p><strong>DXVA_ProcAmpControlBltFnCode</strong> constant (defined in <em>dxva.h</em>).</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>lpInputData</strong></p></td>
<td align="left"><p>Pointer to a <a href="/windows-hardware/drivers/ddi/dxva/ns-dxva-_dxva_procampcontrolblt" data-raw-source="[&lt;strong&gt;DXVA_ProcAmpControlBlt&lt;/strong&gt;](/windows-hardware/drivers/ddi/dxva/ns-dxva-_dxva_procampcontrolblt)"><strong>DXVA_ProcAmpControlBlt</strong></a> structure.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>lpOutputData</strong></p></td>
<td align="left"><p>NULL.</p></td>
</tr>
</tbody>
</table>

 

For the DirectX VA device used for ProcAmp control, RenderMoComp is called without calling the display driver-supplied BeginMoCompFrame or EndMoCompFrame function.

## <span id="see_also"></span>See also


[**DXVA\_VideoDesc**](/windows-hardware/drivers/ddi/dxva/ns-dxva-_dxva_videodesc)

[**DXVA\_ProcAmpControlCaps**](/windows-hardware/drivers/ddi/dxva/ns-dxva-_dxva_procampcontrolcaps)

[**DXVA\_ProcAmpControlBlt**](/windows-hardware/drivers/ddi/dxva/ns-dxva-_dxva_procampcontrolblt)

[**DD\_MOTIONCOMPCALLBACKS**](/windows/win32/api/ddrawint/ns-ddrawint-dd_motioncompcallbacks)

[**DD\_CREATEMOCOMPDATA**](/windows/win32/api/ddrawint/ns-ddrawint-dd_createmocompdata)

