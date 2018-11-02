---
title: Windows 2000 Display Driver Model (XDDM) Design Guide
description: Windows 2000 Display Driver Model (XDDM) Design Guide
ms.assetid: 24cb232b-e289-45c8-8d55-42614a4dfd54
keywords:
- display devices WDK
- display driver model WDK Windows 2000
- Windows 2000 display driver model WDK
- display drivers WDK , Windows 2000
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Windows 2000 Display Driver Model (XDDM) Design Guide


## <span id="ddk_windows_2000_display_driver_model_gg"></span><span id="DDK_WINDOWS_2000_DISPLAY_DRIVER_MODEL_GG"></span>


Display adapter drivers that run on Windows Vista can adhere to one of two models: the [Windows Display Driver Model (WDDM)](windows-vista-display-driver-model-design-guide.md) or the Windows 2000 display driver model (XDDM). Drivers that adhere to Windows Display Driver Model (WDDM) run only on Windows Vista and later. Drivers that adhere to XDDM run on Windows 2000 and later operating systems (including Windows Vista and Windows 7).

**Note**  XDDM and VGA drivers will not compile on Windows 8 and later versions. If display hardware is attached to a Windows 8 computer without a driver that is certified to support WDDM 1.2 or later, the system defaults to running the Microsoft Basic Display Driver.

 

The following sections describe the Windows 2000 display driver model:

-   [Introduction to Display (Windows 2000 Model)](introduction-to-display--windows-2000-model-.md)

-   [Display Drivers (Windows 2000 Model)](display-drivers--windows-2000-model-.md)

-   [DirectDraw](directdraw.md)

-   [Direct3D DDI](direct3d.md)

-   [DirectX Video Acceleration](directx-video-acceleration.md)

-   [Video Miniport Drivers in the Windows 2000 Display Driver Model](video-miniport-drivers-in-the-windows-2000-display-driver-model.md)

-   [Implementation Tips and Requirements for the Windows Display Driver Model (WDDM)](implementation-tips-and-requirements-for-the-windows-vista-display-dri.md)

-   [GDI](gdi.md)

**Note**   The documentation for the Windows 2000 display driver model no longer includes information about how to create a display driver that runs on the Microsoft Windows 98/Me platforms. If you want to create a display driver for Windows 98/Me, you can use the WDK documentation that released with Windows Vista. You can obtain the WDK for Windows Vista RTM from the [Microsoft Connect website](http://go.microsoft.com/fwlink/p/?linkid=101629).

 

 

 





