---
title: DD_DXAPI_OPENVIDEOPORT Control Code (Windows Drivers)
description: Learn more about the DD_DXAPI_OPENVIDEOPORT control code.
keywords:
- DD_DXAPI_OPENVIDEOPORT
- ddkmapi/DD_DXAPI_OPENVIDEOPORT
ms.date: 10/12/2022
---

# DD\_DXAPI\_OPENVIDEOPORT control code

A video capture driver passes DD\_DXAPI\_OPENVIDEOPORT in the *dwFunctionNum* parameter of the [**DxApi**](/windows-hardware/drivers/ddi/dxapi/nf-dxapi-dxapi) function to notify the kernel-mode video transport that the driver requires a hardware video port.

## Input Parameters

- *lpvInBuffer*  
    Pointer to a [**DDOPENVIDEOPORTIN**](/windows/win32/api/ddkmapi/ns-ddkmapi-ddopenvideoportin) structure that contains the DirectDraw VPE object information.

## Output Parameters

- *lpvOutBuffer*  
    Pointer to a [**DDOPENVIDEOPORTOUT**](/windows/win32/api/ddkmapi/ns-ddkmapi-ddopenvideoportout) structure that contains the new VPE object handle information.

## Remarks

The object is specified by the **dwVideoPortHandle** member of DDOPENVIDEOPORTIN, which is the hardware video port ID specified when the [*VPE*](vpe-callback-functions.md) object was created in user mode. The **hDirectDraw** member of DDOPENVIDEOPORTIN specifies the DirectDraw object with which the video port is associated. The driver must also specify a callback that is called when the VPE object becomes unusable due to it being released at user mode. The **pContext** member of DDOPENVIDEOPORTIN contains a value that is passed if the [*pfnVideoPortClose*](/windows/win32/api/ddkmapi/ns-ddkmapi-ddopenvideoportin#members) callback function is ever called.

If the **ddRVal** member of DDOPENVIDEOPORTOUT is set to DD\_OK, the output from this function identifier is a new DirectDraw surface handle. This new handle must be used on all subsequent calls that reference this VPE object.

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

[**DDOPENVIDEOPORTIN**](/windows/win32/api/ddkmapi/ns-ddkmapi-ddopenvideoportin)

[**DDOPENVIDEOPORTOUT**](/windows/win32/api/ddkmapi/ns-ddkmapi-ddopenvideoportout)

[*NotifyCallback*](notify-callback-functions-in-a-video-capture-driver.md)
