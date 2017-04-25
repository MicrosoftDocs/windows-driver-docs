---
title: Point Sprites
description: Point Sprites
ms.assetid: 1841d68a-68c3-4522-8935-46bab9bb7c47
keywords:
- DirectX 8.0 release notes WDK Windows 2000 display , point sprites
- point sprites WDK DirectX 8.0
- size WDK point sprites
- point size WDK DirectX 8.0
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Point Sprites


## <span id="ddk_point_sprites_gg"></span><span id="DDK_POINT_SPRITES_GG"></span>


DirectX 8.0 introduces support for point sprites. A point sprite is an extension to basic point rendering that allows the size of the point to be specified, either by a render state or by a vertex component. When accelerated, the point sprites are rendered in hardware as a screen space quadrilateral formed of two triangles, and render states such as textures and blending are used.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Point%20Sprites%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




