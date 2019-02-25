---
title: Reporting Width and Height of Compressed Texture Surfaces
description: Reporting Width and Height of Compressed Texture Surfaces
ms.assetid: 262262b6-9fef-4f28-beec-373f78a10f8f
keywords:
- surfaces WDK DirectDraw , compressed textures
- textures WDK DirectDraw , compressed
- drawing compressed textures WDK DirectDraw , width
- DirectDraw compressed textures WDK Windows 2000 display , width
- compressed texture surfaces WDK DirectDraw , width
- drawing compressed textures WDK DirectDraw , height
- DirectDraw compressed textures WDK Windows 2000 display , height
- compressed texture surfaces WDK DirectDraw , height
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Reporting Width and Height of Compressed Texture Surfaces


## <span id="ddk_reporting_width_and_height_of_compressed_texture_surfaces_gg"></span><span id="DDK_REPORTING_WIDTH_AND_HEIGHT_OF_COMPRESSED_TEXTURE_SURFACES_GG"></span>


When the DirectX runtime requests that a driver create a DXT*n* compressed texture surface whose width and height are less than 4x4, the driver actually allocates a 4x4 block of memory for the texture surface. However, the driver reports the width and height of the texture surface as the values that the runtime requested. For example, if a 2x2 DXT1 compressed texture surface is requested, the driver allocates a 4x4 block but reports that the block is 2x2 by leaving the requested texture size unchanged. To request a specific DXT*n* compressed texture size, the runtime sets the **dwWidth** and **dwHeight** members of a [**DDSURFACEDESC**](https://msdn.microsoft.com/library/windows/hardware/ff550339) or [**DDSURFACEDESC2**](https://msdn.microsoft.com/library/windows/hardware/ff550340) structure that represents the texture surface. The driver does not alter these size settings even if it allocates a 4x4 texture surface when the request is for a texture surface whose width and height are less than 4x4.

 

 





