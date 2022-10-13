---
title: DD_DXAPI_OPENDIRECTDRAW control code (Windows Drivers)
description: Learn more about the DD_DXAPI_OPENDIRECTDRAW control code.
keywords:
- IP Helper WDK networking
ms.date: 10/12/2022
---

# DD\_DXAPI\_OPENDIRECTDRAW control code

A video capture driver passes DD\_DXAPI\_OPENDIRECTDRAW in the *dwFunctionNum* parameter of the [**DxApi**](/windows-hardware/drivers/ddi/dxapi/nf-dxapi-dxapi) function to notify the kernel-mode video transport that the driver requires a DirectDraw object.

## Input Parameters

- *lpvInBuffer*  
    Pointer to a [**DDOPENDIRECTDRAWIN**](/windows/win32/api/ddkmapi/ns-ddkmapi-ddopendirectdrawin) structure that contains the DirectDraw handle information.

## Output Parameters

- *lpvOutBuffer*  
    Pointer to a [**DDOPENDIRECTDRAWOUT**](/windows/win32/api/ddkmapi/ns-ddkmapi-ddopendirectdrawout) structure that contains the new DirectDraw handle information.

## Remarks

The object is specified by the **dwDirectDrawHandle** member of DDOPENDIRECTDRAWIN, which is the handle passed down from user mode. The driver must also specify a callback that is called if the DirectDraw object goes away. The **pContext** member of DDOPENDIRECTDRAWIN contains a value that is passed if the [*pfnDirectDrawClose*](/windows/win32/api/ddkmapi/ns-ddkmapi-ddopendirectdrawin#members) callback is ever called.

If the **ddRVal** member of DDOPENDIRECTDRAWOUT is set to DD\_OK, the output from this function identifier is a new DirectDraw handle. This new handle must be used on all subsequent calls that require a DirectDraw handle.

This function identifier can only be called from PASSIVE\_LEVEL.

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

[**DDOPENDIRECTDRAWIN**](/windows/win32/api/ddkmapi/ns-ddkmapi-ddopendirectdrawin)

[**DDOPENDIRECTDRAWOUT**](/windows/win32/api/ddkmapi/ns-ddkmapi-ddopendirectdrawout)

[*NotifyCallback*](notify-callback-functions-in-a-video-capture-driver.md)
