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
ms.date: 04/20/2017
ms.localizationpriority: medium
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
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff556176" data-raw-source="[&lt;strong&gt;DrvAlphaBlend&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556176)"><strong>DrvAlphaBlend</strong></a></p></td>
<td align="left"><p>Provides bit block transfer capabilities with <a href="https://msdn.microsoft.com/library/windows/hardware/ff556270#wdkgloss-alpha-blending" data-raw-source="[&lt;em&gt;alpha blending&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556270#wdkgloss-alpha-blending)"><em>alpha blending</em></a>.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff556180" data-raw-source="[&lt;strong&gt;DrvBitBlt&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556180)"><strong>DrvBitBlt</strong></a></p></td>
<td align="left"><p>Executes general bit block transfers to and from surfaces.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff556185" data-raw-source="[&lt;strong&gt;DrvCreateDeviceBitmap&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556185)"><strong>DrvCreateDeviceBitmap</strong></a></p></td>
<td align="left"><p>Creates and manages a bitmap with a driver-defined format.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff556187" data-raw-source="[&lt;strong&gt;DrvDeleteDeviceBitmap&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556187)"><strong>DrvDeleteDeviceBitmap</strong></a></p></td>
<td align="left"><p>Deletes a device-managed bitmap.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff556202" data-raw-source="[&lt;strong&gt;DrvDitherColor&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556202)"><strong>DrvDitherColor</strong></a></p></td>
<td align="left"><p>Requests a device to create a brush dithered against a <a href="https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-palette" data-raw-source="[&lt;em&gt;device palette&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-palette)"><em>device palette</em></a>.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff556220" data-raw-source="[&lt;strong&gt;DrvFillPath&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556220)"><strong>DrvFillPath</strong></a></p></td>
<td align="left"><p>Paints a closed path for a <a href="https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-managed-surface" data-raw-source="[&lt;em&gt;device-managed surface&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-managed-surface)"><em>device-managed surface</em></a>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff556236" data-raw-source="[&lt;strong&gt;DrvGradientFill&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556236)"><strong>DrvGradientFill</strong></a></p></td>
<td align="left"><p>Shades the specified primitives.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff556238" data-raw-source="[&lt;strong&gt;DrvIcmCheckBitmapBits&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556238)"><strong>DrvIcmCheckBitmapBits</strong></a></p></td>
<td align="left"><p>Checks whether the pixels in the specified bitmap lie within the device gamut of the specified transform.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff556239" data-raw-source="[&lt;strong&gt;DrvIcmCreateColorTransform&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556239)"><strong>DrvIcmCreateColorTransform</strong></a></p></td>
<td align="left"><p>Creates an ICM color transform.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff556241" data-raw-source="[&lt;strong&gt;DrvIcmDeleteColorTransform&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556241)"><strong>DrvIcmDeleteColorTransform</strong></a></p></td>
<td align="left"><p>Deletes the specified ICM color transform.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff556243" data-raw-source="[&lt;strong&gt;DrvIcmSetDeviceGammaRamp&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556243)"><strong>DrvIcmSetDeviceGammaRamp</strong></a></p></td>
<td align="left"><p>Sets the hardware <a href="https://msdn.microsoft.com/library/windows/hardware/ff556283#wdkgloss-gamma-ramp" data-raw-source="[&lt;em&gt;gamma ramp&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556283#wdkgloss-gamma-ramp)"><em>gamma ramp</em></a> of the specified display device.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff556245" data-raw-source="[&lt;strong&gt;DrvLineTo&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556245)"><strong>DrvLineTo</strong></a></p></td>
<td align="left"><p>Draws a single solid integer-only cosmetic line.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff556258" data-raw-source="[&lt;strong&gt;DrvPlgBlt&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556258)"><strong>DrvPlgBlt</strong></a></p></td>
<td align="left"><p>Provides rotate bit block transfer capabilities between combinations of device-managed and GDI-managed surfaces.</p></td>
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
<td align="left"><p>Performs a stretching bit block transfer using a <a href="https://msdn.microsoft.com/library/windows/hardware/ff556331#wdkgloss-raster-operation--rop-" data-raw-source="[&lt;em&gt;ROP&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556331#wdkgloss-raster-operation--rop-)"><em>ROP</em></a>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff556311" data-raw-source="[&lt;strong&gt;DrvStrokeAndFillPath&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556311)"><strong>DrvStrokeAndFillPath</strong></a></p></td>
<td align="left"><p>Simultaneously fills and strokes a path.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff556323" data-raw-source="[&lt;strong&gt;DrvSynchronize&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556323)"><strong>DrvSynchronize</strong></a></p></td>
<td align="left"><p>Coordinates drawing operations between GDI and a display driver-supported coprocessor device; for <a href="https://msdn.microsoft.com/library/windows/hardware/ff556279#wdkgloss-engine-managed-surface" data-raw-source="[&lt;em&gt;engine-managed surfaces&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556279#wdkgloss-engine-managed-surface)"><em>engine-managed surfaces</em></a> only.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff557273" data-raw-source="[&lt;strong&gt;DrvSynchronizeSurface&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff557273)"><strong>DrvSynchronizeSurface</strong></a></p></td>
<td align="left"><p>Coordinates drawing operations between GDI and a display driver-supported coprocessor device; for engine-managed surfaces only. If a driver provides both <em>DrvSynchronize</em> and <em>DrvSynchronizeSurface</em>, GDI will call only <em>DrvSynchronizeSurface</em>.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff557283" data-raw-source="[&lt;strong&gt;DrvTransparentBlt&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff557283)"><strong>DrvTransparentBlt</strong></a></p></td>
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
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff556248" data-raw-source="[&lt;strong&gt;DrvMovePointer&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556248)"><strong>DrvMovePointer</strong></a></p></td>
<td align="left"><p>Moves a pointer to a new position, and redraws it.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff556278" data-raw-source="[&lt;strong&gt;DrvSaveScreenBits&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556278)"><strong>DrvSaveScreenBits</strong></a></p></td>
<td align="left"><p>Saves or restores a specified rectangle of the screen (display driver only).</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff556289" data-raw-source="[&lt;strong&gt;DrvSetPointerShape&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556289)"><strong>DrvSetPointerShape</strong></a></p></td>
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
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff556192" data-raw-source="[&lt;strong&gt;DrvDestroyFont&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556192)"><strong>DrvDestroyFont</strong></a></p></td>
<td align="left"><p>Notifies driver that a font realization is no longer needed; driver can free allocated data structures.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff556203" data-raw-source="[&lt;strong&gt;DrvDrawEscape&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556203)"><strong>DrvDrawEscape</strong></a></p></td>
<td align="left"><p>Implements draw-type escape functions.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff556217" data-raw-source="[&lt;strong&gt;DrvEscape&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556217)"><strong>DrvEscape</strong></a></p></td>
<td align="left"><p>Queries information from a device not available in a device-independent DDI.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff556226" data-raw-source="[&lt;strong&gt;DrvFree&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556226)"><strong>DrvFree</strong></a></p></td>
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
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff556215" data-raw-source="[&lt;strong&gt;DrvEndDoc&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556215)"><strong>DrvEndDoc</strong></a></p></td>
<td align="left"><p>Sends end-of-document information.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff556223" data-raw-source="[&lt;strong&gt;DrvFontManagement&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556223)"><strong>DrvFontManagement</strong></a></p></td>
<td align="left"><p>Allows access to printer functionality not directly available through GDI.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff556230" data-raw-source="[&lt;strong&gt;DrvGetGlyphMode&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556230)"><strong>DrvGetGlyphMode</strong></a></p></td>
<td align="left"><p>Returns type of font information to be stored for a particular font.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff556250" data-raw-source="[&lt;strong&gt;DrvNextBand&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556250)"><strong>DrvNextBand</strong></a></p></td>
<td align="left"><p>Realizes the contents of a surface&#39;s just-drawn band.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff556268" data-raw-source="[&lt;em&gt;DrvQueryPerBandInfo&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556268)"><em>DrvQueryPerBandInfo</em></a></p></td>
<td align="left"><p>Returns banding information for the specified banded printer surface.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff556281" data-raw-source="[&lt;em&gt;DrvSendPage&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556281)"><em>DrvSendPage</em></a></p></td>
<td align="left"><p>Sends raw bits from a surface to the printer.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff556292" data-raw-source="[&lt;strong&gt;DrvStartBanding&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556292)"><strong>DrvStartBanding</strong></a></p></td>
<td align="left"><p>Prepares the driver for banding.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff556296" data-raw-source="[&lt;strong&gt;DrvStartDoc&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556296)"><strong>DrvStartDoc</strong></a></p></td>
<td align="left"><p>Sends start-of-document control information.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff556298" data-raw-source="[&lt;strong&gt;DrvStartPage&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556298)"><strong>DrvStartPage</strong></a></p></td>
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
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff556259" data-raw-source="[&lt;strong&gt;DrvQueryAdvanceWidths&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556259)"><strong>DrvQueryAdvanceWidths</strong></a></p></td>
<td align="left"><p>Supplies character advance widths for a specified set of glyphs.</p></td>
</tr>
</tbody>
</table>

 

 

 





