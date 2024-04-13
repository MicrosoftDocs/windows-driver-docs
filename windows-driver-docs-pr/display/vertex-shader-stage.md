---
title: Vertex Shader Stage
description: Vertex Shader Stage
ms.date: 04/20/2017
---

# Vertex Shader Stage


The vertex shader stage processes vertices by performing operations such as transformations, skinning, and lighting. Vertex shaders always operate on a single input vertex and produce a single output vertex. This stage of the rendering pipeline must always be active.

The Direct3D runtime calls the following driver functions to create, set up, and destroy the vertex shader:

[**CalcPrivateShaderSize**](/windows-hardware/drivers/ddi/d3d10umddi/nc-d3d10umddi-pfnd3d10ddi_calcprivateshadersize)

[**CreateVertexShader(D3D10)**](/windows-hardware/drivers/ddi/d3d10umddi/nc-d3d10umddi-pfnd3d10ddi_createvertexshader)

[**DestroyShader**](/windows-hardware/drivers/ddi/d3d10umddi/nc-d3d10umddi-pfnd3d10ddi_destroyshader)

[**VsSetConstantBuffers**](/windows-hardware/drivers/ddi/d3d10umddi/nc-d3d10umddi-pfnd3d10ddi_setconstantbuffers)

[**VsSetSamplers**](/windows-hardware/drivers/ddi/d3d10umddi/nc-d3d10umddi-pfnd3d10ddi_setsamplers)

[**VsSetShader**](/windows-hardware/drivers/ddi/d3d10umddi/nc-d3d10umddi-pfnd3d10ddi_setshader)

[**VsSetShaderResources**](/windows-hardware/drivers/ddi/d3d10umddi/nc-d3d10umddi-pfnd3d10ddi_setshaderresources)

 

