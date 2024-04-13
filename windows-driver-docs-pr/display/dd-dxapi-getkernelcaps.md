---
title: DD_DXAPI_GETKERNELCAPS Control Code (Windows Drivers)
description: Learn more about the DD_DXAPI_GETKERNELCAPS control code.
keywords:
- DD_DXAPI_GETKERNELCAPS
- ddkmapi/DD_DXAPI_GETKERNELCAPS
ms.date: 10/12/2022
---

# DD\_DXAPI\_GETKERNELCAPS control code

A video capture driver passes DD\_DXAPI\_GETKERNELCAPS in the *dwFunctionNum* parameter of the [**DxApi**](/windows-hardware/drivers/ddi/dxapi/nf-dxapi-dxapi) function to return the capabilities of this kernel-mode device.

## Input Parameters

- *lpvInBuffer*  
    Pointer to the DirectDraw handle (HANDLE hDirectDraw;).

## Output Parameters

- *lpvOutBuffer*  
    Pointer to a [**DDGETKERNELCAPSOUT**](/windows/win32/api/ddkmapi/ns-ddkmapi-ddgetkernelcapsout) structure that contains the capabilities of the specified DirectDraw object.

## Remarks

The DirectDraw handle in *lpvInBuffer* specifies the DirectDraw object for which to return the kernel-mode capabilities. The **dwCaps** member of DDGETKERNELCAPSOUT contains the DDKERNELCAPS\_*Xxx* flags and the **dwIRQCaps** member contains the DDIRQ\_*Xxx* flags. These flags are defined in *ddkernel.h*.

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

[**DDGETKERNELCAPSOUT**](/windows/win32/api/ddkmapi/ns-ddkmapi-ddgetkernelcapsout)
