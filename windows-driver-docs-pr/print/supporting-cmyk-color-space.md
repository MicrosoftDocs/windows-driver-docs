---
title: Supporting CMYK Color Space
description: Supporting CMYK Color Space
ms.assetid: b8ac5f1a-c903-4313-b7de-0335f4c44367
keywords:
- CMYK color space WDK print
- BR_CMYKCOLOR
- XO_FROM_CMYK
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Supporting CMYK Color Space





Regardless of whether color management is being handled by the application, system, driver, or device, a printer graphics DLL color space. This is done by setting the GCAPS\_CMYKCOLOR flag in the [**DEVINFO**](https://docs.microsoft.com/windows/desktop/api/winddi/ns-winddi-tagdevinfo) structure. If this flag is set and CMYK profiles are in use, then GDI sends CMYK color data, instead of RGB data, to the printer graphics DLL for bitmaps, brushes, and pens. GDI also sets the following flags:

-   The BR\_CMYKCOLOR flag in the **flColorType** member of the [**BRUSHOBJ**](https://docs.microsoft.com/windows/desktop/api/winddi/ns-winddi-_brushobj) structure.

-   The XO\_FROM\_CMYK flag in the **flXlate** member of the [**XLATEOBJ**](https://docs.microsoft.com/windows/desktop/api/winddi/ns-winddi-_xlateobj) structure.

Note that if the driver supports CMYK color space, it must also support halftoning. Thus if the driver sets the GCAPS\_CMYKCOLOR flag in DEVINFO, it must also set GCAPS\_HALFTONE.

 

 




