---
title: Palletized Textures
description: Palletized Textures
ms.assetid: 031739fe-32ee-46f1-a32a-de84f17eb528
keywords:
- DirectX 8.0 release notes WDK Windows 2000 display , palletized textures
- textures WDK DirectX 8.0
- palletized textures WDK DirectX 8.0
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Palletized Textures


## <span id="ddk_palettized_textures_gg"></span><span id="DDK_PALETTIZED_TEXTURES_GG"></span>


Although API support for palletized textures has been changed for DirectX 8.0, this is not reflected in the DDI. The existing palette-oriented DP2 tokens continue to be used to notify the driver of the binding between a palette and a texture and of updates to palettes.

It cannot be assumed, because an association between a surface and a palette has been established with D3DDP2OP\_SETPALETTE, that the **lpPalette** field of the surface structure points to a valid palette. The association between a palette and a surface established by the DP2 stream is not reflected in the actual surface and palette data structures.

Furthermore, DirectDraw's palette DDI entry points are not called for these palettes. All DDI notifications of texture palette operations are done through the DP2 stream.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Palletized%20Textures%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




