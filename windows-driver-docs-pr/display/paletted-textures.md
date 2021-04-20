---
title: Paletted Textures
description: Paletted Textures
keywords:
- texture management WDK Direct3D , paletted textures
- paletted textures WDK Direct3D
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Paletted Textures


## <span id="ddk_paletted_textures_gg"></span><span id="DDK_PALETTED_TEXTURES_GG"></span>


Direct3D allows palettes to be used with textures. A palette can be attached to a texture, just as it can to any other DirectDrawSurface object. To support paletted textures, drivers must respond to the D3DDP2OP\_SETPALETTE and D3DDP2OP\_UPDATEPALETTE operation codes in their implementation of [**D3dDrawPrimitives2**](/windows-hardware/drivers/ddi/d3dhal/nc-d3dhal-lpd3dhal_drawprimitives2cb). These operation codes are followed by [**D3DHAL\_DP2SETPALETTE**](/windows-hardware/drivers/ddi/d3dhal/ns-d3dhal-_d3dhal_dp2setpalette) and [**D3DHAL\_DP2UPDATEPALETTE**](/windows-hardware/drivers/ddi/d3dhal/ns-d3dhal-_d3dhal_dp2updatepalette) structures, respectively, in the command stream. D3DDP2OP\_SETPALETTE creates an association between a palette handle and a surface handle (already created by [**D3dCreateSurfaceEx**](/windows/win32/api/ddrawint/nc-ddrawint-pdd_createsurfaceex)). Later, D3DDP2OP\_UPDATEPALETTE can be sent multiple times to set the values of the palette entries for this texture.

 

