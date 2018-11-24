---
title: Header Files for DirectX 9.0 Drivers
description: Header Files for DirectX 9.0 Drivers
ms.assetid: b8628c92-0983-4f3a-af64-ef54201ee689
keywords:
- header files WDK DirectX 9.0
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Header Files for DirectX 9.0 Drivers


## <span id="ddk_header_files_for_directx_9_0_drivers_gg"></span><span id="DDK_HEADER_FILES_FOR_DIRECTX_9_0_DRIVERS_GG"></span>


A DirectX 9.0 display driver's source code must include the *d3d9.h* header file. The header files *d3d9caps.h* and *d3d9types.h* are included in *d3d9.h*.

To support DirectX 8.1 and earlier versions of the DirectX runtime, the driver's source code must include both old and new DirectX headers, for example *d3d.h*, *d3d8.h*, and *d3d9.h*.

To avoid problems when building a DirectX 9.0 version driver, define DIRECT3D\_VERSION as 0x0900 in the driver's source code before including any header files. Doing so prevents the possibility of DirectX 9.0 features being missed as described in the [DIRECT3D\_VERSION](direct3d-version.md) topic. To ensure that the build process retrieves all the necessary symbols in header files, include *d3d9.h* and *d3d8.h* before *winddi.h* or *d3dnthal.h*.

 

 





