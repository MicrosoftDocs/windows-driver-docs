---
title: User Clip Planes
description: User Clip Planes
keywords:
- clip planes WDK Direct3D
- user-defined clip planes WDK Direct3D
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# User Clip Planes


## <span id="ddk_user_clip_planes_gg"></span><span id="DDK_USER_CLIP_PLANES_GG"></span>


User-defined clip planes are enabled for the latest DirectX release. These work just like other clip planes but they are settable by the application. The driver must handle these planes by responding to the D3DDP2OP\_SETCLIPPLANE operation code in [**D3dDrawPrimitives2**](/windows-hardware/drivers/ddi/d3dhal/nc-d3dhal-lpd3dhal_drawprimitives2cb).

 

