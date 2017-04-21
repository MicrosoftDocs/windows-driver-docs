---
title: Creating and Destroying a Context
description: Creating and Destroying a Context
ms.assetid: 31462b0a-ed06-4138-ab91-7ec98bc5ff14
keywords:
- context WDK Direct3D , creating
- context WDK Direct3D , destroying
- D3dContextCreate
- D3dContextDestroy
- destroying context WDK Direct3D
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Creating and Destroying a Context


## <span id="ddk_creating_and_destroying_a_context_gg"></span><span id="DDK_CREATING_AND_DESTROYING_A_CONTEXT_GG"></span>


A driver must create and initialize a device-specific context that encapsulates the state information that it requires to perform rendering. State is not shared between contexts; so the driver must maintain full state information for each context that it creates.

To create a context, the driver should do the following:

-   Allocate the device-specific context and zero-initialize it.

-   See [**D3dContextCreate**](https://msdn.microsoft.com/library/windows/hardware/ff542178) for additional steps to be done within that callback. The **D3dContextCreate** callback is called when an application creates a Direct3D HAL device. The driver must implement this callback.

The driver must be able to reference all texture handles created by [**D3dCreateSurfaceEx**](https://msdn.microsoft.com/library/windows/hardware/ff542840) within a created context. This enables the driver to clean up all driver-specific data related to textures created within this context when a call to the [**D3dContextDestroy**](https://msdn.microsoft.com/library/windows/hardware/ff542180) function is made.

Direct3D calls [**D3dContextDestroy**](https://msdn.microsoft.com/library/windows/hardware/ff542180) when an application requests that a Direct3D HAL device be destroyed. The driver should free all resources that it allocated to the specified context. These resources include, for example, texture resources, vertex and pixel [shaders](direct3d-shaders.md), [declarations and code for vertex shaders](separating-declarations-and-code-for-vertex-shaders.md), and resources for [asynchronous queries](supporting-asynchronous-query-operations.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Creating%20and%20Destroying%20a%20Context%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




