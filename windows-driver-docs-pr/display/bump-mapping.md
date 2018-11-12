---
title: Bump Mapping
description: Bump Mapping
ms.assetid: 38c7da06-cfe6-4285-8958-3d1eb22b1bcd
keywords:
- Direct3D WDK Windows 2000 display , bump mapping
- bump mapping WDK Direct3D
- surface wrinkles WDK Direct3D
- surface dimples WDK Direct3D
- wrinkles WDK Direct3D
- dimples WDK Direct3D
- texture management WDK Direct3D , bump mapping
- per-pixel texturing WDK Direct3D
- emulation WDK Direct3D
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Bump Mapping


## <span id="ddk_bump_mapping_gg"></span><span id="DDK_BUMP_MAPPING_GG"></span>


Bump mapping enables a surface to appear wrinkled or dimpled without the need to model these depressions geometrically. It involves perturbing the angles of the surface normals according to information given in a two-dimensional "bump map." This causes the local reflection model, where intensity is mainly a function of the surface normal, to produce local variations on a smooth surface. This deception is evident only when silhouetted, because in that case the perturbations are no longer visible at the edges. That is, the silhouette follows the line of the model and is therefore not perturbed. This appears to add texture to a surface, rather than modulating the color of a flat surface.

Because bump mapping for Direct3D is done by texturing a surface in the rendering phase without perturbing the geometry, it bypasses modeling problems that would otherwise occur. If the object is polygonal, the mesh has to be fine enough to receive the perturbations from the texture map. This is a drawback, if the texture is to be an option.

Bump mapping in Direct3D can be described as per-pixel texture coordinate perturbation of diffuse and specular environment maps. Rasterizers provide information about the contour of the bump map in terms of delta values, which the system applies to the u and v texture coordinates of an environment map in the next texture stage. The delta values are encoded in the pixel format of the bump map surface and are integrated with multiple-texture blending through the D3DTEXTURESTAGESTATETYPE enumerated type. For more information, see the DirectX SDK documentation.

This technique allows the lighting environment of the scene to be represented in an image environment map (either for diffuse or specular effects). It permits the lights to be of any number, shape, color, or intensity distribution that can be represented in such a map. These maps can be created in advance for static cases, or updated dynamically for changing light sources, by using blts.

Conventional bump mapping schemes derived from Phong shading are limited to spherical light sources of constant color and fixed fall-off curve. These do not require the additional texture addressing capabilities of per-pixel environment mapping and can work well for diffuse lighting effects, but cannot produce the visually structured specular highlights required for photorealism. In the future, use of such techniques will be facilitated by the integration of environment mapping calculations directly into the Direct3D geometry pipeline.

Bump mapping is commonly provided in photorealistic renderers. It can be used to drastically increase surface detail effects, without tessellating the surface into large numbers of small triangles. When used with specular effects, bump maps can simulate reflective yet rough surfaces, such as wet stone or pavement. When supported by 3D accelerators, such effects can be performed in real time, allowing dynamic light source changes.

When a DirectDrawSurface object is created with a bump-map format, that texture is considered to be a *bump map*. This object can be bound into the Direct3D device using any of the textures bound to the texture stages. A programmed texture blending stage can be set to perform the bump map operation by setting D3DTOP\_BUMPENVMAP. This bump-map texture uses the texture coordinates of the flexible vertex format specified by this stage's texture coordinate identifier to position itself on the rendered objects. It also respects the specified texture stage's controlling filtering, wrapping, and so on.

The bump values in this texture perturbs the texture coordinates used by the immediately following texture, which should be considered a specular or diffuse environment map.

### <span id="emulation"></span><span id="EMULATION"></span>Emulation

This methodology can be emulated on any hardware that supports an 8-bit paletted texture mode. The restriction is that the environment map used (the texture immediately following the bump texture map) must have a resolution of exactly 16X16 texels, and no filtering. This is indicated by the D3DTEXOPCAPS\_MAXBUMPENVMAP16X16 flag. Other parts have no limits on the size of the environment map that the bump map can perturb.

Bump mapping is enabled with the multiple-texture blending operations D3DTOP\_BUMPENVMAP and D3DTOP\_BUMPENVMAPPREMODULATE. The latter operation is a combination of bump mapping and gloss mapping that allows the specular reflection intensity to be encoded in the same surface as the bump map data.

There are now four additional texture states provided at each stage:

D3DTSS\_BUMPENVMAT00

D3DTSS\_BUMPENVMAT01

D3DTSS\_BUMPENVMAT10

D3DTSS\_BUMPENVMAT11

 

 





