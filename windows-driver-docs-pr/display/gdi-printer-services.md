---
title: GDI Printer Services
description: GDI Printer Services
ms.assetid: b63c9822-f737-42fb-a831-31d16b3495c9
keywords:
- GDI WDK Windows 2000 display , printer services
- graphics drivers WDK Windows 2000 display , printer services
- drawing WDK GDI , printer services
- printer services WDK GDI
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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
<td align="left"><p>[<strong>EngEnumForms</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564850)</p></td>
<td align="left"><p>Enumerates the forms supported by the specified printer.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>EngGetForm</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564938)</p></td>
<td align="left"><p>Gets the FORM_INFO_1 details for the specified form.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>EngGetPrinter</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564945)</p></td>
<td align="left"><p>Retrieves information about the specified printer.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>EngGetPrinterData</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564948)</p></td>
<td align="left"><p>Retrieves configuration data for the specified printer.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>EngGetPrinterDataFileName</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564951)</p></td>
<td align="left"><p>Retrieves the string name of the printer's data file.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>EngGetPrinterDriver</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564954)</p></td>
<td align="left"><p>Retrieves driver data for the specified printer.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>EngMapFontFile</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564972)</p></td>
<td align="left"><p>Obsolete. See the entry in this table for <strong>EngMapFontFileFD</strong>.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>EngMapFontFileFD</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564973)</p></td>
<td align="left"><p>Maps a font file into system memory, if necessary, and returns a pointer to the base location of the font data in the file.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>EngMarkBandingSurface</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564975)</p></td>
<td align="left"><p>Marks the specified printer surface as a banding surface.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>EngSetPrinterData</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565020)</p></td>
<td align="left"><p>Obsolete. Sets the configuration data for the specified printer.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>EngUnmapFontFile</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565441)</p></td>
<td align="left"><p>Obsolete. See the entry in this table for <strong>EngUnmapFontFileFD</strong>.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>EngUnmapFontFileFD</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565445)</p></td>
<td align="left"><p>Unmaps the specified font file from system memory.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>EngWritePrinter</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565467)</p></td>
<td align="left"><p>Allows printer graphics DLLs to send a data stream to printer hardware.</p></td>
</tr>
</tbody>
</table>

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20GDI%20Printer%20Services%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




