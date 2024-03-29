---
title: Cube Environment Map Support
description: Cube Environment Map Support
keywords:
- mapping cube environments
- environment mapping WDK Direct3D
- cube environment maps WDK Direct3D
- lighting WDK Direct3D
- reflections WDK Direct3D
- 360-degree environments WDK Direct3D
- real-time environment mapping WDK Direct3D
- circular maps WDK Direct3D
- spherical maps WDK Direct3D
ms.date: 04/20/2017
---

# Cube Environment Map Support


## <span id="ddk_cube_environment_map_support_gg"></span><span id="DDK_CUBE_ENVIRONMENT_MAP_SUPPORT_GG"></span>


Multiple texture support in Direct3D allows the use of environment maps for lighting and reflections. However, single-map 360-degree solutions like circular or spherical maps are not robust enough to be widely used in real time. The most suitable solution for real-time generation and addressing of a 360-degree environment is a cubical map, composed of six textures (faces). Each face can be generated by pointing a camera with a 90-degree field-of-view in the appropriate direction. Per-vertex vectors (normal, reflection, or refraction) are provided to the rasterization hardware that then iterates them across the polygon and calculates the intersections of the interpolated vectors with the faces of the cube map. If the application or API generates the cube environment map, the driver does not require the information about the transformation matrix or coordinate space in which the per-vertex vectors are defined. This is because the vectors are used only to address the environment map, which is logically in the same coordinate space.

Addressing of a circular map involves vector normalization; addressing of a spherical map requires the use of trigonometric functions. All types of single-map environments are nonlinear: a circular map is extremely distorted and anisotropic near its periphery, while a spherical map has large distortions near its poles. This makes it necessary to re-create the environment map every time the viewpoint changes in such a way that the central view area becomes distorted.

Cubical environment maps, formed by pointing a real or simulated camera with 90-degree field-of-view in six different directions, are free of these disadvantages. They can be generated faster but need to be updated less frequently, have fewer distortions, and can be addressed by using equations similar to the ones already used for perspective-correct texture mapping.

In general, cube maps are the best choice to provide real-time environment mapping for complex lighting and reflections.

The cube map enables are passed to the driver using the [**D3dDrawPrimitives2**](/windows-hardware/drivers/ddi/d3dhal/nc-d3dhal-lpd3dhal_drawprimitives2cb) render state mechanism. [FVF](fvf--flexible-vertex-format-.md) texture coordinates are passed with FVF code 01 for that texture coordinate set.

The cube map is defined in world coordinates; that is, its world transform matrix is the identity matrix. The cube map can appear to be in a different space if texture transforms are used on the corresponding texture coordinate indexes. These texture coordinate indexes will be looking directly at face four, the +z face. Y is up by default. The origin of the (u,v) texel grid is at the upper left corner of each face, in order to allow creation of the face without any additional transformations by pointing camera from the center of the cube.

**DirectDrawCreateEx** takes a flag that indicates a cube map is to be created. Some faces need not be allocated at the API level, although drivers may pad as required. The surface descriptor contains a bitfield with six bits indicating the faces that the application expects to use. When faces are attained with the **IDirectDrawSurface7::GetAttachedSurface** method , the **NULL** faces are skipped. The dimensions of each face are available from its surface descriptor, and the face bitcode field indicates which face it is. For more information about **DirectDrawCreateEx** and **IDirectDrawSurface7::GetAttachedSurface**, see the DirectDraw SDK documentation.

The pointer returned from **DirectDrawCreate** is actually a pointer to the first non-**NULL** face in the cube. The face identifier can be obtained by taking the surface's bitcode. This is the pointer that is passed to the **IDirect3DDevice7::SetTexture** method (described in the Direct3D SDK documentation) to make this map available in the multiple-texture pipeline.

If any of the surfaces are intended to be rendered to, the cube map must be created with the D3DPTEXTURECAPS\_CUBEMAP cap flag set.

Any faces not created by the call are assumed to be filled with the color specified in the surface descriptor's **dwEmptyFaceColor** member. (See the [**DDSURFACEDESC2**](/previous-versions/windows/hardware/drivers/ff550340(v=vs.85)) structure.)

**Note**   Current restrictions: All cube faces must be the same size and must be square. The cube faces can be MIP mapped. No color keying is supported with cube map textures. As with other textures, alpha channels and alpha palettes are supported.

 

 

