---
title: Direct3D Texture Management
description: Direct3D Texture Management
keywords:
- texture management WDK Direct3D
- Direct3D WDK Windows 2000 display , texture management
- texture management WDK Direct3D , about texture management
ms.date: 04/20/2017
---

# Direct3D Texture Management


## <span id="ddk_direct3d_texture_management_gg"></span><span id="DDK_DIRECT3D_TEXTURE_MANAGEMENT_GG"></span>


Although texture support is optional, most of today's drivers are capable of supporting it. Drivers that support texture mapping must respond to all of the texture-related operation codes in the Microsoft Direct3D DDI. For more information about texture-related operation codes, see [**D3DHAL\_DP2OPERATION**](/windows-hardware/drivers/ddi/d3dhal/ne-d3dhal-_d3dhal_dp2operation).

Drivers must also validate the texture stage states with the [**D3dValidateTextureStageState**](/windows-hardware/drivers/ddi/d3dhal/nc-d3dhal-lpd3dhal_validatetexturestagestatecb) callback.

The following sections describe how drivers implement support for textures:

[Multiple Textures](multiple-textures.md)

[Paletted Textures](paletted-textures.md)

[Texture Blitting](texture-blitting.md)

[Driver-Managed Textures](driver-managed-textures.md)

[Driver-Managed Resources](driver-managed-resources.md)

 

