---
title: Points to Consider when Restoring Complex Flipping Chains
description: Points to Consider when Restoring Complex Flipping Chains
ms.assetid: f368576f-a0a0-4def-888d-abf4fea8f6fb
keywords:
- context WDK Direct3D , D3dCreateSurfaceEx
- D3dCreateSurfaceEx
- flipping chain WDK Direct3D
- Z-buffer WDK Direct3D
- restoring flipping chains WDK Direct3D
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Points to Consider when Restoring Complex Flipping Chains


## <span id="ddk_points_to_consider_when_restoring_complex_flipping_chains_gg"></span><span id="DDK_POINTS_TO_CONSIDER_WHEN_RESTORING_COMPLEX_FLIPPING_CHAINS_GG"></span>


When a complex primary surface is created, it might or might not have an attached Z-buffer. When a surface is restored, it is possible that the application has added an attachment to a Z-buffer. Driver writers should be aware of these different scenarios when going through surface attachment lists in [**D3dCreateSurfaceEx**](https://msdn.microsoft.com/library/windows/hardware/ff542840).

A typical technique, presented in the *Perm3* sample driver, is to mark a surface's **dwReserved1** field when *D3dCreateSurfaceEx* is called for that surface. The driver only marks the surface if **fpVidMem** (a member of the [**DD\_SURFACE\_GLOBAL**](https://msdn.microsoft.com/library/windows/hardware/ff551726) structure) is not equal to zero. This is because **fpVidMem** could be zero because the application restored a primary surface that had a back buffer with an explicitly attached Z-buffer, but the Z-buffer had not yet been restored. At some later time, the application restores the Z-buffer, and the driver then marks it. If the application restores the Z-buffer before restoring the primary chain, the driver may receive the Z-buffer, already marked, attached to the back buffer when *D3dCreateSurfaceEx* is called.

**Note**   The Microsoft Windows Driver Kit (WDK) does not contain the 3Dlabs Permedia3 sample display driver (*Perm3.h*). You can get this sample driver from the Windows Server 2003 SP1 Driver Development Kit (DDK), which you can download from the DDK - Windows Driver Development Kit page of the WDHC website.

 

 

 





