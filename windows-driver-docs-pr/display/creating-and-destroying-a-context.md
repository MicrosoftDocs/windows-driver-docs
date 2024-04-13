---
title: Creating and Destroying a Context
description: Creating and Destroying a Context
keywords:
- context WDK Direct3D , creating
- context WDK Direct3D , destroying
- D3dContextCreate
- D3dContextDestroy
- destroying context WDK Direct3D
ms.date: 04/20/2017
---

# Creating and Destroying a Context


## <span id="ddk_creating_and_destroying_a_context_gg"></span><span id="DDK_CREATING_AND_DESTROYING_A_CONTEXT_GG"></span>


A driver must create and initialize a device-specific context that encapsulates the state information that it requires to perform rendering. State is not shared between contexts; so the driver must maintain full state information for each context that it creates.

To create a context, the driver should do the following:

-   Allocate the device-specific context and zero-initialize it.

-   See [**D3dContextCreate**](/windows-hardware/drivers/ddi/d3dhal/nc-d3dhal-lpd3dhal_contextcreatecb) for additional steps to be done within that callback. The **D3dContextCreate** callback is called when an application creates a Direct3D HAL device. The driver must implement this callback.

The driver must be able to reference all texture handles created by [**D3dCreateSurfaceEx**](/windows/win32/api/ddrawint/nc-ddrawint-pdd_createsurfaceex) within a created context. This enables the driver to clean up all driver-specific data related to textures created within this context when a call to the [**D3dContextDestroy**](/windows-hardware/drivers/ddi/d3dhal/nc-d3dhal-lpd3dhal_contextdestroycb) function is made.

Direct3D calls [**D3dContextDestroy**](/windows-hardware/drivers/ddi/d3dhal/nc-d3dhal-lpd3dhal_contextdestroycb) when an application requests that a Direct3D HAL device be destroyed. The driver should free all resources that it allocated to the specified context. These resources include, for example, texture resources, vertex and pixel [shaders](direct3d-shaders.md), [declarations and code for vertex shaders](separating-declarations-and-code-for-vertex-shaders.md), and resources for [asynchronous queries](supporting-asynchronous-query-operations.md).

 

