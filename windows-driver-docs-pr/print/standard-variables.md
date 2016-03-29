---
title: Standard Variables
description: Standard Variables
ms.assetid: d3f85c0f-7387-4301-8b1e-904471aed4b0
keywords: ["GPD file entries WDK Unidrv , standard variables", "variables WDK GPD files", "standard variables WDK GPD files"]
---

# Standard Variables


## <a href="" id="ddk-standard-variables-gg"></a>


The GPD language defines a set of standard variables that can be referenced within command strings, using the [command string format](command-string-format.md). The Unidrv driver assigns values to these variables. From the point of view of a GPD file, the variables are read-only.

All standard variables are stored as DWORD integers.

The following [printer command](printer-commands.md) entry specifies the command string that is sent to an HP LaserJet 4P when a block of raster data is ready:

```
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
<th align="left">Standard Variable Name</th>
<th align="left">Value</th>
<th align="left">Comments</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>BlueValue</strong></p></td>
<td align="left"><p>Blue component of the current color.</p></td>
<td align="left"><p>Valid for use in CmdDefinePaletteEntry command strings. (Also see <strong>GreenValue</strong>, <strong>RedValue</strong>.)</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>CurrentFontID</strong></p></td>
<td align="left"><p>Identification number of the current downloaded soft font.</p></td>
<td align="left"><p>Valid if current print job includes downloaded soft fonts.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>CurrentPaletteIndex</strong></p></td>
<td align="left"><p>Current index into the color palette.</p></td>
<td align="left"><p>Valid for use in CmdSelectPaletteEntry command strings. (Also see <strong>GreenValue</strong>, <strong>RedValue</strong>.)</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>CursorOriginX</strong></p></td>
<td align="left"><p>X coordinate of cursor origin, in master units.</p></td>
<td align="left"><p>Valid whenever a print job is in progress.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>CursorOriginY</strong></p></td>
<td align="left"><p>Y coordinate of cursor origin, in master units.</p></td>
<td align="left"><p>Valid whenever a print job is in progress.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>DestX</strong></p></td>
<td align="left"><p>X coordinate of cursor destination, in master units, relative to the cursor origin.</p></td>
<td align="left"><p>Valid for use in CmdXMoveAbsolute command strings.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>DestXRel</strong></p></td>
<td align="left"><p>X coordinate of cursor destination, in master units, relative to the current cursor position.</p></td>
<td align="left"><p>Valid for use in CmdXMoveRelLeft and CmdXMoveRelRight command strings.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>DestY</strong></p></td>
<td align="left"><p>Y coordinate of cursor destination, in master units, relative to the cursor origin.</p></td>
<td align="left"><p>Valid for use in CmdYMoveAbsolute command strings.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>DestYRel</strong></p></td>
<td align="left"><p>Y coordinate of cursor destination, in master units, relative to the current cursor position.</p></td>
<td align="left"><p>Valid for use in CmdYMoveRelUp and CmdYMoveRelDown command strings.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>FontBold</strong></p></td>
<td align="left"><p>Set to one if current font is bold, or zero otherwise.</p></td>
<td align="left"><p>Valid when a font has been specified.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>FontHeight</strong></p></td>
<td align="left"><p>Height, in master units, of the current font.</p></td>
<td align="left"><p>Valid when a font has been specified.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>FontItalic</strong></p></td>
<td align="left"><p>Set to one if current font is italic, or zero otherwise.</p></td>
<td align="left"><p>Valid when a font has been specified.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>FontMaxWidth</strong></p></td>
<td align="left"><p>Set to the maximum character increment of all glyphs in the font.</p></td>
<td align="left"><p>Valid when a font has been specified.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>FontStrikeThru</strong></p></td>
<td align="left"><p>Set to one if strike-through is enabled for the current font, or zero otherwise.</p></td>
<td align="left"><p>Valid when a font has been specified.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>FontUnderLine</strong></p></td>
<td align="left"><p>Set to one if current font is underlined, or zero otherwise.</p></td>
<td align="left"><p>Valid when a font has been specified.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>FontWidth</strong></p></td>
<td align="left"><p>Width, in master units, of the current font.</p></td>
<td align="left"><p>Valid when a font has been specified.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>GraphicsXRes</strong></p></td>
<td align="left"><p>Current horizontal resolution for graphics, in DPI.</p></td>
<td align="left"><p>Valid whenever a print job is in progress.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>GraphicsYRes</strong></p></td>
<td align="left"><p>Current vertical resolution for graphics, in DPI.</p></td>
<td align="left"><p>Valid whenever a print job is in progress.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>GrayPercentage</strong></p></td>
<td align="left"><p>Gray level (percentage) to use for gray fill.</p></td>
<td align="left"><p>Valid for use in CmdRectGrayFill command strings.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>GreenValue</strong></p></td>
<td align="left"><p>Green component of the current color.</p></td>
<td align="left"><p>Valid for use in CmdDefinePaletteEntry command strings. (Also see <strong>BlueValue</strong>, <strong>RedValue</strong>.)</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>LinefeedSpacing</strong></p></td>
<td align="left"><p>Amount of vertical space, in master units, representing a linefeed.</p></td>
<td align="left"><p>Valid for use in CmdSetLineSpacing command strings.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>NextFontID</strong></p></td>
<td align="left"><p>Identification number of the next soft font to be downloaded.</p></td>
<td align="left"><p>Valid for use in CmdSetFontID command strings.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>NextGlyph</strong></p></td>
<td align="left"><p>The two-byte code of the next glyph to download.</p></td>
<td align="left"><p>Valid for use in CmdSetCharCode command strings.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>NumOfCopies</strong></p></td>
<td align="left"><p>Number of copies requested by the user.</p></td>
<td align="left"><p>Valid whenever a print job is in progress.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>NumOfDataBytes</strong></p></td>
<td align="left"><p>Number of bytes of raster data ready for transfer.</p></td>
<td align="left"><p>Valid for use in any CmdSend<em>XXX</em>Data command string.</p>
<p>If data is compressed, the value is the number of bytes after compression.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>PageNumber</strong></p></td>
<td align="left"><p>The number of the page currently being printed. Note that this does not necessarily correspond to the application's page number, but rather the number of times [<em>DrvSendPage</em>](https://msdn.microsoft.com/library/windows/hardware/ff556281) has been called.</p>
<p>This value is initialized by [<strong>DrvStartDoc</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556296) and is incremented by <strong>DrvSendPage</strong>.</p>
<p>For example, if N-up = 4 is selected, <strong>PageNumber</strong> is incremented to 2 only when the fifth page of the document is being printed.</p>
<p>As another example, if a document is printed in reverse order (back to front) the <strong>PageNumber</strong> standard variable still reports the first page to be printed as page 1, even though this is the last page of the document.</p>
<p>This behavior is needed to properly support the auto-duplexing feature.</p>
<p>The OEM should use <strong>PageNumber</strong> only to determine whether the current page is the front or back side.</p></td>
<td align="left"><p>Valid whenever a print job is in progress.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>PaletteIndexToProgram</strong></p></td>
<td align="left"><p>Index into the color palette for the next entry to program.</p></td>
<td align="left"><p>Valid for use in CmdDefinePaletteEntry command strings. (Also see <strong>RedValue</strong>, <strong>GreenValue</strong>, <strong>BlueValue</strong>, <strong>CurrentPaletteIndex</strong>.)</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>PatternBrushID</strong></p></td>
<td align="left"><p>Identification number of a downloaded pattern brush.</p></td>
<td align="left"><p>Valid for use with CmdDownloadPattern and CmdSelectPattern command strings.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>PatternBrushSize</strong></p></td>
<td align="left"><p>Size, in bytes, of the current pattern brush.</p></td>
<td align="left"><p>Valid for use with CmdDownloadPattern command string.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>PatternBrushType</strong></p></td>
<td align="left"><p></p>
Type of the current pattern brush. Value can be:
2: Shading pattern
3: Cross-hatch pattern
4: User-defined pattern</td>
<td align="left"><p>Valid for use with CmdDownloadPattern and CmdSelectPattern command strings.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>PhysPaperLength</strong></p></td>
<td align="left"><p>Portrait-mode length, in y-master units, of the paper currently in use.</p></td>
<td align="left"><p>Valid whenever a print job is in progress.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>PhysPaperWidth</strong></p></td>
<td align="left"><p>Portrait-mode width, in master units, of the paper currently in use.</p></td>
<td align="left"><p>Valid whenever a print job is in progress.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>PrintDirInCCDegrees</strong></p></td>
<td align="left"><p>Amount of rotation, measured counterclockwise, in degrees.</p></td>
<td align="left"><p>Valid when the driver sends either the CmdSetSimpleRotation or CmdSetAnyRotation command string.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>RasterDataHeightInPixels</strong></p></td>
<td align="left"><p>Height, in pixels, of the image represented by current data.</p></td>
<td align="left"><p>Valid for use in any CmdSend<em>XXX</em>Data command string, and in CmdSetSrcBmpHeight command strings. Compression does not modify this value.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>RasterDataWidthInBytes</strong></p></td>
<td align="left"><p>Number of bytes contained in a scan line.</p></td>
<td align="left"><p>Valid for use in any CmdSend<em>XXX</em>Data command string, and in CmdSetSrcBmpWidth command strings. Compression does not modify this value.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>RectXSize</strong></p></td>
<td align="left"><p>Rectangle width, in x-master units.</p></td>
<td align="left"><p>Valid for use in CmdSetRectWidth command strings.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>RectYSize</strong></p></td>
<td align="left"><p>Rectangle length, in y-master units.</p></td>
<td align="left"><p>Valid for use in CmdSetRectHeight command strings.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>RedValue</strong></p></td>
<td align="left"><p>Red component of the current color.</p></td>
<td align="left"><p>Valid for use in CmdDefinePaletteEntry command strings. (Also see <strong>GreenValue</strong>, <strong>BlueValue</strong>.)</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>TextXRes</strong></p></td>
<td align="left"><p>Current horizontal resolution for text, in DPI.</p></td>
<td align="left"><p>Valid whenever a print job is in progress.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>TextYRes</strong></p></td>
<td align="left"><p>Current vertical resolution for text, in DPI.</p></td>
<td align="left"><p>Valid whenever a print job is in progress.</p></td>
</tr>
</tbody>
</table>

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Standard%20Variables%20%20RELEASE:%20%283/29/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




