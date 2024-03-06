---
title: DD_DXAPI_UNREGISTER_CALLBACK Control Code (Windows Drivers)
description: Learn more about the DD_DXAPI_UNREGISTER_CALLBACK control code.
keywords:
- DD_DXAPI_UNREGISTER_CALLBACK
- ddkmapi/DD_DXAPI_UNREGISTER_CALLBACK
ms.date: 10/12/2022
---

# DD\_DXAPI\_UNREGISTER\_CALLBACK control code

A video capture driver passes DD\_DXAPI\_UNREGISTER\_CALLBACK in the *dwFunctionNum* parameter of the [**DxApi**](/windows-hardware/drivers/ddi/dxapi/nf-dxapi-dxapi) function to release the registration of a previously-registered callback.

## Input Parameters

- *lpvInBuffer*  
    Pointer to a [**DDREGISTERCALLBACK**](/windows/win32/api/ddkmapi/ns-ddkmapi-ddregistercallback) structure that contains the information required to release a callback.

## Output Parameters

- *lpvOutBuffer*  
    Pointer to a DWORD that contains the DirectDraw return value.

## Remarks

This function identifier can only release one event at a time.

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

[**DDREGISTERCALLBACK**](/windows/win32/api/ddkmapi/ns-ddkmapi-ddregistercallback)
