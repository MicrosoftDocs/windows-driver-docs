---
title: Rasterizer Block
description: Rasterizer Block
ms.assetid: 115c265d-0264-4a8a-b07b-710438394c68
---

# Rasterizer Block


The rasterizer block clips, sets up primitives, and determines how to call the pixel shader stage. The Direct3D runtime does not view the rasterizer block as a stage in the pipeline. Instead, the Direct3D runtime views the rasterizer block as an interface between pipeline stages that happens to perform a significant set of fixed function operations. Many of these fixed function operations can be adjusted by software developers.

The rasterizer always determines that input positions are provided in clip-space, performs clipping and perspective divide, and applies viewport scale and offset.

The Direct3D runtime calls the following driver functions to create, set up, and destroy the state of the rasterizer:

[**CalcPrivateRasterizerStateSize**](https://msdn.microsoft.com/library/windows/hardware/ff538298)

[**CreateRasterizerState**](https://msdn.microsoft.com/library/windows/hardware/ff540676)

[**DestroyRasterizerState**](https://msdn.microsoft.com/library/windows/hardware/ff552788)

[**SetRasterizerState**](https://msdn.microsoft.com/library/windows/hardware/ff569550)

[**SetScissorRects**](https://msdn.microsoft.com/library/windows/hardware/ff569659)

[**SetViewports**](https://msdn.microsoft.com/library/windows/hardware/ff569698)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Rasterizer%20Block%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




