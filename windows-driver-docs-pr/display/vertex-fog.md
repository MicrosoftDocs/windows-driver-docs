---
title: Vertex Fog
description: Vertex Fog
keywords:
- vertex fog WDK Direct3D
- iterated fog WDK Direct3D
- local fog WDK Direct3D
- fogging WDK Direct3D
- D3DRENDERSTATE_FOGENABLE
- perspective-correct fog WDK Direct3D
- layered atmosphere model WDK Direct3D
- color fog calculations WDK Direct3D
- D3DPRASTERCAPS_FOGVERTEX
- D3DRENDERSTATE_FOGDENSITY
- D3DRENDERSTATE_FOGCOLOR
- D3DRENDERSTATE_SHADEMODE
ms.date: 04/20/2017
---

# Vertex Fog

Vertex fog is enabled using the D3DRENDERSTATE_FOGENABLE render state. Vertex fog can be made perspective-correct. For scenes with large polygons, vertex fog might not be the better choice, because the vertices are farther apart.

Vertex fog can be used in two ways:

1. Make use of Direct3D lighting code using D3DVERTEX structures (described in the Direct3D SDK documentation) to define the fog blending factor.

2. Make use of D3DLVERTEX or D3DTLVERTEX structures (both are described in the Direct3D SDK documentation). This is useful for doing custom fog effects such as layered fog, range-based fog, and volume fog.

When using fog with the D3DVERTEX structure, **PRIMCAPS.dwRasterCaps** has the D3DPRASTERCAPS_FOGVERTEX flag set. Individual calls to the **IDirect3DDevice7::SetRenderState** method are used to set D3DRENDERSTATE_FOGENABLE to **TRUE**, and D3DRENDERSTATE_FOGCOLOR to a 24-bit RGB color. For linear fog, the **IDirect3DDevice7::SetRenderState** method is used to set D3DRENDERSTATE_FOGSTART and D3DRENDERSTATE_FOGEND. For exponential and exponential squared fog, the D3DRENDERSTATE_FOGDENSITY render state is set with D3DLIGHTSTATETYPE. For more information, see the Direct3D SDK documentation.

When using fog with the D3DTLVERTEX structure, the **IDirect3DDevice7::SetRenderState** method is used to set D3DRENDERSTATE_FOGENABLE to **TRUE**, set the color of the fog in D3DRENDERSTATE_FOGCOLOR, and set D3DRENDERSTATE_FOGTABLEMODE to D3DFOG_NONE (this is set in the D3DTLVERTEX structure itself). A fog blend factor **f** is defined at each vertex. This is the alpha component of the specular RGBA.

The following figure illustrates a sample relationship between altitude and fog density in a layered atmosphere model.

:::image type="content" source="images/d3dfig25.png" alt-text="Diagram showing the relationship between altitude and fog density in a layered atmosphere model.":::

The fog blending factor is calculated during the lighting phase and is placed in the alpha component of the specular color value in the vertex. This should then be interpolated according to the current shade mode set up by the D3DRENDERSTATE_SHADEMODE render state.

The fog blending factors for vertices v1, v2, and v3 are determined by using the following calculations.

:::image type="content" source="images/d3dfig8.png" alt-text="Equations for calculating fog-blending factors for vertices v1, v2, and v3.":::

f1, f2, and f3 are interpolated across the triangle based on the current shade mode.

The new color, **C**, is obtained from the following formula:

```C = (1- f) \* fog_color + f \* src_color```

In this formula,

* **f** is the source, interpolated fog blending factor
* **fog_color** is the current fog color (set by the render state D3DRENDERSTATE_FOGCOLOR)
* **src_color** is the source, interpolated, textured color

If **f**, the fog blending factor, is 0.0, then **C** is set to a value identical to the fog color. If **f** is 1.0 there is no fog effect.

Fog factor in a vertex is a function of the distance from the camera position to the vertex. This distance could be approximated by taking only Z value in camera space. For per-vertex fog we compute (X<sub>c</sub>,Y<sub>c</sub>,Z<sub>c</sub>) in camera space by transforming the vertex using **Mworld\*Mview** and then compute the distance to the vertex.

In RGB mode, fog factor **f** is scaled to be in the range 0 through 255, and is written to the alpha component of the specular output color.

In Ramp mode, diffuse and specular components are multiplied by the fog factor **f** and are clamped to be in the range 0.0 through 1.0.
