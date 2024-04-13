---
title: GDI Support Services
description: GDI Support Services
keywords:
- GDI WDK Windows 2000 display , service routines
- graphics drivers WDK Windows 2000 display , service routines
- drawing WDK GDI , service routines
- service routines WDK GDI
ms.date: 04/20/2017
---

# GDI Support Services

*GDI* exports many service routines that can simplify driver design. The driver can call these routines directly. The names of routines that are general graphics engine services whose names begin with **Eng**. Service routines related to a particular object always start with the name of the object; for example, [**CLIPOBJ_cEnumStart**](/windows/win32/api/winddi/nf-winddi-clipobj_cenumstart) is a [**CLIPOBJ**](/windows/win32/api/winddi/ns-winddi-clipobj) service.

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

[Using the Graphics DDI](using-the-graphics-ddi.md) describes the graphics DDI entry points and also explains where many of these service routines can be used to help the driver implement the entry points.
