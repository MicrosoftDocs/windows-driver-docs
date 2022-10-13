---
title: DD_DXAPI_REGISTER_CALLBACK control code (Windows Drivers)
description: Learn more about the DD_DXAPI_REGISTER_CALLBACK control code.
keywords:
- DD_DXAPI_REGISTER_CALLBACK
- ddkmapi/DD_DXAPI_REGISTER_CALLBACK
ms.date: 10/12/2022
---

# DD\_DXAPI\_REGISTER\_CALLBACK control code

A video capture driver passes DD\_DXAPI\_REGISTER\_CALLBACK in the *dwFunctionNum* parameter of the [**DxApi**](/windows-hardware/drivers/ddi/dxapi/nf-dxapi-dxapi) function to register a callback that is called when an event occurs.

## Input Parameters

- *lpvInBuffer*  
    Pointer to a [**DDREGISTERCALLBACK**](/windows/win32/api/ddkmapi/ns-ddkmapi-ddregistercallback) structure that contains the information required to register a callback.

## Output Parameters

- *lpvOutBuffer*  
    Pointer to a DWORD that contains the DirectDraw return value.

## Remarks

This function identifier can only register a single event at a time. If the client wants to be called for multiple events, it must call DD\_DXAPI\_REGISTER\_CALLBACK multiple times.

The IRQ events are actually called at IRQ time, so the callback function must return quickly and only perform calls that are safe.

The **pContext** member of DDREGISTERCALLBACK contains client data that is passed back to the client when the [*pfnDirectDrawClose*](/windows/win32/api/ddkmapi/ns-ddkmapi-ddopendirectdrawin#members) callback is called.

This function identifier can only be called from PASSIVE\_LEVEL.

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

[*NotifyCallback*](notify-callback-functions-in-a-video-capture-driver.md)
