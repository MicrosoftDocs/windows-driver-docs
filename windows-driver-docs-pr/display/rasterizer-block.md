---
title: Rasterizer Block
description: Rasterizer Block
ms.assetid: 115c265d-0264-4a8a-b07b-710438394c68
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 





