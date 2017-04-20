---
title: Improving Performance of Operation Handling
description: Improving Performance of Operation Handling
ms.assetid: 14b5aa90-15ee-40c6-8f5b-e776b07932ab
keywords:
- Direct3D WDK Windows 2000 display , operation codes
- operation codes WDK Direct3D
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Improving Performance of Operation Handling


## <span id="ddk_improving_performance_of_operation_handling_gg"></span><span id="DDK_IMPROVING_PERFORMANCE_OF_OPERATION_HANDLING_GG"></span>


To improve the performance of your display driver, you should observe the following items when you implement your driver to render graphics primitives and process state changes:

-   The DirectX runtime filters redundant requests to set render-state parameters. That is, if an application calls the **IDirect3DDevice8::SetRenderState** method multiple times to set the same device render-state parameter before it renders a scene, the runtime filters out redundant calls, and your driver's [**D3dDrawPrimitives2**](https://msdn.microsoft.com/library/windows/hardware/ff544704) function only receives one request to set this particular render-state parameter. Therefore, you do not have to implement your driver to perform this filtering action.

-   Your driver should only write to render-state registers just before it draws primitives and not every time it receives an operation request ([**D3DHAL\_DP2OPERATION**](https://msdn.microsoft.com/library/windows/hardware/ff545678)).

For more information about **IDirect3DDevice8::SetRenderState**, see the Direct3D SDK documentation.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Improving%20Performance%20of%20Operation%20Handling%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




