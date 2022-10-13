---
title: DD_DXAPI_OPENSURFACE control code (Windows Drivers)
description: Learn more about the DD_DXAPI_OPENSURFACE control code.
keywords:
- DD_DXAPI_OPENSURFACE
- ddkmapi/DD_DXAPI_OPENSURFACE
ms.date: 10/12/2022
---

# DD\_DXAPI\_OPENSURFACE control code

A video capture driver passes DD\_DXAPI\_OPENSURFACE in the *dwFunctionNum* parameter of the [**DxApi**](/windows-hardware/drivers/ddi/dxapi/nf-dxapi-dxapi) function to notify the kernel-mode video transport that the driver requires a surface object.

## Input Parameters

- *lpvInBuffer*  
    Pointer to a [**DDOPENSURFACEIN**](/windows/win32/api/ddkmapi/ns-ddkmapi-ddopensurfacein) structure that contains the DirectDrawSurface object information.

## Output Parameters

- *lpvOutBuffer*  
    Pointer to a [**DDOPENSURFACEOUT**](/windows/win32/api/ddkmapi/ns-ddkmapi-ddopensurfaceout) structure that contains the new DirectDrawSurface handle information.

## Remarks

The object is specified by the **dwSurfaceHandle** member of DDOPENSURFACEIN, which is the handle passed down from user mode. The **hDirectDraw** member of DDOPENSURFACEIN specifies the DirectDraw object with which the surface is associated. The driver must also specify a callback that is called when the surface becomes unusable due to it being released at user mode, a full-screen command prompt, or a mode change. The **pContext** member contains a value that is passed if the [*pfnSurfaceClose*](/windows/win32/api/ddkmapi/ns-ddkmapi-ddopensurfacein#members) callback function is ever called.

If the **ddRVal** member of DDOPENSURFACEOUT is set to DD\_OK, the output from this function identifier is a new surface handle. This new handle must be used on all subsequent calls that reference this surface.

This function identifier can only be called from PASSIVE\_LEVEL.

## Requirements

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Header</p></td>
<td>Ddkmapi.h (include Ddkmapi.h)</td>
</tr>
</tbody>
</table>

## See also

[**DDOPENSURFACEIN**](/windows/win32/api/ddkmapi/ns-ddkmapi-ddopensurfacein)

[**DDOPENSURFACEOUT**](/windows/win32/api/ddkmapi/ns-ddkmapi-ddopensurfaceout)

[*NotifyCallback*](notify-callback-functions-in-a-video-capture-driver.md)
