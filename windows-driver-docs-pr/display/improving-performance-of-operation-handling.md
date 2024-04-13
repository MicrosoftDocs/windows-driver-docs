---
title: Improving Performance of Operation Handling
description: Improving Performance of Operation Handling
keywords:
- Direct3D WDK Windows 2000 display , operation codes
- operation codes WDK Direct3D
ms.date: 04/20/2017
---

# Improving Performance of Operation Handling


## <span id="ddk_improving_performance_of_operation_handling_gg"></span><span id="DDK_IMPROVING_PERFORMANCE_OF_OPERATION_HANDLING_GG"></span>


To improve the performance of your display driver, you should observe the following items when you implement your driver to render graphics primitives and process state changes:

-   The DirectX runtime filters redundant requests to set render-state parameters. That is, if an application calls the **IDirect3DDevice8::SetRenderState** method multiple times to set the same device render-state parameter before it renders a scene, the runtime filters out redundant calls, and your driver's [**D3dDrawPrimitives2**](/windows-hardware/drivers/ddi/d3dhal/nc-d3dhal-lpd3dhal_drawprimitives2cb) function only receives one request to set this particular render-state parameter. Therefore, you do not have to implement your driver to perform this filtering action.

-   Your driver should only write to render-state registers just before it draws primitives and not every time it receives an operation request ([**D3DHAL\_DP2OPERATION**](/windows-hardware/drivers/ddi/d3dhal/ne-d3dhal-_d3dhal_dp2operation)).

For more information about **IDirect3DDevice8::SetRenderState**, see the Direct3D SDK documentation.

 

