---
title: Rasterizer Block
description: Rasterizer Block
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Rasterizer Block


The rasterizer block clips, sets up primitives, and determines how to call the pixel shader stage. The Direct3D runtime does not view the rasterizer block as a stage in the pipeline. Instead, the Direct3D runtime views the rasterizer block as an interface between pipeline stages that happens to perform a significant set of fixed function operations. Many of these fixed function operations can be adjusted by software developers.

The rasterizer always determines that input positions are provided in clip-space, performs clipping and perspective divide, and applies viewport scale and offset.

The Direct3D runtime calls the following driver functions to create, set up, and destroy the state of the rasterizer:

[**CalcPrivateRasterizerStateSize**](/windows-hardware/drivers/ddi/d3d10umddi/nc-d3d10umddi-pfnd3d10ddi_calcprivaterasterizerstatesize)

[**CreateRasterizerState**](/windows-hardware/drivers/ddi/d3d10umddi/nc-d3d10umddi-pfnd3d10ddi_createrasterizerstate)

[**DestroyRasterizerState**](/windows-hardware/drivers/ddi/d3d10umddi/nc-d3d10umddi-pfnd3d10ddi_destroyrasterizerstate)

[**SetRasterizerState**](/windows-hardware/drivers/ddi/d3d10umddi/nc-d3d10umddi-pfnd3d10ddi_setrasterizerstate)

[**SetScissorRects**](/windows-hardware/drivers/ddi/d3d10umddi/nc-d3d10umddi-pfnd3d10ddi_setscissorrects)

[**SetViewports**](/windows-hardware/drivers/ddi/d3d10umddi/nc-d3d10umddi-pfnd3d10ddi_setviewports)

 

