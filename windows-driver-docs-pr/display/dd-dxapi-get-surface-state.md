---
title: DD_DXAPI_GET_SURFACE_STATE control code (Windows Drivers)
description: Learn more about the DD_DXAPI_GET_SURFACE_STATE control code.
keywords:
- DD_DXAPI_GET_SURFACE_STATE
- ddkmapi/DD_DXAPI_GET_SURFACE_STATE
ms.date: 10/12/2022
---

# DD\_DXAPI\_GET\_SURFACE\_STATE control code

A video capture driver passes DD\_DXAPI\_GET\_SURFACE\_STATE in the *dwFunctionNum* parameter of the [**DxApi**](/windows-hardware/drivers/ddi/dxapi/nf-dxapi-dxapi) function to indicate whether the overlay surface is in bob or weave mode and whether it can be put into bob or weave mode.

## Input Parameters

- *lpvInBuffer*  
    Pointer to a [**DDGETSURFACESTATEIN**](/windows/win32/api/ddkmapi/ns-ddkmapi-ddgetsurfacestatein) structure that contains the surface handle.

## Output Parameters

- *lpvOutBuffer*  
    Pointer to a [**DDGETSURFACESTATEOUT**](/windows/win32/api/ddkmapi/ns-ddkmapi-ddgetsurfacestateout) structure that contains the surface capabilities.

## Remarks

The **dwStateCaps** member of DDGETSURFACESTATEOUT returns the surface's capabilities, including DDSTATE\_BOB and DDSTATE\_WEAVE. The **dwStateStatus** member of DDGETSURFACESTATEOUT can return DDSTATE\_BOB, DDSTATE\_WEAVE, DDSTATE\_SOFTWARE\_AUTOFLIP (so the caller can know whether the hardware is using software or hardware autoflipping) and DDSTATE\_EXPLICITLY\_SET (indicating the caller is in this state due to a previous DD\_DXAPI\_SET\_SURFACE\_STATE call).

This function identifier can be called at raised IRQL.

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

[**DDGETSURFACESTATEIN**](/windows/win32/api/ddkmapi/ns-ddkmapi-ddgetsurfacestatein)

[**DDGETSURFACESTATEOUT**](/windows/win32/api/ddkmapi/ns-ddkmapi-ddgetsurfacestateout)
