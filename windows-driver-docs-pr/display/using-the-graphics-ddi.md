---
title: Using the Graphics DDI
description: Using the Graphics DDI
ms.assetid: e48d117b-8c1c-4617-84f8-b0b489b1083a
keywords:
- drawing WDK GDI , DDI
- GDI WDK Windows 2000 display , DDI
- graphics drivers WDK Windows 2000 display , DDI
- DDI WDK graphics
- GDI WDK Windows 2000 display , functions
- graphics drivers WDK Windows 2000 display , functions
- functions WDK graphics
- drawing WDK GDI , functions
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Using the Graphics DDI


## <span id="ddk_using_the_graphics_ddi_gg"></span><span id="DDK_USING_THE_GRAPHICS_DDI_GG"></span>


In response to device-independent application calls routed through the Graphics Device Interface (GDI), a graphics driver must ensure that its graphics device produces the required output. A graphics driver controls graphics output by implementing as much of the graphics Device Driver Interface (DDI) as is necessary.

Graphics DDI function names are in the *DrvXxx* form. GDI calls these *DrvXxx* functions to pass data to the driver. When an application makes a request of GDI, and GDI determines that the driver supports the relevant function, GDI calls that function. It is the responsibility of the driver to provide the function and return to GDI upon the function's completion.

This section describes the graphics DDI functions that writers of display and printer drivers must be aware of. Graphics DDI function declarations, structure definitions, and constants can be found in *winddi.h*. For more information about the graphics DDI functions, see [GDI Functions Implemented by Printer and Display Drivers](https://msdn.microsoft.com/library/windows/hardware/ff566549).

The topics contained in this section are as follows:

[Graphics Driver Functions](graphics-driver-functions.md)

[Supporting Initialization and Termination Functions](supporting-initialization-and-termination-functions.md)

[Floating-Point Operations in Graphics Driver Functions](floating-point-operations-in-graphics-driver-functions.md)

[Creating Device-Dependent Bitmaps](creating-device-dependent-bitmaps.md)

[Supporting Graphics Output](supporting-graphics-output.md)

[Supporting Graphics DDI Color and Pattern Functions](supporting-graphics-ddi-color-and-pattern-functions.md)

[Supporting Graphics DDI Font and Text Functions](supporting-graphics-ddi-font-and-text-functions.md)

[The DEVMODEW Structure](the-devmodew-structure.md)

 

 





