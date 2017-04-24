---
title: Return Codes for Direct3D Driver Callbacks
description: Return Codes for Direct3D Driver Callbacks
ms.assetid: 033beb6e-5872-4cb3-8f39-459e2fff82cd
keywords:
- Direct3D WDK Windows 2000 display , return codes
- return codes WDK Direct3D
- callbacks WDK Direct3D
- callback functions WDK Direct3D
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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
<td align="left"><p>The driver has performed the operation and returned a valid return code for that operation in the <strong>ddrval</strong> member of the structure passed to the driver's callback. If this code is D3D_OK, Direct3D proceeds with the function. Otherwise, Direct3D returns the error code provided by the driver and aborts the function.</p></td>
</tr>
<tr class="even">
<td align="left"><p>DDHAL_DRIVER_NOTHANDLED</p></td>
<td align="left"><p>The driver has no comment on the requested operation. If the driver is required to have implemented a particular callback, Direct3D reports an error condition. Otherwise, Direct3D handles the operation as if the driver callback had not been defined by executing the Direct3D device-independent implementation. Direct3D typically ignores any value returned in the <strong>ddrval</strong> member of that callback's parameter structure.</p></td>
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

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Return%20Codes%20for%20Direct3D%20Driver%20Callbacks%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




