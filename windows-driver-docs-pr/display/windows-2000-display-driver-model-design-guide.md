---
title: Windows 2000 Display Driver Model (XDDM) Design Guide
description: Windows 2000 Display Driver Model (XDDM) Design Guide
ms.assetid: 24cb232b-e289-45c8-8d55-42614a4dfd54
keywords: ["display devices WDK", "display driver model WDK Windows 2000", "Windows 2000 display driver model WDK", "display drivers WDK , Windows 2000"]
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

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Windows%202000%20Display%20Driver%20Model%20%28XDDM%29%20Design%20Guide%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




