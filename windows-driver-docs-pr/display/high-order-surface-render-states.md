---
title: High Order Surface Render States
description: High Order Surface Render States
keywords:
- DirectX 8.0 release notes WDK Windows 2000 display , high order surfaces, render states
- high order surfaces WDK DirectX 8.0 , render states
- render states WDK DirectX 8.0
- render states WDK DirectX 8.0 , high order surfaces
ms.date: 04/20/2017
---

# High Order Surface Render States


## <span id="ddk_high_order_surface_render_states_gg"></span><span id="DDK_HIGH_ORDER_SURFACE_RENDER_STATES_GG"></span>


There are three render states that are used with high order surfaces. These render states are described below.

### <span id="d3drs_patchedgestyle"></span><span id="D3DRS_PATCHEDGESTYLE"></span>D3DRS\_PATCHEDGESTYLE

This render state is used to control whether patch edges use discrete or continuous tessellation. See the DirectX 8.0 SDK documentation for more details.

### <span id="d3drs_patchsegments"></span><span id="D3DRS_PATCHSEGMENTS"></span>D3DRS\_PATCHSEGMENTS

This render state gives the number of segments to be used for each edge of the patch. If an explicit number of segments is specified in the DP2 token those segments should override the value of this render state. For more details, see the DirectX 8.0 SDK documentation.

### <span id="d3drs_deletertpatch"></span><span id="D3DRS_DELETERTPATCH"></span> D3DRS\_DELETERTPATCH

This render state notifies the driver that a patch is to be deleted. For more information, see [**D3DRENDERSTATETYPE**](/windows-hardware/drivers/ddi/d3d9types/ne-d3d9types-_d3drenderstatetype).

 

