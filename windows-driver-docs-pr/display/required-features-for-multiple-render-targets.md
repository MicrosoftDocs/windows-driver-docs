---
title: Required Features for Multiple Render Targets
description: Required Features for Multiple Render Targets
ms.assetid: fa807bde-8c3b-4ba8-b899-cdcd0b8d2458
keywords: ["rendering multiple targets WDK DirectX 9.0 , required features", "multiple render targets WDK DirectX 9.0 , required features", "simultaneous render targets WDK DirectX 9.0 , required features"]
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Required%20Features%20for%20Multiple%20Render%20Targets%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




