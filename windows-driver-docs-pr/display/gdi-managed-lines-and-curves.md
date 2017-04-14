---
title: GDI-Managed Lines and Curves
description: GDI-Managed Lines and Curves
ms.assetid: 1a7625ec-6994-488c-a722-cf436a83e213
keywords: ["GDI WDK Windows 2000 display , rendering engine", "graphics drivers WDK Windows 2000 display , rendering engine", "drawing WDK GDI , rendering engine", "rendering engine WDK GDI", "lines WDK GDI", "GDI WDK Windows 2000 display , lines", "graphics drivers WDK Windows 2000 display , lines", "drawing WDK GDI , lines", "GDI WDK Windows 2000 display , curves", "graphics drivers WDK Windows 2000 display , curves", "drawing WDK GDI , curves"]
---

# GDI-Managed Lines and Curves


## <span id="ddk_gdi_managed_lines_and_curves_gg"></span><span id="DDK_GDI_MANAGED_LINES_AND_CURVES_GG"></span>


GDI offers improved definitions of lines and curves. Lines are not required to have integer endpoints in DEVICE coordinates, as was true for Microsoft Windows 3.x. This allows the driver to transform graphics objects without gross rounding. The fundamental curve in GDI is a Bezier curve (cubic spline) rather than an ellipse. All GDI internal operations are handled with Bezier curves, which are supported by most high-end devices. For devices that do not handle Bezier curves, GDI breaks curves down into line segments before calling the driver to draw them.

GDI can download regions to be filled in the form of paths, as well as rectangles. Drivers can decompose paths into trapezoids or spans for filling.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20GDI-Managed%20Lines%20and%20Curves%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




