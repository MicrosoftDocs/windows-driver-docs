---
title: Pixel Shader Stage
description: Pixel Shader Stage
ms.assetid: 969b6cb9-7b03-4c9f-bf4a-e8d9b442c847
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Pixel Shader Stage


Input data that is available to the pixel shader stage includes vertex attributes that can be selected, on a per-Element basis, to be interpolated with or without perspective correction, or be treated as constant per-primitive.

Outputs are one or more 4-vectors of output data for the current pixel location, or no color (if the pixel is discarded).

The Direct3D runtime calls the following driver functions to create, set up, and destroy the pixel shader:

[**CalcPrivateShaderSize**](https://msdn.microsoft.com/library/windows/hardware/ff538315)

[**CreatePixelShader(D3D10)**](https://msdn.microsoft.com/library/windows/hardware/ff540670)

[**DestroyShader**](https://msdn.microsoft.com/library/windows/hardware/ff552805)

[**PsSetConstantBuffers**](https://msdn.microsoft.com/library/windows/hardware/ff569207)

[**PsSetSamplers**](https://msdn.microsoft.com/library/windows/hardware/ff569208)

[**PsSetShader**](https://msdn.microsoft.com/library/windows/hardware/ff569209)

[**PsSetShaderResources**](https://msdn.microsoft.com/library/windows/hardware/ff569210)

 

 





