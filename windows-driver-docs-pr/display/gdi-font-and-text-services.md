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
ms.date: 04/20/2017
ms.localizationpriority: medium
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
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564192" data-raw-source="[&lt;strong&gt;EngComputeGlyphSet&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564192)"><strong>EngComputeGlyphSet</strong></a></p></td>
<td align="left"><p>Computes the glyph set supported on a device.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564877" data-raw-source="[&lt;strong&gt;EngFntCacheAlloc&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564877)"><strong>EngFntCacheAlloc</strong></a></p></td>
<td align="left"><p>Allocates memory for a cached font file.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564882" data-raw-source="[&lt;strong&gt;EngFntCacheFault&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564882)"><strong>EngFntCacheFault</strong></a></p></td>
<td align="left"><p>Reports an error to the font engine if the font driver encountered an error reading from or writing to a font data cache.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564887" data-raw-source="[&lt;strong&gt;EngFntCacheLookUp&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564887)"><strong>EngFntCacheLookUp</strong></a></p></td>
<td align="left"><p>Retrieves a pointer to cached font file data.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564917" data-raw-source="[&lt;strong&gt;EngGetCurrentCodePage&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564917)"><strong>EngGetCurrentCodePage</strong></a></p></td>
<td align="left"><p>Returns the system&#39;s default OEM and ANSI code pages.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564956" data-raw-source="[&lt;strong&gt;EngGetType1FontList&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564956)"><strong>EngGetType1FontList</strong></a></p></td>
<td align="left"><p>Retrieves a list of PostScript Type 1 fonts that are installed both locally and remotely.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff565034" data-raw-source="[&lt;strong&gt;EngTextOut&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff565034)"><strong>EngTextOut</strong></a></p></td>
<td align="left"><p>This is the GDI simulation for the <a href="https://msdn.microsoft.com/library/windows/hardware/ff557277" data-raw-source="[&lt;strong&gt;DrvTextOut&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff557277)"><strong>DrvTextOut</strong></a> function.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff565977" data-raw-source="[&lt;strong&gt;FONTOBJ_cGetAllGlyphHandles&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff565977)"><strong>FONTOBJ_cGetAllGlyphHandles</strong></a></p></td>
<td align="left"><p>Allows the driver to retrieve every glyph handle of a GDI font. The driver uses this service to download an entire font.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff565982" data-raw-source="[&lt;strong&gt;FONTOBJ_cGetGlyphs&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff565982)"><strong>FONTOBJ_cGetGlyphs</strong></a></p></td>
<td align="left"><p>Translates glyph handles into pointers to the associated glyph data for the font consumer. These pointers are valid until the next call to <strong>FONTOBJ_cGetGlyphs</strong>.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff565989" data-raw-source="[&lt;strong&gt;FONTOBJ_pfdg&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff565989)"><strong>FONTOBJ_pfdg</strong></a></p></td>
<td align="left"><p>Retrieves the pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff565625" data-raw-source="[&lt;strong&gt;FD_GLYPHSET&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff565625)"><strong>FD_GLYPHSET</strong></a> structure associated with the specified font.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff565990" data-raw-source="[&lt;strong&gt;FONTOBJ_pifi&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff565990)"><strong>FONTOBJ_pifi</strong></a></p></td>
<td align="left"><p>Retrieves the pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff567418" data-raw-source="[&lt;strong&gt;IFIMETRICS&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567418)"><strong>IFIMETRICS</strong></a> structure that describes the associated font.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff565993" data-raw-source="[&lt;strong&gt;FONTOBJ_pjOpenTypeTablePointer&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff565993)"><strong>FONTOBJ_pjOpenTypeTablePointer</strong></a></p></td>
<td align="left"><p>Returns a pointer to a view of an OpenType table.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff565996" data-raw-source="[&lt;strong&gt;FONTOBJ_pQueryGlyphAttrs&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff565996)"><strong>FONTOBJ_pQueryGlyphAttrs</strong></a></p></td>
<td align="left"><p>Returns information about a font&#39;s glyphs.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff566001" data-raw-source="[&lt;strong&gt;FONTOBJ_pvTrueTypeFontFile&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566001)"><strong>FONTOBJ_pvTrueTypeFontFile</strong></a></p></td>
<td align="left"><p>Retrieves a pointer to a view of a TrueType, OpenType, or Type1 font file.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff566003" data-raw-source="[&lt;strong&gt;FONTOBJ_pwszFontFilePaths&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566003)"><strong>FONTOBJ_pwszFontFilePaths</strong></a></p></td>
<td align="left"><p>Retrieves the file path(s) associated with a font.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff566008" data-raw-source="[&lt;strong&gt;FONTOBJ_pxoGetXform&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566008)"><strong>FONTOBJ_pxoGetXform</strong></a></p></td>
<td align="left"><p>Retrieves the Notional-to-Device transform for the associated font. This transform is required for a driver to realize a driver-supplied font.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff566013" data-raw-source="[&lt;strong&gt;FONTOBJ_vGetInfo&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566013)"><strong>FONTOBJ_vGetInfo</strong></a></p></td>
<td align="left"><p>Returns information that describes the associated font.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff569739" data-raw-source="[&lt;strong&gt;STROBJ_bEnum&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff569739)"><strong>STROBJ_bEnum</strong></a></p></td>
<td align="left"><p>Enumerates glyph identities and positions in the specified STROBJ.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff569740" data-raw-source="[&lt;strong&gt;STROBJ_bEnumPositionsOnly&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff569740)"><strong>STROBJ_bEnumPositionsOnly</strong></a></p></td>
<td align="left"><p>Enumerates glyph identities and positions for a specified text string, but does not create cached glyph bitmaps.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff569741" data-raw-source="[&lt;strong&gt;STROBJ_bGetAdvanceWidths&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff569741)"><strong>STROBJ_bGetAdvanceWidths</strong></a></p></td>
<td align="left"><p>Returns vectors specifying the probable widths of glyphs making up a specified string.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff569742" data-raw-source="[&lt;strong&gt;STROBJ_dwGetCodePage&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff569742)"><strong>STROBJ_dwGetCodePage</strong></a></p></td>
<td align="left"><p>Returns the code page associated with the specified STROBJ.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff569743" data-raw-source="[&lt;strong&gt;STROBJ_fxBreakExtra&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff569743)"><strong>STROBJ_fxBreakExtra</strong></a></p></td>
<td align="left"><p>Retrieves the amount of extra space to be added to each space character in a string when displaying and/or printing justified text.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff569745" data-raw-source="[&lt;strong&gt;STROBJ_vEnumStart&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff569745)"><strong>STROBJ_vEnumStart</strong></a></p></td>
<td align="left"><p>Restarts the enumeration of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff566824" data-raw-source="[&lt;strong&gt;GLYPHPOS&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566824)"><strong>GLYPHPOS</strong></a> array for the specified STROBJ. This function should be called by the driver prior to subsequent enumerations.</p></td>
</tr>
</tbody>
</table>

 

 

 





