---
title: Rendering Point Sprites
description: Rendering Point Sprites
ms.assetid: f2bdfd93-5b79-4f48-87b6-a76847892f5e
keywords:
- DirectX 8.0 release notes WDK Windows 2000 display , point sprites
- point sprites WDK DirectX 8.0
- size WDK point sprites
- point size WDK DirectX 8.0
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Rendering Point Sprites


## <span id="ddk_rendering_point_sprites_gg"></span><span id="DDK_RENDERING_POINT_SPRITES_GG"></span>


A screen space point **P = (X, Y, Z, W)** of screen-space size **S** is rasterized as a quadrilateral with the following 4 vertices:

```
(Xâˆ’S/2, Yâˆ’S/2, Z, W)
(X+S/2, Yâˆ’S/2, Z, W)
(Xâˆ’S/2, Y+S/2, Z, W)
(X+S/2, Y+S/2, Z, W)
```

The vertex color attributes are duplicated at each of the 4 vertices, therefore each point is always rendered with constant colors.

The assignment of texture coordinates is controlled by the D3DRS\_POINTSPRITEENABLE setting. If D3DRS\_POINTSPRITEENABLE is set to **FALSE**, then the texture coordinates of the vertex are duplicated at each of the 4 vertices. If no texture coordinates are present in the vertex the default values of (0.0f, 0.0f, 0.0f, 1.0f) are used for the corners of the point sprite. If the D3DRS\_POINTSPRITEENABLE is set to **TRUE**, then the texture coordinates at the 4 vertices, starting from the top left corner and winding clockwise, are set to:

```
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Rendering%20Point%20Sprites%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




