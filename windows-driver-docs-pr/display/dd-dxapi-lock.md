---
title: DD_DXAPI_LOCK control code (Windows Drivers)
description: Learn more about the DD_DXAPI_LOCK control code.
keywords:
- DD_DXAPI_LOCK
- ddkmapi/DD_DXAPI_LOCK
ms.date: 10/12/2022
---

# DD\_DXAPI\_LOCK control code

A video capture driver passes DD\_DXAPI\_LOCK in the *dwFunctionNum* parameter of the [**DxApi**](/windows-hardware/drivers/ddi/dxapi/nf-dxapi-dxapi) function to allow the client to access the surface for an indefinite amount of time.

## Input Parameters

- *lpvInBuffer*  
    Pointer to a [**DDLOCKIN**](/windows/win32/api/ddkmapi/ns-ddkmapi-ddlockin) structure that contains the handle information required for the lock.

## Output Parameters

- *lpvOutBuffer*  
    Pointer to a [**DDLOCKOUT**](/windows/win32/api/ddkmapi/ns-ddkmapi-ddlockout) structure that contains the surface information from the surface that is locked.

## Remarks

If the surface ever becomes unusable due to a full-screen command prompt, a resolution change, and so on, the [*pfnSurfaceClose*](/windows/win32/api/ddkmapi/ns-ddkmapi-ddopensurfacein#members) callback specified in the [**DD\_DXAPI\_OPENSURFACE**](dd-dxapi-opensurface.md) function identifier is called to notify the client that it should no longer access this surface.

The **lpSurface** member of DDLOCKOUT contains the pointer that can be used to access the surface. The other members of DDLOCKOUT relate closely to their counterparts in the [**DDSURFACEDESC**](/windows/win32/api/ddraw/ns-ddraw-ddsurfacedesc) structure (**dwSurfWidth** correlates to **dwWidth**, **SurfaceCaps** correlates to **ddsCaps**, **dwFormatFlags** correlates to **ddpfPixelFormat.dwFlags**, and so on).

There is no corresponding Unlock function identifier.

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

[**DD\_DXAPI\_OPENSURFACE**](dd-dxapi-opensurface.md)

[**DDLOCKIN**](/windows/win32/api/ddkmapi/ns-ddkmapi-ddlockin)

[**DDLOCKOUT**](/windows/win32/api/ddkmapi/ns-ddkmapi-ddlockout)

[**DDSURFACEDESC**](/windows/win32/api/ddraw/ns-ddraw-ddsurfacedesc)

[*NotifyCallback*](notify-callback-functions-in-a-video-capture-driver.md)
