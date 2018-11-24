---
title: IPrintOemUni COM Interface
description: IPrintOemUni COM Interface
ms.assetid: b120def0-f270-49c6-b12f-10c220801f51
keywords:
- IPrintOemUni
ms.date: 04/20/2017
ms.localizationpriority: medium
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
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554216" data-raw-source="[&lt;strong&gt;IPrintOemUni::CommandCallback&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554216)"><strong>IPrintOemUni::CommandCallback</strong></a></p></td>
<td><p>Allows a rendering plug-in to provide dynamically generated printer commands.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554224" data-raw-source="[&lt;strong&gt;IPrintOemUni::Compression&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554224)"><strong>IPrintOemUni::Compression</strong></a></p></td>
<td><p>Allows a rendering plug-in to provide a customized bitmap compression method.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554230" data-raw-source="[&lt;strong&gt;IPrintOemUni::DevMode&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554230)"><strong>IPrintOemUni::DevMode</strong></a></p></td>
<td><p>Performs operations on a rendering plug-in&#39;s private DEVMODE members.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554232" data-raw-source="[&lt;strong&gt;IPrintOemUni::DisableDriver&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554232)"><strong>IPrintOemUni::DisableDriver</strong></a></p></td>
<td><p>Frees resources that were allocated by a rendering plug-in&#39;s <strong>IPrintOemUni::EnableDriver</strong> method.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554238" data-raw-source="[&lt;strong&gt;IPrintOemUni::DisablePDEV&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554238)"><strong>IPrintOemUni::DisablePDEV</strong></a></p></td>
<td><p>Allows a rendering plug-in to delete the private PDEV structure that was allocated by its <a href="https://msdn.microsoft.com/library/windows/hardware/ff554249" data-raw-source="[&lt;strong&gt;IPrintOemUni::EnablePDEV&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554249)"><strong>IPrintOemUni::EnablePDEV</strong></a> method.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554241" data-raw-source="[&lt;strong&gt;IPrintOemUni::DownloadCharGlyph&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554241)"><strong>IPrintOemUni::DownloadCharGlyph</strong></a></p></td>
<td><p>Allows a rendering plug-in to download a character glyph for a specified soft font to the printer.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554242" data-raw-source="[&lt;strong&gt;IPrintOemUni::DownloadFontHeader&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554242)"><strong>IPrintOemUni::DownloadFontHeader</strong></a></p></td>
<td><p>Allows a rendering plug-in to download a font&#39;s header information to a printer.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554245" data-raw-source="[&lt;strong&gt;IPrintOemUni::DriverDMS&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554245)"><strong>IPrintOemUni::DriverDMS</strong></a></p></td>
<td><p>Allows a rendering plug-in to indicate that it will use a device-managed drawing surface.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554248" data-raw-source="[&lt;strong&gt;IPrintOemUni::EnableDriver&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554248)"><strong>IPrintOemUni::EnableDriver</strong></a></p></td>
<td><p>Allows a rendering plug-in to hook out some graphics DDI functions. Note that this method and <strong>IPrintOemUni::DisableDriver</strong> must be considered as a pair; if one is implemented, the other must be implemented as well.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554249" data-raw-source="[&lt;strong&gt;IPrintOemUni::EnablePDEV&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554249)"><strong>IPrintOemUni::EnablePDEV</strong></a></p></td>
<td><p>Allows a rendering plug-in to create its own PDEV structure.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554252" data-raw-source="[&lt;strong&gt;IPrintOemUni::FilterGraphics&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554252)"><strong>IPrintOemUni::FilterGraphics</strong></a></p></td>
<td><p>Allows a rendering plug-in to modify scan line data and send it to the spooler.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554253" data-raw-source="[&lt;strong&gt;IPrintOemUni::GetImplementedMethod&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554253)"><strong>IPrintOemUni::GetImplementedMethod</strong></a></p></td>
<td><p>(Implementation required.) Allows Unidrv to determine which <code>IPrintOemUni</code> interface methods have been implemented by a rendering plug-in.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554256" data-raw-source="[&lt;strong&gt;IPrintOemUni::GetInfo&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554256)"><strong>IPrintOemUni::GetInfo</strong></a></p></td>
<td><p>(Implementation required.) Returns a rendering plug-in&#39;s identification information.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554258" data-raw-source="[&lt;strong&gt;IPrintOemUni::HalftonePattern&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554258)"><strong>IPrintOemUni::HalftonePattern</strong></a></p></td>
<td><p>Allows a rendering plug-in to create or modify a halftone pattern before it is used in a halftoning operation.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554261" data-raw-source="[&lt;strong&gt;IPrintOemUni::ImageProcessing&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554261)"><strong>IPrintOemUni::ImageProcessing</strong></a></p></td>
<td><p>Allows a rendering plug-in to modify image bitmap data, in order to perform color formatting or halftoning.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554264" data-raw-source="[&lt;strong&gt;IPrintOemUni::MemoryUsage&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554264)"><strong>IPrintOemUni::MemoryUsage</strong></a></p></td>
<td><p>Allows a rendering plug-in to specify the amount of memory required for use by its <a href="https://msdn.microsoft.com/library/windows/hardware/ff554261" data-raw-source="[&lt;strong&gt;IPrintOemUni::ImageProcessing&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554261)"><strong>IPrintOemUni::ImageProcessing</strong></a> method.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554267" data-raw-source="[&lt;strong&gt;IPrintOemUni::OutputCharStr&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554267)"><strong>IPrintOemUni::OutputCharStr</strong></a></p></td>
<td><p>Allows a rendering plug-in to control the printing of font glyphs.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554269" data-raw-source="[&lt;strong&gt;IPrintOemUni::PublishDriverInterface&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554269)"><strong>IPrintOemUni::PublishDriverInterface</strong></a></p></td>
<td><p>(Implementation required.) Supplies a pointer to the Unidrv driver&#39;s <a href="iprintoemdriveruni-com-interface.md" data-raw-source="[IPrintOemDriverUni COM interface](iprintoemdriveruni-com-interface.md)">IPrintOemDriverUni COM interface</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff552940" data-raw-source="[IPrintCoreHelperUni interface](https://msdn.microsoft.com/library/windows/hardware/ff552940)">IPrintCoreHelperUni interface</a>.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554270" data-raw-source="[&lt;strong&gt;IPrintOemUni::ResetPDEV&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554270)"><strong>IPrintOemUni::ResetPDEV</strong></a></p></td>
<td><p>Allows a rendering plug-in to reset its PDEV structure.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554274" data-raw-source="[&lt;strong&gt;IPrintOemUni::SendFontCmd&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554274)"><strong>IPrintOemUni::SendFontCmd</strong></a></p></td>
<td><p>Allows a rendering plug-in to modify a printer&#39;s font selection command and then send it to the printer.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554277" data-raw-source="[&lt;strong&gt;IPrintOemUni::TextOutAsBitmap&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554277)"><strong>IPrintOemUni::TextOutAsBitmap</strong></a></p></td>
<td><p>Allows a rendering plug-in to create a bitmap image of a text string.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554279" data-raw-source="[&lt;strong&gt;IPrintOemUni::TTDownloadMethod&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554279)"><strong>IPrintOemUni::TTDownloadMethod</strong></a></p></td>
<td><p>Allows a rendering plug-in to indicate the format that Unidrv should use for a specified TrueType font.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554283" data-raw-source="[&lt;strong&gt;IPrintOemUni::TTYGetInfo&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554283)"><strong>IPrintOemUni::TTYGetInfo</strong></a></p></td>
<td><p>Allows a rendering plug-in to supply Unidrv with information relevant to text-only printers.</p></td>
</tr>
</tbody>
</table>

 

For more information, see [Implementing Printer Driver COM Interfaces](implementing-printer-driver-com-interfaces.md).

 

 




