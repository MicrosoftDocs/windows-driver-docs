---
title: Pixel Shader Stage
description: Pixel Shader Stage
ms.assetid: 969b6cb9-7b03-4c9f-bf4a-e8d9b442c847
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Pixel%20Shader%20Stage%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




