---
title: Marking Formats for Gamma and Linear Conversion
description: Marking Formats for Gamma and Linear Conversion
ms.assetid: 1285b04e-b67a-46d2-82b2-3cde433bf578
keywords:
- gamma correction WDK DirectX 9.0 , marking formats for gamma conversion
- marking formats for conversion WDK DirectX 9.0
- linear conversions WDK DirectX 9.0
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Marking Formats for Gamma and Linear Conversion


## <span id="ddk_marking_formats_for_gamma_and_linear_conversion_gg"></span><span id="DDK_MARKING_FORMATS_FOR_GAMMA_AND_LINEAR_CONVERSION_GG"></span>


A DirectX 9.0 version driver marks texture formats for linear or gamma conversion so that it can determine whether to convert textures of those formats in order to accurately process or render them.

Texture content is typically stored in sRGB format, which is gamma corrected. However, for the pixel pipeline to perform accurate blending operations on sRGB-formatted textures, the driver must convert those textures to a linear format before reading from them. When the pixel pipeline is ready to write those textures out to the render target, the driver must convert those textures back to sRGB format. In this way, the pixel pipeline performs all operations in linear space.

The driver specifies the following flags in the **dwOperations** member of the [**DDPIXELFORMAT**](https://msdn.microsoft.com/library/windows/hardware/ff550274) structure for a texture surface's format to mark the format for conversion:

-   D3DFORMAT\_OP\_SRGBREAD to indicate whether a texture is gamma 2.2 corrected or not (sRGB or not), and if it must be converted to a linear format by the driver either for blending operations or for the sampler at lookup time.

-   D3DFORMAT\_OP\_SRGBWRITE to indicate whether the pixel pipeline should gamma correct back to sRGB space when writing out to the render target.

 

 





