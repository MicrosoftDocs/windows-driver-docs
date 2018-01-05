---
title: DXVA\_DeinterlaceContainerDeviceClass ProcAmpControlQueryCaps method
description: The sample ProcAmpControlQueryCaps function allows the VMR to query the driver to determine input requirements of the ProcAmp control device and additional video processing operations that might be supported.
ms.assetid: e89f9a01-e8b3-4311-ad3b-296021c9795e
keywords: ["ProcAmpControlQueryCaps method Display Devices", "ProcAmpControlQueryCaps method Display Devices , DXVA_DeinterlaceContainerDeviceClass interface", "DXVA_DeinterlaceContainerDeviceClass interface Display Devices , ProcAmpControlQueryCaps method"]
topic_type:
- apiref
api_name:
- DXVA_DeinterlaceContainerDeviceClass.ProcAmpControlQueryCaps
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

# DXVA\_DeinterlaceContainerDeviceClass::ProcAmpControlQueryCaps method


The sample *ProcAmpControlQueryCaps* function allows the [*VMR*](https://msdn.microsoft.com/library/windows/hardware/ff556344#wdkgloss-video-mixer-renderer--vmr-) to query the driver to determine input requirements of the ProcAmp control device and additional video processing operations that might be supported. The query can occur at the same time that the ProcAmp adjustments operation is being performed.

Syntax
------

```ManagedCPlusPlus
HRESULT ProcAmpControlQueryCaps(
  [in]  DXVA_VideoDesc          *lpVideoDescription,
  [out] DXVA_ProcAmpControlCaps *lpProcAmpCaps
);
```

Parameters
----------

*lpVideoDescription* \[in\]
Supplies a pointer to a [**DXVA\_VideoDesc**](https://msdn.microsoft.com/library/windows/hardware/ff564070) structure that defines the ProcAmp control parameters for the video to be processed.

*lpProcAmpCaps* \[out\]
Receives a pointer to a [**DXVA\_ProcAmpControlCaps**](https://msdn.microsoft.com/library/windows/hardware/ff564019) structure that contains the driver capabilities for ProcAmp control operations.

Return value
------------

Returns zero (S\_OK or DD\_OK) if successful; otherwise, returns an error code. Refer to *ddraw.h* for a complete list of error codes.

Remarks
-------

The driver reports its capabilities to a user-mode component for the ProcAmp control mode in the [**DXVA\_ProcAmpControlCaps**](https://msdn.microsoft.com/library/windows/hardware/ff564019) structure pointed to by *lpProcAmpCaps*.

The sample *ProcAmpControlQueryCaps* function maps directly to a call to the **RenderMoComp** member of the [**DD\_MOTIONCOMPCALLBACKS**](https://msdn.microsoft.com/library/windows/hardware/ff551660) structure. The **RenderMoComp** function points to the driver-supplied *DdMoCompRender* callback that references the [**DD\_RENDERMOCOMPDATA**](https://msdn.microsoft.com/library/windows/hardware/ff551693) structure. The DD\_RENDERMOCOMPDATA structure is filled as follows.

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
<td align="left"><p>Zero</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>lpBufferInfo</strong></p></td>
<td align="left"><p>NULL</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>dwFunction</strong></p></td>
<td align="left"><p><strong>DXVA_ProcAmpControlQueryCapsFnCode</strong> constant (defined in <em>dxva.h</em>)</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>lpInputData</strong></p></td>
<td align="left"><p>Pointer to a filled [<strong>DXVA_VideoDesc</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564070) structure.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>lpOutputData</strong></p></td>
<td align="left"><p>Pointer to a [<strong>DXVA_ProcAmpControlCaps</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564019) structure.</p></td>
</tr>
</tbody>
</table>

 

Note that the RenderMoComp function will be called without the display driver-supplied BeginMoCompFrame or EndMoCompFrame function being called first.

**Example Code**

The following code provides an example of how you can implement your *ProcAmpControlQueryCaps* function:

```
HRESULT
DXVA_DeinterlaceContainerDeviceClass::ProcAmpControlQueryCaps(
    LPDXVA_VideoDesc lpVideoDesc,
    LPDXVA_ProcAmpControlCaps lpProcAmpControlCaps
    )
{
    // only the YUY2 and YV12 formats can be operated on
    if (lpVideoDesc->d3dFormat != &#39;2YUY&#39; &amp;&amp;
        lpVideoDesc->d3dFormat != &#39;21VY&#39;) {
        return E_INVALIDARG;
    }
    lpProcAmpControlCaps->InputPool = D3DPOOL_DEFAULT;
    lpProcAmpControlCaps->d3dOutputFormat = lpVideoDesc->d3dFormat;
    lpProcAmpControlCaps->ProcAmpControlProps =
        DXVA_ProcAmp_Brightness |
        DXVA_ProcAmp_Contrast |
        DXVA_ProcAmp_Hue |
        DXVA_ProcAmp_Saturation;
    lpProcAmpControlCaps->VideoProcessingCaps = DXVA_VideoProcess_None;
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


[**DXVA\_VideoDesc**](https://msdn.microsoft.com/library/windows/hardware/ff564070)

[**DXVA\_ProcAmpControlCaps**](https://msdn.microsoft.com/library/windows/hardware/ff564019)

[**DD\_MOTIONCOMPCALLBACKS**](https://msdn.microsoft.com/library/windows/hardware/ff551660)

[**DD\_RENDERMOCOMPDATA**](https://msdn.microsoft.com/library/windows/hardware/ff551693)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20DXVA_DeinterlaceContainerDeviceClass::ProcAmpControlQueryCaps%20method%20%20RELEASE:%20%281/4/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





