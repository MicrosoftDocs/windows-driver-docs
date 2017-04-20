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
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Texture support


## <span id="ddk_texture_support_gg"></span><span id="DDK_TEXTURE_SUPPORT_GG"></span>


A texture in 3D space flips the same way as any other surface. A *texture* is just a flat image that has bits set to specify that it can be transformed (texture mapped) onto a 3D surface. A texture can be mapped onto a 3D surface and the motion can be rendered smoothly by page flipping the texture. Flip waits for the renderer to finish reading (like waiting for the scan line). If the flipping driver supports textures, it must be able to recognize and handle them appropriately. For more details on textures, see [Direct3D Texture Management](direct3d-texture-management.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Texture%20support%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




