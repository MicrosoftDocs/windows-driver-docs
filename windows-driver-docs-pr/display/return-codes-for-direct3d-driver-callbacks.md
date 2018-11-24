---
title: Return Codes for Direct3D Driver Callbacks
description: Return Codes for Direct3D Driver Callbacks
ms.assetid: 033beb6e-5872-4cb3-8f39-459e2fff82cd
keywords:
- Direct3D WDK Windows 2000 display , return codes
- return codes WDK Direct3D
- callbacks WDK Direct3D
- callback functions WDK Direct3D
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Return Codes for Direct3D Driver Callbacks


## <span id="ddk_return_codes_for_direct3d_driver_callbacks_gg"></span><span id="DDK_RETURN_CODES_FOR_DIRECT3D_DRIVER_CALLBACKS_GG"></span>


The following table lists values that can be returned by the [Direct3D Driver-Supplied Functions](https://msdn.microsoft.com/library/windows/hardware/ff552859). The DDHAL\_DRIVER\_*Xxx* values actually are returned in the DWORD return value. The D3D\_OK value, D3DHAL\_*Xxx* values, and D3DERR\_*Xxx* error codes are returned in the **ddrval** member of the structure to which the particular function's parameter points.

For specific error codes that each function can return, see the function and structure descriptions in the reference section. Refer to Direct3D header files *d3d.h* and *d3dhal.h* for a complete listing of error codes and return values (also, *d3d8.h* and *d3d9.h* for DirectX versions 8.0 and 9.0). Note that error codes are represented by negative values and cannot be combined.

A function in a Direct3D driver must return one of the two return codes: DDHAL\_DRIVER\_HANDLED or DDHAL\_DRIVER\_NOTHANDLED. If the driver returns DDHAL\_DRIVER\_HANDLED, then it must also return either D3D\_OK or one of the values listed in *d3d.h* or *d3dhal.h*. A function in a Direct3D driver can return the values in the following table. These values are defined in *d3d.h* and *d3dhal.h*.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Value</th>
<th align="left">Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>D3D_OK (defined as DD_OK)</p></td>
<td align="left"><p>The request completed successfully.</p></td>
</tr>
<tr class="even">
<td align="left"><p>D3DHAL_CONTEXT_BAD</p></td>
<td align="left"><p>The context that was passed in was not valid.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>DDHAL_DRIVER_HANDLED</p></td>
<td align="left"><p>The driver has performed the operation and returned a valid return code for that operation in the <strong>ddrval</strong> member of the structure passed to the driver&#39;s callback. If this code is D3D_OK, Direct3D proceeds with the function. Otherwise, Direct3D returns the error code provided by the driver and aborts the function.</p></td>
</tr>
<tr class="even">
<td align="left"><p>DDHAL_DRIVER_NOTHANDLED</p></td>
<td align="left"><p>The driver has no comment on the requested operation. If the driver is required to have implemented a particular callback, Direct3D reports an error condition. Otherwise, Direct3D handles the operation as if the driver callback had not been defined by executing the Direct3D device-independent implementation. Direct3D typically ignores any value returned in the <strong>ddrval</strong> member of that callback&#39;s parameter structure.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>D3DHAL_OUTOFCONTEXTS</p></td>
<td align="left"><p>There are no more contexts left in this process.</p></td>
</tr>
<tr class="even">
<td align="left"><p>D3DERR_UNSUPPORTEDCOLOROPERATION</p></td>
<td align="left"><p>The color operation is not supported.</p></td>
</tr>
</tbody>
</table>

 

 

 





