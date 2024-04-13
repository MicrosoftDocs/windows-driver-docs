---
title: DD_DXAPI_GET_VP_FIELD_NUMBER Control Code (Windows Drivers)
description: Learn more about the DD_DXAPI_GET_VP_FIELD_NUMBER control code.
keywords:
- DD_DXAPI_GET_VP_FIELD_NUMBER
- ddkmapi/DD_DXAPI_GET_VP_FIELD_NUMBER
ms.date: 10/12/2022
---

# DD\_DXAPI\_GET\_VP\_FIELD\_NUMBER control code

A video capture driver passes DD\_DXAPI\_GET\_VP\_FIELD\_NUMBER in the *dwFunctionNum* parameter of the [**DxApi**](/windows-hardware/drivers/ddi/dxapi/nf-dxapi-dxapi) function to return the field number of the current hardware video port field.

## Input Parameters

- *lpvInBuffer*  
    Pointer to a [**DDGETFIELDNUMIN**](/windows/win32/api/ddkmapi/ns-ddkmapi-ddgetfieldnumin) structure that contains the required DirectDraw and VPE object handles.

## Output Parameters

- *lpvOutBuffer*  
    Pointer to a [**DDGETFIELDNUMOUT**](/windows/win32/api/ddkmapi/ns-ddkmapi-ddgetfieldnumout) structure that contains the field number.

## Remarks

This function identifier can be used when using the [*VPE*](vpe-callback-functions.md) capture functions, because they also return the field number being captured.

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

[**DDGETFIELDNUMIN**](/windows/win32/api/ddkmapi/ns-ddkmapi-ddgetfieldnumin)

[**DDGETFIELDNUMOUT**](/windows/win32/api/ddkmapi/ns-ddkmapi-ddgetfieldnumout)
