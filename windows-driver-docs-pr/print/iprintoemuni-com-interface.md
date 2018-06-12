---
title: IPrintOemUni COM Interface
author: windows-driver-content
description: IPrintOemUni COM Interface
ms.assetid: b120def0-f270-49c6-b12f-10c220801f51
keywords:
- IPrintOemUni
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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
<td><p>[<strong>IPrintOemUni::CommandCallback</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554216)</p></td>
<td><p>Allows a rendering plug-in to provide dynamically generated printer commands.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>IPrintOemUni::Compression</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554224)</p></td>
<td><p>Allows a rendering plug-in to provide a customized bitmap compression method.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>IPrintOemUni::DevMode</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554230)</p></td>
<td><p>Performs operations on a rendering plug-in's private DEVMODE members.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>IPrintOemUni::DisableDriver</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554232)</p></td>
<td><p>Frees resources that were allocated by a rendering plug-in's <strong>IPrintOemUni::EnableDriver</strong> method.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>IPrintOemUni::DisablePDEV</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554238)</p></td>
<td><p>Allows a rendering plug-in to delete the private PDEV structure that was allocated by its [<strong>IPrintOemUni::EnablePDEV</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554249) method.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>IPrintOemUni::DownloadCharGlyph</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554241)</p></td>
<td><p>Allows a rendering plug-in to download a character glyph for a specified soft font to the printer.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>IPrintOemUni::DownloadFontHeader</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554242)</p></td>
<td><p>Allows a rendering plug-in to download a font's header information to a printer.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>IPrintOemUni::DriverDMS</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554245)</p></td>
<td><p>Allows a rendering plug-in to indicate that it will use a device-managed drawing surface.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>IPrintOemUni::EnableDriver</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554248)</p></td>
<td><p>Allows a rendering plug-in to hook out some graphics DDI functions. Note that this method and <strong>IPrintOemUni::DisableDriver</strong> must be considered as a pair; if one is implemented, the other must be implemented as well.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>IPrintOemUni::EnablePDEV</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554249)</p></td>
<td><p>Allows a rendering plug-in to create its own PDEV structure.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>IPrintOemUni::FilterGraphics</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554252)</p></td>
<td><p>Allows a rendering plug-in to modify scan line data and send it to the spooler.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>IPrintOemUni::GetImplementedMethod</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554253)</p></td>
<td><p>(Implementation required.) Allows Unidrv to determine which <code>IPrintOemUni</code> interface methods have been implemented by a rendering plug-in.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>IPrintOemUni::GetInfo</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554256)</p></td>
<td><p>(Implementation required.) Returns a rendering plug-in's identification information.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>IPrintOemUni::HalftonePattern</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554258)</p></td>
<td><p>Allows a rendering plug-in to create or modify a halftone pattern before it is used in a halftoning operation.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>IPrintOemUni::ImageProcessing</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554261)</p></td>
<td><p>Allows a rendering plug-in to modify image bitmap data, in order to perform color formatting or halftoning.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>IPrintOemUni::MemoryUsage</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554264)</p></td>
<td><p>Allows a rendering plug-in to specify the amount of memory required for use by its [<strong>IPrintOemUni::ImageProcessing</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554261) method.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>IPrintOemUni::OutputCharStr</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554267)</p></td>
<td><p>Allows a rendering plug-in to control the printing of font glyphs.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>IPrintOemUni::PublishDriverInterface</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554269)</p></td>
<td><p>(Implementation required.) Supplies a pointer to the Unidrv driver's [IPrintOemDriverUni COM interface](iprintoemdriveruni-com-interface.md) or [IPrintCoreHelperUni interface](https://msdn.microsoft.com/library/windows/hardware/ff552940).</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>IPrintOemUni::ResetPDEV</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554270)</p></td>
<td><p>Allows a rendering plug-in to reset its PDEV structure.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>IPrintOemUni::SendFontCmd</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554274)</p></td>
<td><p>Allows a rendering plug-in to modify a printer's font selection command and then send it to the printer.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>IPrintOemUni::TextOutAsBitmap</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554277)</p></td>
<td><p>Allows a rendering plug-in to create a bitmap image of a text string.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>IPrintOemUni::TTDownloadMethod</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554279)</p></td>
<td><p>Allows a rendering plug-in to indicate the format that Unidrv should use for a specified TrueType font.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>IPrintOemUni::TTYGetInfo</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554283)</p></td>
<td><p>Allows a rendering plug-in to supply Unidrv with information relevant to text-only printers.</p></td>
</tr>
</tbody>
</table>

 

For more information, see [Implementing Printer Driver COM Interfaces](implementing-printer-driver-com-interfaces.md).

 

 




