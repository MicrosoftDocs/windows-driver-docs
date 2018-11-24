---
title: Optional Display Driver Functions
description: Optional Display Driver Functions
ms.assetid: 7c1489c9-40de-4b44-95b7-af227c7d8205
keywords:
- graphics DDI functions WDK Windows 2000 display
ms.date: 04/20/2017
ms.localizationpriority: medium
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
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff556185" data-raw-source="[&lt;strong&gt;DrvCreateDeviceBitmap&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556185)"><strong>DrvCreateDeviceBitmap</strong></a></p></td>
<td align="left"><p>Creates and manages a bitmap with a driver-defined format.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff556187" data-raw-source="[&lt;strong&gt;DrvDeleteDeviceBitmap&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556187)"><strong>DrvDeleteDeviceBitmap</strong></a></p></td>
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
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff556176" data-raw-source="[&lt;strong&gt;DrvAlphaBlend&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556176)"><strong>DrvAlphaBlend</strong></a></p></td>
<td align="left"><p>Provides <a href="https://msdn.microsoft.com/library/windows/hardware/ff556272#wdkgloss-bit-block-transfer" data-raw-source="[&lt;em&gt;bit-block transfer&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556272#wdkgloss-bit-block-transfer)"><em>bit-block transfer</em></a> capabilities with <a href="https://msdn.microsoft.com/library/windows/hardware/ff556270#wdkgloss-alpha-blending" data-raw-source="[&lt;em&gt;alpha blending&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556270#wdkgloss-alpha-blending)"><em>alpha blending</em></a>.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff556180" data-raw-source="[&lt;strong&gt;DrvBitBlt&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556180)"><strong>DrvBitBlt</strong></a></p></td>
<td align="left"><p>Provides general bit-block transfer capabilities between <a href="https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-managed-surface" data-raw-source="[&lt;em&gt;device-managed surfaces&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-managed-surface)"><em>device-managed surfaces</em></a>, between GDI-managed standard-format bitmaps, or between a device-managed surface and a GDI-managed standard-format bitmap.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff556202" data-raw-source="[&lt;strong&gt;DrvDitherColor&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556202)"><strong>DrvDitherColor</strong></a></p></td>
<td align="left"><p>Requests a device to create a brush dithered against a <a href="https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-palette" data-raw-source="[&lt;em&gt;device palette&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-palette)"><em>device palette</em></a>.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff556220" data-raw-source="[&lt;strong&gt;DrvFillPath&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556220)"><strong>DrvFillPath</strong></a></p></td>
<td align="left"><p>Paints a closed path for a device-managed surface.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff556236" data-raw-source="[&lt;strong&gt;DrvGradientFill&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556236)"><strong>DrvGradientFill</strong></a></p></td>
<td align="left"><p>Shades the specified primitives.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff556245" data-raw-source="[&lt;strong&gt;DrvLineTo&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556245)"><strong>DrvLineTo</strong></a></p></td>
<td align="left"><p>Draws a single, solid, integer-only cosmetic line.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff556258" data-raw-source="[&lt;strong&gt;DrvPlgBlt&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556258)"><strong>DrvPlgBlt</strong></a></p></td>
<td align="left"><p>Provides rotate <a href="https://msdn.microsoft.com/library/windows/hardware/ff556272#wdkgloss-bit-block-transfer" data-raw-source="[&lt;em&gt;bit-block transfer&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556272#wdkgloss-bit-block-transfer)"><em>bit-block transfer</em></a> capabilities between combinations of device-managed and GDI-managed surfaces.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff556273" data-raw-source="[&lt;strong&gt;DrvRealizeBrush&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556273)"><strong>DrvRealizeBrush</strong></a></p></td>
<td align="left"><p>Realizes a specified brush for a defined surface.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff556302" data-raw-source="[&lt;strong&gt;DrvStretchBlt&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556302)"><strong>DrvStretchBlt</strong></a></p></td>
<td align="left"><p>Allows stretching block transfers among device-managed and GDI-managed surfaces.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff556306" data-raw-source="[&lt;strong&gt;DrvStretchBltROP&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556306)"><strong>DrvStretchBltROP</strong></a></p></td>
<td align="left"><p>Performs a stretching bit-block transfer using a <a href="https://msdn.microsoft.com/library/windows/hardware/ff556331#wdkgloss-raster-operation--rop-" data-raw-source="[&lt;em&gt;ROP&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556331#wdkgloss-raster-operation--rop-)"><em>ROP</em></a>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff556311" data-raw-source="[&lt;strong&gt;DrvStrokeAndFillPath&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556311)"><strong>DrvStrokeAndFillPath</strong></a></p></td>
<td align="left"><p>Simultaneously strokes and fills a path.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff557283" data-raw-source="[&lt;strong&gt;DrvTransparentBlt&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff557283)"><strong>DrvTransparentBlt</strong></a></p></td>
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
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff556238" data-raw-source="[&lt;strong&gt;DrvIcmCheckBitmapBits&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556238)"><strong>DrvIcmCheckBitmapBits</strong></a></p></td>
<td align="left"><p>Checks whether the pixels in the specified bitmap lie within the device gamut of the specified transform.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff556239" data-raw-source="[&lt;strong&gt;DrvIcmCreateColorTransform&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556239)"><strong>DrvIcmCreateColorTransform</strong></a></p></td>
<td align="left"><p>Creates an ICM color transform.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff556241" data-raw-source="[&lt;strong&gt;DrvIcmDeleteColorTransform&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556241)"><strong>DrvIcmDeleteColorTransform</strong></a></p></td>
<td align="left"><p>Deletes the specified ICM color transform.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff556243" data-raw-source="[&lt;strong&gt;DrvIcmSetDeviceGammaRamp&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556243)"><strong>DrvIcmSetDeviceGammaRamp</strong></a></p></td>
<td align="left"><p>Sets the hardware <a href="https://msdn.microsoft.com/library/windows/hardware/ff556283#wdkgloss-gamma-ramp" data-raw-source="[&lt;em&gt;gamma ramp&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556283#wdkgloss-gamma-ramp)"><em>gamma ramp</em></a> of the specified display device.</p></td>
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
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff556190" data-raw-source="[&lt;strong&gt;DrvDescribePixelFormat&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556190)"><strong>DrvDescribePixelFormat</strong></a></p></td>
<td align="left"><p>Describes the pixel format for a device-specified PDEV by writing a pixel format description to a PIXELFORMATDESCRIPTOR structure.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff556248" data-raw-source="[&lt;strong&gt;DrvMovePointer&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556248)"><strong>DrvMovePointer</strong></a></p></td>
<td align="left"><p>Moves a pointer to a new position and redraws it.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff556278" data-raw-source="[&lt;strong&gt;DrvSaveScreenBits&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556278)"><strong>DrvSaveScreenBits</strong></a></p></td>
<td align="left"><p>Saves or restores a specified rectangle of the screen.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff556285" data-raw-source="[&lt;strong&gt;DrvSetPixelFormat&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556285)"><strong>DrvSetPixelFormat</strong></a></p></td>
<td align="left"><p>Sets the pixel format of a window.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff556289" data-raw-source="[&lt;strong&gt;DrvSetPointerShape&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556289)"><strong>DrvSetPointerShape</strong></a></p></td>
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
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff556192" data-raw-source="[&lt;strong&gt;DrvDestroyFont&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556192)"><strong>DrvDestroyFont</strong></a></p></td>
<td align="left"><p>Notifies driver that a font realization is no longer needed; driver can free allocated data structures.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff556203" data-raw-source="[&lt;strong&gt;DrvDrawEscape&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556203)"><strong>DrvDrawEscape</strong></a></p></td>
<td align="left"><p>Implements draw-type escape functions.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff556217" data-raw-source="[&lt;strong&gt;DrvEscape&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556217)"><strong>DrvEscape</strong></a></p></td>
<td align="left"><p>Queries information from a device not available in a device-independent graphics DDI.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff556226" data-raw-source="[&lt;strong&gt;DrvFree&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556226)"><strong>DrvFree</strong></a></p></td>
<td align="left"><p>Frees storage associated with an indicated data structure.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff556252" data-raw-source="[&lt;strong&gt;DrvNotify&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556252)"><strong>DrvNotify</strong></a></p></td>
<td align="left"><p>Allows a display driver to be notified about certain information by GDI.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff556323" data-raw-source="[&lt;strong&gt;DrvSynchronize&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556323)"><strong>DrvSynchronize</strong></a></p></td>
<td align="left"><p>Coordinates drawing operations between GDI and a display driver-supported coprocessor device; for <a href="https://msdn.microsoft.com/library/windows/hardware/ff556279#wdkgloss-engine-managed-surface" data-raw-source="[&lt;em&gt;engine-managed surfaces&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556279#wdkgloss-engine-managed-surface)"><em>engine-managed surfaces</em></a> only.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff557273" data-raw-source="[&lt;strong&gt;DrvSynchronizeSurface&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff557273)"><strong>DrvSynchronizeSurface</strong></a></p></td>
<td align="left"><p>Allows drawing operations performed by a device&#39;s coprocessor to be coordinated with GDI.</p></td>
</tr>
</tbody>
</table>

 

Display drivers can also optionally implement the Microsoft DirectDraw and/or Direct3D interfaces. See the following sections for details:

[DirectDraw](directdraw.md)

[Direct3D DDI](direct3d.md)

A list of optional functions for all graphics drivers appears in [Optional Graphics Driver Functions](optional-graphics-driver-functions.md).

 

 





