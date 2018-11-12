---
title: D3dCreateSurfaceEx Handles
description: D3dCreateSurfaceEx Handles
ms.assetid: ada78f89-422b-470d-9423-09968ae113e8
keywords:
- context WDK Direct3D , D3dCreateSurfaceEx
- D3dCreateSurfaceEx
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# D3dCreateSurfaceEx Handles


## <span id="ddk_d3dcreatesurfaceex_handles_gg"></span><span id="DDK_D3DCREATESURFACEEX_HANDLES_GG"></span>


Certain situations can cause [**D3dCreateSurfaceEx**](https://msdn.microsoft.com/library/windows/hardware/ff542840) to be called for an invalid, destroyed surface. Drivers can robustly handle this case by simply ignoring any **D3dCreateSurfaceEx** call for a video memory surface that has an **fpVidMem** (a member of the [**DD\_SURFACE\_GLOBAL**](https://msdn.microsoft.com/library/windows/hardware/ff551726) structure) of zero. However, a driver can get a **D3dCreateSurfaceEx** call with a system memory surface that has an **fpVidMem** value of zero, which means that the system memory surface is in the process of being destroyed. The driver should then free any existing driver-side data related to this surface.

 

 





