---
title: Cross Platform Direct3D Driver Development
description: Cross Platform Direct3D Driver Development
ms.assetid: 9363e0f9-4a58-4473-969f-eb54d0678632
keywords:
- Direct3D WDK Windows 2000 display , cross platform development
- cross-platform development WDK Direct3D
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Cross Platform Direct3D Driver Development


## <span id="ddk_cross_platform_direct3d_driver_development_gg"></span><span id="DDK_CROSS_PLATFORM_DIRECT3D_DRIVER_DEVELOPMENT_GG"></span>


The Microsoft Windows 2000 and later and Windows 98/Me Direct3D DDI types are not directly compatible when they are compiled, because of naming differences and some type changes of structure and function members in each DDI type. Logically however, equivalent members in each DDI type serve the same purpose.

If your code will be portable between Windows 2000 and later and Windows 98/Me, use *dx95type.h*, a utility file that is included in the Windows Driver Kit (WDK) and previous Driver Development Kits (DDKs). It contains type definitions and macros that map some naming differences that occur between the Windows 98/Me and Windows 2000 and later platforms, enabling common driver code to be used between them.

 

 





