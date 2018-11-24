---
title: Texture support
description: Texture support
ms.assetid: 8ae4d4bf-9fef-4e5e-a88a-5cb93519c802
keywords:
- drawing page flips WDK DirectDraw , textures
- DirectDraw flipping WDK Windows 2000 display , textures
- page flipping WDK DirectDraw , textures
- flipping WDK DirectDraw , textures
- textures WDK DirectDraw , flipping
- 3D surface flips WDK DirectDraw
- surfaces WDK DirectDraw , flipping
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Texture support


## <span id="ddk_texture_support_gg"></span><span id="DDK_TEXTURE_SUPPORT_GG"></span>


A texture in 3D space flips the same way as any other surface. A *texture* is just a flat image that has bits set to specify that it can be transformed (texture mapped) onto a 3D surface. A texture can be mapped onto a 3D surface and the motion can be rendered smoothly by page flipping the texture. Flip waits for the renderer to finish reading (like waiting for the scan line). If the flipping driver supports textures, it must be able to recognize and handle them appropriately. For more details on textures, see [Direct3D Texture Management](direct3d-texture-management.md).

 

 





