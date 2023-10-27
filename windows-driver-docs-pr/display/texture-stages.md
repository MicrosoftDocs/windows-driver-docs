---
title: Texture Stages
description: Texture Stages
keywords:
- multiple textures WDK Direct3D , texture stages
- texture stages WDK Direct3D
- texture management WDK Direct3D , stages
ms.date: 04/20/2017
---

# Texture Stages

The texture stage indicates the location of the texture in the texture pipeline. The position with the highest non-NULL texture is closest to the frame buffer. Each stage is a texture blending unit that performs the operation used to combine an associated texture onto a polygon, as shown in the following figure.

:::image type="content" source="images/d3dfig36.png" alt-text="Diagram illustrating a single texture stage in the texture pipeline.":::

The current texture enters the stage and is blended with another texture and a diffuse component with the result being passed forward to the next stage in the texture pipeline (or frame buffer if this is the last stage).

There are eight texture stages, numbered zero through seven, with zero being furthest from the frame buffer, and corresponding to the render state texture handle D3DRENDERSTATE_TEXTUREHANDLE, which is described in the DirectX SDK documentation. The driver must handle up to eight texture coordinates, even if the hardware does not support that many.

In multiple texture rendering, the lower-numbered texture stages are farther away from the frame buffer. The lowest texture stage in the cascade is picked up and filtered to get a *texel*, or texture element. A blending operation occurs between that texel and the next as it cascades down the texture pipeline toward the frame buffer.

For example, if two textures, Texture0 and Texture1, are blended together, the resulting texel enters the rasterization pipeline just as a single texture would using legacy texturing. With three textures, Texture0 gets blended with Texture1. The resulting texel is then blended with Texture2 according to some programmable weight. This means that Texture0 cannot influence Texture2 directly; it can only do so by being blended with Texture1, as illustrated in the following figure.

:::image type="content" source="images/d3dfig35.png" alt-text="Diagram illustrating a three-stage texture pipeline with blending operations.":::

Each texture stage introduces one texture into the pipeline. The pixel pipeline is separate and comes after multiple texture operations. This may include fog application or frame buffer alpha blending.
