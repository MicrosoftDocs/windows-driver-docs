---
title: DD_DXAPI_OPENVPCAPTUREDEVICE control code (Windows Drivers)
description: Learn more about the DD_DXAPI_OPENVPCAPTUREDEVICE control code.
keywords:
- DD_DXAPI_OPENVPCAPTUREDEVICE
- ddkmapi/DD_DXAPI_OPENVPCAPTUREDEVICE
ms.date: 10/12/2022
---

# DD\_DXAPI\_OPENVPCAPTUREDEVICE control code

A video capture driver passes DD\_DXAPI\_OPENVPCAPTUREDEVICE in the *dwFunctionNum* parameter of the [**DxApi**](/windows-hardware/drivers/ddi/dxapi/nf-dxapi-dxapi) function to open the device for video capture.

## Input Parameters

- *lpvInBuffer*  
    Pointer to a [**DDOPENVPCAPTUREDEVICEIN**](/windows/win32/api/ddkmapi/ns-ddkmapi-ddopenvpcapturedevicein) structure that contains the relevant VPE object information required for the capture.

## Output Parameters

- *lpvOutBuffer*  
    Pointer to a [**DDOPENVPCAPTUREDEVICEOUT**](/windows/win32/api/ddkmapi/ns-ddkmapi-ddopenvpcapturedeviceout) structure that contains the new capture handle.

## Remarks

A [*VPE*](vpe-callback-functions.md) capture device allows hardware video port data to be automatically bus mastered from the surface to a specified buffer. Opening the capture device determines which lines are to be captured. For example, for [*VBI*](video-vbi-capture.md), the capture driver may only be interested in the first 21 lines. If the capture driver wants to capture different regions to different buffers (for example, VBI and video to separate buffers), multiple capture devices can be created.

When a capture device is created, the kernel-mode video transport creates a queue for each device. The driver can later add buffers to this queue. Each time the hardware video port V-sync occurs, the kernel-mode video transport automatically initiates the correct bus masters from the frame buffer surface most recently filled by the hardware video port to the buffer in the queue. If you don't want to capture on every field, you can indicate this by setting the **dwCaptureEveryNFields** member of DDOPENVPCAPTUREDEVICEIN to something other than 1.

The **hDirectDraw** and **hVideoPort** members of DDOPENVPCAPTUREDEVICEIN specify the DirectDraw object and [*VPE*](vpe-callback-functions.md) object from which you want to capture. The **dwStartLine** and **dwEndLine** members indicate which lines are to be captured. The **dwStartLine** member is relative to the start of the surface (0 is the first line) and **dwEndLine** is inclusive (setting **dwStartLine** and **dwEndLine** to 0 causes the first line to be captured).

The driver must also specify a callback that is called when the capture device becomes unusable due to the VPE object being released at user mode. The **pContext** member of DDOPENVPCAPTUREDEVICEIN contains a value that is passed if the [*pfnCaptureClose*](/windows/win32/api/ddkmapi/ns-ddkmapi-ddopenvpcapturedevicein#members) callback function is ever called.

If the **ddRVal** member of DDOPENVPCAPTUREDEVICEOUT is set to DD\_OK, the output from this function identifier is a new DirectDraw capture handle. This new handle must be used on all subsequent calls that reference this capture device.

This function identifier can only be called from PASSIVE\_LEVEL.

## Requirements

<table>
<tbody>
<tr class="odd">
<td><p>Header</p></td>
<td>Ddkmapi.h (include Ddkmapi.h)</td>
</tr>
</tbody>
</table>

## See also

[**DDOPENVPCAPTUREDEVICEIN**](/windows/win32/api/ddkmapi/ns-ddkmapi-ddopenvpcapturedevicein)

[**DDOPENVPCAPTUREDEVICEOUT**](/windows/win32/api/ddkmapi/ns-ddkmapi-ddopenvpcapturedeviceout)

[*NotifyCallback*](notify-callback-functions-in-a-video-capture-driver.md)
