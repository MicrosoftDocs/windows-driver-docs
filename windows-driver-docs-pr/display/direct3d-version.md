---
title: DIRECT3D_VERSION
description: DIRECT3D_VERSION
ms.assetid: 09032f06-d31f-4d9f-80bd-e6b9b8d5cbaa
keywords:
- DirectX 8.0 release notes WDK Windows 2000 display , header files
- header files WDK DirectX 8.0
- DIRECT3D_VERSION
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# DIRECT3D\_VERSION


## <span id="ddk_direct3d_version_gg"></span><span id="DDK_DIRECT3D_VERSION_GG"></span>


A DirectX display driver must support DirectX 7.0 and earlier versions of the DirectX runtime. To do that, it is necessary to include both old and new DirectX headers, for example *d3d.h* and *d3d8.h*. However, this can cause a problem with the definition of the preprocessor symbol DIRECT3D\_VERSION. This preprocessor symbol is used in the header files to indicate which structures and functions should be included. If the DIRECT3D\_VERSION has not already been defined, the DirectX header files set the value of DIRECT3D\_VERSION to the most recent version they were designed for. Thus, *d3d.h* sets DIRECT3D\_VERSION to 0x0700 and *d3d8.h* sets DIRECT3D\_VERSION to 0x0800. If *d3d.h* is included in your source before *d3d8.h*, new Direct3D 8.0 features are not defined and compiler errors will result.

To avoid this, define DIRECT3D\_VERSION to 0x0800 before including any header files. In order to get all the necessary symbols in header files, include d3d8.h before *winddi.h* or *d3dnthal.h*.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20DIRECT3D_VERSION%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




