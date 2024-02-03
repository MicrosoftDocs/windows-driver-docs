---
title: DD_DXAPI_GET_POLARITY Control Code (Windows Drivers)
description: Learn more about the DD_DXAPI_GET_POLARITY control code.
keywords:
- DD_DXAPI_GET_POLARITY
- ddkmapi/DD_DXAPI_GET_POLARITY
ms.date: 10/12/2022
---

# DD\_DXAPI\_GET\_POLARITY control code

A video capture driver passes DD\_DXAPI\_GET\_POLARITY in the *dwFunctionNum* parameter of the [**DxApi**](/windows-hardware/drivers/ddi/dxapi/nf-dxapi-dxapi) function to return the polarity of the current hardware video port field.

## Input Parameters

- *lpvInBuffer*  
    Pointer to a [**DDGETPOLARITYIN**](/windows/win32/api/ddkmapi/ns-ddkmapi-ddgetpolarityin) structure that contains the handle information.

## Output Parameters

- *lpvOutBuffer*  
    Pointer to a [**DDGETPOLARITYOUT**](/windows/win32/api/ddkmapi/ns-ddkmapi-ddgetpolarityout) structure that contains the polarity information.

## Remarks

The **bPolarity** member of DDGETPOLARITYOUT is set to **TRUE** if the current field is the even field of an interlaced video signal.

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

[**DDGETPOLARITYIN**](/windows/win32/api/ddkmapi/ns-ddkmapi-ddgetpolarityin)

[**DDGETPOLARITYOUT**](/windows/win32/api/ddkmapi/ns-ddkmapi-ddgetpolarityout)
