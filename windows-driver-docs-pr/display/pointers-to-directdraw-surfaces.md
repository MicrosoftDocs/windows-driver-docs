---
title: Pointers to DirectDraw Surfaces
description: Pointers to DirectDraw Surfaces
ms.assetid: 5d7c8b22-d2d3-4e40-b7b2-7277e051812c
keywords:
- context WDK Direct3D , DirectDraw surface pointers
- DirectDraw surface pointers WDK Direct3D
- surface pointers for DirectDraw WDK Direct3D
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Pointers to DirectDraw Surfaces


## <span id="ddk_pointers_to_directdraw_surfaces_gg"></span><span id="DDK_POINTERS_TO_DIRECTDRAW_SURFACES_GG"></span>


Driver writers might be tempted to keep a pointer to the DirectDrawSurface data structures inside their private driver-side surface structures. However, this practice does not succeed on Microsoft Windows 2000 and later because access to DirectDraw kernel-side data structures is mediated through a management scheme that insulates these structures from user mode and from drivers. [**EngLockDirectDrawSurface**](https://msdn.microsoft.com/library/windows/hardware/ff564966) provides a pointer to the structure that is valid until the [**EngUnlockDirectDrawSurface**](https://msdn.microsoft.com/library/windows/hardware/ff565042) routine is called.

Outside of this lock/unlock pair, the structure is not guaranteed to reside, or even exist, at the same location. Additionally, these lock/unlock pairs impede performance. If the driver keeps its own copies of the surface structures, then the locks are not needed. Updates to data within the driver-side surface structures are made during low-frequency calls like [**D3dCreateSurfaceEx**](https://msdn.microsoft.com/library/windows/hardware/ff542840). The result is that less code must be executed during high-frequency calls like [**D3dDrawPrimitives2**](https://msdn.microsoft.com/library/windows/hardware/ff544704).

 

 





