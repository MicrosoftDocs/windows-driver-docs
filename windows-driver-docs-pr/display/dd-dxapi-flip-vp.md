---
title: DD_DXAPI_FLIP_VP control code (Windows Drivers)
description: Learn more about the DD_DXAPI_FLIP_VP control code.
keywords:
- DD_DXAPI_FLIP_VP
- ddkmapi/DD_DXAPI_FLIP_VP
ms.date: 10/12/2022
---

# DD\_DXAPI\_FLIP\_VP control code

A video capture driver passes DD\_DXAPI\_FLIP\_VP in the *dwFunctionNum* parameter of the [**DxApi**](/windows-hardware/drivers/ddi/dxapi/nf-dxapi-dxapi) function to cause the hardware video port to write data to a different surface.

## Input Parameters

- *lpvInBuffer*  
    Pointer to a [**DDFLIPVIDEOPORT**](/windows/win32/api/ddkmapi/ns-ddkmapi-ddflipvideoport) structure that contains the handle information required to flip the hardware video port.

## Output Parameters

- *lpvOutBuffer*  
    Pointer to a DWORD that contains the DirectDraw return value.

## Remarks

The **dwFlags** member of the DDFLIPVIDEOPORT structure should contain DDVPFLIP\_VIDEO or DDVPFLIP\_VBI to indicate whether the video or the [*VBI*](video-vbi-capture.md) region of the video signal should be flipped. To flip both regions, this function identifier should be called twice.

This function identifier cannot be called while autoflipping.

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

[**DDFLIPVIDEOPORT**](/windows/win32/api/ddkmapi/ns-ddkmapi-ddflipvideoport)
