---
title: Creating the Compressed Texture Surface
description: Creating the Compressed Texture Surface
ms.assetid: 6d1cc079-642c-4662-ae72-c0362d8a5b2a
keywords:
- drawing compressed textures WDK DirectDraw , creating
- DirectDraw compressed textures WDK Windows 2000 display , creating
- compressed texture surfaces WDK DirectDraw , creating
- surfaces WDK DirectDraw , compressed textures
- textures WDK DirectDraw , compressed
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Creating the Compressed Texture Surface


## <span id="ddk_creating_the_compressed_texture_surface_gg"></span><span id="DDK_CREATING_THE_COMPRESSED_TEXTURE_SURFACE_GG"></span>


Whenever DirectDraw requests the driver to create a surface, the driver must determine whether it is being asked to create a compressed texture surface. To determine this, the driver must check for information that has previously been set by DirectDraw in the [**DDSURFACEDESC2**](https://msdn.microsoft.com/library/windows/hardware/ff550340) structure for the surface being created. Your driver must include the following verification steps (as with any surface):

-   Check for the DDSCAPS\_TEXTURE flag in the **dwFlags** member of the [**DDSCAPS**](https://msdn.microsoft.com/library/windows/hardware/ff550286) structure.

-   Check for the DDPF\_FOURCC flag in the **dwFlags** member of the [**DDPIXELFORMAT**](https://msdn.microsoft.com/library/windows/hardware/ff550274) structure for the surface being created. This check should occur before the following **dwFourCC** check.

-   Check for one of the DXT codes in the **dwFourCC** member of the [**DDPIXELFORMAT**](https://msdn.microsoft.com/library/windows/hardware/ff550274) structure for the surface being created.

-   Check the width and height members (**dwWidth** and **dwHeight**) of the [**DDSURFACEDESC2**](https://msdn.microsoft.com/library/windows/hardware/ff550340) structure. DirectDraw sets these members to multiples of 4 pixels.

 

 





