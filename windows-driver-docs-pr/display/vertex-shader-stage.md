---
title: Vertex Shader Stage
description: Vertex Shader Stage
ms.assetid: 310ef24a-7647-4f5e-b89f-a3ff330d5df4
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Vertex Shader Stage


The vertex shader stage processes vertices by performing operations such as transformations, skinning, and lighting. Vertex shaders always operate on a single input vertex and produce a single output vertex. This stage of the rendering pipeline must always be active.

The Direct3D runtime calls the following driver functions to create, set up, and destroy the vertex shader:

[**CalcPrivateShaderSize**](https://docs.microsoft.com/windows-hardware/drivers/ddi/d3d10umddi/nc-d3d10umddi-pfnd3d10ddi_calcprivateshadersize)

[**CreateVertexShader(D3D10)**](https://docs.microsoft.com/windows-hardware/drivers/ddi/d3d10umddi/nc-d3d10umddi-pfnd3d10ddi_createvertexshader)

[**DestroyShader**](https://docs.microsoft.com/windows-hardware/drivers/ddi/d3d10umddi/nc-d3d10umddi-pfnd3d10ddi_destroyshader)

[**VsSetConstantBuffers**](https://docs.microsoft.com/windows-hardware/drivers/ddi/d3d10umddi/nc-d3d10umddi-pfnd3d10ddi_setconstantbuffers)

[**VsSetSamplers**](https://docs.microsoft.com/windows-hardware/drivers/ddi/d3d10umddi/nc-d3d10umddi-pfnd3d10ddi_setsamplers)

[**VsSetShader**](https://docs.microsoft.com/windows-hardware/drivers/ddi/d3d10umddi/nc-d3d10umddi-pfnd3d10ddi_setshader)

[**VsSetShaderResources**](https://docs.microsoft.com/windows-hardware/drivers/ddi/d3d10umddi/nc-d3d10umddi-pfnd3d10ddi_setshaderresources)

 

 





