---
title: Return Values for DirectDraw
description: Return Values for DirectDraw
ms.assetid: da4cc7d7-6826-48aa-96c6-004e31fc3e3e
keywords:
- return values WDK DirectDraw
- drawing WDK DirectDraw , return values
- DirectDraw WDK Windows 2000 display , return values
- errors WDK DirectDraw
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Return Values for DirectDraw


## <span id="ddk_return_values_for_directdraw_gg"></span><span id="DDK_RETURN_VALUES_FOR_DIRECTDRAW_GG"></span>


The following tables list values that can be returned by the [DirectDraw driver-supplied functions](https://msdn.microsoft.com/library/windows/hardware/ff553833). The DDHAL\_DRIVER\_*Xxx* values actually are returned in the DWORD return value. The DD\_OK value and DDERR\_*Xxx* error codes are returned in the **ddRVal** member of the structure to which the particular function's parameter points.

For specific error codes that each function can return, see the function descriptions in the reference section. Refer to DirectDraw header files *ddraw.h* and *dxmini.h* for a complete listing of error codes and return values. Note that error codes are represented by negative values and cannot be combined.

A function in a DirectDraw driver must return one of the two return codes: DDHAL\_DRIVER\_HANDLED or DDHAL\_DRIVER\_NOTHANDLED. If the driver returns DDHAL\_DRIVER\_HANDLED, then it must also return either DD\_OK or one of the error codes listed in *ddraw.h*. A function in a DirectDraw driver can return the codes in the following table. These codes are defined in *ddraw.h*.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Return Code</th>
<th align="left">Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>DD_OK</p></td>
<td align="left"><p>The request completed successfully.</p></td>
</tr>
<tr class="even">
<td align="left"><p>DDHAL_DRIVER_HANDLED</p></td>
<td align="left"><p>The driver has performed the operation and returned a valid return code for that operation in the <strong>ddrval</strong> member of the structure passed to the driver&#39;s callback. If this code is DD_OK, DirectDraw or Direct3D proceeds with the function. Otherwise, DirectDraw or Direct3D returns the error code provided by the driver and aborts the function.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>DDHAL_DRIVER_NOCKEYHW</p></td>
<td align="left"><p>The display driver couldn&#39;t handle the call because it ran out of color key hardware resources.</p></td>
</tr>
<tr class="even">
<td align="left"><p>DDHAL_DRIVER_NOTHANDLED</p></td>
<td align="left"><p>The driver has no comment on the requested operation. If the driver is required to have implemented a particular callback, DirectDraw or Direct3D reports an error condition. Otherwise, DirectDraw or Direct3D handles the operation as if the driver callback had not been defined by executing the DirectDraw or Direct3D device-independent implementation. DirectDraw and Direct3D typically ignore any value returned in the <strong>ddrval</strong> member of that callback&#39;s parameter structure.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>DDERR_GENERIC</p></td>
<td align="left"><p>There is an undefined error condition.</p></td>
</tr>
<tr class="even">
<td align="left"><p>DDERR_OUTOFCAPS</p></td>
<td align="left"><p>The hardware needed for the requested operation has already been allocated.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>DDERR_UNSUPPORTED</p></td>
<td align="left"><p>The operation is not supported.</p></td>
</tr>
</tbody>
</table>

 

A [DxApi function](https://msdn.microsoft.com/library/windows/hardware/ff557387) that is implemented in a [video miniport driver](video-miniport-drivers-in-the-windows-2000-display-driver-model.md) returns one of the codes in the following table. These codes are defined in *dxmini.h*.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Return Code</th>
<th align="left">Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>DX_OK</p></td>
<td align="left"><p>The request completed successfully.</p></td>
</tr>
<tr class="even">
<td align="left"><p>DXERR_GENERIC</p></td>
<td align="left"><p>There is an undefined error condition.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>DXERR_OUTOFCAPS</p></td>
<td align="left"><p>The hardware needed for the requested operation has already been allocated.</p></td>
</tr>
<tr class="even">
<td align="left"><p>DXERR_UNSUPPORTED</p></td>
<td align="left"><p>The operation is not supported.</p></td>
</tr>
</tbody>
</table>

 

 

 





