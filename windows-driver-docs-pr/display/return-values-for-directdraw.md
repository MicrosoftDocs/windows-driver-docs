---
title: Return Values for DirectDraw
description: Return Values for DirectDraw
keywords:
- return values WDK DirectDraw
- drawing WDK DirectDraw , return values
- DirectDraw WDK Windows 2000 display , return values
- errors WDK DirectDraw
ms.date: 04/20/2017
---

# Return Values for DirectDraw

The following tables list values that can be returned by the [DirectDraw driver-supplied functions](windows-2000-driver-initialization.md). The DDHAL_DRIVER_*Xxx* values actually are returned in the DWORD return value. The DD_OK value and DDERR_*Xxx* error codes are returned in the **ddRVal** member of the structure to which the particular function's parameter points.

For specific error codes that each function can return, see the function descriptions in the reference section. Refer to DirectDraw header files *ddraw.h* and *dxmini.h* for a complete listing of error codes and return values. Note that error codes are represented by negative values and cannot be combined.

A function in a DirectDraw driver must return one of the two return codes: DDHAL_DRIVER_HANDLED or DDHAL_DRIVER_NOTHANDLED. If the driver returns DDHAL_DRIVER_HANDLED, then it must also return either DD_OK or one of the error codes listed in *ddraw.h*. A function in a DirectDraw driver can return the codes in the following table. These codes are defined in *ddraw.h*.

| Return code | Meaning |
| ----------- | ------- |
| DD_OK | The request completed successfully. |
| DDHAL_DRIVER_HANDLED | The driver has performed the operation and returned a valid return code for that operation in the **ddrval** member of the structure passed to the driver's callback. If this code is DD_OK, DirectDraw or Direct3D proceeds with the function. Otherwise, DirectDraw or Direct3D returns the error code provided by the driver and aborts the function. |
| DDHAL_DRIVER_NOCKEYHW | The display driver couldn't handle the call because it ran out of color key hardware resources. |
| DDHAL_DRIVER_NOTHANDLED | The driver has no comment on the requested operation. If the driver is required to have implemented a particular callback, DirectDraw or Direct3D reports an error condition. Otherwise, DirectDraw or Direct3D handles the operation as if the driver callback had not been defined by executing the DirectDraw or Direct3D device-independent implementation. DirectDraw and Direct3D typically ignore any value returned in the **ddrval** member of that callback's parameter structure. |
| DDERR_GENERIC | There is an undefined error condition. |
| DDERR_OUTOFCAPS | The hardware needed for the requested operation has already been allocated. |
| DDERR_UNSUPPORTED | The operation is not supported. |

A [DxApi function](dxapi-miniport-driver-functions-for-windows-2000-and-later.md) that is implemented in a [video miniport driver](video-miniport-drivers-in-the-windows-2000-display-driver-model.md) returns one of the codes in the following table. These codes are defined in *dxmini.h*.

| Return code | Meaning |
| ----------- | ------- |
| DX_OK | The request completed successfully. |
| DXERR_GENERIC | There is an undefined error condition. |
| DXERR_OUTOFCAPS | The hardware needed for the requested operation has already been allocated. |
| DXERR_UNSUPPORTED | The operation is not supported. |
