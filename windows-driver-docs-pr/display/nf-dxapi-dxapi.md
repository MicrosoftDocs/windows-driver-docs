---
title: DxApi function (dxapi.h)
description: The DxApi function accepts commands from the hardware decoder's video capture driver to access the DxApi interface functions that are implemented in a video miniport driver.
ms.date: 06/05/2024
keywords: ["DxApi function"]
---

# DxApi function

The **DxApi** function accepts commands from the hardware decoder's video capture driver to access the DxApi interface functions that are implemented in a [video miniport driver](video-miniport-drivers-in-the-windows-2000-display-driver-model.md).

## Parameters

* **dwFunctionNum** indicates the behavior of the **DxApi** function (function identifier). See the Remarks section for the list of function identifiers.

* **lpvInBuffer** points to the input buffer.

* **cbInBuffer** indicates the size in bytes of the input buffer.

* **lpvOutBuffer** points to the output buffer.

* **cbOutBuffer** indicates the size in bytes of the output buffer.

## Returns

**DxApi** returns the number of bytes actually written to the output buffer.

## Remarks

**DxApi** accepts a function identifier (**dwFunctionNum**), an input buffer (**lpvInBuffer**) and its size (**cbInBuffer**), and an output buffer (**lpvOutBuffer**) and its size (**cbOutBuffer**). The behavior of the function and the size and format of the input and output buffers depend on the specified function identifier. The return value is the number of actual bytes written into the output buffer.

The following function identifiers are defined for the **DxApi** function in the *ddkmapi.h* header file:

* [**DD_DXAPI_ADDVPCAPTUREBUFFER**](/previous-versions/windows/hardware/drivers/ff550599(v=vs.85))  
* [**DD_DXAPI_CLOSEHANDLE**](/previous-versions/windows/hardware/drivers/ff550606(v=vs.85))  
* [**DD_DXAPI_FLIP_OVERLAY**](/previous-versions/windows/hardware/drivers/ff550612(v=vs.85))  
* [**DD_DXAPI_FLIP_VP**](/previous-versions/windows/hardware/drivers/ff550618(v=vs.85))  
* [**DD_DXAPI_FLUSHVPCAPTUREBUFFERS**](/previous-versions/windows/hardware/drivers/ff550622(v=vs.85))  
* [**DD_DXAPI_GET_CURRENT_VP_AUTOFLIP_SURFACE**](/previous-versions/windows/hardware/drivers/ff550642(v=vs.85))  
* [**DD_DXAPI_GET_LAST_VP_AUTOFLIP_SURFACE**](/previous-versions/windows/hardware/drivers/ff550650(v=vs.85))  
* [**DD_DXAPI_GET_POLARITY**](/previous-versions/windows/hardware/drivers/ff550660(v=vs.85))  
* [**DD_DXAPI_GET_SURFACE_STATE**](/previous-versions/windows/hardware/drivers/ff550673(v=vs.85))  
* [**DD_DXAPI_GET_VP_FIELD_NUMBER**](/previous-versions/windows/hardware/drivers/ff550686(v=vs.85))  
* [**DD_DXAPI_GETKERNELCAPS**](/previous-versions/windows/hardware/drivers/ff550629(v=vs.85))  
* [**DD_DXAPI_GETVERSIONNUMBER**](/previous-versions/windows/hardware/drivers/ff550637(v=vs.85))  
* [**DD_DXAPI_LOCK**](/previous-versions/windows/hardware/drivers/ff550695(v=vs.85))  
* [**DD_DXAPI_OPENDIRECTDRAW**](/previous-versions/windows/hardware/drivers/ff550702(v=vs.85))  
* [**DD_DXAPI_OPENSURFACE**](/previous-versions/windows/hardware/drivers/ff550711(v=vs.85))  
* [**DD_DXAPI_OPENVIDEOPORT**](/previous-versions/windows/hardware/drivers/ff551498(v=vs.85))  
* [**DD_DXAPI_OPENVPCAPTUREDEVICE**](/previous-versions/windows/hardware/drivers/ff551500(v=vs.85))  
* [**DD_DXAPI_REGISTER_CALLBACK**](/previous-versions/windows/hardware/drivers/ff551502(v=vs.85))  
* [**DD_DXAPI_SET_SURFACE_STATE**](/previous-versions/windows/hardware/drivers/ff551504(v=vs.85))  
* [**DD_DXAPI_SET_VP_FIELD_NUMBER**](/previous-versions/windows/hardware/drivers/ff551507(v=vs.85))  
* [**DD_DXAPI_SET_VP_SKIP_FIELD**](/previous-versions/windows/hardware/drivers/ff551510(v=vs.85))  
* [**DD_DXAPI_UNREGISTER_CALLBACK**](/previous-versions/windows/hardware/drivers/ff551514(v=vs.85))  
