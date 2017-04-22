---
title: Optional Graphics Driver Functions
description: Optional Graphics Driver Functions
ms.assetid: 3cdef152-4bcc-426a-9aa7-fd94acf2331f
keywords:
- GDI WDK Windows 2000 display , functions, optional
- graphics drivers WDK Windows 2000 display , functions, optional
- functions WDK graphics , optional
- drawing WDK GDI , functions, optional
- GDI WDK Windows 2000 display , DDI, optional functions
- graphics drivers WDK Windows 2000 display , DDI, optional functions
- DDI WDK graphics , optional functions
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Optional Graphics Driver Functions


## <span id="ddk_optional_graphics_driver_functions_gg"></span><span id="DDK_OPTIONAL_GRAPHICS_DRIVER_FUNCTIONS_GG"></span>


In the interests of reducing driver size, driver writers usually add only those optional functions that are well-supported in hardware. For example, a driver for hardware that supports Image Color Management (ICM) can implement the *DrvIcmXxx* functions. The following tables list the functions that a graphics driver can optionally implement.

### <span id="Display_and_Printer_Driver_Functions_"></span><span id="display_and_printer_driver_functions_"></span><span id="DISPLAY_AND_PRINTER_DRIVER_FUNCTIONS_"></span>Display and Printer Driver Functions

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Entry Point</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>[<strong>DrvAlphaBlend</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556176)</p></td>
<td align="left"><p>Provides bit block transfer capabilities with [<em>alpha blending</em>](https://msdn.microsoft.com/library/windows/hardware/ff556270#wdkgloss-alpha-blending).</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>DrvBitBlt</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556180)</p></td>
<td align="left"><p>Executes general bit block transfers to and from surfaces.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>DrvCreateDeviceBitmap</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556185)</p></td>
<td align="left"><p>Creates and manages a bitmap with a driver-defined format.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>DrvDeleteDeviceBitmap</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556187)</p></td>
<td align="left"><p>Deletes a device-managed bitmap.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>DrvDitherColor</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556202)</p></td>
<td align="left"><p>Requests a device to create a brush dithered against a [<em>device palette</em>](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-palette).</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>DrvFillPath</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556220)</p></td>
<td align="left"><p>Paints a closed path for a [<em>device-managed surface</em>](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-managed-surface).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>DrvGradientFill</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556236)</p></td>
<td align="left"><p>Shades the specified primitives.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>DrvIcmCheckBitmapBits</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556238)</p></td>
<td align="left"><p>Checks whether the pixels in the specified bitmap lie within the device gamut of the specified transform.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>DrvIcmCreateColorTransform</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556239)</p></td>
<td align="left"><p>Creates an ICM color transform.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>DrvIcmDeleteColorTransform</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556241)</p></td>
<td align="left"><p>Deletes the specified ICM color transform.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>DrvIcmSetDeviceGammaRamp</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556243)</p></td>
<td align="left"><p>Sets the hardware [<em>gamma ramp</em>](https://msdn.microsoft.com/library/windows/hardware/ff556283#wdkgloss-gamma-ramp) of the specified display device.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>DrvLineTo</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556245)</p></td>
<td align="left"><p>Draws a single solid integer-only cosmetic line.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>DrvPlgBlt</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556258)</p></td>
<td align="left"><p>Provides rotate bit block transfer capabilities between combinations of device-managed and GDI-managed surfaces.</p></td>
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
<td align="left"><p>Performs a stretching bit block transfer using a [<em>ROP</em>](https://msdn.microsoft.com/library/windows/hardware/ff556331#wdkgloss-raster-operation--rop-).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>DrvStrokeAndFillPath</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556311)</p></td>
<td align="left"><p>Simultaneously fills and strokes a path.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>DrvSynchronize</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556323)</p></td>
<td align="left"><p>Coordinates drawing operations between GDI and a display driver-supported coprocessor device; for [<em>engine-managed surfaces</em>](https://msdn.microsoft.com/library/windows/hardware/ff556279#wdkgloss-engine-managed-surface) only.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>DrvSynchronizeSurface</strong>](https://msdn.microsoft.com/library/windows/hardware/ff557273)</p></td>
<td align="left"><p>Coordinates drawing operations between GDI and a display driver-supported coprocessor device; for engine-managed surfaces only. If a driver provides both <em>DrvSynchronize</em> and <em>DrvSynchronizeSurface</em>, GDI will call only <em>DrvSynchronizeSurface</em>.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>DrvTransparentBlt</strong>](https://msdn.microsoft.com/library/windows/hardware/ff557283)</p></td>
<td align="left"><p>Provides bit block transfer capabilities with transparency.</p></td>
</tr>
</tbody>
</table>

 

### <span id="Functions_Used_Exclusively_by_Display_Drivers"></span><span id="functions_used_exclusively_by_display_drivers"></span><span id="FUNCTIONS_USED_EXCLUSIVELY_BY_DISPLAY_DRIVERS"></span>Functions Used Exclusively by Display Drivers

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Entry Point</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>[<strong>DrvMovePointer</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556248)</p></td>
<td align="left"><p>Moves a pointer to a new position, and redraws it.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>DrvSaveScreenBits</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556278)</p></td>
<td align="left"><p>Saves or restores a specified rectangle of the screen (display driver only).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>DrvSetPointerShape</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556289)</p></td>
<td align="left"><p>Removes the pointer from the screen, if the driver has drawn it, and then sets a new pointer shape.</p></td>
</tr>
</tbody>
</table>

 

### <span id="Functions_Used_Primarily_by_Printer_Drivers"></span><span id="functions_used_primarily_by_printer_drivers"></span><span id="FUNCTIONS_USED_PRIMARILY_BY_PRINTER_DRIVERS"></span>Functions Used Primarily by Printer Drivers

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Entry Point</th>
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
<td align="left"><p>Queries information from a device not available in a device-independent DDI.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>DrvFree</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556226)</p></td>
<td align="left"><p>Frees font storage associated with an indicated data structure.</p></td>
</tr>
</tbody>
</table>

 

### <span id="Functions_Used_Exclusively_by_Printer_Drivers"></span><span id="functions_used_exclusively_by_printer_drivers"></span><span id="FUNCTIONS_USED_EXCLUSIVELY_BY_PRINTER_DRIVERS"></span>Functions Used Exclusively by Printer Drivers

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Entry Point</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>[<strong>DrvEndDoc</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556215)</p></td>
<td align="left"><p>Sends end-of-document information.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>DrvFontManagement</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556223)</p></td>
<td align="left"><p>Allows access to printer functionality not directly available through GDI.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>DrvGetGlyphMode</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556230)</p></td>
<td align="left"><p>Returns type of font information to be stored for a particular font.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>DrvNextBand</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556250)</p></td>
<td align="left"><p>Realizes the contents of a surface's just-drawn band.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<em>DrvQueryPerBandInfo</em>](https://msdn.microsoft.com/library/windows/hardware/ff556268)</p></td>
<td align="left"><p>Returns banding information for the specified banded printer surface.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>DrvSendPage</em>](https://msdn.microsoft.com/library/windows/hardware/ff556281)</p></td>
<td align="left"><p>Sends raw bits from a surface to the printer.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>DrvStartBanding</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556292)</p></td>
<td align="left"><p>Prepares the driver for banding.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>DrvStartDoc</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556296)</p></td>
<td align="left"><p>Sends start-of-document control information.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>DrvStartPage</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556298)</p></td>
<td align="left"><p>Sends start-of-page control information.</p></td>
</tr>
</tbody>
</table>

 

### <span id="Font_Driver_Function"></span><span id="font_driver_function"></span><span id="FONT_DRIVER_FUNCTION"></span>Font Driver Function

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Entry Point</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>[<strong>DrvQueryAdvanceWidths</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556259)</p></td>
<td align="left"><p>Supplies character advance widths for a specified set of glyphs.</p></td>
</tr>
</tbody>
</table>

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Optional%20Graphics%20Driver%20Functions%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




