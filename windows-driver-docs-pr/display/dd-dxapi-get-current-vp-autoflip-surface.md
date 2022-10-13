---
title: DD_DXAPI_GET_CURRENT_VP_AUTOFLIP_SURFACE control code (Windows Drivers)
description: Learn more about the DD_DXAPI_GET_CURRENT_VP_AUTOFLIP_SURFACE control code.
keywords:
- DD_DXAPI_GET_CURRENT_VP_AUTOFLIP_SURFACE
- ddkmapi/DD_DXAPI_GET_CURRENT_VP_AUTOFLIP_SURFACE
ms.date: 10/12/2022
---

# DD\_DXAPI\_GET\_CURRENT\_VP\_AUTOFLIP\_SURFACE control code

A video capture driver passes DD\_DXAPI\_GET\_CURRENT\_VP\_AUTOFLIP\_SURFACE in the *dwFunctionNum* parameter of the [**DxApi**](/windows-hardware/drivers/ddi/dxapi/nf-dxapi-dxapi) function to return the surface handles that are receiving the current video and [*VBI*](video-vbi-capture.md) data from the hardware video port.

## Input Parameters

- *lpvInBuffer*  
    Pointer to a [**DDGETAUTOFLIPIN**](/windows/win32/api/ddkmapi/ns-ddkmapi-ddgetautoflipin) structure that contains the required handle information.

## Output Parameters

- *lpvOutBuffer*  
    Pointer to a [**DDGETAUTOFLIPOUT**](/windows/win32/api/ddkmapi/ns-ddkmapi-ddgetautoflipout) structure that contains the surface information and the [*VBI*](video-vbi-capture.md) data from the hardware video port.

## Remarks

An error is returned in the **ddRVal** member of DDGETAUTOFLIPOUT if the hardware video port is not in autoflip mode. This function identifier also returns the polarity of the current field, where the **bPolarity** member of DDGETAUTOFLIPOUT is set to **TRUE** if the current field is the even field of an interlaced video signal.

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

[**DDGETAUTOFLIPIN**](/windows/win32/api/ddkmapi/ns-ddkmapi-ddgetautoflipin)

[**DDGETAUTOFLIPOUT**](/windows/win32/api/ddkmapi/ns-ddkmapi-ddgetautoflipout)
