---
title: Marking Formats for Gamma and Linear Conversion
description: Marking Formats for Gamma and Linear Conversion
ms.assetid: 1285b04e-b67a-46d2-82b2-3cde433bf578
keywords:
- gamma correction WDK DirectX 9.0 , marking formats for gamma conversion
- marking formats for conversion WDK DirectX 9.0
- linear conversions WDK DirectX 9.0
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Marking Formats for Gamma and Linear Conversion


## <span id="ddk_marking_formats_for_gamma_and_linear_conversion_gg"></span><span id="DDK_MARKING_FORMATS_FOR_GAMMA_AND_LINEAR_CONVERSION_GG"></span>


A DirectX 9.0 version driver marks texture formats for linear or gamma conversion so that it can determine whether to convert textures of those formats in order to accurately process or render them.

Texture content is typically stored in sRGB format, which is gamma corrected. However, for the pixel pipeline to perform accurate blending operations on sRGB-formatted textures, the driver must convert those textures to a linear format before reading from them. When the pixel pipeline is ready to write those textures out to the render target, the driver must convert those textures back to sRGB format. In this way, the pixel pipeline performs all operations in linear space.

The driver specifies the following flags in the **dwOperations** member of the [**DDPIXELFORMAT**](https://msdn.microsoft.com/library/windows/hardware/ff550274) structure for a texture surface's format to mark the format for conversion:

-   D3DFORMAT\_OP\_SRGBREAD to indicate whether a texture is gamma 2.2 corrected or not (sRGB or not), and if it must be converted to a linear format by the driver either for blending operations or for the sampler at lookup time.

-   D3DFORMAT\_OP\_SRGBWRITE to indicate whether the pixel pipeline should gamma correct back to sRGB space when writing out to the render target.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Marking%20Formats%20for%20Gamma%20and%20Linear%20Conversion%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




