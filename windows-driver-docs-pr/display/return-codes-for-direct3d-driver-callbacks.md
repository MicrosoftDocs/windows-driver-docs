---
title: Return Codes for Direct3D Driver Callbacks
description: Return Codes for Direct3D Driver Callbacks
keywords:
- Direct3D WDK Windows 2000 display , return codes
- return codes WDK Direct3D
- callbacks WDK Direct3D
- callback functions WDK Direct3D
ms.date: 04/20/2017
---

# Return Codes for Direct3D Driver Callbacks

The following table lists values that can be returned by the [Direct3D Driver-Supplied Functions](driver-functions-to-support-direct3d.md). The DDHAL_DRIVER_*Xxx* values actually are returned in the DWORD return value. The D3D_OK value, D3DHAL_*Xxx* values, and D3DERR_*Xxx* error codes are returned in the **ddrval** member of the structure to which the particular function's parameter points.

For specific error codes that each function can return, see the function and structure descriptions in the reference section. Refer to Direct3D header files *d3d.h* and *d3dhal.h* for a complete listing of error codes and return values (also, *d3d8.h* and *d3d9.h* for DirectX versions 8.0 and 9.0). Note that error codes are represented by negative values and cannot be combined.

A function in a Direct3D driver must return one of the two return codes: DDHAL_DRIVER_HANDLED or DDHAL_DRIVER_NOTHANDLED. If the driver returns DDHAL_DRIVER_HANDLED, then it must also return either D3D_OK or one of the values listed in *d3d.h* or *d3dhal.h*. A function in a Direct3D driver can return the values in the following table. These values are defined in *d3d.h* and *d3dhal.h*.

| Value | Meaning |
| ----- | ------- |
| D3D_OK (defined as DD_OK) | The request completed successfully. |
| D3DHAL_CONTEXT_BAD | The context that was passed in was not valid. |
| DDHAL_DRIVER_HANDLED | The driver has performed the operation and returned a valid return code for that operation in the **ddrval** member of the structure passed to the driver's callback. If this code is D3D_OK, Direct3D proceeds with the function. Otherwise, Direct3D returns the error code provided by the driver and aborts the function. |
| DDHAL_DRIVER_NOTHANDLED | The driver has no comment on the requested operation. If the driver is required to have implemented a particular callback, Direct3D reports an error condition. Otherwise, Direct3D handles the operation as if the driver callback had not been defined by executing the Direct3D device-independent implementation. Direct3D typically ignores any value returned in the **ddrval** member of that callback's parameter structure. |
| D3DHAL_OUTOFCONTEXTS | There are no more contexts left in this process. |
| D3DERR_UNSUPPORTEDCOLOROPERATION | The color operation is not supported. |
