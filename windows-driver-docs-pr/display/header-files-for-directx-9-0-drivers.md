---
title: Header Files for DirectX 9.0 Drivers
description: Header Files for DirectX 9.0 Drivers
ms.assetid: b8628c92-0983-4f3a-af64-ef54201ee689
keywords:
- header files WDK DirectX 9.0
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Header Files for DirectX 9.0 Drivers


## <span id="ddk_header_files_for_directx_9_0_drivers_gg"></span><span id="DDK_HEADER_FILES_FOR_DIRECTX_9_0_DRIVERS_GG"></span>


A DirectX 9.0 display driver's source code must include the *d3d9.h* header file. The header files *d3d9caps.h* and *d3d9types.h* are included in *d3d9.h*.

To support DirectX 8.1 and earlier versions of the DirectX runtime, the driver's source code must include both old and new DirectX headers, for example *d3d.h*, *d3d8.h*, and *d3d9.h*.

To avoid problems when building a DirectX 9.0 version driver, define DIRECT3D\_VERSION as 0x0900 in the driver's source code before including any header files. Doing so prevents the possibility of DirectX 9.0 features being missed as described in the [DIRECT3D\_VERSION](direct3d-version.md) topic. To ensure that the build process retrieves all the necessary symbols in header files, include *d3d9.h* and *d3d8.h* before *winddi.h* or *d3dnthal.h*.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Header%20Files%20for%20DirectX%209.0%20Drivers%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




