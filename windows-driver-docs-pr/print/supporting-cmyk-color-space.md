---
title: Supporting CMYK Color Space
description: Supporting CMYK Color Space
keywords:
- CMYK color space WDK print
- BR_CMYKCOLOR
- XO_FROM_CMYK
ms.date: 01/30/2023
---

# Supporting CMYK Color Space

[!include[Print Support Apps](../includes/print-support-apps.md)]

Regardless of whether color management is being handled by the application, system, driver, or device, a [printer graphics DLL](printer-graphics-dll.md) must indicate whether it supports the *CMYK* color space. This is done by setting the GCAPS_CMYKCOLOR flag in the [**DEVINFO**](/windows/win32/api/winddi/ns-winddi-devinfo) structure. If this flag is set and CMYK profiles are in use, then GDI sends CMYK color data, instead of RGB data, to the printer graphics DLL for bitmaps, brushes, and pens. GDI also sets the following flags:

- The BR_CMYKCOLOR flag in the **flColorType** member of the [**BRUSHOBJ**](/windows/win32/api/winddi/ns-winddi-brushobj) structure.

- The XO_FROM_CMYK flag in the **flXlate** member of the [**XLATEOBJ**](/windows/win32/api/winddi/ns-winddi-xlateobj) structure.

If the driver supports CMYK color space, it must also support halftoning. Therefore, if the driver sets the GCAPS_CMYKCOLOR flag in DEVINFO, it must also set GCAPS_HALFTONE.
