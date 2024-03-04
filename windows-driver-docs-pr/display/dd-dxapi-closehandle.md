---
title: DD_DXAPI_CLOSEHANDLE Control Code (Windows Drivers)
description: Learn more about the DD_DXAPI_CLOSEHANDLE control code.
keywords:
- DD_DXAPI_CLOSEHANDLE
- ddkmapi/DD_DXAPI_CLOSEHANDLE
ms.date: 10/12/2022
---

# DD\_DXAPI\_CLOSEHANDLE control code

A video capture driver passes DD\_DXAPI\_CLOSEHANDLE in the *dwFunctionNum* parameter of the [**DxApi**](/windows-hardware/drivers/ddi/dxapi/nf-dxapi-dxapi) function to close the kernel-mode handle to the DirectDraw object, surface, VPE object, or VPE capture object.

## Input Parameters

- *lpvInBuffer*  
    Pointer to the [**DDCLOSEHANDLE**](/windows/win32/api/ddkmapi/ns-ddkmapi-ddclosehandle) structure that contains the appropriate handle.

## Output Parameters

- *lpvOutBuffer*  
    Pointer to a DWORD that contains the DirectDraw return value.

## Remarks

Calling this function identifier does not cause the corresponding close routines to be called.

This function identifier can only be called at PASSIVE\_LEVEL.

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

[**DDCLOSEHANDLE**](/windows/win32/api/ddkmapi/ns-ddkmapi-ddclosehandle)
