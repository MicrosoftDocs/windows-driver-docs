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
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Creating the Compressed Texture Surface


## <span id="ddk_creating_the_compressed_texture_surface_gg"></span><span id="DDK_CREATING_THE_COMPRESSED_TEXTURE_SURFACE_GG"></span>


Whenever DirectDraw requests the driver to create a surface, the driver must determine whether it is being asked to create a compressed texture surface. To determine this, the driver must check for information that has previously been set by DirectDraw in the [**DDSURFACEDESC2**](https://msdn.microsoft.com/library/windows/hardware/ff550340) structure for the surface being created. Your driver must include the following verification steps (as with any surface):

-   Check for the DDSCAPS\_TEXTURE flag in the **dwFlags** member of the [**DDSCAPS**](https://msdn.microsoft.com/library/windows/hardware/ff550286) structure.

-   Check for the DDPF\_FOURCC flag in the **dwFlags** member of the [**DDPIXELFORMAT**](https://msdn.microsoft.com/library/windows/hardware/ff550274) structure for the surface being created. This check should occur before the following **dwFourCC** check.

-   Check for one of the DXT codes in the **dwFourCC** member of the [**DDPIXELFORMAT**](https://msdn.microsoft.com/library/windows/hardware/ff550274) structure for the surface being created.

-   Check the width and height members (**dwWidth** and **dwHeight**) of the [**DDSURFACEDESC2**](https://msdn.microsoft.com/library/windows/hardware/ff550340) structure. DirectDraw sets these members to multiples of 4 pixels.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Creating%20the%20Compressed%20Texture%20Surface%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




