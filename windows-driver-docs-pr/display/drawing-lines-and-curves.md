---
title: Drawing Lines and Curves
description: Drawing Lines and Curves
ms.assetid: 0816fb69-7811-4319-b050-00ded21a10d4
keywords:
- lines WDK GDI
- GDI WDK Windows 2000 display , lines
- graphics drivers WDK Windows 2000 display , lines
- drawing WDK GDI , lines
- GDI WDK Windows 2000 display , curves
- graphics drivers WDK Windows 2000 display , curves
- drawing WDK GDI , curves
- brushes WDK GDI
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Drawing Lines and Curves


## <span id="ddk_drawing_lines_and_curves_gg"></span><span id="DDK_DRAWING_LINES_AND_CURVES_GG"></span>


The types of lines and curves included in graphic output are [geometric lines](geometric-wide-lines.md), [cosmetic lines](cosmetic-lines.md), and [Bezier curves](bezier-curves.md).

For line and curve output, a driver can support the [**DrvStrokePath**](https://msdn.microsoft.com/library/windows/hardware/ff556316), [**DrvFillPath**](https://msdn.microsoft.com/library/windows/hardware/ff556220), and [**DrvStrokeAndFillPath**](https://msdn.microsoft.com/library/windows/hardware/ff556311) functions. The driver must support **DrvStrokePath** for drawing lines if the surface is device-managed; drivers are not required to support curves.

When GDI draws a line or curve with any set of attributes, GDI can call [**DrvStrokePath**](https://msdn.microsoft.com/library/windows/hardware/ff556316). At a minimum, the **DrvStrokePath** function must support the drawing of solid and styled cosmetic lines with a solid color brush and arbitrary clipping. The GDI PATHOBJ\_*Xxx* and CLIPOBJ\_*Xxx* service functions make this possible by breaking down the lines into a set of lines one pixel wide with precomputed clipping. **DrvStrokePath** provides a pointer, **plineattrs**, to the [**LINEATTRS**](https://msdn.microsoft.com/library/windows/hardware/ff568195) structure that defines the various line attributes.

When the path or clipping is too complex for the driver to process on the device, the driver can punt the callback to GDI by calling the [**EngStrokePath**](https://msdn.microsoft.com/library/windows/hardware/ff565033) function. In this case, GDI can break the [**DrvStrokePath**](https://msdn.microsoft.com/library/windows/hardware/ff556316) call into a set of lines one pixel wide with precomputed clipping.

By calling the CLIPOBJ\_*Xxx* services from GDI, a driver can have GDI enumerate all the lines in the path and perform all of the line clipping calculations. In addition, a driver can use the PATHOBJ\_*Xxx*, CLIPOBJ\_*Xxx*, or XFORMOBJ\_*Xxx* services to simplify the graphics operations. For example, a driver can use [**CLIPOBJ\_cEnumStart**](https://msdn.microsoft.com/library/windows/hardware/ff539421) and [**CLIPOBJ\_bEnum**](https://msdn.microsoft.com/library/windows/hardware/ff539420) to enumerate the rectangles in a [*clip region*](https://msdn.microsoft.com/library/windows/hardware/ff556274#wdkgloss-clip-region), send this region down to the printer, and clip to it. The driver can also use [**PATHOBJ\_vEnumStart**](https://msdn.microsoft.com/library/windows/hardware/ff568856) and [**PATHOBJ\_bEnum**](https://msdn.microsoft.com/library/windows/hardware/ff568851) to enumerate lines or curves in the path. It can then send the path to the device, and stroke it.

 

 





