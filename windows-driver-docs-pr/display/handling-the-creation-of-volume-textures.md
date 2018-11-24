---
title: Handling the Creation of Volume Textures
description: Handling the Creation of Volume Textures
ms.assetid: d5f521df-cd52-4c7e-9ad2-5df343c96e8c
keywords:
- textures WDK DirectX 8.0
- DirectX 8.0 release notes WDK Windows 2000 display , volume textures
- volume textures WDK DirectX 8.0
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Handling the Creation of Volume Textures


## <span id="ddk_handling_the_creation_of_volume_textures_gg"></span><span id="DDK_HANDLING_THE_CREATION_OF_VOLUME_TEXTURES_GG"></span>


DirectX 8.0 introduces a new surface capability bit DDSCAPS2\_VOLUME. This flag is set in the **ddsCapsEx.dwCaps2** field of the surface's [**DD\_SURFACE\_MORE**](https://msdn.microsoft.com/library/windows/hardware/ff551737) structure. In the [*DdCreateSurface*](https://msdn.microsoft.com/library/windows/hardware/ff549263) and [**D3dCreateSurfaceEx**](https://msdn.microsoft.com/library/windows/hardware/ff542840) callbacks the depth of the volume texture can be found in the low word of the **dwCaps4** field of the extended surface capabilities (**ddsCapsEx**) of the surface's DD\_SURFACE\_MORE structure. The driver should return the "slice pitch" (that is, the number of bytes to add to move from one 2D slice of the volume to the next) of the volume texture in the **dwBlockSizeY** field of the surface global structure.

 

 





