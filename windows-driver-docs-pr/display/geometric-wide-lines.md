---
title: Geometric Wide Lines
description: Geometric Wide Lines
ms.assetid: 769b801c-6950-4f0f-9163-c4ddf070e519
keywords: ["lines WDK GDI , geometric wide", "GDI WDK Windows 2000 display , lines, geometric wide", "graphics drivers WDK Windows 2000 display , lines, geometric wide", "drawing WDK GDI , lines, geometric wide", "geometric wide lines WDK GDI", "geometric lines WDK GDI"]
---

# Geometric Wide Lines


## <span id="ddk_geometric_wide_lines_gg"></span><span id="DDK_GEOMETRIC_WIDE_LINES_GG"></span>


The shape of a *geometric* line is determined by the width, join style, and end-cap style of the brush, and the current world-to-device transform in the [**XFORMOBJ**](https://msdn.microsoft.com/library/windows/hardware/ff570618) structure. The line can be drawn using either a solid or a nonsolid brush.

Drivers for more advanced hardware may support geometric wide lines in the [**DrvStrokePath**](https://msdn.microsoft.com/library/windows/hardware/ff556316) function. GDI determines whether a driver can draw a path containing a geometric line by testing the GCAPS\_GEOMETRICWIDE capability flag in the [**DEVINFO**](https://msdn.microsoft.com/library/windows/hardware/ff552835) structure returned in the call to [**DrvEnablePDEV**](https://msdn.microsoft.com/library/windows/hardware/ff556211). If the driver does not have the capability, or if the function fails to handle an operation because the path or clipping is too complex for the device, GDI automatically transforms the call to the simpler [**DrvFillPath**](https://msdn.microsoft.com/library/windows/hardware/ff556220) function.

A geometric wide line has a specific meaning to a display driver graphics function. A path containing device coordinates is transformed to world coordinates using the inverse of the current transform. A geometric construction with the specified width then obtains a widened version of the path, taking into account joins and end caps. This path is transformed to device coordinates again and filled with the specified brush.

Styling of a geometric wide line is specified by an array of floating-point values. The array has a finite length, but is used as though it repeats indefinitely. The first array entry specifies the length, in world coordinates, of the first dash; the next entry specifies the length of the first gap. After this, lengths of dashes and gaps alternate. For example, the style array {3.0,1.0,1.0,1.0} causes a line to be drawn with alternating long and short dashes.

Styling can be thought of as the driver moving along a path before widening, "erasing" the parts of the path corresponding to the gaps. This breaks the path into many subpaths. The broken path is then widened as if it had no line style, applying end caps and joins as usual. Style arrays can be of odd length. For example, the style array {1.0} causes the driver to draw a line with alternating dashes. The style state (defined as the current distance into the styling array) is provided for the beginning of the first subpath in a path. It is considered to be reset to 0.0 at the beginning of each subsequent subpath, which occurs after any Win32 **MoveToEx** operation.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Geometric%20Wide%20Lines%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




