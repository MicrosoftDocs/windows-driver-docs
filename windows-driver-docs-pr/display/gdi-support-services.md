---
title: GDI Support Services
description: GDI Support Services
ms.assetid: a5521f9f-ddf6-4892-bf6d-aebb7936df11
keywords:
- GDI WDK Windows 2000 display , service routines
- graphics drivers WDK Windows 2000 display , service routines
- drawing WDK GDI , service routines
- service routines WDK GDI
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# GDI Support Services


## <span id="ddk_gdi_support_services_gg"></span><span id="DDK_GDI_SUPPORT_SERVICES_GG"></span>


[*GDI*](https://msdn.microsoft.com/library/windows/hardware/ff556283#wdkgloss-graphics-device-interface--gdi-) exports many service routines that can simplify driver design. The driver can call these routines directly. The names of routines that are general graphics engine services whose names begin with **Eng**. Service routines related to a particular object always start with the name of the object; for example, [**CLIPOBJ\_cEnumStart**](https://msdn.microsoft.com/library/windows/hardware/ff539421) is a [**CLIPOBJ**](https://msdn.microsoft.com/library/windows/hardware/ff539417) service.

**Note**   The service routines in which the first argument is a pointer to a user object are methods on that user object, and are called using the usual C++ conventions. Therefore, drivers written in C++ can access the service routines as methods.

 

These service routines fall into the following categories:

[Surface management](gdi-support-for-surfaces.md)

[Palette services](gdi-support-for-palettes.md)

[Path services](gdi-services-for-paths.md)

[Window services](gdi-support-for-window-objects.md)

[Rendering services](gdi-drawing-and-related-services.md)

[Font and text services](gdi-font-and-text-services.md)

[Memory services](gdi-memory-services.md)

[Event services](gdi-event-services.md)

[File, Module, and Process services](gdi-file--module--and-process-services.md)

[Semaphore services](gdi-semaphore-services.md)

[Printer services](gdi-printer-services.md)

[Driver-related services](gdi-driver-related-services.md)

[Information services](gdi-information-services.md)

[Utility services](gdi-utility-services.md)

[Floating-point services](gdi-floating-point-services.md)

[Halftone services](gdi-halftone-services.md)

[Using the Graphics DDI](using-the-graphics-ddi.md) describes the graphics DDI entry points and also explains where many of these service routines can be used to help the driver implement the entry points. For detailed descriptions of each of the service functions, see [GDI Functions Called by Printer and Display Drivers](https://msdn.microsoft.com/library/windows/hardware/ff566544).

 

 





