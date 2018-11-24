---
title: Standard Variables
description: Standard Variables
ms.assetid: d3f85c0f-7387-4301-8b1e-904471aed4b0
keywords:
- GPD file entries WDK Unidrv , standard variables
- variables WDK GPD files
- standard variables WDK GPD files
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Standard Variables





The GPD language defines a set of standard variables that can be referenced within command strings, using the [command string format](command-string-format.md). The Unidrv driver assigns values to these variables. From the point of view of a GPD file, the variables are read-only.

All standard variables are stored as DWORD integers.

The following [printer command](printer-commands.md) entry specifies the command string that is sent to an HP LaserJet 4P when a block of raster data is ready:

```cpp
*Command: CmdSendBlockData: "<1B>*b" %d{NumOfDataBytes} "W"
```

The following table contains all of the standard variables, in alphabetic order.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>Standard Variable Name</th>
<th>Value</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>BlueValue</strong></p></td>
<td><p>Blue component of the current color.</p></td>
<td><p>Valid for use in CmdDefinePaletteEntry command strings. (Also see <strong>GreenValue</strong>, <strong>RedValue</strong>.)</p></td>
</tr>
<tr class="even">
<td><p><strong>CurrentFontID</strong></p></td>
<td><p>Identification number of the current downloaded soft font.</p></td>
<td><p>Valid if current print job includes downloaded soft fonts.</p></td>
</tr>
<tr class="odd">
<td><p><strong>CurrentPaletteIndex</strong></p></td>
<td><p>Current index into the color palette.</p></td>
<td><p>Valid for use in CmdSelectPaletteEntry command strings. (Also see <strong>GreenValue</strong>, <strong>RedValue</strong>.)</p></td>
</tr>
<tr class="even">
<td><p><strong>CursorOriginX</strong></p></td>
<td><p>X coordinate of cursor origin, in master units.</p></td>
<td><p>Valid whenever a print job is in progress.</p></td>
</tr>
<tr class="odd">
<td><p><strong>CursorOriginY</strong></p></td>
<td><p>Y coordinate of cursor origin, in master units.</p></td>
<td><p>Valid whenever a print job is in progress.</p></td>
</tr>
<tr class="even">
<td><p><strong>DestX</strong></p></td>
<td><p>X coordinate of cursor destination, in master units, relative to the cursor origin.</p></td>
<td><p>Valid for use in CmdXMoveAbsolute command strings.</p></td>
</tr>
<tr class="odd">
<td><p><strong>DestXRel</strong></p></td>
<td><p>X coordinate of cursor destination, in master units, relative to the current cursor position.</p></td>
<td><p>Valid for use in CmdXMoveRelLeft and CmdXMoveRelRight command strings.</p></td>
</tr>
<tr class="even">
<td><p><strong>DestY</strong></p></td>
<td><p>Y coordinate of cursor destination, in master units, relative to the cursor origin.</p></td>
<td><p>Valid for use in CmdYMoveAbsolute command strings.</p></td>
</tr>
<tr class="odd">
<td><p><strong>DestYRel</strong></p></td>
<td><p>Y coordinate of cursor destination, in master units, relative to the current cursor position.</p></td>
<td><p>Valid for use in CmdYMoveRelUp and CmdYMoveRelDown command strings.</p></td>
</tr>
<tr class="even">
<td><p><strong>FontBold</strong></p></td>
<td><p>Set to one if current font is bold, or zero otherwise.</p></td>
<td><p>Valid when a font has been specified.</p></td>
</tr>
<tr class="odd">
<td><p><strong>FontHeight</strong></p></td>
<td><p>Height, in master units, of the current font.</p></td>
<td><p>Valid when a font has been specified.</p></td>
</tr>
<tr class="even">
<td><p><strong>FontItalic</strong></p></td>
<td><p>Set to one if current font is italic, or zero otherwise.</p></td>
<td><p>Valid when a font has been specified.</p></td>
</tr>
<tr class="odd">
<td><p><strong>FontMaxWidth</strong></p></td>
<td><p>Set to the maximum character increment of all glyphs in the font.</p></td>
<td><p>Valid when a font has been specified.</p></td>
</tr>
<tr class="even">
<td><p><strong>FontStrikeThru</strong></p></td>
<td><p>Set to one if strike-through is enabled for the current font, or zero otherwise.</p></td>
<td><p>Valid when a font has been specified.</p></td>
</tr>
<tr class="odd">
<td><p><strong>FontUnderLine</strong></p></td>
<td><p>Set to one if current font is underlined, or zero otherwise.</p></td>
<td><p>Valid when a font has been specified.</p></td>
</tr>
<tr class="even">
<td><p><strong>FontWidth</strong></p></td>
<td><p>Width, in master units, of the current font.</p></td>
<td><p>Valid when a font has been specified.</p></td>
</tr>
<tr class="odd">
<td><p><strong>GraphicsXRes</strong></p></td>
<td><p>Current horizontal resolution for graphics, in DPI.</p></td>
<td><p>Valid whenever a print job is in progress.</p></td>
</tr>
<tr class="even">
<td><p><strong>GraphicsYRes</strong></p></td>
<td><p>Current vertical resolution for graphics, in DPI.</p></td>
<td><p>Valid whenever a print job is in progress.</p></td>
</tr>
<tr class="odd">
<td><p><strong>GrayPercentage</strong></p></td>
<td><p>Gray level (percentage) to use for gray fill.</p></td>
<td><p>Valid for use in CmdRectGrayFill command strings.</p></td>
</tr>
<tr class="even">
<td><p><strong>GreenValue</strong></p></td>
<td><p>Green component of the current color.</p></td>
<td><p>Valid for use in CmdDefinePaletteEntry command strings. (Also see <strong>BlueValue</strong>, <strong>RedValue</strong>.)</p></td>
</tr>
<tr class="odd">
<td><p><strong>LinefeedSpacing</strong></p></td>
<td><p>Amount of vertical space, in master units, representing a linefeed.</p></td>
<td><p>Valid for use in CmdSetLineSpacing command strings.</p></td>
</tr>
<tr class="even">
<td><p><strong>NextFontID</strong></p></td>
<td><p>Identification number of the next soft font to be downloaded.</p></td>
<td><p>Valid for use in CmdSetFontID command strings.</p></td>
</tr>
<tr class="odd">
<td><p><strong>NextGlyph</strong></p></td>
<td><p>The two-byte code of the next glyph to download.</p></td>
<td><p>Valid for use in CmdSetCharCode command strings.</p></td>
</tr>
<tr class="even">
<td><p><strong>NumOfCopies</strong></p></td>
<td><p>Number of copies requested by the user.</p></td>
<td><p>Valid whenever a print job is in progress.</p></td>
</tr>
<tr class="odd">
<td><p><strong>NumOfDataBytes</strong></p></td>
<td><p>Number of bytes of raster data ready for transfer.</p></td>
<td><p>Valid for use in any CmdSend<em>XXX</em>Data command string.</p>
<p>If data is compressed, the value is the number of bytes after compression.</p></td>
</tr>
<tr class="even">
<td><p><strong>PageNumber</strong></p></td>
<td><p>The number of the page currently being printed. Note that this does not necessarily correspond to the application&#39;s page number, but rather the number of times <a href="https://msdn.microsoft.com/library/windows/hardware/ff556281" data-raw-source="[&lt;em&gt;DrvSendPage&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556281)"><em>DrvSendPage</em></a> has been called.</p>
<p>This value is initialized by <a href="https://msdn.microsoft.com/library/windows/hardware/ff556296" data-raw-source="[&lt;strong&gt;DrvStartDoc&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556296)"><strong>DrvStartDoc</strong></a> and is incremented by <strong>DrvSendPage</strong>.</p>
<p>For example, if N-up = 4 is selected, <strong>PageNumber</strong> is incremented to 2 only when the fifth page of the document is being printed.</p>
<p>As another example, if a document is printed in reverse order (back to front) the <strong>PageNumber</strong> standard variable still reports the first page to be printed as page 1, even though this is the last page of the document.</p>
<p>This behavior is needed to properly support the auto-duplexing feature.</p>
<p>The OEM should use <strong>PageNumber</strong> only to determine whether the current page is the front or back side.</p></td>
<td><p>Valid whenever a print job is in progress.</p></td>
</tr>
<tr class="odd">
<td><p><strong>PaletteIndexToProgram</strong></p></td>
<td><p>Index into the color palette for the next entry to program.</p></td>
<td><p>Valid for use in CmdDefinePaletteEntry command strings. (Also see <strong>RedValue</strong>, <strong>GreenValue</strong>, <strong>BlueValue</strong>, <strong>CurrentPaletteIndex</strong>.)</p></td>
</tr>
<tr class="even">
<td><p><strong>PatternBrushID</strong></p></td>
<td><p>Identification number of a downloaded pattern brush.</p></td>
<td><p>Valid for use with CmdDownloadPattern and CmdSelectPattern command strings.</p></td>
</tr>
<tr class="odd">
<td><p><strong>PatternBrushSize</strong></p></td>
<td><p>Size, in bytes, of the current pattern brush.</p></td>
<td><p>Valid for use with CmdDownloadPattern command string.</p></td>
</tr>
<tr class="even">
<td><p><strong>PatternBrushType</strong></p></td>
<td><p></p>
Type of the current pattern brush. Value can be:
2: Shading pattern
3: Cross-hatch pattern
4: User-defined pattern</td>
<td><p>Valid for use with CmdDownloadPattern and CmdSelectPattern command strings.</p></td>
</tr>
<tr class="odd">
<td><p><strong>PhysPaperLength</strong></p></td>
<td><p>Portrait-mode length, in y-master units, of the paper currently in use.</p></td>
<td><p>Valid whenever a print job is in progress.</p></td>
</tr>
<tr class="even">
<td><p><strong>PhysPaperWidth</strong></p></td>
<td><p>Portrait-mode width, in master units, of the paper currently in use.</p></td>
<td><p>Valid whenever a print job is in progress.</p></td>
</tr>
<tr class="odd">
<td><p><strong>PrintDirInCCDegrees</strong></p></td>
<td><p>Amount of rotation, measured counterclockwise, in degrees.</p></td>
<td><p>Valid when the driver sends either the CmdSetSimpleRotation or CmdSetAnyRotation command string.</p></td>
</tr>
<tr class="even">
<td><p><strong>RasterDataHeightInPixels</strong></p></td>
<td><p>Height, in pixels, of the image represented by current data.</p></td>
<td><p>Valid for use in any CmdSend<em>XXX</em>Data command string, and in CmdSetSrcBmpHeight command strings. Compression does not modify this value.</p></td>
</tr>
<tr class="odd">
<td><p><strong>RasterDataWidthInBytes</strong></p></td>
<td><p>Number of bytes contained in a scan line.</p></td>
<td><p>Valid for use in any CmdSend<em>XXX</em>Data command string, and in CmdSetSrcBmpWidth command strings. Compression does not modify this value.</p></td>
</tr>
<tr class="even">
<td><p><strong>RectXSize</strong></p></td>
<td><p>Rectangle width, in x-master units.</p></td>
<td><p>Valid for use in CmdSetRectWidth command strings.</p></td>
</tr>
<tr class="odd">
<td><p><strong>RectYSize</strong></p></td>
<td><p>Rectangle length, in y-master units.</p></td>
<td><p>Valid for use in CmdSetRectHeight command strings.</p></td>
</tr>
<tr class="even">
<td><p><strong>RedValue</strong></p></td>
<td><p>Red component of the current color.</p></td>
<td><p>Valid for use in CmdDefinePaletteEntry command strings. (Also see <strong>GreenValue</strong>, <strong>BlueValue</strong>.)</p></td>
</tr>
<tr class="odd">
<td><p><strong>TextXRes</strong></p></td>
<td><p>Current horizontal resolution for text, in DPI.</p></td>
<td><p>Valid whenever a print job is in progress.</p></td>
</tr>
<tr class="even">
<td><p><strong>TextYRes</strong></p></td>
<td><p>Current vertical resolution for text, in DPI.</p></td>
<td><p>Valid whenever a print job is in progress.</p></td>
</tr>
</tbody>
</table>

 

 

 




