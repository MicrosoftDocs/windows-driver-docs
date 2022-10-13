---
title: DD_DXAPI_GETVERSIONNUMBER control code (Windows Drivers)
description: Learn more about the DD_DXAPI_GETVERSIONNUMBER control code.
keywords:
- DD_DXAPI_GETVERSIONNUMBER
- ddkmapi/DD_DXAPI_GETVERSIONNUMBER
ms.date: 10/12/2022
---

# DD\_DXAPI\_GETVERSIONNUMBER control code

A video capture driver passes DD\_DXAPI\_GETVERSIONNUMBER in the *dwFunctionNum* parameter of the [**DxApi**](/windows-hardware/drivers/ddi/dxapi/nf-dxapi-dxapi) function to return the version of the kernel-mode video transport (*dxapi.sys*) that is supported by the [video miniport driver](video-miniport-drivers-in-the-windows-2000-display-driver-model.md)'s [DxApi interface](/windows/win32/api/dxmini/ns-dxmini-dxapi_interface).

## Input Parameters

- *lpvInBuffer*  
    Is **NULL**.

## Output Parameters

- *lpvOutBuffer*  
    Pointer to a [**DDGETVERSIONNUMBER**](/windows/win32/api/ddkmapi/ns-ddkmapi-ddgetversionnumber) structure that contains the version number of the kernel-mode video transport component of DirectDraw.

## Remarks

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

[**DDGETVERSIONNUMBER**](/windows/win32/api/ddkmapi/ns-ddkmapi-ddgetversionnumber)
