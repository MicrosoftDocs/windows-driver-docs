---
title: Introduction to Deferred Contexts
description: Introduction to Deferred Contexts
keywords:
- Direct3D version 11 WDK Windows 7 display , deferred contexts, introduction
- Direct3D version 11 WDK Windows Server 2008 R2 display , deferred contexts, introduction
- deferred contexts WDK Windows 7 display , introduction
- deferred contexts WDK Windows Server 2008 R2 display , introduction
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Introduction to Deferred Contexts


This section applies only to Windows 7 and later, and Windows Server 2008 R2 and later versions of Windows operating system.

Deferred contexts are used by an application to create command lists. If a user-mode display driver indicates that it supports command lists through the D3D11DDICAPS\_COMMANDLISTS\_BUILD\_2 flag of the [**D3D11DDI\_THREADING\_CAPS**](/windows-hardware/drivers/ddi/d3d10umddi/ns-d3d10umddi-d3d11ddi_threading_caps) structure, it must also support the ability to create and manipulate deferred contexts. For more information about how the driver indicates threading capabilities, see [Supporting Threading, Command Lists, and 3-D Pipeline](supporting-threading--command-lists--and-3-d-pipeline.md). Deferred contexts differ from the immediate context in that the commands that the deferred contexts record cannot be executed until the application explicitly requests to execute the commands, by executing the generated command list. To create and use a deferred context, Direct3D version 11 provides the following new DDI functions. These functions are a subset of information that is required to create the device/immediate context combination.

-   [**AbandonCommandList**](/windows-hardware/drivers/ddi/d3d10umddi/nc-d3d10umddi-pfnd3d11ddi_abandoncommandlist)

-   [**CalcPrivateDeferredContextSize**](/windows-hardware/drivers/ddi/d3d10umddi/nc-d3d10umddi-pfnd3d11ddi_calcprivatedeferredcontextsize)

-   [**CreateDeferredContext**](/windows-hardware/drivers/ddi/d3d10umddi/nc-d3d10umddi-pfnd3d11ddi_createdeferredcontext)

-   [**RecycleCreateDeferredContext**](/windows-hardware/drivers/ddi/d3d10umddi/nc-d3d10umddi-pfnd3d11ddi_recyclecreatedeferredcontext)

The semantics of the [**CalcPrivateDeferredContextSize**](/windows-hardware/drivers/ddi/d3d10umddi/nc-d3d10umddi-pfnd3d11ddi_calcprivatedeferredcontextsize) and [**CreateDeferredContext**](/windows-hardware/drivers/ddi/d3d10umddi/nc-d3d10umddi-pfnd3d11ddi_createdeferredcontext) functions are similar to other similar DDI functions.

The Direct3D runtime passes in a new driver handle and core layer handle for each call to the driver's [**CreateDeferredContext**](/windows-hardware/drivers/ddi/d3d10umddi/nc-d3d10umddi-pfnd3d11ddi_createdeferredcontext) function to create each deferred context. The pipeline state of each deferred context must be equivalent to the pipeline state that the immediate context has after the clear-state operation is performed on it. The driver must fill members of the [**D3D11DDI\_DEVICEFUNCS**](/windows-hardware/drivers/ddi/d3d10umddi/ns-d3d10umddi-d3d11ddi_devicefuncs) structure that the **p11ContextFuncs** member of [**D3D11DDIARG\_CREATEDEFERREDCONTEXT**](/windows-hardware/drivers/ddi/d3d10umddi/ns-d3d10umddi-d3d11ddiarg_createdeferredcontext) structure points to with a subset of the functions from its function table; the runtime uses each of the corresponding deferred context D3D10DDI\_HDEVICE handle values that the **hDrvContext** member of D3D11DDIARG\_CREATEDEFERREDCONTEXT specifies with this function table.

The driver must continue to provide functions that start with *pfnCreate*, *pfnOpen*, and *pfnDestroy* for the deferred context. These functions share the same threading semantics as the rest of the deferred context, and they are used to open and close context-local DDI handles as described in [Using Context-Local DDI Handles](using-context-local-ddi-handles.md). Functions that start with *pfnCalcPrivate* or *pfnCheck* are not leveraged for deferred contexts; therefore, the driver can set the members of [**D3D11DDI\_DEVICEFUNCS**](/windows-hardware/drivers/ddi/d3d10umddi/ns-d3d10umddi-d3d11ddi_devicefuncs) for these functions to **NULL** when the deferred context is created. The majority of the remaining device functions are leveraged for deferred context support. The driver does not leverage its [**QueryGetData**](/windows-hardware/drivers/ddi/d3d10umddi/nc-d3d10umddi-pfnd3d10ddi_querygetdata) function, though. However, the driver leverages its [**ResourceMap**](/windows-hardware/drivers/ddi/d3d10umddi/nc-d3d10umddi-pfnd3d10ddi_resourcemap) and [**ResourceUnmap**](/windows-hardware/drivers/ddi/d3d10umddi/nc-d3d10umddi-pfnd3d10ddi_resourceunmap) functions. The driver only supports the [**ResourceIsStagingBusy**](/windows-hardware/drivers/ddi/d3d10umddi/nc-d3d10umddi-pfnd3d10ddi_resourceisstagingbusy) function and new DDI functions for Direct3D version 11 resource clamps on the immediate context by using immediate-context handles. For a complete list of the functions that are not leveraged for deferred contexts, see [Excluding DDI Functions for Deferred Contexts](excluding-ddi-functions-for-deferred-contexts.md).

The driver leverages the core layer callback functions that are provided in the memory block that the **p11UMCallbacks** member of [**D3D11DDIARG\_CREATEDEFERREDCONTEXT**](/windows-hardware/drivers/ddi/d3d10umddi/ns-d3d10umddi-d3d11ddiarg_createdeferredcontext) points to. These core layer callback functions provide the refresh-state DDI for each deferred context. Most importantly, however, is the addition of the [**pfnPerformAmortizedProcessingCb**](/windows-hardware/drivers/ddi/d3d10umddi/nc-d3d10umddi-pfnd3d11ddi_perform_amortized_processing_cb) callback function that is described in [Changes from Direct3D 10](changes-from-direct3d-10.md).

The driver should not expect the [**pfnDisableDeferredStagingResourceDestruction**](/windows-hardware/drivers/ddi/d3d10umddi/nc-d3d10umddi-pfnd3d10ddi_disable_deferred_staging_resource_destruction_cb) callback function to which the **pfnDisableDeferredStagingResourceDestruction** member of [**D3D11DDI\_CORELAYER\_DEVICECALLBACKS**](/windows-hardware/drivers/ddi/d3d10umddi/ns-d3d10umddi-d3d11ddi_corelayer_devicecallbacks) points to be valid. The driver should have called **pfnDisableDeferredStagingResourceDestruction** within the [**CreateDevice(D3D10)**](/windows-hardware/drivers/ddi/d3d10umddi/nc-d3d10umddi-pfnd3d10ddi_createdevice) function for the device/immediate context; afterward, the driver should never call **pfnDisableDeferredStagingResourceDestruction** with the new Direct3D version 11 DDI semantics.

The driver's [**RecycleCreateDeferredContext**](/windows-hardware/drivers/ddi/d3d10umddi/nc-d3d10umddi-pfnd3d11ddi_recyclecreatedeferredcontext) function must clear out the pipeline state for the deferred context, similar to how the driver's [**CreateDeferredContext**](/windows-hardware/drivers/ddi/d3d10umddi/nc-d3d10umddi-pfnd3d11ddi_createdeferredcontext) clears out the pipeline state for the deferred context. After the runtime calls the driver's [**AbandonCommandList**](/windows-hardware/drivers/ddi/d3d10umddi/nc-d3d10umddi-pfnd3d11ddi_abandoncommandlist), [**CreateCommandList**](/windows-hardware/drivers/ddi/d3d10umddi/nc-d3d10umddi-pfnd3d11ddi_createcommandlist), or [**RecycleCreateCommandList**](/windows-hardware/drivers/ddi/d3d10umddi/nc-d3d10umddi-pfnd3d11ddi_recyclecreatecommandlist), the runtime can use the deferred context handle with either the driver's [**DestroyDevice(D3D10)**](/windows-hardware/drivers/ddi/d3d10umddi/nc-d3d10umddi-pfnd3d10ddi_destroydevice) or **RecycleCreateDeferredContext** function. For more information about **RecycleCreateDeferredContext**, see [Optimization for Small Command Lists](supporting-command-lists.md).

 

