---
title: Pointers to DirectDraw Surfaces
description: Pointers to DirectDraw Surfaces
ms.assetid: 5d7c8b22-d2d3-4e40-b7b2-7277e051812c
keywords:
- context WDK Direct3D , DirectDraw surface pointers
- DirectDraw surface pointers WDK Direct3D
- surface pointers for DirectDraw WDK Direct3D
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Pointers to DirectDraw Surfaces


## <span id="ddk_pointers_to_directdraw_surfaces_gg"></span><span id="DDK_POINTERS_TO_DIRECTDRAW_SURFACES_GG"></span>


Driver writers might be tempted to keep a pointer to the DirectDrawSurface data structures inside their private driver-side surface structures. However, this practice does not succeed on Microsoft Windows 2000 and later because access to DirectDraw kernel-side data structures is mediated through a management scheme that insulates these structures from user mode and from drivers. [**EngLockDirectDrawSurface**](https://msdn.microsoft.com/library/windows/hardware/ff564966) provides a pointer to the structure that is valid until the [**EngUnlockDirectDrawSurface**](https://msdn.microsoft.com/library/windows/hardware/ff565042) routine is called.

Outside of this lock/unlock pair, the structure is not guaranteed to reside, or even exist, at the same location. Additionally, these lock/unlock pairs impede performance. If the driver keeps its own copies of the surface structures, then the locks are not needed. Updates to data within the driver-side surface structures are made during low-frequency calls like [**D3dCreateSurfaceEx**](https://msdn.microsoft.com/library/windows/hardware/ff542840). The result is that less code must be executed during high-frequency calls like [**D3dDrawPrimitives2**](https://msdn.microsoft.com/library/windows/hardware/ff544704).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Pointers%20to%20DirectDraw%20Surfaces%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




