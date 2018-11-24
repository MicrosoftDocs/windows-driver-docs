---
title: Rendering Point Sprites
description: Rendering Point Sprites
ms.assetid: f2bdfd93-5b79-4f48-87b6-a76847892f5e
keywords:
- DirectX 8.0 release notes WDK Windows 2000 display , point sprites
- point sprites WDK DirectX 8.0
- size WDK point sprites
- point size WDK DirectX 8.0
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Rendering Point Sprites


## <span id="ddk_rendering_point_sprites_gg"></span><span id="DDK_RENDERING_POINT_SPRITES_GG"></span>


A screen space point **P = (X, Y, Z, W)** of screen-space size **S** is rasterized as a quadrilateral with the following 4 vertices:

```cpp
(Xâˆ’S/2, Yâˆ’S/2, Z, W)
(X+S/2, Yâˆ’S/2, Z, W)
(Xâˆ’S/2, Y+S/2, Z, W)
(X+S/2, Y+S/2, Z, W)
```

The vertex color attributes are duplicated at each of the 4 vertices, therefore each point is always rendered with constant colors.

The assignment of texture coordinates is controlled by the D3DRS\_POINTSPRITEENABLE setting. If D3DRS\_POINTSPRITEENABLE is set to **FALSE**, then the texture coordinates of the vertex are duplicated at each of the 4 vertices. If no texture coordinates are present in the vertex the default values of (0.0f, 0.0f, 0.0f, 1.0f) are used for the corners of the point sprite. If the D3DRS\_POINTSPRITEENABLE is set to **TRUE**, then the texture coordinates at the 4 vertices, starting from the top left corner and winding clockwise, are set to:

```cpp
(0.0f, 0.0f)
(1.0f, 0.0f)
(0.0f, 1.0f)
(1.0f, 1.0f)
```

When clipping is enabled, points are clipped as follows: If the vertex is outside the view frustum in Z (either near or far), then the point is not rendered. If the point, taking into account the point size, is totally outside the viewport in x or y, then the point is not rendered. Remaining points are rendered. Note that it is possible for the point position to be outside the viewport (in x or y) and still be partially visible.

Points may or may not be correctly clipped to user-defined clip planes. If D3DDEVCAPS\_CLIPPLANESCALEDPOINTS is not set, then points are clipped to user-defined clip planes based only on the vertex position, ignoring the point size. In this case, scaled points are fully rendered when the vertex position is inside the clip planes, and are discarded when the vertex position is outside a clip plane. Applications may prevent potential 'popping' artifacts by adding a border geometry to clip planes that is as large as the maximum point size.

If the D3DDEVCAPS\_CLIPPLANESCALEDPOINTS bit is set, then the scaled points are correctly clipped to user-defined clip planes.

It is important to remember that point sprites should have no dependencies on the culling or fill modes. Point sprites should always be rendered regardless of the cull or fill mode.

Also it is important that in point fill mode with flat shading that the rules for flat shading a primitive are complied with. This means that the first vertex of a primitive dictates the color of that primitive and hence the color for each vertex of the primitive. This is not what occurs with version 8.0 of the reference rasterizer or the sample driver and is fixed in version 8.1.

 

 





