---
title: Required Features for Multiple Render Targets
description: Required Features for Multiple Render Targets
ms.assetid: fa807bde-8c3b-4ba8-b899-cdcd0b8d2458
keywords:
- rendering multiple targets WDK DirectX 9.0 , required features
- multiple render targets WDK DirectX 9.0 , required features
- simultaneous render targets WDK DirectX 9.0 , required features
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Required Features for Multiple Render Targets


## <span id="ddk_required_features_for_multiple_render_targets_gg"></span><span id="DDK_REQUIRED_FEATURES_FOR_MULTIPLE_RENDER_TARGETS_GG"></span>


A DirectX 9.0 version driver that supports rendering to multiple targets simultaneously must support the following features:

-   All surfaces for a given multiple render target group are allocated atomically. This limitation is addressed by treating this as a new type of surface format with multiple RGBA channels interleaved.

-   Only 32-bit surface formats are supported (for example, RGBA8, RGBA10, U16V16, and R32f type formats). This limitation is expressed by the name of the new surface formats.

-   A multiple render target group cannot be the primary (that is, the surface that is displayed). The multiple render target group must be off-screen only. This limitation is expressed by the surface format enumeration.

-   A multiple render target group cannot be a mipmap. That is, the creation of a MIP chain fails.

-   An element of a multiple render target group cannot be set as a texture at the same time as being a render target. However different elements of the group surface can simultaneously be textures and render targets.

-   No antialiasing of a multiple render target group is supported.

-   An element of a multiple render target group when used as a texture cannot be filtered. That is, no sampler state can affect the lookup.

-   An element of a multiple render target group cannot be locked.

-   Multiple elements of a multiple render target group can be used simultaneously, by assigning each element to various stages like typical textures.

-   Elements of a multiple render target group support gamma 2.2-1.0 conversion on read, just like other texture formats.

-   The D3DDP2OP\_CLEAR operation code clears all elements of a multiple render target group.

 

 





