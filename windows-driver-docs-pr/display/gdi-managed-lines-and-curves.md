---
title: GDI-Managed Lines and Curves
description: GDI-Managed Lines and Curves
ms.assetid: 1a7625ec-6994-488c-a722-cf436a83e213
keywords:
- GDI WDK Windows 2000 display , rendering engine
- graphics drivers WDK Windows 2000 display , rendering engine
- drawing WDK GDI , rendering engine
- rendering engine WDK GDI
- lines WDK GDI
- GDI WDK Windows 2000 display , lines
- graphics drivers WDK Windows 2000 display , lines
- drawing WDK GDI , lines
- GDI WDK Windows 2000 display , curves
- graphics drivers WDK Windows 2000 display , curves
- drawing WDK GDI , curves
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# GDI-Managed Lines and Curves


## <span id="ddk_gdi_managed_lines_and_curves_gg"></span><span id="DDK_GDI_MANAGED_LINES_AND_CURVES_GG"></span>


GDI offers improved definitions of lines and curves. Lines are not required to have integer endpoints in DEVICE coordinates, as was true for Microsoft Windows 3.x. This allows the driver to transform graphics objects without gross rounding. The fundamental curve in GDI is a Bezier curve (cubic spline) rather than an ellipse. All GDI internal operations are handled with Bezier curves, which are supported by most high-end devices. For devices that do not handle Bezier curves, GDI breaks curves down into line segments before calling the driver to draw them.

GDI can download regions to be filled in the form of paths, as well as rectangles. Drivers can decompose paths into trapezoids or spans for filling.

 

 





