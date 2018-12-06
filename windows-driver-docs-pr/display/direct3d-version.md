---
title: DIRECT3D_VERSION
description: DIRECT3D_VERSION
ms.assetid: 09032f06-d31f-4d9f-80bd-e6b9b8d5cbaa
keywords:
- DirectX 8.0 release notes WDK Windows 2000 display , header files
- header files WDK DirectX 8.0
- DIRECT3D_VERSION
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# DIRECT3D\_VERSION


## <span id="ddk_direct3d_version_gg"></span><span id="DDK_DIRECT3D_VERSION_GG"></span>


A DirectX display driver must support DirectX 7.0 and earlier versions of the DirectX runtime. To do that, it is necessary to include both old and new DirectX headers, for example *d3d.h* and *d3d8.h*. However, this can cause a problem with the definition of the preprocessor symbol DIRECT3D\_VERSION. This preprocessor symbol is used in the header files to indicate which structures and functions should be included. If the DIRECT3D\_VERSION has not already been defined, the DirectX header files set the value of DIRECT3D\_VERSION to the most recent version they were designed for. Thus, *d3d.h* sets DIRECT3D\_VERSION to 0x0700 and *d3d8.h* sets DIRECT3D\_VERSION to 0x0800. If *d3d.h* is included in your source before *d3d8.h*, new Direct3D 8.0 features are not defined and compiler errors will result.

To avoid this, define DIRECT3D\_VERSION to 0x0800 before including any header files. In order to get all the necessary symbols in header files, include d3d8.h before *winddi.h* or *d3dnthal.h*.

 

 





