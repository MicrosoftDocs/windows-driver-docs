---
title: Optional Graphics Driver Functions
description: Optional Graphics Driver Functions
keywords:
- GDI WDK Windows 2000 display , functions, optional
- graphics drivers WDK Windows 2000 display , functions, optional
- functions WDK graphics , optional
- drawing WDK GDI , functions, optional
- GDI WDK Windows 2000 display , DDI, optional functions
- graphics drivers WDK Windows 2000 display , DDI, optional functions
- DDI WDK graphics , optional functions
ms.date: 04/20/2017
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
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-drvalphablend" data-raw-source="[&lt;strong&gt;DrvAlphaBlend&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-drvalphablend)"><strong>DrvAlphaBlend</strong></a></p></td>
<td align="left"><p>Provides bit block transfer capabilities with <a href="/windows-hardware/drivers/#wdkgloss-alpha-blending" data-raw-source="&lt;em&gt;alpha blending&lt;/em&gt;"><em>alpha blending</em></a>.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-drvbitblt" data-raw-source="[&lt;strong&gt;DrvBitBlt&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-drvbitblt)"><strong>DrvBitBlt</strong></a></p></td>
<td align="left"><p>Executes general bit block transfers to and from surfaces.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-drvcreatedevicebitmap" data-raw-source="[&lt;strong&gt;DrvCreateDeviceBitmap&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-drvcreatedevicebitmap)"><strong>DrvCreateDeviceBitmap</strong></a></p></td>
<td align="left"><p>Creates and manages a bitmap with a driver-defined format.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-drvdeletedevicebitmap" data-raw-source="[&lt;strong&gt;DrvDeleteDeviceBitmap&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-drvdeletedevicebitmap)"><strong>DrvDeleteDeviceBitmap</strong></a></p></td>
<td align="left"><p>Deletes a device-managed bitmap.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-drvdithercolor" data-raw-source="[&lt;strong&gt;DrvDitherColor&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-drvdithercolor)"><strong>DrvDitherColor</strong></a></p></td>
<td align="left"><p>Requests a device to create a brush dithered against a <a href="/windows-hardware/drivers/#wdkgloss-device-palette" data-raw-source="&lt;em&gt;device palette&lt;/em&gt;"><em>device palette</em></a>.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-drvfillpath" data-raw-source="[&lt;strong&gt;DrvFillPath&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-drvfillpath)"><strong>DrvFillPath</strong></a></p></td>
<td align="left"><p>Paints a closed path for a <a href="/windows-hardware/drivers/#wdkgloss-device-managed-surface" data-raw-source="&lt;em&gt;device-managed surface&lt;/em&gt;"><em>device-managed surface</em></a>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-drvgradientfill" data-raw-source="[&lt;strong&gt;DrvGradientFill&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-drvgradientfill)"><strong>DrvGradientFill</strong></a></p></td>
<td align="left"><p>Shades the specified primitives.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-drvicmcheckbitmapbits" data-raw-source="[&lt;strong&gt;DrvIcmCheckBitmapBits&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-drvicmcheckbitmapbits)"><strong>DrvIcmCheckBitmapBits</strong></a></p></td>
<td align="left"><p>Checks whether the pixels in the specified bitmap lie within the device gamut of the specified transform.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-drvicmcreatecolortransform" data-raw-source="[&lt;strong&gt;DrvIcmCreateColorTransform&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-drvicmcreatecolortransform)"><strong>DrvIcmCreateColorTransform</strong></a></p></td>
<td align="left"><p>Creates an ICM color transform.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-drvicmdeletecolortransform" data-raw-source="[&lt;strong&gt;DrvIcmDeleteColorTransform&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-drvicmdeletecolortransform)"><strong>DrvIcmDeleteColorTransform</strong></a></p></td>
<td align="left"><p>Deletes the specified ICM color transform.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-drvicmsetdevicegammaramp" data-raw-source="[&lt;strong&gt;DrvIcmSetDeviceGammaRamp&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-drvicmsetdevicegammaramp)"><strong>DrvIcmSetDeviceGammaRamp</strong></a></p></td>
<td align="left"><p>Sets the hardware <a href="/windows-hardware/drivers/#wdkgloss-gamma-ramp" data-raw-source="&lt;em&gt;gamma ramp&lt;/em&gt;"><em>gamma ramp</em></a> of the specified display device.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-drvlineto" data-raw-source="[&lt;strong&gt;DrvLineTo&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-drvlineto)"><strong>DrvLineTo</strong></a></p></td>
<td align="left"><p>Draws a single solid integer-only cosmetic line.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-drvplgblt" data-raw-source="[&lt;strong&gt;DrvPlgBlt&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-drvplgblt)"><strong>DrvPlgBlt</strong></a></p></td>
<td align="left"><p>Provides rotate bit block transfer capabilities between combinations of device-managed and GDI-managed surfaces.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-drvrealizebrush" data-raw-source="[&lt;strong&gt;DrvRealizeBrush&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-drvrealizebrush)"><strong>DrvRealizeBrush</strong></a></p></td>
<td align="left"><p>Realizes a specified brush for a defined surface.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-drvstretchblt" data-raw-source="[&lt;strong&gt;DrvStretchBlt&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-drvstretchblt)"><strong>DrvStretchBlt</strong></a></p></td>
<td align="left"><p>Allows stretching block transfers among device-managed and GDI-managed surfaces.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-drvstretchbltrop" data-raw-source="[&lt;strong&gt;DrvStretchBltROP&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-drvstretchbltrop)"><strong>DrvStretchBltROP</strong></a></p></td>
<td align="left"><p>Performs a stretching bit block transfer using a <a href="/windows-hardware/drivers/#wdkgloss-raster-operation--rop-" data-raw-source="&lt;em&gt;ROP&lt;/em&gt;"><em>ROP</em></a>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-drvstrokeandfillpath" data-raw-source="[&lt;strong&gt;DrvStrokeAndFillPath&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-drvstrokeandfillpath)"><strong>DrvStrokeAndFillPath</strong></a></p></td>
<td align="left"><p>Simultaneously fills and strokes a path.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-drvsynchronize" data-raw-source="[&lt;strong&gt;DrvSynchronize&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-drvsynchronize)"><strong>DrvSynchronize</strong></a></p></td>
<td align="left"><p>Coordinates drawing operations between GDI and a display driver-supported coprocessor device; for <a href="/windows-hardware/drivers/#wdkgloss-engine-managed-surface" data-raw-source="&lt;em&gt;engine-managed surfaces&lt;/em&gt;"><em>engine-managed surfaces</em></a> only.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-drvsynchronizesurface" data-raw-source="[&lt;strong&gt;DrvSynchronizeSurface&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-drvsynchronizesurface)"><strong>DrvSynchronizeSurface</strong></a></p></td>
<td align="left"><p>Coordinates drawing operations between GDI and a display driver-supported coprocessor device; for engine-managed surfaces only. If a driver provides both <em>DrvSynchronize</em> and <em>DrvSynchronizeSurface</em>, GDI will call only <em>DrvSynchronizeSurface</em>.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-drvtransparentblt" data-raw-source="[&lt;strong&gt;DrvTransparentBlt&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-drvtransparentblt)"><strong>DrvTransparentBlt</strong></a></p></td>
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
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-drvmovepointer" data-raw-source="[&lt;strong&gt;DrvMovePointer&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-drvmovepointer)"><strong>DrvMovePointer</strong></a></p></td>
<td align="left"><p>Moves a pointer to a new position, and redraws it.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-drvsavescreenbits" data-raw-source="[&lt;strong&gt;DrvSaveScreenBits&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-drvsavescreenbits)"><strong>DrvSaveScreenBits</strong></a></p></td>
<td align="left"><p>Saves or restores a specified rectangle of the screen (display driver only).</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-drvsetpointershape" data-raw-source="[&lt;strong&gt;DrvSetPointerShape&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-drvsetpointershape)"><strong>DrvSetPointerShape</strong></a></p></td>
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
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-drvdestroyfont" data-raw-source="[&lt;strong&gt;DrvDestroyFont&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-drvdestroyfont)"><strong>DrvDestroyFont</strong></a></p></td>
<td align="left"><p>Notifies driver that a font realization is no longer needed; driver can free allocated data structures.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-drvdrawescape" data-raw-source="[&lt;strong&gt;DrvDrawEscape&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-drvdrawescape)"><strong>DrvDrawEscape</strong></a></p></td>
<td align="left"><p>Implements draw-type escape functions.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-drvescape" data-raw-source="[&lt;strong&gt;DrvEscape&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-drvescape)"><strong>DrvEscape</strong></a></p></td>
<td align="left"><p>Queries information from a device not available in a device-independent DDI.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-drvfree" data-raw-source="[&lt;strong&gt;DrvFree&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-drvfree)"><strong>DrvFree</strong></a></p></td>
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
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-drvenddoc" data-raw-source="[&lt;strong&gt;DrvEndDoc&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-drvenddoc)"><strong>DrvEndDoc</strong></a></p></td>
<td align="left"><p>Sends end-of-document information.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-drvfontmanagement" data-raw-source="[&lt;strong&gt;DrvFontManagement&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-drvfontmanagement)"><strong>DrvFontManagement</strong></a></p></td>
<td align="left"><p>Allows access to printer functionality not directly available through GDI.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-drvgetglyphmode" data-raw-source="[&lt;strong&gt;DrvGetGlyphMode&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-drvgetglyphmode)"><strong>DrvGetGlyphMode</strong></a></p></td>
<td align="left"><p>Returns type of font information to be stored for a particular font.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-drvnextband" data-raw-source="[&lt;strong&gt;DrvNextBand&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-drvnextband)"><strong>DrvNextBand</strong></a></p></td>
<td align="left"><p>Realizes the contents of a surface's just-drawn band.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-drvqueryperbandinfo" data-raw-source="[&lt;em&gt;DrvQueryPerBandInfo&lt;/em&gt;](/windows/win32/api/winddi/nf-winddi-drvqueryperbandinfo)"><em>DrvQueryPerBandInfo</em></a></p></td>
<td align="left"><p>Returns banding information for the specified banded printer surface.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-drvsendpage" data-raw-source="[&lt;em&gt;DrvSendPage&lt;/em&gt;](/windows/win32/api/winddi/nf-winddi-drvsendpage)"><em>DrvSendPage</em></a></p></td>
<td align="left"><p>Sends raw bits from a surface to the printer.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-drvstartbanding" data-raw-source="[&lt;strong&gt;DrvStartBanding&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-drvstartbanding)"><strong>DrvStartBanding</strong></a></p></td>
<td align="left"><p>Prepares the driver for banding.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-drvstartdoc" data-raw-source="[&lt;strong&gt;DrvStartDoc&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-drvstartdoc)"><strong>DrvStartDoc</strong></a></p></td>
<td align="left"><p>Sends start-of-document control information.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-drvstartpage" data-raw-source="[&lt;strong&gt;DrvStartPage&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-drvstartpage)"><strong>DrvStartPage</strong></a></p></td>
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
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-drvqueryadvancewidths" data-raw-source="[&lt;strong&gt;DrvQueryAdvanceWidths&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-drvqueryadvancewidths)"><strong>DrvQueryAdvanceWidths</strong></a></p></td>
<td align="left"><p>Supplies character advance widths for a specified set of glyphs.</p></td>
</tr>
</tbody>
</table>

 

