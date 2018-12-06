---
title: MIP Map Surface Creation Update
description: MIP Map Surface Creation Update
ms.assetid: a89a11ed-d450-43bb-b0cd-75132d19dbc3
keywords:
- MIP map surfaces WDK Direct3D
- D3DRENDERSTATE_MIPMAPLODBIAS
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# MIP Map Surface Creation Update


## <span id="ddk_mip_map_surface_creation_update_gg"></span><span id="DDK_MIP_MAP_SURFACE_CREATION_UPDATE_GG"></span>


Before DirectX 7.0, the attachment chain for a MIP map usually consisted only of the sublevels of that MIP map. With the advent of cubic environment maps, this is no longer the case. Each face of a cubic environment may itself be a MIP map and, as such, the attachment chain of a surface forming one face of a cubic environment map can consist of links to the other faces of the cube map as well as links to sublevels of the MIP map.

As the attachment chain of a MIP map surface can now contain links to surfaces other than simply a lower level MIP map, a new capability bit has been introduced, DDSCAPS2\_MIPMAPSUBLEVEL (see the [**DDSCAPS2**](https://msdn.microsoft.com/library/windows/hardware/ff550292) structure for this and the following flags). This bit is set for all but the top-level surface of a MIP map chain. Thus, given the top-level surface of a MIP map chain you can find the surface representing the next lowest level of the MIP map chain by traversing the attachment list of the top-level surface looking for a surface with the DDSCAPS2\_MIPMAPSUBLEVEL capability bit set.

To determine if a surface is a face of a cubic environment map, check for the surface capability bit DDSCAPS2\_CUBEMAP. If the DDSCAPS\_MIPMAP capability bit is not set, the attachment list of this surface consists of the other faces of the cube map that are being created (check for the capability bits DDSCAPS2\_CUBEMAP\_POSITIVEX, DDSCAPS2\_CUBEMAP\_NEGATIVEX, DDSCAPS2\_CUBEMAP\_POSITIVEY, DDSCAPS2\_CUBEMAP\_NEGATIVEY, DDSCAPS2\_CUBEMAP\_POSITIVEZ, DDSCAPS2\_CUBEMAP\_NEGATIVEZ).

If the DDSCAPS\_MIPMAP capability bit is set then the attached surface list of the cube map surface consists of links to the other faces of the cube map as above and also to the next level of the MIP map for this face. The sublevel of the MIP map can be identified via the DDSCAPS2\_MIPMAPSUBLEVEL bit described above.

### <span id="d3drenderstate_mipmaplodbias"></span><span id="D3DRENDERSTATE_MIPMAPLODBIAS"></span>D3DRENDERSTATE\_MIPMAPLODBIAS

Although this render state is obsolete, its functionality has been moved into the texture stage states, that is, D3DRENDERSTATE\_MIPMAPLODBIAS is exactly equivalent to the D3DTSS\_MIPMAPLODBIAS enumerator in the D3DTEXTURESTAGESTATETYPE enumerated type for texture stage zero. On receiving the D3DRENDERSTATE\_MIPMAPLODBIAS render state through a legacy interface, your driver should simply map this to the same code that handles D3DTSS\_MIPMAPLODBIAS for texture stage zero.

The MIP map LOD bias is a floating-point value used to change the level of detail (LOD) bias. This value offsets the value of the MIP map level that is computed by trilinear texturing. It is usually in the range -1.0 to 1.0; the default value is 0.0. Current WHQL/DCT tests require the MIP map LOD bias to operate in the range -3.0 to 3.0.

Each unit bias (+/-1.0) biases the selection by exactly one MIP map level. A negative bias causes the use of larger MIP map levels, resulting in a sharper but more aliased image. A positive bias causes the use of smaller MIP map levels, resulting in a blurrier image. Applying a negative bias also results in the referencing of a smaller amount of texture data, which can boost performance on some systems.

**Note**   DirectX 9.0 and later applications can use the D3DSAMP\_MIPMAPLODBIAS value in the D3DSAMPLERSTATETYPE enumeration to control the level of detail bias for mipmaps. The runtime maps user-mode sampler states (D3DSAMP\_*Xxx*) to kernel-mode D3DTSS\_*Xxx* values so that drivers are not required to process user-mode sampler states. Drivers still should process the D3DTSS\_MIPMAPLODBIAS value. For more information about D3DSAMPLERSTATETYPE, see the latest DirectX SDK documentation.

 

 

 





