---
title: Supporting Threading, Command Lists, and 3-D Pipeline
description: Supporting Threading, Command Lists, and 3-D Pipeline
keywords:
- Direct3D version 11 WDK Windows 7 display , threading support
- Direct3D version 11 WDK Windows Server 2008 R2 display , threading support
- Direct3D version 11 WDK Windows 7 display , command lists support
- Direct3D version 11 WDK Windows Server 2008 R2 display , command lists support
- Direct3D version 11 WDK Windows 7 display , 3-D pipeline support
- Direct3D version 11 WDK Windows Server 2008 R2 display , 3-D pipeline support
- threading support for Direct3D version 11 WDK Windows 7 display
- threading support for Direct3D version 11 WDK Windows Server 2008 R2 display
- command lists support for Direct3D version 11 WDK Windows 7 display
- tcommand lists support for Direct3D version 11 WDK Windows Server 2008 R2 display
- pipeline support for Direct3D version 11 WDK Windows 7 display
- pipeline support for Direct3D version 11 WDK Windows Server 2008 R2 display
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Supporting Threading, Command Lists, and 3-D Pipeline

This section applies only to Windows 7 and later, and Windows Server 2008 R2 and later versions of Windows operating system.

A user-mode display driver indicates the new Direct3D version 11 capabilities that it supports (for example, threading, command lists, and 3-D pipeline) when the Direct3D version 11 runtime calls the driver's [**GetCaps(D3D10_2)**](/windows-hardware/drivers/ddi/d3d10umddi/nc-d3d10umddi-pfnd3d10_2ddi_getcaps) function. *GetCaps(D3D10_2)* is one of the driver's adapter-specific functions that the driver provides in the [**D3D10_2DDI_ADAPTERFUNCS**](/windows-hardware/drivers/ddi/d3d10umddi/ns-d3d10umddi-d3d10_2ddi_adapterfuncs) structure that the **pAdapterFuncs_2** member of the [**D3D10DDIARG_OPENADAPTER**](/windows-hardware/drivers/ddi/d3d10umddi/ns-d3d10umddi-d3d10ddiarg_openadapter) structure points to. For more information about providing adapter-specific functions during driver initialization, see [Initializing Communication with the Direct3D Version 11 DDI](initializing-communication-with-the-direct3d-version-11-ddi.md). When its **GetCaps(D3D10_2)** function is called, the user-mode display driver provides new Direct3D version 11 capabilities based on the request type (which is specified in the **Type** member of the [**D3D10_2DDIARG_GETCAPS**](/windows-hardware/drivers/ddi/d3d10umddi/ns-d3d10umddi-d3d10_2ddiarg_getcaps) structure that the *GetCaps(D3D10_2)* function's *pData* parameter points to).

## Threading and Command Lists

The Direct3D version 11 API requires a mode of operation where it can synchronize the application threads to ensure that only one of the threads runs in the DDI at a time. The Direct3D version 11 API also requires a mode of operation with a software emulation of command lists. These modes of operation are required by and leveraged on prior-version DDIs (such as, the Direct3D version 10 DDI). Therefore, as a development aid for driver writers, these same modes of operation are extended to exist on the Direct3D version 11 DDI. Driver writers can decide which modes of operations they would like their drivers to support for the Direct3D version 11 DDI.

All drivers should eventually fully support all types of threading operations (that is, all drivers should eventually support all the threading capabilities of the [**D3D11DDI_THREADING_CAPS**](/windows-hardware/drivers/ddi/d3d10umddi/ns-d3d10umddi-d3d11ddi_threading_caps) structure). However, the driver can require that the API emulate command lists or enforce a single-threaded mode of operation for the driver. The API must be aware of the driver's threading capabilities during the creation of an API device, but before the creation of a DDI device. Therefore, the runtime determines the driver's threading capabilities when it calls the driver's [**GetCaps(D3D10_2)**](/windows-hardware/drivers/ddi/d3d10umddi/nc-d3d10umddi-pfnd3d10_2ddi_getcaps) adapter-specific function with the **Type** member of [**D3D10_2DDIARG_GETCAPS**](/windows-hardware/drivers/ddi/d3d10umddi/ns-d3d10umddi-d3d10_2ddiarg_getcaps) set to D3D11DDICAPS_THREADING. The driver returns a pointer to a **D3D11DDI_THREADING_CAPS** structure in the **pData** member of D3D10_2DDIARG_GETCAPS that identifies the driver's threading capabilities. The driver must support free-threaded mode (D3D11DDICAPS_FREETHREADED) if the driver also supports command lists (D3D11DDICAPS_COMMANDLISTS_BUILD_2) because command lists build on free-threaded mode. The driver must opt-in to support the free-threaded mode and command lists. The application can determine the support that the driver indicated through the use of the application-level **CheckFeatureSupport** function and the D3D11_FEATURE_THREADING constant; however, some applications might not care due to the support that the API provides.

## 3-D Pipeline Level

Drivers that support the Direct3D version 11 DDI are not required to support all the hardware features of the Direct3D version 11 DDI. Drivers can support the new threading model of the Direct3D version 11 DDI on top of hardware that only supports the Direct3D version 10 DDI. The Direct3D version 11 runtime determines the driver's maximum hardware level of support when the runtime calls the driver's [**GetCaps(D3D10_2)**](/windows-hardware/drivers/ddi/d3d10umddi/nc-d3d10umddi-pfnd3d10_2ddi_getcaps) function with the **Type** member of [**D3D10_2DDIARG_GETCAPS**](/windows-hardware/drivers/ddi/d3d10umddi/ns-d3d10umddi-d3d10_2ddiarg_getcaps) set to D3D11DDICAPS_3DPIPELINESUPPORT. The driver returns a pointer to a [**D3D11DDI_3DPIPELINESUPPORT_CAPS**](/windows-hardware/drivers/ddi/d3d10umddi/ns-d3d10umddi-d3d11ddi_3dpipelinesupport_caps) structure in the **pData** member of **D3D10_2DDIARG_GETCAPS** that identifies the maximum hardware level of support.

The API does not use just the DDI version as the primary indicator of API feature level support; the API allows the driver to feed back into this process. The runtime chooses a [**D3D11DDI_3DPIPELINELEVEL**](/windows-hardware/drivers/ddi/d3d10umddi/ne-d3d10umddi-d3d11ddi_3dpipelinelevel) value and feeds back the value to the driver during device creation in a call to the driver's [**CreateDevice(D3D10)**](/windows-hardware/drivers/ddi/d3d10umddi/nc-d3d10umddi-pfnd3d10ddi_createdevice) function, as part of the **Flags** member of the [**D3D10DDIARG_CREATEDEVICE**](/windows-hardware/drivers/ddi/d3d10umddi/ns-d3d10umddi-d3d10ddiarg_createdevice) structure.

If the driver supports hardware levels less than Direct3D version 11 on the Direct3D version 11 DDI, there are minor ramifications to the operation of the driver. The first is that the Direct3D version 11 runtime might never call many new Direct3D version 11 DDI functions at all. For example, the Direct3D version 11 runtime does not call any of the new shader-stage DDI functions (like [**DsSetShader**](/windows-hardware/drivers/ddi/d3d10umddi/nc-d3d10umddi-pfnd3d10ddi_setshader)) if the driver supports a hardware feature level that is less than Direct3D version 11. Other DDI functions follow the rules of the feature level and ignore the fact that the Direct3D version 11 DDI might be associated with higher capabilities. For example, even though IAVertexInputSlots for the Direct3D version 11 API is 32, the Direct3D version 10 feature level only allows 16 and that is what the driver should expect.

Deprecated or converted features present another interesting aspect. Deprecation is not possible at the Direct3D version 11 DDI level because deprecation must support the ability to express earlier-version DDI functions. For example, the Direct3D 11 API version of PIPELINESTATS is always constant; however, it requests different [**D3D10_DDI_QUERY_DATA_PIPELINE_STATISTICS**](/windows-hardware/drivers/ddi/d3d10umddi/ns-d3d10umddi-d3d10_ddi_query_data_pipeline_statistics) with Direct3D 10 feature levels and [**D3D11_DDI_QUERY_DATA_PIPELINE_STATISTICS**](/windows-hardware/drivers/ddi/d3d10umddi/ns-d3d10umddi-d3d11_ddi_query_data_pipeline_statistics) with Direct3D 11 feature levels, and so on. Even though the API attempted to deprecate the text filter size, it is easier for drivers to deprecate the DDI function table entry, in its entirety, than to attempt to re-use the function table entry for something else.

Even if a driver that supports the Direct3D version 11 DDI does not support the full Direct3D version 11 feature level, the driver cannot opt-out of "extended format awareness", as described in [Supporting Extended Format Awareness](supporting-extended-format-awareness.md). Because the driver supports the Direct3D version 11 DDI, the driver should handle the following tasks:

* Support BGR formats

* Correctly respond to calls to its [**CheckFormatSupport**](/windows-hardware/drivers/ddi/d3d10umddi/nc-d3d10umddi-pfnd3d10ddi_checkformatsupport) function to check for XR_BIAS support. The driver should either claim support or deny support.

* Allow casting of fully typed back buffers

The Direct3D version 11 API also informs the driver whether the application uses multiple threads through the D3D11DDI_CREATEDEVICE_FLAG_SINGLETHREADED flag. If this flag is present in the **Flags** member of the [**D3D10DDIARG_CREATEDEVICE**](/windows-hardware/drivers/ddi/d3d10umddi/ns-d3d10umddi-d3d10ddiarg_createdevice) structure when a display device is created through a call to the driver's [**CreateDevice(D3D10)**](/windows-hardware/drivers/ddi/d3d10umddi/nc-d3d10umddi-pfnd3d10ddi_createdevice) function, the driver can determine that no deferred contexts are created and that the driver is not required to synchronize, as concurrent creates do not occur.
