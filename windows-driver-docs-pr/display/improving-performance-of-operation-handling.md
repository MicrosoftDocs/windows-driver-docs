---
title: Improving Performance of Operation Handling
description: Improving Performance of Operation Handling
ms.assetid: 14b5aa90-15ee-40c6-8f5b-e776b07932ab
keywords:
- Direct3D WDK Windows 2000 display , operation codes
- operation codes WDK Direct3D
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Improving Performance of Operation Handling


## <span id="ddk_improving_performance_of_operation_handling_gg"></span><span id="DDK_IMPROVING_PERFORMANCE_OF_OPERATION_HANDLING_GG"></span>


To improve the performance of your display driver, you should observe the following items when you implement your driver to render graphics primitives and process state changes:

-   The DirectX runtime filters redundant requests to set render-state parameters. That is, if an application calls the **IDirect3DDevice8::SetRenderState** method multiple times to set the same device render-state parameter before it renders a scene, the runtime filters out redundant calls, and your driver's [**D3dDrawPrimitives2**](https://msdn.microsoft.com/library/windows/hardware/ff544704) function only receives one request to set this particular render-state parameter. Therefore, you do not have to implement your driver to perform this filtering action.

-   Your driver should only write to render-state registers just before it draws primitives and not every time it receives an operation request ([**D3DHAL\_DP2OPERATION**](https://msdn.microsoft.com/library/windows/hardware/ff545678)).

For more information about **IDirect3DDevice8::SetRenderState**, see the Direct3D SDK documentation.

 

 





