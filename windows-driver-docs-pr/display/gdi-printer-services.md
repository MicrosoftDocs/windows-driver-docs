---
title: GDI Printer Services
description: GDI Printer Services
ms.assetid: b63c9822-f737-42fb-a831-31d16b3495c9
keywords:
- GDI WDK Windows 2000 display , printer services
- graphics drivers WDK Windows 2000 display , printer services
- drawing WDK GDI , printer services
- printer services WDK GDI
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# GDI Printer Services


## <span id="ddk_gdi_printer_services_gg"></span><span id="DDK_GDI_PRINTER_SERVICES_GG"></span>


GDI provides a number of services that are of interest to printer driver writers. The following table lists these services.

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
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564850" data-raw-source="[&lt;strong&gt;EngEnumForms&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564850)"><strong>EngEnumForms</strong></a></p></td>
<td align="left"><p>Enumerates the forms supported by the specified printer.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564938" data-raw-source="[&lt;strong&gt;EngGetForm&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564938)"><strong>EngGetForm</strong></a></p></td>
<td align="left"><p>Gets the FORM_INFO_1 details for the specified form.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564945" data-raw-source="[&lt;strong&gt;EngGetPrinter&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564945)"><strong>EngGetPrinter</strong></a></p></td>
<td align="left"><p>Retrieves information about the specified printer.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564948" data-raw-source="[&lt;strong&gt;EngGetPrinterData&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564948)"><strong>EngGetPrinterData</strong></a></p></td>
<td align="left"><p>Retrieves configuration data for the specified printer.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564951" data-raw-source="[&lt;strong&gt;EngGetPrinterDataFileName&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564951)"><strong>EngGetPrinterDataFileName</strong></a></p></td>
<td align="left"><p>Retrieves the string name of the printer&#39;s data file.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564954" data-raw-source="[&lt;strong&gt;EngGetPrinterDriver&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564954)"><strong>EngGetPrinterDriver</strong></a></p></td>
<td align="left"><p>Retrieves driver data for the specified printer.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564972" data-raw-source="[&lt;strong&gt;EngMapFontFile&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564972)"><strong>EngMapFontFile</strong></a></p></td>
<td align="left"><p>Obsolete. See the entry in this table for <strong>EngMapFontFileFD</strong>.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564973" data-raw-source="[&lt;strong&gt;EngMapFontFileFD&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564973)"><strong>EngMapFontFileFD</strong></a></p></td>
<td align="left"><p>Maps a font file into system memory, if necessary, and returns a pointer to the base location of the font data in the file.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564975" data-raw-source="[&lt;strong&gt;EngMarkBandingSurface&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564975)"><strong>EngMarkBandingSurface</strong></a></p></td>
<td align="left"><p>Marks the specified printer surface as a banding surface.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff565020" data-raw-source="[&lt;strong&gt;EngSetPrinterData&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff565020)"><strong>EngSetPrinterData</strong></a></p></td>
<td align="left"><p>Obsolete. Sets the configuration data for the specified printer.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff565441" data-raw-source="[&lt;strong&gt;EngUnmapFontFile&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff565441)"><strong>EngUnmapFontFile</strong></a></p></td>
<td align="left"><p>Obsolete. See the entry in this table for <strong>EngUnmapFontFileFD</strong>.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff565445" data-raw-source="[&lt;strong&gt;EngUnmapFontFileFD&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff565445)"><strong>EngUnmapFontFileFD</strong></a></p></td>
<td align="left"><p>Unmaps the specified font file from system memory.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff565467" data-raw-source="[&lt;strong&gt;EngWritePrinter&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff565467)"><strong>EngWritePrinter</strong></a></p></td>
<td align="left"><p>Allows printer graphics DLLs to send a data stream to printer hardware.</p></td>
</tr>
</tbody>
</table>

 

 

 





