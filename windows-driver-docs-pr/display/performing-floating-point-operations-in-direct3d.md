---
title: Performing Floating-point Operations in Direct3D
description: Performing Floating-point Operations in Direct3D
ms.assetid: 2da736cf-d062-4c5a-b9f5-6b35f199660f
keywords:
- floating-point operations WDK Direct3D
- Direct3D WDK Windows 2000 display , floating-point operations
- callback functions WDK Direct3D
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Performing Floating-point Operations in Direct3D


## <span id="ddk_performing_floating_point_operations_in_direct3d_gg"></span><span id="DDK_PERFORMING_FLOATING_POINT_OPERATIONS_IN_DIRECT3D_GG"></span>


The DirectX runtime saves and restores floating-point state when it calls many of a display driver's Direct3D callback functions. However, as described in [Performing Floating-point Operations in DirectDraw](performing-floating-point-operations-in-directdraw.md), some of the driver's Direct3D callback functions must save floating-point state prior to performing floating-point operations and must restore floating-point state when the operations complete.

The DirectX runtime saves and restores floating-point state as required for the following Direct3D callback functions:

-   [**D3dContextCreate**](https://msdn.microsoft.com/library/windows/hardware/ff542178)

-   [**D3dContextDestroy**](https://msdn.microsoft.com/library/windows/hardware/ff542180)

-   [**D3dDrawPrimitives2**](https://msdn.microsoft.com/library/windows/hardware/ff544704)

-   [**D3dGetDriverState**](https://msdn.microsoft.com/library/windows/hardware/ff544708)

-   [**D3dValidateTextureStageState**](https://msdn.microsoft.com/library/windows/hardware/ff549064)

For the following callback functions, a Direct3D-supported display driver must save floating-point state before performing floating-point operations, and restore it when the operations are complete:

-   [**D3dCreateSurfaceEx**](https://msdn.microsoft.com/library/windows/hardware/ff542840)

-   [**D3dDestroyDDLocal**](https://msdn.microsoft.com/library/windows/hardware/ff544685)

-   [D3DBuffer Callbacks](https://msdn.microsoft.com/library/windows/hardware/ff542176)

For more information about floating-point operations, see [Floating-Point Operations in Graphics Driver Functions](floating-point-operations-in-graphics-driver-functions.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Performing%20Floating-point%20Operations%20in%20Direct3D%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




