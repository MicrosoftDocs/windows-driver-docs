---
title: Texture Stages
description: Texture Stages
ms.assetid: 98149615-ef64-4b0d-9adf-d6b72324e1b4
keywords:
- multiple textures WDK Direct3D , texture stages
- texture stages WDK Direct3D
- texture management WDK Direct3D , stages
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Texture Stages


## <span id="ddk_texture_stages_gg"></span><span id="DDK_TEXTURE_STAGES_GG"></span>


The texture stage indicates the location of the texture in the texture pipeline. The position with the highest non-NULL texture is closest to the frame buffer. Each stage is a texture blending unit that performs the operation used to combine an associated texture onto a polygon, as shown in the following figure.

![diagram illustrating a single texture stage](images/d3dfig36.png)

The current texture enters the stage and is blended with another texture and a diffuse component with the result being passed forward to the next stage in the texture pipeline (or frame buffer if this is the last stage).

There are eight texture stages, numbered zero through seven, with zero being furthest from the frame buffer, and corresponding to the render state texture handle D3DRENDERSTATE\_TEXTUREHANDLE, which is described in the DirectX SDK documentation. The driver must handle up to eight texture coordinates, even if the hardware does not support that many.

In multiple texture rendering, the lower-numbered texture stages are farther away from the frame buffer. The lowest texture stage in the cascade is picked up and filtered to get a *texel*, or texture element. A blending operation occurs between that texel and the next as it cascades down the texture pipeline toward the frame buffer.

For example, if two textures, Texture0 and Texture1, are blended together, the resulting texel enters the rasterization pipeline just as a single texture would using legacy texturing. With three textures, Texture0 gets blended with Texture1. The resulting texel is then blended with Texture2 according to some programmable weight. This means that Texture0 cannot influence Texture2 directly; it can only do so by being blended with Texture1, as illustrated in the following figure.

![diagram illustrating a three-stage texture pipeline](images/d3dfig35.png)

Each texture stage introduces one texture into the pipeline. The pixel pipeline is separate and comes after multiple texture operations. This may include fog application or frame buffer alpha blending.

 

 





