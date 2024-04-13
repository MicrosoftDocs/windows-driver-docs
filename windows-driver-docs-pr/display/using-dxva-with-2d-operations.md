---
title: Using DXVA with 2D Operations
description: Using DXVA with 2D Operations
keywords:
- two-dimensional operations WDK DirectX 9.0 , DXVA
- 2D operations WDK DirectX 9.0 , DXVA
- DXVA WDK DirectX 9.0
- DXVA WDK DirectX 9.0 , 2D operations
- DirectX Video Acceleration WDK DirectX 9.0
- DirectX Video Acceleration WDK DirectX 9.0 , 2D operations
ms.date: 04/20/2017
---

# Using DXVA with 2D Operations


## <span id="ddk_using_dxva_with_2d_operations_gg"></span><span id="DDK_USING_DXVA_WITH_2D_OPERATIONS_GG"></span>


DirectX 9.0 and later drivers use the D3DDP2OP\_BLT operation code to perform blits between [DirectX Video Acceleration](directx-video-acceleration.md) (DXVA) surfaces. Therefore, if the runtime detects a DirectX 9.0 or later driver, the runtime must call the driver's [**D3dCreateSurfaceEx**](/windows/win32/api/ddrawint/nc-ddrawint-pdd_createsurfaceex) function to create any DXVA (or 2D-only) surface.

 

