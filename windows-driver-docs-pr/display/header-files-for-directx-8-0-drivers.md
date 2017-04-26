---
title: Header Files for DirectX 8.0 Drivers
description: Header Files for DirectX 8.0 Drivers
ms.assetid: 716fc6dc-b1e9-4c81-ae84-03f8a91cc47f
keywords:
- DirectX 8.0 release notes WDK Windows 2000 display , header files
- header files WDK DirectX 8.0
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Header Files for DirectX 8.0 Drivers


## <span id="ddk_header_files_for_directx_8_0_drivers_gg"></span><span id="DDK_HEADER_FILES_FOR_DIRECTX_8_0_DRIVERS_GG"></span>


A DirectX 8.0 display driver's source code must include the *d3d8.h* header file. The header files *d3d8caps.h* and *d3d8types.h* are included in *d3d8.h*.

The DirectX 8.0 Driver Development Kit (DDK) introduces a new DDI-only header file called *d3dhalex.h*. This header file contains optional helper definitions and macros. Currently, this header contains some macros to assist with reporting D3DCAPS8 to the runtime.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Header%20Files%20for%20DirectX%208.0%20Drivers%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




