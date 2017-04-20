---
title: D3dCreateSurfaceEx Handles and DirectDraw DDIs
description: D3dCreateSurfaceEx Handles and DirectDraw DDIs
ms.assetid: 626b04a2-3c50-425a-bbdf-3fb24fc95215
keywords:
- context WDK Direct3D , D3dCreateSurfaceEx
- D3dCreateSurfaceEx
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# D3dCreateSurfaceEx Handles and DirectDraw DDIs


## <span id="ddk_d3dcreatesurfaceex_handles_and_directdraw_ddis_gg"></span><span id="DDK_D3DCREATESURFACEEX_HANDLES_AND_DIRECTDRAW_DDIS_GG"></span>


Handles do not completely insulate a DirectX 7.0 driver from the DirectDraw-managed DDRAWI\_DDSURFACE\_MORE and DDRAWI\_DDSURFACE\_LCL structures. These structure names are essentially aliases for the structures [**DD\_SURFACE\_MORE**](https://msdn.microsoft.com/library/windows/hardware/ff551737) and [**DD\_SURFACE\_LOCAL**](https://msdn.microsoft.com/library/windows/hardware/ff551733). In DirectDraw DDIs such as [*DdBlt*](https://msdn.microsoft.com/library/windows/hardware/ff549205) and [*DdFlip*](https://msdn.microsoft.com/library/windows/hardware/ff549306), the driver is passed surface structure pointers, and must be able to use these structures instead of its private representations.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20D3dCreateSurfaceEx%20Handles%20and%20DirectDraw%20DDIs%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




