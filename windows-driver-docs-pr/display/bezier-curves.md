---
title: Bezier Curves
description: Bezier Curves
ms.assetid: 322ff79b-e5b8-4247-99eb-1aa3779216ef
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


## <span id="ddk_bezier_curves_gg"></span><span id="DDK_BEZIER_CURVES_GG"></span>


Some advanced hardware devices can draw paths containing Bezier curves (cubic splines), which are general-purpose curve primitives. If so, the driver can include support for these curves in the [**DrvStrokePath**](https://msdn.microsoft.com/library/windows/hardware/ff556316) function.

When GDI must draw a Bezier curve path on a device-managed surface, it will test the GCAPS\_BEZIERS flag (in the [**DEVINFO**](https://msdn.microsoft.com/library/windows/hardware/ff552835) structure) to determine if it should call [**DrvStrokePath**](https://msdn.microsoft.com/library/windows/hardware/ff556316). If called, this function either performs the requested operation or decides not to handle it, just as it does for geometric wide lines. In the latter case, GDI breaks the request down into simpler operations, for example, by converting curves to line approximations.

 

 





