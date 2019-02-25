---
title: Texture Stage Operations
description: Texture Stage Operations
ms.assetid: da2213bb-41f1-440b-8f69-19f69e739954
keywords:
- multiple textures WDK Direct3D , texture stages
- texture stages WDK Direct3D
- texture management WDK Direct3D , stages
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 





