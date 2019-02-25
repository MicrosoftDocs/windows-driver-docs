---
title: D3dCreateSurfaceEx and MIP Maps
description: D3dCreateSurfaceEx and MIP Maps
ms.assetid: d0f4ee41-7622-4153-877c-17c88f8147a9
keywords:
- MIP map surfaces WDK Direct3D
- context WDK Direct3D , D3dCreateSurfaceEx
- D3dCreateSurfaceEx
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# D3dCreateSurfaceEx and MIP Maps


## <span id="ddk_d3dcreatesurfaceex_and_mip_maps_gg"></span><span id="DDK_D3DCREATESURFACEEX_AND_MIP_MAPS_GG"></span>


Each level in a MIP map is associated with a different handle value. These handles might not be consecutive, however. The Direct3D DDI is designed so that only the top-level surface's handle is passed as an argument in the **IDirect3DDevice7::SetTexture** API method (described in the Direct3D SDK documentation), and then the current level-of-detail is specified by a texture stage state (D3DTSS\_MAXMIPLEVEL). The most natural way to work with MIP maps is to build one driver-side structure that represents the entire MIP map.

 

 





