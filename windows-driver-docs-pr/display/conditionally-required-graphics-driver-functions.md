---
title: Conditionally Required Graphics Driver Functions
description: Conditionally Required Graphics Driver Functions
ms.assetid: db5816e2-83a1-491d-99f5-d693fefcf1fd
keywords:
- GDI WDK Windows 2000 display , functions, conditionally required
- graphics drivers WDK Windows 2000 display , functions, conditionally required
- functions WDK graphics , conditionally required
- drawing WDK GDI , functions, conditionally required
- GDI WDK Windows 2000 display , DDI, conditionally required functions
- graphics drivers WDK Windows 2000 display , DDI, conditionally required functions
- DDI WDK graphics , conditionally required functions
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Conditionally Required Graphics Driver Functions


## <span id="ddk_conditionally_required_graphics_driver_functions_gg"></span><span id="DDK_CONDITIONALLY_REQUIRED_GRAPHICS_DRIVER_FUNCTIONS_GG"></span>


Besides the functions that are always required, certain other functions may be required, depending on how a driver is implemented. The conditionally-required functions are listed in the following table. If the driver manages its own primary surface (using the [**EngCreateDeviceSurface**](https://msdn.microsoft.com/library/windows/hardware/ff564206) function to get a handle to the surface), or its own offscreen bitmaps, the driver must also support several [drawing functions](optional-display-driver-functions.md). Drivers writing to standard format [*DIBs*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-independent-bitmap--dib-) usually allow GDI to manage most or all of these operations. Displays that support settable palettes must also support the [**DrvSetPalette**](https://msdn.microsoft.com/library/windows/hardware/ff556282) function.

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
<td align="left"><p>[<strong>DrvCopyBits</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556182)</p></td>
<td align="left"><p>[<em>Device-managed surfaces</em>](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-managed-surface)</p></td>
<td align="left"><p>Translates between device-managed raster surfaces and GDI standard-format bitmaps.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>DrvDescribePixelFormat</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556190)</p></td>
<td align="left"><p>Displays that support windows with different pixel formats on a single surface</p></td>
<td align="left"><p>Describes a PDEV's pixel format.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>DrvGetTrueTypeFile</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556235)</p></td>
<td align="left"><p>TrueType font drivers</p></td>
<td align="left"><p>Gives GDI access to a memory-mapped TrueType font file.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>DrvLoadFontFile</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556247)</p></td>
<td align="left"><p>Font drivers</p></td>
<td align="left"><p>Specifies file to use for font realizations.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>DrvQueryFont</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556262)</p></td>
<td align="left"><p>Printer drivers</p></td>
<td align="left"><p>Retrieves a GDI structure for a given font.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>DrvQueryFontCaps</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556263)</p></td>
<td align="left"><p>Font drivers</p></td>
<td align="left"><p>Asks driver for font driver capabilities.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>DrvQueryFontData</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556264)</p></td>
<td align="left"><p>Printer drivers</p></td>
<td align="left"><p>Retrieves information about a realized font.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>DrvQueryFontFile</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556265)</p></td>
<td align="left"><p>Font drivers</p></td>
<td align="left"><p>Asks driver for font file information.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>DrvQueryFontTree</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556266)</p></td>
<td align="left"><p>Printer drivers</p></td>
<td align="left"><p>Queries a tree structure defining one of three types of font mapping.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>DrvQueryTrueTypeOutline</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556269)</p></td>
<td align="left"><p>TrueType font drivers</p></td>
<td align="left"><p>Returns TrueType glyph handles to GDI.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>DrvQueryTrueTypeTable</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556271)</p></td>
<td align="left"><p>TrueType font drivers</p></td>
<td align="left"><p>Gives GDI access to TrueType font files.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>DrvResetPDEV</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556276)</p></td>
<td align="left"><p>Devices that allow mode changes in documents</p></td>
<td align="left"><p>Transfers driver state from old PDEV to new PDEV.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>DrvSetPalette</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556282)</p></td>
<td align="left"><p>Displays that support settable palettes</p></td>
<td align="left"><p>Realizes the palette for a specified device.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>DrvSetPixelFormat</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556285)</p></td>
<td align="left"><p>Displays that support windows with different pixel formats on a single surface</p></td>
<td align="left"><p>Sets a window's pixel format.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>DrvStrokePath</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556316)</p></td>
<td align="left"><p>Device-managed surfaces</p></td>
<td align="left"><p>Renders a path on the display.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>DrvSwapBuffers</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556322)</p></td>
<td align="left"><p>Drivers that support a pixel format with double buffering</p></td>
<td align="left"><p>Displays contents of a surface's hidden buffer.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>DrvTextOut</strong>](https://msdn.microsoft.com/library/windows/hardware/ff557277)</p></td>
<td align="left"><p>Device-managed surfaces or drivers that define fonts</p></td>
<td align="left"><p>Renders a set of character images (glyphs) at specified positions.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>DrvUnloadFontFile</strong>](https://msdn.microsoft.com/library/windows/hardware/ff557287)</p></td>
<td align="left"><p>Font drivers</p></td>
<td align="left"><p>Informs driver that a font file is not needed.</p></td>
</tr>
</tbody>
</table>

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Conditionally%20Required%20Graphics%20Driver%20Functions%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




