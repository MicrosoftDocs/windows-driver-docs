---
title: IPrintOemUni COM Interface
description: IPrintOemUni COM Interface
keywords:
- IPrintOemUni
ms.date: 04/20/2017
---

# IPrintOemUni COM Interface





The `IPrintOemUni` COM interface is the means by which the [printer graphics DLL](printer-graphics-dll.md) for Unidrv communicates with a rendering plug-in. The `IPrintOemUni` interface is implemented by each rendering plug-in.

The following table lists and describes all of the methods provided by the `IPrintOemUni` interface. Rendering plug-ins must define all listed methods. If a method is not needed, it can simply return E\_NOTIMPL.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Method</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemuni-commandcallback" data-raw-source="[&lt;strong&gt;IPrintOemUni::CommandCallback&lt;/strong&gt;](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemuni-commandcallback)"><strong>IPrintOemUni::CommandCallback</strong></a></p></td>
<td><p>Allows a rendering plug-in to provide dynamically generated printer commands.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemuni-compression" data-raw-source="[&lt;strong&gt;IPrintOemUni::Compression&lt;/strong&gt;](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemuni-compression)"><strong>IPrintOemUni::Compression</strong></a></p></td>
<td><p>Allows a rendering plug-in to provide a customized bitmap compression method.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemuni-devmode" data-raw-source="[&lt;strong&gt;IPrintOemUni::DevMode&lt;/strong&gt;](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemuni-devmode)"><strong>IPrintOemUni::DevMode</strong></a></p></td>
<td><p>Performs operations on a rendering plug-in's private DEVMODE members.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemuni-disabledriver" data-raw-source="[&lt;strong&gt;IPrintOemUni::DisableDriver&lt;/strong&gt;](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemuni-disabledriver)"><strong>IPrintOemUni::DisableDriver</strong></a></p></td>
<td><p>Frees resources that were allocated by a rendering plug-in's <strong>IPrintOemUni::EnableDriver</strong> method.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemuni-disablepdev" data-raw-source="[&lt;strong&gt;IPrintOemUni::DisablePDEV&lt;/strong&gt;](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemuni-disablepdev)"><strong>IPrintOemUni::DisablePDEV</strong></a></p></td>
<td><p>Allows a rendering plug-in to delete the private PDEV structure that was allocated by its <a href="/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemuni-enablepdev" data-raw-source="[&lt;strong&gt;IPrintOemUni::EnablePDEV&lt;/strong&gt;](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemuni-enablepdev)"><strong>IPrintOemUni::EnablePDEV</strong></a> method.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemuni-downloadcharglyph" data-raw-source="[&lt;strong&gt;IPrintOemUni::DownloadCharGlyph&lt;/strong&gt;](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemuni-downloadcharglyph)"><strong>IPrintOemUni::DownloadCharGlyph</strong></a></p></td>
<td><p>Allows a rendering plug-in to download a character glyph for a specified soft font to the printer.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemuni-downloadfontheader" data-raw-source="[&lt;strong&gt;IPrintOemUni::DownloadFontHeader&lt;/strong&gt;](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemuni-downloadfontheader)"><strong>IPrintOemUni::DownloadFontHeader</strong></a></p></td>
<td><p>Allows a rendering plug-in to download a font's header information to a printer.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemuni-driverdms" data-raw-source="[&lt;strong&gt;IPrintOemUni::DriverDMS&lt;/strong&gt;](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemuni-driverdms)"><strong>IPrintOemUni::DriverDMS</strong></a></p></td>
<td><p>Allows a rendering plug-in to indicate that it will use a device-managed drawing surface.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemuni-enabledriver" data-raw-source="[&lt;strong&gt;IPrintOemUni::EnableDriver&lt;/strong&gt;](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemuni-enabledriver)"><strong>IPrintOemUni::EnableDriver</strong></a></p></td>
<td><p>Allows a rendering plug-in to hook out some graphics DDI functions. Note that this method and <strong>IPrintOemUni::DisableDriver</strong> must be considered as a pair; if one is implemented, the other must be implemented as well.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemuni-enablepdev" data-raw-source="[&lt;strong&gt;IPrintOemUni::EnablePDEV&lt;/strong&gt;](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemuni-enablepdev)"><strong>IPrintOemUni::EnablePDEV</strong></a></p></td>
<td><p>Allows a rendering plug-in to create its own PDEV structure.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemuni-filtergraphics" data-raw-source="[&lt;strong&gt;IPrintOemUni::FilterGraphics&lt;/strong&gt;](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemuni-filtergraphics)"><strong>IPrintOemUni::FilterGraphics</strong></a></p></td>
<td><p>Allows a rendering plug-in to modify scan line data and send it to the spooler.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemuni-getimplementedmethod" data-raw-source="[&lt;strong&gt;IPrintOemUni::GetImplementedMethod&lt;/strong&gt;](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemuni-getimplementedmethod)"><strong>IPrintOemUni::GetImplementedMethod</strong></a></p></td>
<td><p>(Implementation required.) Allows Unidrv to determine which <code>IPrintOemUni</code> interface methods have been implemented by a rendering plug-in.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemuni-getinfo" data-raw-source="[&lt;strong&gt;IPrintOemUni::GetInfo&lt;/strong&gt;](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemuni-getinfo)"><strong>IPrintOemUni::GetInfo</strong></a></p></td>
<td><p>(Implementation required.) Returns a rendering plug-in's identification information.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemuni-halftonepattern" data-raw-source="[&lt;strong&gt;IPrintOemUni::HalftonePattern&lt;/strong&gt;](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemuni-halftonepattern)"><strong>IPrintOemUni::HalftonePattern</strong></a></p></td>
<td><p>Allows a rendering plug-in to create or modify a halftone pattern before it is used in a halftoning operation.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemuni-imageprocessing" data-raw-source="[&lt;strong&gt;IPrintOemUni::ImageProcessing&lt;/strong&gt;](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemuni-imageprocessing)"><strong>IPrintOemUni::ImageProcessing</strong></a></p></td>
<td><p>Allows a rendering plug-in to modify image bitmap data, in order to perform color formatting or halftoning.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemuni-memoryusage" data-raw-source="[&lt;strong&gt;IPrintOemUni::MemoryUsage&lt;/strong&gt;](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemuni-memoryusage)"><strong>IPrintOemUni::MemoryUsage</strong></a></p></td>
<td><p>Allows a rendering plug-in to specify the amount of memory required for use by its <a href="/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemuni-imageprocessing" data-raw-source="[&lt;strong&gt;IPrintOemUni::ImageProcessing&lt;/strong&gt;](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemuni-imageprocessing)"><strong>IPrintOemUni::ImageProcessing</strong></a> method.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemuni-outputcharstr" data-raw-source="[&lt;strong&gt;IPrintOemUni::OutputCharStr&lt;/strong&gt;](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemuni-outputcharstr)"><strong>IPrintOemUni::OutputCharStr</strong></a></p></td>
<td><p>Allows a rendering plug-in to control the printing of font glyphs.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemuni-publishdriverinterface" data-raw-source="[&lt;strong&gt;IPrintOemUni::PublishDriverInterface&lt;/strong&gt;](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemuni-publishdriverinterface)"><strong>IPrintOemUni::PublishDriverInterface</strong></a></p></td>
<td><p>(Implementation required.) Supplies a pointer to the Unidrv driver's <a href="iprintoemdriveruni-com-interface.md" data-raw-source="[IPrintOemDriverUni COM interface](iprintoemdriveruni-com-interface.md)">IPrintOemDriverUni COM interface</a> or <a href="/windows-hardware/drivers/ddi/prcomoem/nn-prcomoem-iprintcorehelperuni" data-raw-source="[IPrintCoreHelperUni interface](/windows-hardware/drivers/ddi/prcomoem/nn-prcomoem-iprintcorehelperuni)">IPrintCoreHelperUni interface</a>.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemuni-resetpdev" data-raw-source="[&lt;strong&gt;IPrintOemUni::ResetPDEV&lt;/strong&gt;](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemuni-resetpdev)"><strong>IPrintOemUni::ResetPDEV</strong></a></p></td>
<td><p>Allows a rendering plug-in to reset its PDEV structure.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemuni-sendfontcmd" data-raw-source="[&lt;strong&gt;IPrintOemUni::SendFontCmd&lt;/strong&gt;](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemuni-sendfontcmd)"><strong>IPrintOemUni::SendFontCmd</strong></a></p></td>
<td><p>Allows a rendering plug-in to modify a printer's font selection command and then send it to the printer.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemuni-textoutasbitmap" data-raw-source="[&lt;strong&gt;IPrintOemUni::TextOutAsBitmap&lt;/strong&gt;](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemuni-textoutasbitmap)"><strong>IPrintOemUni::TextOutAsBitmap</strong></a></p></td>
<td><p>Allows a rendering plug-in to create a bitmap image of a text string.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemuni-ttdownloadmethod" data-raw-source="[&lt;strong&gt;IPrintOemUni::TTDownloadMethod&lt;/strong&gt;](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemuni-ttdownloadmethod)"><strong>IPrintOemUni::TTDownloadMethod</strong></a></p></td>
<td><p>Allows a rendering plug-in to indicate the format that Unidrv should use for a specified TrueType font.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemuni-ttygetinfo" data-raw-source="[&lt;strong&gt;IPrintOemUni::TTYGetInfo&lt;/strong&gt;](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemuni-ttygetinfo)"><strong>IPrintOemUni::TTYGetInfo</strong></a></p></td>
<td><p>Allows a rendering plug-in to supply Unidrv with information relevant to text-only printers.</p></td>
</tr>
</tbody>
</table>

 

For more information, see [Implementing Printer Driver COM Interfaces](implementing-printer-driver-com-interfaces.md).

