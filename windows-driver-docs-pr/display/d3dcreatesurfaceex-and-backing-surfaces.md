---
title: D3dCreateSurfaceEx and Backing Surfaces
description: D3dCreateSurfaceEx and Backing Surfaces
ms.assetid: aad37654-616f-4cbd-9a9c-07458fb61947
keywords:
- context WDK Direct3D , D3dCreateSurfaceEx
- D3dCreateSurfaceEx
- backing surfaces WDK Direct3D
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# D3dCreateSurfaceEx and Backing Surfaces


## <span id="ddk_d3dcreatesurfaceex_and_backing_surfaces_gg"></span><span id="DDK_D3DCREATESURFACEEX_AND_BACKING_SURFACES_GG"></span>


[**D3dCreateSurfaceEx**](https://msdn.microsoft.com/library/windows/hardware/ff542840) is also called for *backing surfaces*, which are system memory persistent copies of managed surfaces. This allows the driver to allocate a driver-side structure for the surface and respond to the D3DDP2OP\_TEXBLT token for a system to video texture download.

[**D3dCreateSurfaceEx**](https://msdn.microsoft.com/library/windows/hardware/ff542840) should never fail based on the format and capabilities of the backing surface requested because emulation code could support and handle the surface. However, other conditions for failure are valid. For example, the driver can fail **D3dCreateSurfaceEx** if it maintains private data structures and runs out of memory space.

The driver should not fail [**D3dCreateSurfaceEx**](https://msdn.microsoft.com/library/windows/hardware/ff542840) for backing surface formats for which it does not support the pixel format. Such surfaces may be created for use with the software rasterizer. The driver should simply ignore backing surfaces it does not support. (Alternatively, the driver can create a driver-side structure, but the corresponding handle is never subsequently sent to the driver.)

For these backing surfaces, [**D3dCreateSurfaceEx**](https://msdn.microsoft.com/library/windows/hardware/ff542840) causes a failure code to be propagated to the application; the driver can then potentially affect the application in emulation-only mode. A driver's response to such situations can be tested by running the *ddtest.exe* application that is located on the DirectX 7.0 SDK. Run *ddtest.exe* and try to create a backing surface texture of a format unsupported by the driver, but supported by the DirectDraw emulation layer (a list of these formats can be found in the DirectDraw SDK documentation).

 

 





