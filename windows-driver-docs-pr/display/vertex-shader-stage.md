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

[**CalcPrivateShaderSize**](https://msdn.microsoft.com/library/windows/hardware/ff538315)

[**CreateVertexShader(D3D10)**](https://msdn.microsoft.com/library/windows/hardware/ff540720)

[**DestroyShader**](https://msdn.microsoft.com/library/windows/hardware/ff552805)

[**VsSetConstantBuffers**](https://msdn.microsoft.com/library/windows/hardware/ff570573)

[**VsSetSamplers**](https://msdn.microsoft.com/library/windows/hardware/ff570574)

[**VsSetShader**](https://msdn.microsoft.com/library/windows/hardware/ff570575)

[**VsSetShaderResources**](https://msdn.microsoft.com/library/windows/hardware/ff570576)

 

 





