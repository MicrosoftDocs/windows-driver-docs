---
title: D3dCreateSurfaceEx and Complex Surfaces
description: D3dCreateSurfaceEx and Complex Surfaces
ms.assetid: aabe01bd-a7b8-4533-970e-4e1e49ba6596
keywords:
- context WDK Direct3D , D3dCreateSurfaceEx
- D3dCreateSurfaceEx
- complex surfaces WDK Direct3D
- implicit surface attachments WDK Direct3D
- explicit surface attachments WDK Direct3D
- surface attachments WDK Direct3D
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# D3dCreateSurfaceEx and Complex Surfaces


## <span id="ddk_d3dcreatesurfaceex_and_complex_surfaces_gg"></span><span id="DDK_D3DCREATESURFACEEX_AND_COMPLEX_SURFACES_GG"></span>


As explained in [Creating and Destroying DirectDraw Surfaces](creating-and-destroying-directdraw-surfaces.md) in the DirectDraw documentation, creation of a complex surface causes an array of surfaces to be passed to [*DdCreateSurface*](https://msdn.microsoft.com/library/windows/hardware/ff549263). However, even in complex cases, only a pointer to the root surface is passed to [**D3dCreateSurfaceEx**](https://msdn.microsoft.com/library/windows/hardware/ff542840). It is necessary for the driver to go through the attachment lists of the root surface and create driver-side copies for all attached surfaces. This can be a difficult operation if the driver is attempting to handle creations for cube maps or MIP maps.

There are two types of DirectDraw surface attachments, implicit and explicit. An implicit attachment is formed during a complex surface creation. For example, when an application creates a primary flipping chain, the primary and back buffer are created by a single **CreateSurface** API call and are attached to one another implicitly by the **CreateSurface** call. Another example is a MIP map chain where a series of MIP maps are created by a single **CreateSurface** API call. An explicit attachment is formed when surfaces created from different **CreateSurface** calls are attached explicitly by **AddAttachedSurface**.

How and when the DirectX runtime calls a driver's [**D3dCreateSurfaceEx**](https://msdn.microsoft.com/library/windows/hardware/ff542840) function and how the driver processes surfaces depends on whether those surfaces are attached implicitly or explicitly. When two surfaces are explicitly attached, then both of those surfaces were created by separate calls to **CreateSurface** and each surface will have resulted in a call to **D3dCreateSurfaceEx** before the surface attachment was made. However, in the case of an implicitly attached surface, only a single **CreateSurface** and **D3dCreateSurfaceEx** call is made for the entire chain of surfaces. Therefore, when processing a **D3dCreateSurfaceEx** call, a driver must run the attached list of surfaces to identify handles and create driver side data structures for each attached surface. However, the attached surface list may contain a mixture of implicitly and explicitly attached surfaces. The driver will already have been notified of explicitly attached surfaces by **D3dCreateSurfaceEx** and probably will not want to process such surfaces again.

The driver can distinguish between implicit and explicit attachments by means of the DDAL\_IMPLICIT flag stored in the **dwFlags** field of the [**DD\_ATTACHLIST**](https://msdn.microsoft.com/library/windows/hardware/ff550466) data structure. If DDAL\_IMPLICIT is set in the **dwFlags** field, the attachment is implicit and no separate [**D3dCreateSurfaceEx**](https://msdn.microsoft.com/library/windows/hardware/ff542840) call is seen for the attached surface. If this flag is not set, the attachment is explicit and the attached surface results in its own **D3dCreateSurfaceEx** call. By examining this flag, the driver can determine whether it must process an attached surface as part of the parent surface's **D3dCreateSurfaceEx** call or whether a separate **D3dCreateSurfaceEx** call will have been made for the attached surface.

For more information, see the section on surface attachments in [DirectDraw Driver Fundamentals](directdraw-driver-fundamentals.md) and see the sample code included in [**D3dCreateSurfaceEx**](https://msdn.microsoft.com/library/windows/hardware/ff542840).

 

 





