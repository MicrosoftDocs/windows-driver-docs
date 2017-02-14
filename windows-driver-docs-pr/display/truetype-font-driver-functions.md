---
title: TrueType Font Driver Functions
description: TrueType Font Driver Functions
ms.assetid: 9ed59393-c4a6-4d3f-9a18-c9e5493c2dc9
keywords: ["fonts WDK graphics , TrueType driver functions", "GDI WDK Windows 2000 display , fonts, TrueType driver functions", "graphics drivers WDK Windows 2000 display , fonts, TrueType driver functions", "TrueType font drivers WDK GDI"]
---

# TrueType Font Driver Functions


## <span id="ddk_truetype_font_driver_functions_gg"></span><span id="DDK_TRUETYPE_FONT_DRIVER_FUNCTIONS_GG"></span>


TrueType font drivers must support the functions listed in the following table.

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
<td align="left"><p>[<strong>DrvGetTrueTypeFile</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556235)</p></td>
<td align="left"><p>Gives GDI efficient access to the memory-mapped TrueType font file.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>DrvQueryTrueTypeOutline</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556269)</p></td>
<td align="left"><p>Returns glyph handles in native TrueType format.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>DrvQueryTrueTypeTable</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556271)</p></td>
<td align="left"><p>Gives GDI access to specific files in the TrueType font file format.</p></td>
</tr>
</tbody>
</table>

 

All these functions provide GDI with information about TrueType font files. *DrvQueryTrueTypeTable* should give GDI access to specific tables in the TrueType font-file format. *DrvQueryTrueTypeOutline* must send GDI glyph outlines in native TrueType format. *DrvGetTrueTypeFile* returns to GDI the TrueType driver's private entry point that allows GDI efficient access to the memory mapped TrueType font file.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20TrueType%20Font%20Driver%20Functions%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




