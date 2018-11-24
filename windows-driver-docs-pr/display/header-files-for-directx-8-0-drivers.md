---
title: Header Files for DirectX 8.0 Drivers
description: Header Files for DirectX 8.0 Drivers
ms.assetid: 716fc6dc-b1e9-4c81-ae84-03f8a91cc47f
keywords:
- DirectX 8.0 release notes WDK Windows 2000 display , header files
- header files WDK DirectX 8.0
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Header Files for DirectX 8.0 Drivers


## <span id="ddk_header_files_for_directx_8_0_drivers_gg"></span><span id="DDK_HEADER_FILES_FOR_DIRECTX_8_0_DRIVERS_GG"></span>


A DirectX 8.0 display driver's source code must include the *d3d8.h* header file. The header files *d3d8caps.h* and *d3d8types.h* are included in *d3d8.h*.

The DirectX 8.0 Driver Development Kit (DDK) introduces a new DDI-only header file called *d3dhalex.h*. This header file contains optional helper definitions and macros. Currently, this header contains some macros to assist with reporting D3DCAPS8 to the runtime.

 

 





