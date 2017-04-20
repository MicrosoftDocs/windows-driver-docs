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
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Reporting Width and Height of Compressed Texture Surfaces


## <span id="ddk_reporting_width_and_height_of_compressed_texture_surfaces_gg"></span><span id="DDK_REPORTING_WIDTH_AND_HEIGHT_OF_COMPRESSED_TEXTURE_SURFACES_GG"></span>


When the DirectX runtime requests that a driver create a DXT*n* compressed texture surface whose width and height are less than 4x4, the driver actually allocates a 4x4 block of memory for the texture surface. However, the driver reports the width and height of the texture surface as the values that the runtime requested. For example, if a 2x2 DXT1 compressed texture surface is requested, the driver allocates a 4x4 block but reports that the block is 2x2 by leaving the requested texture size unchanged. To request a specific DXT*n* compressed texture size, the runtime sets the **dwWidth** and **dwHeight** members of a [**DDSURFACEDESC**](https://msdn.microsoft.com/library/windows/hardware/ff550339) or [**DDSURFACEDESC2**](https://msdn.microsoft.com/library/windows/hardware/ff550340) structure that represents the texture surface. The driver does not alter these size settings even if it allocates a 4x4 texture surface when the request is for a texture surface whose width and height are less than 4x4.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Reporting%20Width%20and%20Height%20of%20Compressed%20Texture%20Surfaces%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




