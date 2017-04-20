---
title: GDI Font and Text Services
description: GDI Font and Text Services
ms.assetid: c315f3ec-ddee-42d9-8bfb-7bb2e0d1d4b2
keywords:
- fonts WDK GDI
- GDI WDK Windows 2000 display , fonts
- graphics drivers WDK Windows 2000 display , fonts
- drawing WDK GDI , fonts
- GDI WDK Windows 2000 display , text output
- graphics drivers WDK Windows 2000 display , text output
- drawing WDK GDI , text output
- text output WDK GDI
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# GDI Font and Text Services


## <span id="ddk_gdi_font_and_text_services_gg"></span><span id="DDK_GDI_FONT_AND_TEXT_SERVICES_GG"></span>


GDI provides support for font management and text output. The [**FONTOBJ**](https://msdn.microsoft.com/library/windows/hardware/ff565974) structure and related functions give a driver access to a particular instance of a font. To support text output, the driver has access to the [**STROBJ**](https://msdn.microsoft.com/library/windows/hardware/ff569738) structure and related functions. The following table lists FONTOBJ- and STROBJ-related functions.

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
<td align="left"><p>[<strong>EngComputeGlyphSet</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564192)</p></td>
<td align="left"><p>Computes the glyph set supported on a device.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>EngFntCacheAlloc</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564877)</p></td>
<td align="left"><p>Allocates memory for a cached font file.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>EngFntCacheFault</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564882)</p></td>
<td align="left"><p>Reports an error to the font engine if the font driver encountered an error reading from or writing to a font data cache.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>EngFntCacheLookUp</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564887)</p></td>
<td align="left"><p>Retrieves a pointer to cached font file data.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>EngGetCurrentCodePage</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564917)</p></td>
<td align="left"><p>Returns the system's default OEM and ANSI code pages.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>EngGetType1FontList</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564956)</p></td>
<td align="left"><p>Retrieves a list of PostScript Type 1 fonts that are installed both locally and remotely.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>EngTextOut</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565034)</p></td>
<td align="left"><p>This is the GDI simulation for the [<strong>DrvTextOut</strong>](https://msdn.microsoft.com/library/windows/hardware/ff557277) function.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>FONTOBJ_cGetAllGlyphHandles</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565977)</p></td>
<td align="left"><p>Allows the driver to retrieve every glyph handle of a GDI font. The driver uses this service to download an entire font.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>FONTOBJ_cGetGlyphs</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565982)</p></td>
<td align="left"><p>Translates glyph handles into pointers to the associated glyph data for the font consumer. These pointers are valid until the next call to <strong>FONTOBJ_cGetGlyphs</strong>.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>FONTOBJ_pfdg</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565989)</p></td>
<td align="left"><p>Retrieves the pointer to the [<strong>FD_GLYPHSET</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565625) structure associated with the specified font.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>FONTOBJ_pifi</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565990)</p></td>
<td align="left"><p>Retrieves the pointer to the [<strong>IFIMETRICS</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567418) structure that describes the associated font.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>FONTOBJ_pjOpenTypeTablePointer</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565993)</p></td>
<td align="left"><p>Returns a pointer to a view of an OpenType table.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>FONTOBJ_pQueryGlyphAttrs</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565996)</p></td>
<td align="left"><p>Returns information about a font's glyphs.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>FONTOBJ_pvTrueTypeFontFile</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566001)</p></td>
<td align="left"><p>Retrieves a pointer to a view of a TrueType, OpenType, or Type1 font file.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>FONTOBJ_pwszFontFilePaths</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566003)</p></td>
<td align="left"><p>Retrieves the file path(s) associated with a font.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>FONTOBJ_pxoGetXform</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566008)</p></td>
<td align="left"><p>Retrieves the Notional-to-Device transform for the associated font. This transform is required for a driver to realize a driver-supplied font.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>FONTOBJ_vGetInfo</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566013)</p></td>
<td align="left"><p>Returns information that describes the associated font.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>STROBJ_bEnum</strong>](https://msdn.microsoft.com/library/windows/hardware/ff569739)</p></td>
<td align="left"><p>Enumerates glyph identities and positions in the specified STROBJ.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>STROBJ_bEnumPositionsOnly</strong>](https://msdn.microsoft.com/library/windows/hardware/ff569740)</p></td>
<td align="left"><p>Enumerates glyph identities and positions for a specified text string, but does not create cached glyph bitmaps.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>STROBJ_bGetAdvanceWidths</strong>](https://msdn.microsoft.com/library/windows/hardware/ff569741)</p></td>
<td align="left"><p>Returns vectors specifying the probable widths of glyphs making up a specified string.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>STROBJ_dwGetCodePage</strong>](https://msdn.microsoft.com/library/windows/hardware/ff569742)</p></td>
<td align="left"><p>Returns the code page associated with the specified STROBJ.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>STROBJ_fxBreakExtra</strong>](https://msdn.microsoft.com/library/windows/hardware/ff569743)</p></td>
<td align="left"><p>Retrieves the amount of extra space to be added to each space character in a string when displaying and/or printing justified text.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>STROBJ_vEnumStart</strong>](https://msdn.microsoft.com/library/windows/hardware/ff569745)</p></td>
<td align="left"><p>Restarts the enumeration of the [<strong>GLYPHPOS</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566824) array for the specified STROBJ. This function should be called by the driver prior to subsequent enumerations.</p></td>
</tr>
</tbody>
</table>

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20GDI%20Font%20and%20Text%20Services%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




