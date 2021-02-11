---
title: Supporting CMYK Color Space
description: Supporting CMYK Color Space
keywords:
- CMYK color space WDK print
- BR_CMYKCOLOR
- XO_FROM_CMYK
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Supporting CMYK Color Space





Regardless of whether color management is being handled by the application, system, driver, or device, a [printer graphics DLL](printer-graphics-dll.md) must indicate whether it supports the *CMYK* color space. This is done by setting the GCAPS\_CMYKCOLOR flag in the [**DEVINFO**](/windows/win32/api/winddi/ns-winddi-devinfo) structure. If this flag is set and CMYK profiles are in use, then GDI sends CMYK color data, instead of RGB data, to the printer graphics DLL for bitmaps, brushes, and pens. GDI also sets the following flags:

-   The BR\_CMYKCOLOR flag in the **flColorType** member of the [**BRUSHOBJ**](/windows/win32/api/winddi/ns-winddi-brushobj) structure.

-   The XO\_FROM\_CMYK flag in the **flXlate** member of the [**XLATEOBJ**](/windows/win32/api/winddi/ns-winddi-xlateobj) structure.

Note that if the driver supports CMYK color space, it must also support halftoning. Thus if the driver sets the GCAPS\_CMYKCOLOR flag in DEVINFO, it must also set GCAPS\_HALFTONE.

 

