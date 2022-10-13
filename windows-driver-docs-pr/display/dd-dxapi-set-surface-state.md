---
title: DD_DXAPI_SET_SURFACE_STATE control code (Windows Drivers)
description: Learn more about the DD_DXAPI_SET_SURFACE_STATE control code.
keywords:
- DD_DXAPI_SET_SURFACE_STATE
- ddkmapi/DD_DXAPI_SET_SURFACE_STATE
ms.date: 10/12/2022
---

# DD\_DXAPI\_SET\_SURFACE\_STATE control code

A video capture driver passes DD\_DXAPI\_SET\_SURFACE\_STATE in the *dwFunctionNum* parameter of the [**DxApi**](/windows-hardware/drivers/ddi/dxapi/nf-dxapi-dxapi) function to switch the overlay surface between bob and weave mode.

## Input Parameters

- *lpvInBuffer*  
    Pointer to a [**DDSETSURFACESTATE**](/windows/win32/api/ddkmapi/ns-ddkmapi-ddsetsurfacestate) structure that contains the requested surface state information.

## Output Parameters

- *lpvOutBuffer*  
    Pointer to a DWORD that contains the DirectDraw return value.

## Remarks

The **dwState** member of DDSETSURFACESTATE contains the new state, which can be either DDSTATE\_BOB or DDSTATE\_WEAVE.

If the surface is associated with a hardware video port, it is possible to indicate that you would like the state change to occur at a future time. In this instance, the **dwStartField** member of DDSETSURFACESTATE indicates the field on which the state change should occur. A value of 0 indicates it should occur at the start of the next field; a value of one indicates the start of the following field, and so on.

This function identifier can be called at raised IRQL.

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

[**DDSETSURFACESTATE**](/windows/win32/api/ddkmapi/ns-ddkmapi-ddsetsurfacestate)
