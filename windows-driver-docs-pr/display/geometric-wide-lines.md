---
title: Geometric Wide Lines
description: Geometric Wide Lines
ms.assetid: 769b801c-6950-4f0f-9163-c4ddf070e519
keywords:
- lines WDK GDI , geometric wide
- GDI WDK Windows 2000 display , lines, geometric wide
- graphics drivers WDK Windows 2000 display , lines, geometric wide
- drawing WDK GDI , lines, geometric wide
- geometric wide lines WDK GDI
- geometric lines WDK GDI
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Geometric Wide Lines


## <span id="ddk_geometric_wide_lines_gg"></span><span id="DDK_GEOMETRIC_WIDE_LINES_GG"></span>


The shape of a *geometric* line is determined by the width, join style, and end-cap style of the brush, and the current world-to-device transform in the [**XFORMOBJ**](https://msdn.microsoft.com/library/windows/hardware/ff570618) structure. The line can be drawn using either a solid or a nonsolid brush.

Drivers for more advanced hardware may support geometric wide lines in the [**DrvStrokePath**](https://msdn.microsoft.com/library/windows/hardware/ff556316) function. GDI determines whether a driver can draw a path containing a geometric line by testing the GCAPS\_GEOMETRICWIDE capability flag in the [**DEVINFO**](https://msdn.microsoft.com/library/windows/hardware/ff552835) structure returned in the call to [**DrvEnablePDEV**](https://msdn.microsoft.com/library/windows/hardware/ff556211). If the driver does not have the capability, or if the function fails to handle an operation because the path or clipping is too complex for the device, GDI automatically transforms the call to the simpler [**DrvFillPath**](https://msdn.microsoft.com/library/windows/hardware/ff556220) function.

A geometric wide line has a specific meaning to a display driver graphics function. A path containing device coordinates is transformed to world coordinates using the inverse of the current transform. A geometric construction with the specified width then obtains a widened version of the path, taking into account joins and end caps. This path is transformed to device coordinates again and filled with the specified brush.

Styling of a geometric wide line is specified by an array of floating-point values. The array has a finite length, but is used as though it repeats indefinitely. The first array entry specifies the length, in world coordinates, of the first dash; the next entry specifies the length of the first gap. After this, lengths of dashes and gaps alternate. For example, the style array {3.0,1.0,1.0,1.0} causes a line to be drawn with alternating long and short dashes.

Styling can be thought of as the driver moving along a path before widening, "erasing" the parts of the path corresponding to the gaps. This breaks the path into many subpaths. The broken path is then widened as if it had no line style, applying end caps and joins as usual. Style arrays can be of odd length. For example, the style array {1.0} causes the driver to draw a line with alternating dashes. The style state (defined as the current distance into the styling array) is provided for the beginning of the first subpath in a path. It is considered to be reset to 0.0 at the beginning of each subsequent subpath, which occurs after any Win32 **MoveToEx** operation.

 

 





