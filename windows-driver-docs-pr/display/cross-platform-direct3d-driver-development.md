---
title: Cross Platform Direct3D Driver Development
description: Cross Platform Direct3D Driver Development
ms.assetid: 9363e0f9-4a58-4473-969f-eb54d0678632
keywords:
- Direct3D WDK Windows 2000 display , cross platform development
- cross-platform development WDK Direct3D
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Cross Platform Direct3D Driver Development


## <span id="ddk_cross_platform_direct3d_driver_development_gg"></span><span id="DDK_CROSS_PLATFORM_DIRECT3D_DRIVER_DEVELOPMENT_GG"></span>


The Microsoft Windows 2000 and later and Windows 98/Me Direct3D DDI types are not directly compatible when they are compiled, because of naming differences and some type changes of structure and function members in each DDI type. Logically however, equivalent members in each DDI type serve the same purpose.

If your code will be portable between Windows 2000 and later and Windows 98/Me, use *dx95type.h*, a utility file that is included in the Windows Driver Kit (WDK) and previous Driver Development Kits (DDKs). It contains type definitions and macros that map some naming differences that occur between the Windows 98/Me and Windows 2000 and later platforms, enabling common driver code to be used between them.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Cross%20Platform%20Direct3D%20Driver%20Development%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




