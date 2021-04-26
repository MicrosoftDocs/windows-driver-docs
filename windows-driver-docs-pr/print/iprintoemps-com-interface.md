---
title: IPrintOemPS COM Interface
description: IPrintOemPS COM Interface
keywords:
- IPrintOemPS
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# IPrintOemPS COM Interface





The `IPrintOemPS` COM interface is the means by which the [printer graphics DLL](printer-graphics-dll.md) for Pscript5 communicates with a rendering plug-in. The `IPrintOemPS` interface is implemented by each rendering plug-in.

The following table lists and describes all of the methods provided by the `IPrintOemPS` interface. Rendering plug-ins must define all the listed methods. If a method is not needed, it can simply return E\_NOTIMPL.

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
<td><p><a href="/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemps-command" data-raw-source="[&lt;strong&gt;IPrintOemPS::Command&lt;/strong&gt;](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemps-command)"><strong>IPrintOemPS::Command</strong></a></p></td>
<td><p>Allows a rendering plug-in to insert Postscript commands into the print job's data stream.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemps-devmode" data-raw-source="[&lt;strong&gt;IPrintOemPS::DevMode&lt;/strong&gt;](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemps-devmode)"><strong>IPrintOemPS::DevMode</strong></a></p></td>
<td><p>Performs operations on a rendering plug-in's private <a href="/windows/win32/api/wingdi/ns-wingdi-devmodew" data-raw-source="[&lt;strong&gt;DEVMODEW&lt;/strong&gt;](/windows/win32/api/wingdi/ns-wingdi-devmodew)"><strong>DEVMODEW</strong></a> members.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemps-disabledriver" data-raw-source="[&lt;strong&gt;IPrintOemPS::DisableDriver&lt;/strong&gt;](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemps-disabledriver)"><strong>IPrintOemPS::DisableDriver</strong></a></p></td>
<td><p>Frees resources that were allocated by a rendering plug-in's <a href="/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemps-enabledriver" data-raw-source="[&lt;strong&gt;IPrintOemPS::EnableDriver&lt;/strong&gt;](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemps-enabledriver)"><strong>IPrintOemPS::EnableDriver</strong></a> method.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemps-disablepdev" data-raw-source="[&lt;strong&gt;IPrintOemPS::DisablePDEV&lt;/strong&gt;](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemps-disablepdev)"><strong>IPrintOemPS::DisablePDEV</strong></a></p></td>
<td><p>Allows a rendering plug-in to delete the private PDEV structure that was allocated by its <a href="/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemps-enablepdev" data-raw-source="[&lt;strong&gt;IPrintOemPS::EnablePDEV&lt;/strong&gt;](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemps-enablepdev)"><strong>IPrintOemPS::EnablePDEV</strong></a> method.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemps-enabledriver" data-raw-source="[&lt;strong&gt;IPrintOemPS::EnableDriver&lt;/strong&gt;](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemps-enabledriver)"><strong>IPrintOemPS::EnableDriver</strong></a></p></td>
<td><p>Allows a rendering plug-in to hook out some graphics DDI functions. Note that this method and <strong>IPrintOemPS::DisableDriver</strong> must be considered as a pair; if one is implemented, the other must be implemented as well.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemps-enablepdev" data-raw-source="[&lt;strong&gt;IPrintOemPS::EnablePDEV&lt;/strong&gt;](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemps-enablepdev)"><strong>IPrintOemPS::EnablePDEV</strong></a></p></td>
<td><p>Allows a rendering plug-in to create its own PDEV structure.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemps-getinfo" data-raw-source="[&lt;strong&gt;IPrintOemPS::GetInfo&lt;/strong&gt;](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemps-getinfo)"><strong>IPrintOemPS::GetInfo</strong></a></p></td>
<td><p>(Implementation required.) Returns rendering plug-in identification information.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemps-publishdriverinterface" data-raw-source="[&lt;strong&gt;IPrintOemPS::PublishDriverInterface&lt;/strong&gt;](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemps-publishdriverinterface)"><strong>IPrintOemPS::PublishDriverInterface</strong></a></p></td>
<td><p>(Implementation required.) Supplies a pointer to the Pscript5 driver's <a href="iprintoemdriverps-com-interface.md" data-raw-source="[IPrintOemDriverPS COM interface](iprintoemdriverps-com-interface.md)">IPrintOemDriverPS COM interface</a>, <a href="iprintcoreps2-com-interface.md" data-raw-source="[IPrintCorePS2 COM interface](iprintcoreps2-com-interface.md)">IPrintCorePS2 COM interface</a>, or <a href="/windows-hardware/drivers/ddi/prcomoem/nn-prcomoem-iprintcorehelperps" data-raw-source="[IPrintCoreHelperPS interface](/windows-hardware/drivers/ddi/prcomoem/nn-prcomoem-iprintcorehelperps)">IPrintCoreHelperPS interface</a>.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemps-resetpdev" data-raw-source="[&lt;strong&gt;IPrintOemPS::ResetPDEV&lt;/strong&gt;](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemps-resetpdev)"><strong>IPrintOemPS::ResetPDEV</strong></a></p></td>
<td><p>Allows a rendering plug-in to reset its PDEV structure.</p></td>
</tr>
</tbody>
</table>

 

For more information, see [Implementing Printer Driver COM Interfaces](implementing-printer-driver-com-interfaces.md).

