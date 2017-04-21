---
title: Texture Stage Operations
description: Texture Stage Operations
ms.assetid: da2213bb-41f1-440b-8f69-19f69e739954
keywords:
- multiple textures WDK Direct3D , texture stages
- texture stages WDK Direct3D
- texture management WDK Direct3D , stages
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Texture Stage Operations


## <span id="ddk_texture_stage_operations_gg"></span><span id="DDK_TEXTURE_STAGE_OPERATIONS_GG"></span>


An application performs blending operations for texture stages by calling the **IDirect3DDevice7::SetTextureStageState** method. Multiple texture blending operations are performed by a set of texture blending unit stages. Each of these can be individually programmed to carry out a variety of texture blending operations, selected by a parameter. For a description of **IDirect3DDevice7::SetTextureStageState**, see the Direct3D SDK documentation.

Direct3D does not provide a mechanism for specifying more than one texture being introduced at each blending stage. Saturation is defined to occur between texture stages in the pipeline, but it should occur as late as possible within each stage.

The following operations, which are enumerated in D3DTEXTUREOP, are required for PC98 compatibility compliance:

-   D3DTOP\_DISABLE

-   D3DTOP\_SELECTARG1, D3DTOP\_SELECTARG2

-   D3DTOP\_MODULATE

-   D3DTOP\_ADD

-   D3DTOP\_BLENDTEXTUREALPHA

The default values are D3DTOP\_MODULATE for stage one, and D3DTOP\_DISABLE for all other stages. D3DTOP\_MODULATE is used for stage one for backward compatibility, but, by default, all texturing should be disabled.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Texture%20Stage%20Operations%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




