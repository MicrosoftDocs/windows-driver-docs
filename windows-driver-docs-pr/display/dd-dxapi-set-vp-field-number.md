---
title: DD_DXAPI_SET_VP_FIELD_NUMBER Control Code (Windows Drivers)
description: Learn more about the DD_DXAPI_SET_VP_FIELD_NUMBER control code.
keywords:
- DD_DXAPI_SET_VP_FIELD_NUMBER
- ddkmapi/DD_DXAPI_SET_VP_FIELD_NUMBER
ms.date: 10/12/2022
---

# DD\_DXAPI\_SET\_VP\_FIELD\_NUMBER control code

A video capture driver passes DD\_DXAPI\_SET\_VP\_FIELD\_NUMBER in the *dwFunctionNum* parameter of the [**DxApi**](/windows-hardware/drivers/ddi/dxapi/nf-dxapi-dxapi) function to set the internal field number for the specified [*VPE*](vpe-callback-functions.md) object to the specified value.

## Input Parameters

- *lpvInBuffer*  
    Pointer to a [**DDSETFIELDNUM**](/windows/win32/api/ddkmapi/ns-ddkmapi-ddsetfieldnum) structure that specifies the appropriate handles and the field number to be set.

## Output Parameters

- *lpvOutBuffer*  
    Pointer to a DWORD that contains the DirectDraw return value.

## Remarks

The internal field number is returned using the [**DD\_DXAPI\_GET\_VP\_FIELD\_NUMBER**](dd-dxapi-get-vp-field-number.md) and [**DD\_DXAPI\_ADDVPCAPTUREBUFFER**](dd-dxapi-addvpcapturebuffer.md) function identifiers.

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

[**DD\_DXAPI\_ADDVPCAPTUREBUFFER**](dd-dxapi-addvpcapturebuffer.md)

[**DD\_DXAPI\_GET\_VP\_FIELD\_NUMBER**](dd-dxapi-get-vp-field-number.md)

[**DDSETFIELDNUM**](/windows/win32/api/ddkmapi/ns-ddkmapi-ddsetfieldnum)
