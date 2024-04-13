---
title: GDI Printer Services
description: GDI Printer Services
keywords:
- GDI WDK Windows 2000 display , printer services
- graphics drivers WDK Windows 2000 display , printer services
- drawing WDK GDI , printer services
- printer services WDK GDI
ms.date: 04/20/2017
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
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-engenumforms" data-raw-source="[&lt;strong&gt;EngEnumForms&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-engenumforms)"><strong>EngEnumForms</strong></a></p></td>
<td align="left"><p>Enumerates the forms supported by the specified printer.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-enggetform" data-raw-source="[&lt;strong&gt;EngGetForm&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-enggetform)"><strong>EngGetForm</strong></a></p></td>
<td align="left"><p>Gets the FORM_INFO_1 details for the specified form.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-enggetprinter" data-raw-source="[&lt;strong&gt;EngGetPrinter&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-enggetprinter)"><strong>EngGetPrinter</strong></a></p></td>
<td align="left"><p>Retrieves information about the specified printer.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-enggetprinterdata" data-raw-source="[&lt;strong&gt;EngGetPrinterData&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-enggetprinterdata)"><strong>EngGetPrinterData</strong></a></p></td>
<td align="left"><p>Retrieves configuration data for the specified printer.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-enggetprinterdatafilename" data-raw-source="[&lt;strong&gt;EngGetPrinterDataFileName&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-enggetprinterdatafilename)"><strong>EngGetPrinterDataFileName</strong></a></p></td>
<td align="left"><p>Retrieves the string name of the printer's data file.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-enggetprinterdriver" data-raw-source="[&lt;strong&gt;EngGetPrinterDriver&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-enggetprinterdriver)"><strong>EngGetPrinterDriver</strong></a></p></td>
<td align="left"><p>Retrieves driver data for the specified printer.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-engmapfontfile" data-raw-source="[&lt;strong&gt;EngMapFontFile&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-engmapfontfile)"><strong>EngMapFontFile</strong></a></p></td>
<td align="left"><p>Obsolete. See the entry in this table for <strong>EngMapFontFileFD</strong>.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-engmapfontfilefd" data-raw-source="[&lt;strong&gt;EngMapFontFileFD&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-engmapfontfilefd)"><strong>EngMapFontFileFD</strong></a></p></td>
<td align="left"><p>Maps a font file into system memory, if necessary, and returns a pointer to the base location of the font data in the file.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-engmarkbandingsurface" data-raw-source="[&lt;strong&gt;EngMarkBandingSurface&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-engmarkbandingsurface)"><strong>EngMarkBandingSurface</strong></a></p></td>
<td align="left"><p>Marks the specified printer surface as a banding surface.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-engsetprinterdata" data-raw-source="[&lt;strong&gt;EngSetPrinterData&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-engsetprinterdata)"><strong>EngSetPrinterData</strong></a></p></td>
<td align="left"><p>Obsolete. Sets the configuration data for the specified printer.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-engunmapfontfile" data-raw-source="[&lt;strong&gt;EngUnmapFontFile&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-engunmapfontfile)"><strong>EngUnmapFontFile</strong></a></p></td>
<td align="left"><p>Obsolete. See the entry in this table for <strong>EngUnmapFontFileFD</strong>.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-engunmapfontfilefd" data-raw-source="[&lt;strong&gt;EngUnmapFontFileFD&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-engunmapfontfilefd)"><strong>EngUnmapFontFileFD</strong></a></p></td>
<td align="left"><p>Unmaps the specified font file from system memory.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-engwriteprinter" data-raw-source="[&lt;strong&gt;EngWritePrinter&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-engwriteprinter)"><strong>EngWritePrinter</strong></a></p></td>
<td align="left"><p>Allows printer graphics DLLs to send a data stream to printer hardware.</p></td>
</tr>
</tbody>
</table>

 

