---
title: Font Driver Functions
description: Font Driver Functions
keywords:
- fonts WDK graphics , driver functions
- GDI WDK Windows 2000 display , fonts, driver functions
- graphics drivers WDK Windows 2000 display , fonts, driver functions
- DrvLoadFontFile
- DrvUnloadFontFile
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Font Driver Functions


## <span id="ddk_font_driver_functions_gg"></span><span id="DDK_FONT_DRIVER_FUNCTIONS_GG"></span>


In addition to the functions described in the previous topics, the following table lists several other functions that font drivers should support.

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
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-drvloadfontfile" data-raw-source="[&lt;strong&gt;DrvLoadFontFile&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-drvloadfontfile)"><strong>DrvLoadFontFile</strong></a></p></td>
<td align="left"><p>Specifies a file to be used for creating font realizations; the driver must prepare the file for use. Required for font drivers.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-drvqueryadvancewidths" data-raw-source="[&lt;strong&gt;DrvQueryAdvanceWidths&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-drvqueryadvancewidths)"><strong>DrvQueryAdvanceWidths</strong></a></p></td>
<td align="left"><p>Asks the driver to send GDI character advance widths for a specified set of glyphs.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-drvqueryfontcaps" data-raw-source="[&lt;strong&gt;DrvQueryFontCaps&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-drvqueryfontcaps)"><strong>DrvQueryFontCaps</strong></a></p></td>
<td align="left"><p>Copies an array of bits that defines the capabilities of a font driver, to a specified buffer.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-drvqueryfontfile" data-raw-source="[&lt;strong&gt;DrvQueryFontFile&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-drvqueryfontfile)"><strong>DrvQueryFontFile</strong></a></p></td>
<td align="left"><p>Depending on the mode of the query, returns the number of font faces in a font file or in a descriptive string. Required for font drivers.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/winddi/nc-winddi-pfn_drvqueryglyphattrs" data-raw-source="[&lt;strong&gt;DrvQueryGlyphAttrs&lt;/strong&gt;](/windows/win32/api/winddi/nc-winddi-pfn_drvqueryglyphattrs)"><strong>DrvQueryGlyphAttrs</strong></a></p></td>
<td align="left"><p>Returns information about a font's glyphs.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-drvunloadfontfile" data-raw-source="[&lt;strong&gt;DrvUnloadFontFile&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-drvunloadfontfile)"><strong>DrvUnloadFontFile</strong></a></p></td>
<td align="left"><p>Informs driver that a font file is no longer needed so driver can do necessary cleanup. Required for font drivers.</p></td>
</tr>
</tbody>
</table>

 

GDI calls the *DrvLoadFontFile* function with a particular file to be used for creating font realizations. This function is required only of font drivers. When the function *DrvLoadFontFile* is called, the driver performs the conversions necessary to prepare the file for use.

*DrvLoadFontFile* returns a unique identifier that allows GDI to request the correct font using a GDI-maintained font usage table. Once a font is loaded, GDI does not call for the same font to be loaded again.

GDI calls *DrvUnloadFontFile* when the specified font file is no longer needed. The *DrvUnloadFontFile* function is required only in font drivers. *DrvUnloadFontFile* causes all scratch files to be deleted and all allocated system resources to be freed.

GDI calls the *DrvQueryFontFile* function to return information about a font file that was loaded by the driver. *DrvQueryFontFile* is required only in font drivers. The type of information to be returned is specified by *iMode*. If *iMode* is QFF\_DESCRIPTION, the function returns a string that Microsoft NT-based operating systems use to describe the font file. If *iMode* is QFF\_NUMFACES, the function returns the number of faces in the font file. The faces are identified by an index from the range 1 to number of faces.

