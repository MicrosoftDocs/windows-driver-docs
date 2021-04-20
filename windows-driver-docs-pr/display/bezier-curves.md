---
title: Bezier Curves
description: Bezier Curves
keywords:
- GDI WDK Windows 2000 display , curves, Bezier
- graphics drivers WDK Windows 2000 display , curves, Bezier
- drawing WDK GDI , curves, Bezier
- cubic splines WDK GDI
- Bezier curves WDK GDI
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Bezier Curves

Some advanced hardware devices can draw paths containing Bezier curves (cubic splines), which are general-purpose curve primitives. If so, the driver can include support for these curves in the [**DrvStrokePath**](/windows/win32/api/winddi/nf-winddi-drvstrokepath) function.

When GDI must draw a Bezier curve path on a device-managed surface, it will test the GCAPS_BEZIERS flag (in the [**DEVINFO**](/windows/win32/api/winddi/ns-winddi-devinfo) structure) to determine if it should call [**DrvStrokePath**](/windows/win32/api/winddi/nf-winddi-drvstrokepath). If called, this function either performs the requested operation or decides not to handle it, just as it does for geometric wide lines. In the latter case, GDI breaks the request down into simpler operations, for example, by converting curves to line approximations.
