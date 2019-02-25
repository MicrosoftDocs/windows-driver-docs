---
title: Paletted Textures
description: Paletted Textures
ms.assetid: eac46256-db08-4a9b-aaaf-2bc8a9f30e98
keywords:
- texture management WDK Direct3D , paletted textures
- paletted textures WDK Direct3D
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Paletted Textures


## <span id="ddk_paletted_textures_gg"></span><span id="DDK_PALETTED_TEXTURES_GG"></span>


Direct3D allows palettes to be used with textures. A palette can be attached to a texture, just as it can to any other DirectDrawSurface object. To support paletted textures, drivers must respond to the D3DDP2OP\_SETPALETTE and D3DDP2OP\_UPDATEPALETTE operation codes in their implementation of [**D3dDrawPrimitives2**](https://msdn.microsoft.com/library/windows/hardware/ff544704). These operation codes are followed by [**D3DHAL\_DP2SETPALETTE**](https://msdn.microsoft.com/library/windows/hardware/ff545744) and [**D3DHAL\_DP2UPDATEPALETTE**](https://msdn.microsoft.com/library/windows/hardware/ff545923) structures, respectively, in the command stream. D3DDP2OP\_SETPALETTE creates an association between a palette handle and a surface handle (already created by [**D3dCreateSurfaceEx**](https://msdn.microsoft.com/library/windows/hardware/ff542840)). Later, D3DDP2OP\_UPDATEPALETTE can be sent multiple times to set the values of the palette entries for this texture.

 

 





