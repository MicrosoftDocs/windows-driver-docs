---
title: Recommended DirectX 9.0 Driver Support
description: Recommended DirectX 9.0 Driver Support
ms.assetid: 57b4dac8-c694-47ec-b5f9-19247b4de433
keywords: ["unused channel defaults WDK DirectX 9.0", "channel defaults WDK DirectX 9.0"]
---

# Recommended DirectX 9.0 Driver Support


## <span id="ddk_recommended_directx_9_0_driver_support_gg"></span><span id="DDK_RECOMMENDED_DIRECTX_9_0_DRIVER_SUPPORT_GG"></span>


It is recommended that DirectX 9.0 drivers set defaults for unused channels of texture formats.

### <span id="Setting_Defaults_for_Unused_Channels_of_Texture_Formats"></span><span id="setting_defaults_for_unused_channels_of_texture_formats"></span><span id="SETTING_DEFAULTS_FOR_UNUSED_CHANNELS_OF_TEXTURE_FORMATS"></span>Setting Defaults for Unused Channels of Texture Formats

Drivers and their devices should set a default value for the unused channels in texture formats so that applications can rely on a known value being present in those channels that are not provided by input textures.

Similarly to the way that the reference rasterizer for DirectX 8.1 and later versions sets the default value for the unused B channel in the D3DFMT\_G16R16 texture format to 1.0f (see *refrast.cpp* sample code), a DirectX 9.0 version driver should set the default values for the unused channels in the following DirectX 9.0 floating-point texture formats to 1.0f:

-   D3DFMT\_R16F

-   D3DFMT\_G16R16F

-   D3DFMT\_R32F

-   D3DFMT\_G32R32F

A DirectX 9.0 driver should also set the following defaults:

-   The alpha channel (A) (for transparency) to 1.0f, which is opaque.

-   The luminance channel (L) to 1.0f, which produces a maximum light intensity.

The reference rasterizer also sets defaults for the B channel, in addition to the A channel, (of RGBA) to 1.0f for the D3DFMT\_V16U16 format. In this way, the D3DFMT\_V16U16 format operates interchangeably with the D3DFMT\_L6V5U5 format, which actually has an L channel. In the D3DFMT\_L6V5U5 format, luminance is placed in the B channel.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Recommended%20DirectX%209.0%20Driver%20Support%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




