---
title: Using DXVA with 2D Operations
description: Using DXVA with 2D Operations
ms.assetid: a864941d-69ac-48a4-85a2-7e05cd3c9617
keywords:
- two-dimensional operations WDK DirectX 9.0 , DXVA
- 2D operations WDK DirectX 9.0 , DXVA
- DXVA WDK DirectX 9.0
- DXVA WDK DirectX 9.0 , 2D operations
- DirectX Video Acceleration WDK DirectX 9.0
- DirectX Video Acceleration WDK DirectX 9.0 , 2D operations
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Using DXVA with 2D Operations


## <span id="ddk_using_dxva_with_2d_operations_gg"></span><span id="DDK_USING_DXVA_WITH_2D_OPERATIONS_GG"></span>


DirectX 9.0 and later drivers use the D3DDP2OP\_BLT operation code to perform blits between [DirectX Video Acceleration](directx-video-acceleration.md) (DXVA) surfaces. Therefore, if the runtime detects a DirectX 9.0 or later driver, the runtime must call the driver's [**D3dCreateSurfaceEx**](https://msdn.microsoft.com/library/windows/hardware/ff542840) function to create any DXVA (or 2D-only) surface.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Using%20DXVA%20with%202D%20Operations%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




