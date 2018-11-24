---
title: TrueType Font Driver Functions
description: TrueType Font Driver Functions
ms.assetid: 9ed59393-c4a6-4d3f-9a18-c9e5493c2dc9
keywords:
- fonts WDK graphics , TrueType driver functions
- GDI WDK Windows 2000 display , fonts, TrueType driver functions
- graphics drivers WDK Windows 2000 display , fonts, TrueType driver functions
- TrueType font drivers WDK GDI
ms.date: 04/20/2017
ms.localizationpriority: medium
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
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff556235" data-raw-source="[&lt;strong&gt;DrvGetTrueTypeFile&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556235)"><strong>DrvGetTrueTypeFile</strong></a></p></td>
<td align="left"><p>Gives GDI efficient access to the memory-mapped TrueType font file.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff556269" data-raw-source="[&lt;strong&gt;DrvQueryTrueTypeOutline&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556269)"><strong>DrvQueryTrueTypeOutline</strong></a></p></td>
<td align="left"><p>Returns glyph handles in native TrueType format.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff556271" data-raw-source="[&lt;strong&gt;DrvQueryTrueTypeTable&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556271)"><strong>DrvQueryTrueTypeTable</strong></a></p></td>
<td align="left"><p>Gives GDI access to specific files in the TrueType font file format.</p></td>
</tr>
</tbody>
</table>

 

All these functions provide GDI with information about TrueType font files. *DrvQueryTrueTypeTable* should give GDI access to specific tables in the TrueType font-file format. *DrvQueryTrueTypeOutline* must send GDI glyph outlines in native TrueType format. *DrvGetTrueTypeFile* returns to GDI the TrueType driver's private entry point that allows GDI efficient access to the memory mapped TrueType font file.

 

 





