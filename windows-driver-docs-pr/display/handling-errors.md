---
title: Handling Errors
description: Handling Errors
ms.assetid: ac4e056e-3304-4934-887a-5cc2b87989bd
---

# Handling Errors


The [Direct3D version 10 functions](https://msdn.microsoft.com/library/windows/hardware/ff552909) that a user-mode display driver implements typically have VOID for a return parameter type. The primary exception to this rule is the *CalcPrivate***ObjType***Size*-type function (for example, the [**CalcPrivateResourceSize**](https://msdn.microsoft.com/library/windows/hardware/ff538302) function). This type of function returns a SIZE\_T parameter type that indicates the size of the memory region that the driver requires for creating the particular object type through the *Create***ObjType**-type function (for example, [**CreateResource(D3D10)**](https://msdn.microsoft.com/library/windows/hardware/ff540691)).

Returning VOID prevents the user-mode display driver from notifying the Direct3D runtime of errors in the conventional way (that is, through a user-mode display driver's function return parameter). Instead, the user-mode display driver must use the Direct3D runtime's [**pfnSetErrorCb**](https://msdn.microsoft.com/library/windows/hardware/ff568929) callback function to pass such information back to the runtime. The runtime supplies a pointer to its **pfnSetErrorCb** in the [**D3D10DDI\_CORELAYER\_DEVICECALLBACKS**](https://msdn.microsoft.com/library/windows/hardware/ff541820) structure that the **pUMCallbacks** member of the [**D3D10DDIARG\_CREATEDEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff541664) structure points to in a call to the [**CreateDevice(D3D10)**](https://msdn.microsoft.com/library/windows/hardware/ff540635) function.

The reference page for each user-mode display driver function specifies the errors that the function can pass through a call to **pfnSetErrorCb**. This means that if the user-mode display driver calls **pfnSetErrorCb** with an error code that is not allowed for the current user-mode display driver function, the runtime determines that the error condition is critical and acts appropriately. Because the runtime will act appropriately during **pfnSetErrorCb**, you should not expect that you can reverse the effects of calling **pfnSetErrorCb**( E\_FAIL ) by calling something like **pfnSetErrorCb**( S\_OK ). In fact, the runtime determines that S\_OK is just as invalid or critical as E\_FAIL. The concept of an S\_OK return code is equivalent to the user-mode display driver function not calling **pfnSetErrorCb** at all.

If the Direct3D runtime determines that an error condition is critical, it will first take action by logging the error with Dr. Watson--the default post-mortem (just-in-time) debugger. The runtime will then lose the device on purpose, thereby emulating the scenario of receiving the D3DDDIERR\_DEVICEREMOVED error code. By requiring the driver to call the [**pfnSetErrorCb**](https://msdn.microsoft.com/library/windows/hardware/ff568929) callback function, the odds are much greater that every error coming out of the driver will have a useful call stack associated with it. Having a call stack associated with an error enables quick diagnosis and accurate Dr. Watson logs.

You should use [**pfnSetErrorCb**](https://msdn.microsoft.com/library/windows/hardware/ff568929) in your driver code when something goes wrong in your driver even though returning an error code that the runtime does not allow for the particular driver function is determined by the runtime as a driver bug or issue. It would be even worse for the user-mode display driver to absorb critical errors and continue on. The user-mode display driver should call **pfnSetErrorCb** as close to the point of the error detection as possible to provide a useful call stack for post-mortem debugging.

The following table lists the categories of errors that the Direct3D runtime allows from particular driver functions.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Error category</th>
<th align="left">Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>NoErrors</p></td>
<td align="left"><p>The driver should not encounter any errors, including D3DDDIERR_DEVICEREMOVED. The runtime will determine that any call to [<strong>pfnSetErrorCb</strong>](https://msdn.microsoft.com/library/windows/hardware/ff568929) is critical.</p></td>
</tr>
<tr class="even">
<td align="left"><p>AllowDeviceRemoved</p></td>
<td align="left"><p>The driver should not encounter any errors, except for D3DDDIERR_DEVICEREMOVED. The runtime will determine that any call to <strong>pfnSetErrorCb</strong> that does not pass D3DDDIERR_DEVICEREMOVED is critical. The driver is not required to return DEVICEREMOVED if the device has been removed. However, the runtime allows the driver to return DEVICEREMOVED, in case DEVICEREMOVED interfered with the driver function, which typically should not happen.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>AllowOutOfMemory</p></td>
<td align="left"><p>The driver can possibly run out of memory. Therefore, the driver can pass E_OUTOFMEMORY and D3DDDIERR_DEVICEREMOVED through <strong>pfnSetErrorCb</strong>. The runtime will determine that any other error codes are critical.</p></td>
</tr>
<tr class="even">
<td align="left"><p>AllowCounterCreationErrors</p></td>
<td align="left"><p>The driver can possibly run out of memory. The driver also might be unable to create counters due to the exclusive nature of counters. Therefore, the driver can pass E_OUTOFMEMORY, DXGI_DDI_ERR_NONEXCLUSIVE, and D3DDDIERR_DEVICEREMOVED through <strong>pfnSetErrorCb</strong>. The runtime will determine that any other error codes are critical.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>AllowMapErrors</p></td>
<td align="left"><p>The driver should check for resource contention. Therefore, the driver can pass DXGI_DDI_ERR_WASSTILLDRAWING through <strong>pfnSetErrorCb</strong> if the D3D10_DDI_MAP_FLAG_DONOTWAIT flag was passed into the driver's [<strong>ResourceMap</strong>](https://msdn.microsoft.com/library/windows/hardware/ff569492) function. The driver can also pass D3DDDIERR_DEVICEREMOVED through <strong>pfnSetErrorCb</strong>. The runtime will determine that any other error codes are critical.</p></td>
</tr>
<tr class="even">
<td align="left"><p>AllowGetDataErrors</p></td>
<td align="left"><p>The driver should check for query completion. Therefore, the driver can pass DXGI_DDI_ERR_WASSTILLDRAWING through <strong>pfnSetErrorCb</strong> if the query has not finished yet. The driver can also pass D3DDDIERR_DEVICEREMOVED through <strong>pfnSetErrorCb</strong>. The runtime will determine that any other error codes are critical.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>AllowWKCheckCounterErrors</p></td>
<td align="left"><p>The driver's [<strong>CheckCounter</strong>](https://msdn.microsoft.com/library/windows/hardware/ff539385) function should indicate whether it supports any runtime-defined counters. Therefore, the driver can pass DXGI_DDI_ERR_UNSUPPORTED through <strong>pfnSetErrorCb</strong>. The runtime will determine that any other error codes are critical.</p>
<p>The driver cannot return D3DDDIERR_DEVICEREMOVED for any check-type function.</p></td>
</tr>
<tr class="even">
<td align="left"><p>AllowDDCheckCounterErrors</p></td>
<td align="left"><p>The driver should validate the device-dependent counter identifier (counter ID) to ensure that the counter ID is within range and there is enough room to copy each counter string into the provided buffer. The driver can pass E_INVALIDARG through <strong>pfnSetErrorCb</strong>, when the parameters are incorrect in this way.</p>
<p>The driver cannot return D3DDDIERR_DEVICEREMOVED for any check-type function.</p></td>
</tr>
</tbody>
</table>

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Handling%20Errors%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




