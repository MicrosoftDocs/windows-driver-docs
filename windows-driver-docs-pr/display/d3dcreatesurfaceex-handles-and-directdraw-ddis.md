---
title: D3dCreateSurfaceEx Handles and DirectDraw DDIs
description: D3dCreateSurfaceEx Handles and DirectDraw DDIs
ms.assetid: 626b04a2-3c50-425a-bbdf-3fb24fc95215
keywords:
- context WDK Direct3D , D3dCreateSurfaceEx
- D3dCreateSurfaceEx
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# D3dCreateSurfaceEx Handles and DirectDraw DDIs


## <span id="ddk_d3dcreatesurfaceex_handles_and_directdraw_ddis_gg"></span><span id="DDK_D3DCREATESURFACEEX_HANDLES_AND_DIRECTDRAW_DDIS_GG"></span>


Handles do not completely insulate a DirectX 7.0 driver from the DirectDraw-managed DDRAWI\_DDSURFACE\_MORE and DDRAWI\_DDSURFACE\_LCL structures. These structure names are essentially aliases for the structures [**DD\_SURFACE\_MORE**](https://msdn.microsoft.com/library/windows/hardware/ff551737) and [**DD\_SURFACE\_LOCAL**](https://msdn.microsoft.com/library/windows/hardware/ff551733). In DirectDraw DDIs such as [*DdBlt*](https://msdn.microsoft.com/library/windows/hardware/ff549205) and [*DdFlip*](https://msdn.microsoft.com/library/windows/hardware/ff549306), the driver is passed surface structure pointers, and must be able to use these structures instead of its private representations.

 

 





