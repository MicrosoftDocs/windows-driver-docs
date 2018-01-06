---
title: DXVA\_ProcAmpControlDeviceClass ProcAmpControlBlt method
description: The sample ProcAmpControlBlt function performs the ProcAmp adjustment operation by writing the output to the destination surface.
ms.assetid: bf86fd39-554d-4ef1-adb7-202bb70fd3b4
keywords: ["ProcAmpControlBlt method Display Devices", "ProcAmpControlBlt method Display Devices , DXVA_ProcAmpControlDeviceClass interface", "DXVA_ProcAmpControlDeviceClass interface Display Devices , ProcAmpControlBlt method"]
topic_type:
- apiref
api_name:
- DXVA_ProcAmpControlDeviceClass.ProcAmpControlBlt
api_type:
- COM
ms.author: windowsdriverdev
ms.date: 01/05/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# DXVA\_ProcAmpControlDeviceClass::ProcAmpControlBlt method


The sample *ProcAmpControlBlt* function performs the ProcAmp adjustment operation by writing the output to the destination surface.

Syntax
------

```ManagedCPlusPlus
HRESULT ProcAmpControlBlt(
  [in] LPDDSURFACE            lpDDSDstSurface,
  [in] LPDDSURFACE            lpDDSSrcSurface,
  [in] DXVA_ProcAmpControlBlt *ccBlt
);
```

Parameters
----------

*lpDDSDstSurface* \[in\]
Supplies a pointer to the destination surface.

*lpDDSSrcSurface* \[in\]
Supplies a pointer to the source surface.

*ccBlt* \[in\]
Supplies a pointer to a [**DXVA\_ProcAmpControlBlt**](https://msdn.microsoft.com/library/windows/hardware/ff564015) structure that specifies the ProcAmp adjustment data output to the destination surface.

Return value
------------

Returns zero (S\_OK or DD\_OK) if successful; otherwise, returns an error code. Refer to *ddraw.h* for a complete list of error codes.

Remarks
-------

The source and destination rectangles are required for either subrectangle ProcAmp adjustment or stretching. Support for stretching is optional and is reported by the **VideoProcessingCaps** member of the [**DXVA\_ProcAmpControlCaps**](https://msdn.microsoft.com/library/windows/hardware/ff564019) structure. Support for subrectangles is also optional.

The destination surface can be an off-screen plane, a D3D render target, a D3D texture, or a D3D texture that is also a render target. The destination surface will always be allocated in local video memory. The pixel format of the destination surface will be the one indicated in the DXVA\_ProcAmpControlCaps structure, unless a YUV-to-RGB color space conversion is being performed as part of the ProcAmp adjustment procedure. In this case, the destination surface format will be an RGB format with at least 8 bits of precision for each color component.

The sample *ProcAmpControlBlt* function maps directly to a call to the **RenderMoComp** member of the [**DD\_MOTIONCOMPCALLBACKS**](https://msdn.microsoft.com/library/windows/hardware/ff551660) structure. The **RenderMoComp** member points to the driver-supplied *DdMoCompRender* callback that references the [**DD\_RENDERMOCOMPDATA**](https://msdn.microsoft.com/library/windows/hardware/ff551693) structure. The DD\_RENDERMOCOMPDATA structure is filled as follows.

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
<td align="left"><p>Pointer to a [<strong>DXVA_ProcAmpControlBlt</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564015) structure.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>lpOutputData</strong></p></td>
<td align="left"><p>NULL.</p></td>
</tr>
</tbody>
</table>

 

For the DirectX VA device used for ProcAmp control, RenderMoComp is called without calling the display driver-supplied BeginMoCompFrame or EndMoCompFrame function.

## <span id="see_also"></span>See also


[**DXVA\_VideoDesc**](https://msdn.microsoft.com/library/windows/hardware/ff564070)

[**DXVA\_ProcAmpControlCaps**](https://msdn.microsoft.com/library/windows/hardware/ff564019)

[**DXVA\_ProcAmpControlBlt**](https://msdn.microsoft.com/library/windows/hardware/ff564015)

[**DD\_MOTIONCOMPCALLBACKS**](https://msdn.microsoft.com/library/windows/hardware/ff551660)

[**DD\_CREATEMOCOMPDATA**](https://msdn.microsoft.com/library/windows/hardware/ff550529)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20DXVA_ProcAmpControlDeviceClass::ProcAmpControlBlt%20method%20%20RELEASE:%20%281/4/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





