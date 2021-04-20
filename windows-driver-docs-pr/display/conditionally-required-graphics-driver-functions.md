---
title: Conditionally Required Graphics Driver Functions
description: Conditionally Required Graphics Driver Functions
keywords:
- GDI WDK Windows 2000 display , functions, conditionally required
- graphics drivers WDK Windows 2000 display , functions, conditionally required
- functions WDK graphics , conditionally required
- drawing WDK GDI , functions, conditionally required
- GDI WDK Windows 2000 display , DDI, conditionally required functions
- graphics drivers WDK Windows 2000 display , DDI, conditionally required functions
- DDI WDK graphics , conditionally required functions
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Conditionally Required Graphics Driver Functions


## <span id="ddk_conditionally_required_graphics_driver_functions_gg"></span><span id="DDK_CONDITIONALLY_REQUIRED_GRAPHICS_DRIVER_FUNCTIONS_GG"></span>


Besides the functions that are always required, certain other functions may be required, depending on how a driver is implemented. The conditionally-required functions are listed in the following table. If the driver manages its own primary surface (using the [**EngCreateDeviceSurface**](/windows/win32/api/winddi/nf-winddi-engcreatedevicesurface) function to get a handle to the surface), or its own offscreen bitmaps, the driver must also support several [drawing functions](optional-display-driver-functions.md). Drivers writing to standard format *DIBs* usually allow GDI to manage most or all of these operations. Displays that support settable palettes must also support the [**DrvSetPalette**](/windows/win32/api/winddi/nf-winddi-drvsetpalette) function.

It is more common for a printer driver than a display driver to define or draw fonts. A display driver is not required to handle fonts. If the hardware has a resident font, the driver must supply information to GDI about this font. This information includes font metrics, mappings from Unicode to individual glyph identities, individual glyph attributes, and kerning tables.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Entry Point</th>
<th align="left">When Required</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-drvcopybits" data-raw-source="[&lt;strong&gt;DrvCopyBits&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-drvcopybits)"><strong>DrvCopyBits</strong></a></p></td>
<td align="left"><p><a href="/windows-hardware/drivers/#wdkgloss-device-managed-surface" data-raw-source="&lt;em&gt;Device-managed surfaces&lt;/em&gt;"><em>Device-managed surfaces</em></a></p></td>
<td align="left"><p>Translates between device-managed raster surfaces and GDI standard-format bitmaps.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-drvdescribepixelformat" data-raw-source="[&lt;strong&gt;DrvDescribePixelFormat&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-drvdescribepixelformat)"><strong>DrvDescribePixelFormat</strong></a></p></td>
<td align="left"><p>Displays that support windows with different pixel formats on a single surface</p></td>
<td align="left"><p>Describes a PDEV's pixel format.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-drvgettruetypefile" data-raw-source="[&lt;strong&gt;DrvGetTrueTypeFile&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-drvgettruetypefile)"><strong>DrvGetTrueTypeFile</strong></a></p></td>
<td align="left"><p>TrueType font drivers</p></td>
<td align="left"><p>Gives GDI access to a memory-mapped TrueType font file.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-drvloadfontfile" data-raw-source="[&lt;strong&gt;DrvLoadFontFile&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-drvloadfontfile)"><strong>DrvLoadFontFile</strong></a></p></td>
<td align="left"><p>Font drivers</p></td>
<td align="left"><p>Specifies file to use for font realizations.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-drvqueryfont" data-raw-source="[&lt;strong&gt;DrvQueryFont&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-drvqueryfont)"><strong>DrvQueryFont</strong></a></p></td>
<td align="left"><p>Printer drivers</p></td>
<td align="left"><p>Retrieves a GDI structure for a given font.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-drvqueryfontcaps" data-raw-source="[&lt;strong&gt;DrvQueryFontCaps&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-drvqueryfontcaps)"><strong>DrvQueryFontCaps</strong></a></p></td>
<td align="left"><p>Font drivers</p></td>
<td align="left"><p>Asks driver for font driver capabilities.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-drvqueryfontdata" data-raw-source="[&lt;strong&gt;DrvQueryFontData&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-drvqueryfontdata)"><strong>DrvQueryFontData</strong></a></p></td>
<td align="left"><p>Printer drivers</p></td>
<td align="left"><p>Retrieves information about a realized font.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-drvqueryfontfile" data-raw-source="[&lt;strong&gt;DrvQueryFontFile&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-drvqueryfontfile)"><strong>DrvQueryFontFile</strong></a></p></td>
<td align="left"><p>Font drivers</p></td>
<td align="left"><p>Asks driver for font file information.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-drvqueryfonttree" data-raw-source="[&lt;strong&gt;DrvQueryFontTree&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-drvqueryfonttree)"><strong>DrvQueryFontTree</strong></a></p></td>
<td align="left"><p>Printer drivers</p></td>
<td align="left"><p>Queries a tree structure defining one of three types of font mapping.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-drvquerytruetypeoutline" data-raw-source="[&lt;strong&gt;DrvQueryTrueTypeOutline&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-drvquerytruetypeoutline)"><strong>DrvQueryTrueTypeOutline</strong></a></p></td>
<td align="left"><p>TrueType font drivers</p></td>
<td align="left"><p>Returns TrueType glyph handles to GDI.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-drvquerytruetypetable" data-raw-source="[&lt;strong&gt;DrvQueryTrueTypeTable&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-drvquerytruetypetable)"><strong>DrvQueryTrueTypeTable</strong></a></p></td>
<td align="left"><p>TrueType font drivers</p></td>
<td align="left"><p>Gives GDI access to TrueType font files.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-drvresetpdev" data-raw-source="[&lt;strong&gt;DrvResetPDEV&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-drvresetpdev)"><strong>DrvResetPDEV</strong></a></p></td>
<td align="left"><p>Devices that allow mode changes in documents</p></td>
<td align="left"><p>Transfers driver state from old PDEV to new PDEV.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-drvsetpalette" data-raw-source="[&lt;strong&gt;DrvSetPalette&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-drvsetpalette)"><strong>DrvSetPalette</strong></a></p></td>
<td align="left"><p>Displays that support settable palettes</p></td>
<td align="left"><p>Realizes the palette for a specified device.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-drvsetpixelformat" data-raw-source="[&lt;strong&gt;DrvSetPixelFormat&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-drvsetpixelformat)"><strong>DrvSetPixelFormat</strong></a></p></td>
<td align="left"><p>Displays that support windows with different pixel formats on a single surface</p></td>
<td align="left"><p>Sets a window's pixel format.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-drvstrokepath" data-raw-source="[&lt;strong&gt;DrvStrokePath&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-drvstrokepath)"><strong>DrvStrokePath</strong></a></p></td>
<td align="left"><p>Device-managed surfaces</p></td>
<td align="left"><p>Renders a path on the display.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-drvswapbuffers" data-raw-source="[&lt;strong&gt;DrvSwapBuffers&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-drvswapbuffers)"><strong>DrvSwapBuffers</strong></a></p></td>
<td align="left"><p>Drivers that support a pixel format with double buffering</p></td>
<td align="left"><p>Displays contents of a surface's hidden buffer.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-drvtextout" data-raw-source="[&lt;strong&gt;DrvTextOut&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-drvtextout)"><strong>DrvTextOut</strong></a></p></td>
<td align="left"><p>Device-managed surfaces or drivers that define fonts</p></td>
<td align="left"><p>Renders a set of character images (glyphs) at specified positions.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-drvunloadfontfile" data-raw-source="[&lt;strong&gt;DrvUnloadFontFile&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-drvunloadfontfile)"><strong>DrvUnloadFontFile</strong></a></p></td>
<td align="left"><p>Font drivers</p></td>
<td align="left"><p>Informs driver that a font file is not needed.</p></td>
</tr>
</tbody>
</table>

