---
title: DD_DXAPI_FLIP_OVERLAY control code (Windows Drivers)
description: Learn more about the DD_DXAPI_FLIP_OVERLAY control code.
keywords:
- DD_DXAPI_FLIP_OVERLAY
- ddkmapi/DD_DXAPI_FLIP_OVERLAY
ms.date: 10/12/2022
---

# DD\_DXAPI\_FLIP\_OVERLAY control code

A video capture driver passes DD\_DXAPI\_FLIP\_OVERLAY in the *dwFunctionNum* parameter of the [**DxApi**](/windows-hardware/drivers/ddi/dxapi/nf-dxapi-dxapi) function to flip the overlay to display the other surface.

## Input Parameters

- *lpvInBuffer*  
    Pointer to a [**DDFLIPOVERLAY**](/windows/win32/api/ddkmapi/ns-ddkmapi-ddflipoverlay) structure that contains the surface information required for the flip.

## Output Parameters

- *lpvOutBuffer*  
    Pointer to a DWORD that contains the DirectDraw return value.

## Remarks

This call does not rotate the memory pointers as does the user-mode **DdFlip** function, so it is up to the client to keep track of which surface is visible and which is not. The **dwFlags** member of the DDFLIPOVERLAY structure can contain DDFLIP\_EVEN or DDFLIP\_ODD to accommodate bob mode when not using a hardware video port. If the overlay is associated with a hardware video port, the hardware video port is not automatically flipped. This function identifier cannot be called while autoflipping.

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

[**DDFLIPOVERLAY**](/windows/win32/api/ddkmapi/ns-ddkmapi-ddflipoverlay)
