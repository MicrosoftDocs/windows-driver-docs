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
ms.author: windowsdriverdev
ms.date: 01/05/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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
<td align="left"><p>Pointer to a [<strong>DXVA_DeinterlaceQueryModeCaps</strong>](https://msdn.microsoft.com/library/windows/hardware/ff563956) structure.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>lpOutputData</strong></p></td>
<td align="left"><p>Pointer to a [<strong>DXVA_DeinterlaceCaps</strong>](https://msdn.microsoft.com/library/windows/hardware/ff563939) structure.</p></td>
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20DXVA_DeinterlaceContainerDeviceClass::DeinterlaceQueryModeCaps%20method%20%20RELEASE:%20%281/4/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





