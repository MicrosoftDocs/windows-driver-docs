---
title: DD_DXAPI_GET_LAST_VP_AUTOFLIP_SURFACE control code (Windows Drivers)
description: Learn more about the DD_DXAPI_GET_LAST_VP_AUTOFLIP_SURFACE control code.
keywords:
- DD_DXAPI_GET_LAST_VP_AUTOFLIP_SURFACE
- ddkmapi/DD_DXAPI_GET_LAST_VP_AUTOFLIP_SURFACE
ms.date: 10/12/2022
---

# DD\_DXAPI\_GET\_LAST\_VP\_AUTOFLIP\_SURFACE control code

A video capture driver passes DD\_DXAPI\_GET\_LAST\_VP\_AUTOFLIP\_SURFACE in the *dwFunctionNum* parameter of the [**DxApi**](/windows-hardware/drivers/ddi/dxapi/nf-dxapi-dxapi) function to return the surface handles that received the most recent field of data written to the frame buffer (taking field skipping into account).

## Input Parameters

- *lpvInBuffer*  
    Pointer to a [**DDGETAUTOFLIPIN**](/windows/win32/api/ddkmapi/ns-ddkmapi-ddgetautoflipin) structure that contains the required handle information.

## Output Parameters

- *lpvOutBuffer*  
    Pointer to a [**DDGETAUTOFLIPOUT**](/windows/win32/api/ddkmapi/ns-ddkmapi-ddgetautoflipout) structure that contains the surface information and the [*VBI*](video-vbi-capture.md) data from the hardware video port.

## Remarks

The surfaces returned by this function identifier may be the same surfaces that are receiving the current field if the hardware video port is interleaving the data. This function identifier also returns the polarity of the field most recently written to the frame buffer, where the **bPolarity** member of DDGETAUTOFLIPOUT is set to **TRUE** if the field was the even field of an interlaced video signal. An error is returned in the **ddRVal** member of DDGETAUTOFLIPOUT if the hardware video port is not in autoflip mode.

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

[**DDGETAUTOFLIPIN**](/windows/win32/api/ddkmapi/ns-ddkmapi-ddgetautoflipin)

[**DDGETAUTOFLIPOUT**](/windows/win32/api/ddkmapi/ns-ddkmapi-ddgetautoflipout)
