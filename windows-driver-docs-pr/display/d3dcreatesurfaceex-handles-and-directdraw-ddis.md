---
title: D3dCreateSurfaceEx Handles and DirectDraw DDIs
description: D3dCreateSurfaceEx Handles and DirectDraw DDIs
keywords:
- context WDK Direct3D , D3dCreateSurfaceEx
- D3dCreateSurfaceEx
ms.date: 04/20/2017
---

# D3dCreateSurfaceEx Handles and DirectDraw DDIs


## <span id="ddk_d3dcreatesurfaceex_handles_and_directdraw_ddis_gg"></span><span id="DDK_D3DCREATESURFACEEX_HANDLES_AND_DIRECTDRAW_DDIS_GG"></span>


Handles do not completely insulate a DirectX 7.0 driver from the DirectDraw-managed DDRAWI\_DDSURFACE\_MORE and DDRAWI\_DDSURFACE\_LCL structures. These structure names are essentially aliases for the structures [**DD\_SURFACE\_MORE**](/windows/win32/api/ddrawint/ns-ddrawint-dd_surface_more) and [**DD\_SURFACE\_LOCAL**](/windows/win32/api/ddrawint/ns-ddrawint-dd_surface_local). In DirectDraw DDIs such as [*DdBlt*](/windows/win32/api/ddrawint/nc-ddrawint-pdd_surfcb_blt) and [*DdFlip*](/windows/win32/api/ddrawint/nc-ddrawint-pdd_surfcb_flip), the driver is passed surface structure pointers, and must be able to use these structures instead of its private representations.

 

