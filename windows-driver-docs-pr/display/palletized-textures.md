---
title: Palletized Textures
description: Palletized Textures
ms.assetid: 031739fe-32ee-46f1-a32a-de84f17eb528
keywords:
- DirectX 8.0 release notes WDK Windows 2000 display , palletized textures
- textures WDK DirectX 8.0
- palletized textures WDK DirectX 8.0
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Palletized Textures


## <span id="ddk_palettized_textures_gg"></span><span id="DDK_PALETTIZED_TEXTURES_GG"></span>


Although API support for palletized textures has been changed for DirectX 8.0, this is not reflected in the DDI. The existing palette-oriented DP2 tokens continue to be used to notify the driver of the binding between a palette and a texture and of updates to palettes.

It cannot be assumed, because an association between a surface and a palette has been established with D3DDP2OP\_SETPALETTE, that the **lpPalette** field of the surface structure points to a valid palette. The association between a palette and a surface established by the DP2 stream is not reflected in the actual surface and palette data structures.

Furthermore, DirectDraw's palette DDI entry points are not called for these palettes. All DDI notifications of texture palette operations are done through the DP2 stream.

 

 





