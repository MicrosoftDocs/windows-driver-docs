---
title: Recommended DirectX 9.0 Driver Support
description: Recommended DirectX 9.0 Driver Support
ms.assetid: 57b4dac8-c694-47ec-b5f9-19247b4de433
keywords:
- unused channel defaults WDK DirectX 9.0
- channel defaults WDK DirectX 9.0
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 





