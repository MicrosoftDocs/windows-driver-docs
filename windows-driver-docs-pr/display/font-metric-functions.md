---
title: Font Metric Functions
description: Font Metric Functions
ms.assetid: 22d88765-bde5-4f1b-b106-9396868d6fb3
keywords:
- fonts WDK graphics , metric functions
- GDI WDK Windows 2000 display , fonts, metric functions
- graphics drivers WDK Windows 2000 display , fonts, metric functions
- DrvQueryFontData
- DrvQueryFontTree
- DrvFree
- DrvDestroyFont
- DrvQueryFont
- IFIMETRICS
- raster fonts WDK graphics
- notional space coordinate system WDK graphics
- size WDK fonts
- metric functions WDK fonts
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Font Metric Functions


## <span id="ddk_font_metric_functions_gg"></span><span id="DDK_FONT_METRIC_FUNCTIONS_GG"></span>


When a driver must support fonts, it must supply font information to GDI through the [**IFIMETRICS**](https://msdn.microsoft.com/library/windows/hardware/ff567418) structure. There is a separate IFIMETRICS structure for each font. Most of the fields are expressed in terms of FWORDs, each a signed 16-bit quantity, in the design space. If the font is a raster font, the design space and device space are the same and a font unit is equivalent to the distance between pixels.

Basically, the IFIMETRICS structure is the graphics DDI version of a text-metric structure. All distances refer to the notional coordinate system of the font designer. The notional space coordinate system is a right-handed Cartesian coordinate system in which the y-coordinate increases toward the top and the x-coordinate increases toward the right.

The IFIMETRICS structure is designed to be of variable length. No restriction is placed on the length of the character strings associated with the font. It is common practice to store the strings immediately following the last field of the IFIMETRICS structure.

Any driver that provides fonts must support the [**DrvQueryFont**](https://msdn.microsoft.com/library/windows/hardware/ff556262) function. The driver also can include the function [**DrvQueryFontData**](https://msdn.microsoft.com/library/windows/hardware/ff556264) to retrieve information about a realized font. In a call to *DrvQueryFontData*, GDI provides a pointer to an array of glyphs or kerning handles. The driver returns information about associated glyphs in GDI [**GLYPHDATA**](https://msdn.microsoft.com/library/windows/hardware/ff566819) structures. If *DrvQueryFontData* has been given kerning handles, it returns information about kerning pairs in the form of Win32 POINTL structures. The following table lists the font metric functions.

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
<td align="left"><p>[<strong>DrvDestroyFont</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556192)</p></td>
<td align="left"><p>Notifies the driver that a font realization is no longer needed so the driver can free any data structures that it allocated. GDI calls this function once for the font producer and once for the font consumer. Optional--should be supported only if the driver must free allocated resources.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>DrvFree</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556226)</p></td>
<td align="left"><p>Informs the driver that the indicated data structure is no longer needed. Optional--should be implemented only if the driver's memory management requires this information.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>DrvQueryFont</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556262)</p></td>
<td align="left"><p>Returns a pointer to the [<strong>IFIMETRICS</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567418) structure for a font. Required by all drivers that deal with fonts.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>DrvQueryFontData</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556264)</p></td>
<td align="left"><p>Returns information about a realized font. Required (for selected <em>iMode</em> values) by all drivers that deal with fonts.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>DrvQueryFontTree</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556266)</p></td>
<td align="left"><p>Returns pointers to structures that define either the mapping from Unicode to glyph handles or the mapping of kerning pairs to kerning handles. Required by all drivers that deal with fonts.</p></td>
</tr>
</tbody>
</table>

 

The function *DrvQueryFontTree* allows GDI to obtain pointers to tree structures that define one of the following:

-   Mapping from Unicode to glyph handles, including glyph variants (GDI [**FD\_GLYPHSET**](https://msdn.microsoft.com/library/windows/hardware/ff565625) structure)

-   Mapping of kerning pairs to kerning handles ([**FD\_KERNINGPAIR**](https://msdn.microsoft.com/library/windows/hardware/ff565630) structure)

*DrvQueryFontTree* requires effort to generate the needed structures, so the driver should precompute these files if possible. The structures can be stored in a resource or in a file. If the structures are stored in a file, the ideal method for loading or reading them is to call the [**EngMapFontFile**](https://msdn.microsoft.com/library/windows/hardware/ff564972) function, which maps a file to the memory. Because the file does not get added to the swap file, the memory can be made available if needed, which is more efficient than opening and reading in a file.

In particular, the driver returns an identifier in the *pid* parameter. GDI passes it to the [**DrvFree**](https://msdn.microsoft.com/library/windows/hardware/ff556226) function, with the returned pointer, when the [**FD\_GLYPHSET**](https://msdn.microsoft.com/library/windows/hardware/ff565625) structure or an array of [**FD\_KERNINGPAIR**](https://msdn.microsoft.com/library/windows/hardware/ff565630) structures is no longer needed. Depending on how memory is managed in the driver, *pid* can identify the structure, identify how the structure was allocated, or do nothing at all.

[**DrvFree**](https://msdn.microsoft.com/library/windows/hardware/ff556226) and [**DrvDestroyFont**](https://msdn.microsoft.com/library/windows/hardware/ff556192) are both optional functions. GDI calls *DrvFree* to inform the driver that the specified data structure is no longer needed. The driver does not need to implement it unless it allocates memory for the structure and needs to be informed when the corresponding data structure can be released. For example, if the data is associated with the [**FONTOBJ**](https://msdn.microsoft.com/library/windows/hardware/ff565974) structure, the deletion could be deferred until a call to *DrvDestroyFont*, so it would not be necessary to implement *DrvFree*.

*DrvDestroyFont* notifies the driver that a font realization is no longer needed so the driver can free any data structures it allocated. GDI calls this function once for the font producer and once for the font consumer. It should be implemented only if the driver must free allocated resources when the font instance is destroyed.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Font%20Metric%20Functions%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




