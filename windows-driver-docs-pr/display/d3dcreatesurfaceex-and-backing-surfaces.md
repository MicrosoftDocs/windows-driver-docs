---
title: D3dCreateSurfaceEx and Backing Surfaces
description: D3dCreateSurfaceEx and Backing Surfaces
ms.assetid: aad37654-616f-4cbd-9a9c-07458fb61947
keywords:
- context WDK Direct3D , D3dCreateSurfaceEx
- D3dCreateSurfaceEx
- backing surfaces WDK Direct3D
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# D3dCreateSurfaceEx and Backing Surfaces


## <span id="ddk_d3dcreatesurfaceex_and_backing_surfaces_gg"></span><span id="DDK_D3DCREATESURFACEEX_AND_BACKING_SURFACES_GG"></span>


[**D3dCreateSurfaceEx**](https://msdn.microsoft.com/library/windows/hardware/ff542840) is also called for *backing surfaces*, which are system memory persistent copies of managed surfaces. This allows the driver to allocate a driver-side structure for the surface and respond to the D3DDP2OP\_TEXBLT token for a system to video texture download.

[**D3dCreateSurfaceEx**](https://msdn.microsoft.com/library/windows/hardware/ff542840) should never fail based on the format and capabilities of the backing surface requested because emulation code could support and handle the surface. However, other conditions for failure are valid. For example, the driver can fail **D3dCreateSurfaceEx** if it maintains private data structures and runs out of memory space.

The driver should not fail [**D3dCreateSurfaceEx**](https://msdn.microsoft.com/library/windows/hardware/ff542840) for backing surface formats for which it does not support the pixel format. Such surfaces may be created for use with the software rasterizer. The driver should simply ignore backing surfaces it does not support. (Alternatively, the driver can create a driver-side structure, but the corresponding handle is never subsequently sent to the driver.)

For these backing surfaces, [**D3dCreateSurfaceEx**](https://msdn.microsoft.com/library/windows/hardware/ff542840) causes a failure code to be propagated to the application; the driver can then potentially affect the application in emulation-only mode. A driver's response to such situations can be tested by running the *ddtest.exe* application that is located on the DirectX 7.0 SDK. Run *ddtest.exe* and try to create a backing surface texture of a format unsupported by the driver, but supported by the DirectDraw emulation layer (a list of these formats can be found in the DirectDraw SDK documentation).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20D3dCreateSurfaceEx%20and%20Backing%20Surfaces%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




