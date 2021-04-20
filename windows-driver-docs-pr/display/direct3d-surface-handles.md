---
title: Direct3D Surface Handles
description: Direct3D Surface Handles
keywords:
- context WDK Direct3D , surface handles
- surface handles WDK Direct3D
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Direct3D Surface Handles


## <span id="ddk_direct3d_surface_handles_gg"></span><span id="DDK_DIRECT3D_SURFACE_HANDLES_GG"></span>


The Microsoft DirectX 7.0 device driver interface (DDI) is designed to promote a model whereby the Direct3D runtime components parse as little of the command stream as possible before handing the commands to the driver. Additionally, the command stream should be formatted so that it can be used by future hardware.

One important change directed toward these goals is the movement of all surface-related data out of intermediate structures owned by the Direct3D/DirectDraw runtime into structures owned, updated, and formatted by the driver.

Surfaces are referred to by handles embedded in the command stream. In these high-frequency operations, the driver can look up its own representation of a surface from the handle, without resorting to locking a surface via helper functions such as [**EngLockDirectDrawSurface**](/windows/win32/api/winddi/nf-winddi-englockdirectdrawsurface).

The mechanism for assigning these handles is a driver entry point called [**D3dCreateSurfaceEx**](/windows/win32/api/ddrawint/nc-ddrawint-pdd_createsurfaceex). This entry point is called directly after calls to the existing [*DdCanCreateSurface*](/previous-versions/windows/hardware/drivers/ff549213(v=vs.85)) and [*DdCreateSurface*](/previous-versions/windows/hardware/drivers/ff549263(v=vs.85)) entry points, and after a video memory address and handle have been assigned to a surface. At **D3dCreateSurfaceEx** time, the driver copies all pertinent information out of the DirectDraw runtime's copy of the surface structure and into its own surface structure. Driver-side copies are required for surface data such as size, format, and **fpVidMem** (a member of the [**DD\_SURFACE\_GLOBAL**](/windows/win32/api/ddrawint/ns-ddrawint-dd_surface_global) structure).

Handles are guaranteed by the runtime to be unique for each device and for each process. Handles are not guaranteed to be unique for each context, and this has some implications for drivers that are discussed in greater detail in [Creating Driver-Side Surface Structures](creating-driver-side-surface-structures.md).

There is no corresponding **DestroySurfaceEx** call, so driver-side surface structures are destroyed at [*DdDestroySurface*](/windows/win32/api/ddrawint/nc-ddrawint-pdd_surfcb_destroysurface) time.

 

