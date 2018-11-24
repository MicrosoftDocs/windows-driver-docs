---
title: Direct3D Texture Management
description: Direct3D Texture Management
ms.assetid: d67ce56b-ed76-413f-b09f-e25400f1ac6d
keywords:
- texture management WDK Direct3D
- Direct3D WDK Windows 2000 display , texture management
- texture management WDK Direct3D , about texture management
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Direct3D Texture Management


## <span id="ddk_direct3d_texture_management_gg"></span><span id="DDK_DIRECT3D_TEXTURE_MANAGEMENT_GG"></span>


Although texture support is optional, most of today's drivers are capable of supporting it. Drivers that support texture mapping must respond to all of the texture-related operation codes in the Microsoft Direct3D DDI. For more information about texture-related operation codes, see [**D3DHAL\_DP2OPERATION**](https://msdn.microsoft.com/library/windows/hardware/ff545678).

Drivers must also validate the texture stage states with the [**D3dValidateTextureStageState**](https://msdn.microsoft.com/library/windows/hardware/ff549064) callback.

The following sections describe how drivers implement support for textures:

[Multiple Textures](multiple-textures.md)

[Paletted Textures](paletted-textures.md)

[Texture Blitting](texture-blitting.md)

[Driver-Managed Textures](driver-managed-textures.md)

[Driver-Managed Resources](driver-managed-resources.md)

 

 





