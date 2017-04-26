---
title: Optional Display Driver Functions
description: Optional Display Driver Functions
ms.assetid: 7c1489c9-40de-4b44-95b7-af227c7d8205
keywords:
- graphics DDI functions WDK Windows 2000 display
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Optional Display Driver Functions


## <span id="ddk_optional_display_driver_functions_gg"></span><span id="DDK_OPTIONAL_DISPLAY_DRIVER_FUNCTIONS_GG"></span>


In order to reduce driver size, display driver writers usually add only those optional functions that are well supported in video hardware. The display driver can implement the functions listed in the following tables. These functions are sorted into the following categories:

Bitmap Management Functions

Drawing Functions

Image Color Management Functions

Pointer and Window Management Functions

Miscellaneous Functions

### <span id="ddk_bitmap_management_functions_gg"></span><span id="DDK_BITMAP_MANAGEMENT_FUNCTIONS_GG"></span>Bitmap Management Functions

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Function</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>[<strong>DrvCreateDeviceBitmap</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556185)</p></td>
<td align="left"><p>Creates and manages a bitmap with a driver-defined format.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>DrvDeleteDeviceBitmap</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556187)</p></td>
<td align="left"><p>Deletes a device-managed bitmap.</p></td>
</tr>
</tbody>
</table>

 

### <span id="ddk_drawing_functions_gg"></span><span id="DDK_DRAWING_FUNCTIONS_GG"></span>Drawing Functions

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Function</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>[<strong>DrvAlphaBlend</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556176)</p></td>
<td align="left"><p>Provides [<em>bit-block transfer</em>](https://msdn.microsoft.com/library/windows/hardware/ff556272#wdkgloss-bit-block-transfer) capabilities with [<em>alpha blending</em>](https://msdn.microsoft.com/library/windows/hardware/ff556270#wdkgloss-alpha-blending).</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>DrvBitBlt</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556180)</p></td>
<td align="left"><p>Provides general bit-block transfer capabilities between [<em>device-managed surfaces</em>](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-managed-surface), between GDI-managed standard-format bitmaps, or between a device-managed surface and a GDI-managed standard-format bitmap.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>DrvDitherColor</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556202)</p></td>
<td align="left"><p>Requests a device to create a brush dithered against a [<em>device palette</em>](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-palette).</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>DrvFillPath</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556220)</p></td>
<td align="left"><p>Paints a closed path for a device-managed surface.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>DrvGradientFill</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556236)</p></td>
<td align="left"><p>Shades the specified primitives.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>DrvLineTo</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556245)</p></td>
<td align="left"><p>Draws a single, solid, integer-only cosmetic line.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>DrvPlgBlt</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556258)</p></td>
<td align="left"><p>Provides rotate [<em>bit-block transfer</em>](https://msdn.microsoft.com/library/windows/hardware/ff556272#wdkgloss-bit-block-transfer) capabilities between combinations of device-managed and GDI-managed surfaces.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>DrvRealizeBrush</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556273)</p></td>
<td align="left"><p>Realizes a specified brush for a defined surface.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>DrvStretchBlt</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556302)</p></td>
<td align="left"><p>Allows stretching block transfers among device-managed and GDI-managed surfaces.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>DrvStretchBltROP</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556306)</p></td>
<td align="left"><p>Performs a stretching bit-block transfer using a [<em>ROP</em>](https://msdn.microsoft.com/library/windows/hardware/ff556331#wdkgloss-raster-operation--rop-).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>DrvStrokeAndFillPath</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556311)</p></td>
<td align="left"><p>Simultaneously strokes and fills a path.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>DrvTransparentBlt</strong>](https://msdn.microsoft.com/library/windows/hardware/ff557283)</p></td>
<td align="left"><p>Provides bit-block transfer capabilities with transparency.</p></td>
</tr>
</tbody>
</table>

 

### <span id="ddk_image_color_management_functions_gg"></span><span id="DDK_IMAGE_COLOR_MANAGEMENT_FUNCTIONS_GG"></span>Image Color Management Functions

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Function</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>[<strong>DrvIcmCheckBitmapBits</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556238)</p></td>
<td align="left"><p>Checks whether the pixels in the specified bitmap lie within the device gamut of the specified transform.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>DrvIcmCreateColorTransform</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556239)</p></td>
<td align="left"><p>Creates an ICM color transform.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>DrvIcmDeleteColorTransform</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556241)</p></td>
<td align="left"><p>Deletes the specified ICM color transform.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>DrvIcmSetDeviceGammaRamp</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556243)</p></td>
<td align="left"><p>Sets the hardware [<em>gamma ramp</em>](https://msdn.microsoft.com/library/windows/hardware/ff556283#wdkgloss-gamma-ramp) of the specified display device.</p></td>
</tr>
</tbody>
</table>

 

### <span id="ddk_pointer_and_window_management_functions_gg"></span><span id="DDK_POINTER_AND_WINDOW_MANAGEMENT_FUNCTIONS_GG"></span>Pointer and Window Management Functions

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Function</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>[<strong>DrvDescribePixelFormat</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556190)</p></td>
<td align="left"><p>Describes the pixel format for a device-specified PDEV by writing a pixel format description to a PIXELFORMATDESCRIPTOR structure.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>DrvMovePointer</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556248)</p></td>
<td align="left"><p>Moves a pointer to a new position and redraws it.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>DrvSaveScreenBits</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556278)</p></td>
<td align="left"><p>Saves or restores a specified rectangle of the screen.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>DrvSetPixelFormat</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556285)</p></td>
<td align="left"><p>Sets the pixel format of a window.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>DrvSetPointerShape</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556289)</p></td>
<td align="left"><p>Removes the pointer from the screen if the driver has drawn it, and then sets a new pointer shape.</p></td>
</tr>
</tbody>
</table>

 

### <span id="ddk_miscellaneous_functions_gg"></span><span id="DDK_MISCELLANEOUS_FUNCTIONS_GG"></span>Miscellaneous Functions

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Function</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>[<strong>DrvDestroyFont</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556192)</p></td>
<td align="left"><p>Notifies driver that a font realization is no longer needed; driver can free allocated data structures.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>DrvDrawEscape</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556203)</p></td>
<td align="left"><p>Implements draw-type escape functions.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>DrvEscape</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556217)</p></td>
<td align="left"><p>Queries information from a device not available in a device-independent graphics DDI.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>DrvFree</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556226)</p></td>
<td align="left"><p>Frees storage associated with an indicated data structure.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>DrvNotify</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556252)</p></td>
<td align="left"><p>Allows a display driver to be notified about certain information by GDI.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>DrvSynchronize</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556323)</p></td>
<td align="left"><p>Coordinates drawing operations between GDI and a display driver-supported coprocessor device; for [<em>engine-managed surfaces</em>](https://msdn.microsoft.com/library/windows/hardware/ff556279#wdkgloss-engine-managed-surface) only.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>DrvSynchronizeSurface</strong>](https://msdn.microsoft.com/library/windows/hardware/ff557273)</p></td>
<td align="left"><p>Allows drawing operations performed by a device's coprocessor to be coordinated with GDI.</p></td>
</tr>
</tbody>
</table>

 

Display drivers can also optionally implement the Microsoft DirectDraw and/or Direct3D interfaces. See the following sections for details:

[DirectDraw](directdraw.md)

[Direct3D DDI](direct3d.md)

A list of optional functions for all graphics drivers appears in [Optional Graphics Driver Functions](optional-graphics-driver-functions.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Optional%20Display%20Driver%20Functions%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




