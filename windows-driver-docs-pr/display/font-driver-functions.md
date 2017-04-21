---
title: Font Driver Functions
description: Font Driver Functions
ms.assetid: 95bf5a3b-29f8-43d2-9f24-22cfe257ead4
keywords:
- fonts WDK graphics , driver functions
- GDI WDK Windows 2000 display , fonts, driver functions
- graphics drivers WDK Windows 2000 display , fonts, driver functions
- DrvLoadFontFile
- DrvUnloadFontFile
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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
<td align="left"><p>[<strong>DrvLoadFontFile</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556247)</p></td>
<td align="left"><p>Specifies a file to be used for creating font realizations; the driver must prepare the file for use. Required for font drivers.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>DrvQueryAdvanceWidths</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556259)</p></td>
<td align="left"><p>Asks the driver to send GDI character advance widths for a specified set of glyphs.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>DrvQueryFontCaps</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556263)</p></td>
<td align="left"><p>Copies an array of bits that defines the capabilities of a font driver, to a specified buffer.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>DrvQueryFontFile</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556265)</p></td>
<td align="left"><p>Depending on the mode of the query, returns the number of font faces in a font file or in a descriptive string. Required for font drivers.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>DrvQueryGlyphAttrs</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556267)</p></td>
<td align="left"><p>Returns information about a font's glyphs.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>DrvUnloadFontFile</strong>](https://msdn.microsoft.com/library/windows/hardware/ff557287)</p></td>
<td align="left"><p>Informs driver that a font file is no longer needed so driver can do necessary cleanup. Required for font drivers.</p></td>
</tr>
</tbody>
</table>

 

GDI calls the *DrvLoadFontFile* function with a particular file to be used for creating font realizations. This function is required only of font drivers. When the function *DrvLoadFontFile* is called, the driver performs the conversions necessary to prepare the file for use.

*DrvLoadFontFile* returns a unique identifier that allows GDI to request the correct font using a GDI-maintained font usage table. Once a font is loaded, GDI does not call for the same font to be loaded again.

GDI calls *DrvUnloadFontFile* when the specified font file is no longer needed. The *DrvUnloadFontFile* function is required only in font drivers. *DrvUnloadFontFile* causes all scratch files to be deleted and all allocated system resources to be freed.

GDI calls the *DrvQueryFontFile* function to return information about a font file that was loaded by the driver. *DrvQueryFontFile* is required only in font drivers. The type of information to be returned is specified by *iMode*. If *iMode* is QFF\_DESCRIPTION, the function returns a string that Microsoft NT-based operating systems use to describe the font file. If *iMode* is QFF\_NUMFACES, the function returns the number of faces in the font file. The faces are identified by an index from the range 1 to number of faces.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Font%20Driver%20Functions%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




