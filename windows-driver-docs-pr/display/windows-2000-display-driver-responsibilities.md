---
title: Windows 2000 Display Driver Responsibilities
description: Windows 2000 Display Driver Responsibilities
ms.assetid: ccd7ff38-a4a3-4917-bf59-c2a1b864d026
keywords:
- display driver model WDK Windows 2000 , responsibilities
- Windows 2000 display driver model WDK , responsibilities
- display drivers WDK Windows 2000 , about display drivers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Windows 2000 Display Driver Responsibilities


## <span id="ddk_display_driver_responsibilities_gg"></span><span id="DDK_DISPLAY_DRIVER_RESPONSIBILITIES_GG"></span>


A *display driver* is a kernel-mode DLL for which the primary responsibility is *rendering*. When an application calls a Win32 function with device-independent graphics requests, the Graphics Device Interface (GDI) interprets these instructions and calls the display driver. The display driver then translates these requests into commands for the video hardware to draw graphics on the screen.

The display driver can access the hardware directly. This is because there is a wide variety in graphics hardware capabilities, and because display is one of the most time-critical parts of any system. This accessibility and the wide scope of capabilities within GDI provide considerable flexibility when implementing a display driver.

-   By default, GDI handles drawing operations on [*standard format bitmaps*](https://msdn.microsoft.com/library/windows/hardware/ff556336#wdkgloss-standard-format-bitmap), such as on hardware that includes a [*frame buffer*](https://msdn.microsoft.com/library/windows/hardware/ff556280#wdkgloss-frame-buffer). A display driver can hook and implement any of the [drawing functions](optional-display-driver-functions.md) for which the hardware offers special support. For less time-critical operations and more complex operations not supported by the graphics adapter, the driver can punt functions back to GDI and allow GDI to do the work. See [Hooking Versus Punting](hooking-versus-punting.md) for details.

-   For especially time-critical operations, the display driver has direct access to video hardware registers. For example, the VGA display driver for *x*86 systems uses optimized assembly code to implement direct access to hardware registers for some drawing and text operations.
    **Note**   The video miniport driver must manage all resources (for example, memory resources) shared between the video miniport driver and the display driver. The system does not guarantee that resources acquired in the display driver will always be accessible to the video miniport driver.

     

The display driver is discussed in detail in [Display Drivers (Windows 2000 Model)](display-drivers--windows-2000-model-.md).

 

 





