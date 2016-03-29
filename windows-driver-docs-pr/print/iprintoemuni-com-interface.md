---
title: IPrintOemUni COM Interface
description: IPrintOemUni COM Interface
ms.assetid: b120def0-f270-49c6-b12f-10c220801f51
keywords: ["IPrintOemUni"]
---

# IPrintOemUni COM Interface


## <a href="" id="ddk-iprintoemuni-com-interface-gg"></a>


The `IPrintOemUni` COM interface is the means by which the [printer graphics DLL](printer-graphics-dll.md) for Unidrv communicates with a rendering plug-in. The `IPrintOemUni` interface is implemented by each rendering plug-in.

The following table lists and describes all of the methods provided by the `IPrintOemUni` interface. Rendering plug-ins must define all listed methods. If a method is not needed, it can simply return E\_NOTIMPL.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Method</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>[<strong>IPrintOemUni::CommandCallback</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554216)</p></td>
<td align="left"><p>Allows a rendering plug-in to provide dynamically generated printer commands.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>IPrintOemUni::Compression</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554224)</p></td>
<td align="left"><p>Allows a rendering plug-in to provide a customized bitmap compression method.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>IPrintOemUni::DevMode</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554230)</p></td>
<td align="left"><p>Performs operations on a rendering plug-in's private DEVMODE members.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>IPrintOemUni::DisableDriver</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554232)</p></td>
<td align="left"><p>Frees resources that were allocated by a rendering plug-in's <strong>IPrintOemUni::EnableDriver</strong> method.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>IPrintOemUni::DisablePDEV</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554238)</p></td>
<td align="left"><p>Allows a rendering plug-in to delete the private PDEV structure that was allocated by its [<strong>IPrintOemUni::EnablePDEV</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554249) method.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>IPrintOemUni::DownloadCharGlyph</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554241)</p></td>
<td align="left"><p>Allows a rendering plug-in to download a character glyph for a specified soft font to the printer.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>IPrintOemUni::DownloadFontHeader</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554242)</p></td>
<td align="left"><p>Allows a rendering plug-in to download a font's header information to a printer.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>IPrintOemUni::DriverDMS</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554245)</p></td>
<td align="left"><p>Allows a rendering plug-in to indicate that it will use a device-managed drawing surface.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>IPrintOemUni::EnableDriver</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554248)</p></td>
<td align="left"><p>Allows a rendering plug-in to hook out some graphics DDI functions. Note that this method and <strong>IPrintOemUni::DisableDriver</strong> must be considered as a pair; if one is implemented, the other must be implemented as well.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>IPrintOemUni::EnablePDEV</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554249)</p></td>
<td align="left"><p>Allows a rendering plug-in to create its own PDEV structure.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>IPrintOemUni::FilterGraphics</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554252)</p></td>
<td align="left"><p>Allows a rendering plug-in to modify scan line data and send it to the spooler.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>IPrintOemUni::GetImplementedMethod</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554253)</p></td>
<td align="left"><p>(Implementation required.) Allows Unidrv to determine which <code>IPrintOemUni</code> interface methods have been implemented by a rendering plug-in.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>IPrintOemUni::GetInfo</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554256)</p></td>
<td align="left"><p>(Implementation required.) Returns a rendering plug-in's identification information.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>IPrintOemUni::HalftonePattern</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554258)</p></td>
<td align="left"><p>Allows a rendering plug-in to create or modify a halftone pattern before it is used in a halftoning operation.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>IPrintOemUni::ImageProcessing</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554261)</p></td>
<td align="left"><p>Allows a rendering plug-in to modify image bitmap data, in order to perform color formatting or halftoning.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>IPrintOemUni::MemoryUsage</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554264)</p></td>
<td align="left"><p>Allows a rendering plug-in to specify the amount of memory required for use by its [<strong>IPrintOemUni::ImageProcessing</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554261) method.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>IPrintOemUni::OutputCharStr</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554267)</p></td>
<td align="left"><p>Allows a rendering plug-in to control the printing of font glyphs.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>IPrintOemUni::PublishDriverInterface</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554269)</p></td>
<td align="left"><p>(Implementation required.) Supplies a pointer to the Unidrv driver's [IPrintOemDriverUni COM interface](iprintoemdriveruni-com-interface.md) or [IPrintCoreHelperUni interface](https://msdn.microsoft.com/library/windows/hardware/ff552940).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>IPrintOemUni::ResetPDEV</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554270)</p></td>
<td align="left"><p>Allows a rendering plug-in to reset its PDEV structure.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>IPrintOemUni::SendFontCmd</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554274)</p></td>
<td align="left"><p>Allows a rendering plug-in to modify a printer's font selection command and then send it to the printer.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>IPrintOemUni::TextOutAsBitmap</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554277)</p></td>
<td align="left"><p>Allows a rendering plug-in to create a bitmap image of a text string.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>IPrintOemUni::TTDownloadMethod</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554279)</p></td>
<td align="left"><p>Allows a rendering plug-in to indicate the format that Unidrv should use for a specified TrueType font.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>IPrintOemUni::TTYGetInfo</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554283)</p></td>
<td align="left"><p>Allows a rendering plug-in to supply Unidrv with information relevant to text-only printers.</p></td>
</tr>
</tbody>
</table>

 

For more information, see [Implementing Printer Driver COM Interfaces](implementing-printer-driver-com-interfaces.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintOemUni%20COM%20Interface%20%20RELEASE:%20%283/29/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




