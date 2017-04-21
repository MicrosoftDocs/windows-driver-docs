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
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Points to Consider when Restoring Complex Flipping Chains


## <span id="ddk_points_to_consider_when_restoring_complex_flipping_chains_gg"></span><span id="DDK_POINTS_TO_CONSIDER_WHEN_RESTORING_COMPLEX_FLIPPING_CHAINS_GG"></span>


When a complex primary surface is created, it might or might not have an attached Z-buffer. When a surface is restored, it is possible that the application has added an attachment to a Z-buffer. Driver writers should be aware of these different scenarios when going through surface attachment lists in [**D3dCreateSurfaceEx**](https://msdn.microsoft.com/library/windows/hardware/ff542840).

A typical technique, presented in the *Perm3* sample driver, is to mark a surface's **dwReserved1** field when *D3dCreateSurfaceEx* is called for that surface. The driver only marks the surface if **fpVidMem** (a member of the [**DD\_SURFACE\_GLOBAL**](https://msdn.microsoft.com/library/windows/hardware/ff551726) structure) is not equal to zero. This is because **fpVidMem** could be zero because the application restored a primary surface that had a back buffer with an explicitly attached Z-buffer, but the Z-buffer had not yet been restored. At some later time, the application restores the Z-buffer, and the driver then marks it. If the application restores the Z-buffer before restoring the primary chain, the driver may receive the Z-buffer, already marked, attached to the back buffer when *D3dCreateSurfaceEx* is called.

**Note**   The Microsoft Windows Driver Kit (WDK) does not contain the 3Dlabs Permedia3 sample display driver (*Perm3.h*). You can get this sample driver from the Windows Server 2003 SP1 Driver Development Kit (DDK), which you can download from the [DDK - Windows Driver Development Kit](http://go.microsoft.com/fwlink/p/?linkid=21859) page of the WDHC website.

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Points%20to%20Consider%20when%20Restoring%20Complex%20Flipping%20Chains%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




