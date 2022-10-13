---
title: DD_DXAPI_SET_VP_SKIP_FIELD control code (Windows Drivers)
description: Learn more about the DD_DXAPI_SET_VP_SKIP_FIELD control code.
keywords:
- DD_DXAPI_SET_VP_SKIP_FIELD
- ddkmapi/DD_DXAPI_SET_VP_SKIP_FIELD
ms.date: 10/12/2022
---

# DD\_DXAPI\_SET\_VP\_SKIP\_FIELD control code

A video capture driver passes DD\_DXAPI\_SET\_VP\_SKIP\_FIELD in the *dwFunctionNum* parameter of the [**DxApi**](/windows-hardware/drivers/ddi/dxapi/nf-dxapi-dxapi) function to indicate that the hardware video port should not write a future field into the frame buffer.

## Input Parameters

- *lpvInBuffer*  
    Pointer to a [**DDSETSKIPFIELD**](/windows/win32/api/ddkmapi/ns-ddkmapi-ddsetskipfield) structure that contains the [*VPE*](vpe-callback-functions.md) object information and the number of the start field.

## Output Parameters

- *lpvOutBuffer*  
    Pointer to a DWORD that contains the DirectDraw return value.

## Remarks

Skipping a field is useful primarily for undoing the 3:2 pattern often introduced in some video content.

This function identifier only skips a single field and must be called explicitly for each field that needs to be skipped. If [*VBI*](video-vbi-capture.md) data is present in the field, the VBI portion if the data is not skipped.

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

[**DDSETSKIPFIELD**](/windows/win32/api/ddkmapi/ns-ddkmapi-ddsetskipfield)
