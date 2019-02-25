---
title: IPrintOemPS COM Interface
description: IPrintOemPS COM Interface
ms.assetid: 504db6ab-291e-4fba-995d-49a22a3a7c7f
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
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff553199" data-raw-source="[&lt;strong&gt;IPrintOemPS::Command&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff553199)"><strong>IPrintOemPS::Command</strong></a></p></td>
<td><p>Allows a rendering plug-in to insert Postscript commands into the print job&#39;s data stream.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff553205" data-raw-source="[&lt;strong&gt;IPrintOemPS::DevMode&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff553205)"><strong>IPrintOemPS::DevMode</strong></a></p></td>
<td><p>Performs operations on a rendering plug-in&#39;s private <a href="https://msdn.microsoft.com/library/windows/hardware/ff552837" data-raw-source="[&lt;strong&gt;DEVMODEW&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff552837)"><strong>DEVMODEW</strong></a> members.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff553207" data-raw-source="[&lt;strong&gt;IPrintOemPS::DisableDriver&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff553207)"><strong>IPrintOemPS::DisableDriver</strong></a></p></td>
<td><p>Frees resources that were allocated by a rendering plug-in&#39;s <a href="https://msdn.microsoft.com/library/windows/hardware/ff553212" data-raw-source="[&lt;strong&gt;IPrintOemPS::EnableDriver&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff553212)"><strong>IPrintOemPS::EnableDriver</strong></a> method.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff553209" data-raw-source="[&lt;strong&gt;IPrintOemPS::DisablePDEV&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff553209)"><strong>IPrintOemPS::DisablePDEV</strong></a></p></td>
<td><p>Allows a rendering plug-in to delete the private PDEV structure that was allocated by its <a href="https://msdn.microsoft.com/library/windows/hardware/ff553215" data-raw-source="[&lt;strong&gt;IPrintOemPS::EnablePDEV&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff553215)"><strong>IPrintOemPS::EnablePDEV</strong></a> method.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff553212" data-raw-source="[&lt;strong&gt;IPrintOemPS::EnableDriver&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff553212)"><strong>IPrintOemPS::EnableDriver</strong></a></p></td>
<td><p>Allows a rendering plug-in to hook out some graphics DDI functions. Note that this method and <strong>IPrintOemPS::DisableDriver</strong> must be considered as a pair; if one is implemented, the other must be implemented as well.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff553215" data-raw-source="[&lt;strong&gt;IPrintOemPS::EnablePDEV&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff553215)"><strong>IPrintOemPS::EnablePDEV</strong></a></p></td>
<td><p>Allows a rendering plug-in to create its own PDEV structure.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff553221" data-raw-source="[&lt;strong&gt;IPrintOemPS::GetInfo&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff553221)"><strong>IPrintOemPS::GetInfo</strong></a></p></td>
<td><p>(Implementation required.) Returns rendering plug-in identification information.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff553228" data-raw-source="[&lt;strong&gt;IPrintOemPS::PublishDriverInterface&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff553228)"><strong>IPrintOemPS::PublishDriverInterface</strong></a></p></td>
<td><p>(Implementation required.) Supplies a pointer to the Pscript5 driver&#39;s <a href="iprintoemdriverps-com-interface.md" data-raw-source="[IPrintOemDriverPS COM interface](iprintoemdriverps-com-interface.md)">IPrintOemDriverPS COM interface</a>, <a href="iprintcoreps2-com-interface.md" data-raw-source="[IPrintCorePS2 COM interface](iprintcoreps2-com-interface.md)">IPrintCorePS2 COM interface</a>, or <a href="https://msdn.microsoft.com/library/windows/hardware/ff552906" data-raw-source="[IPrintCoreHelperPS interface](https://msdn.microsoft.com/library/windows/hardware/ff552906)">IPrintCoreHelperPS interface</a>.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff553233" data-raw-source="[&lt;strong&gt;IPrintOemPS::ResetPDEV&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff553233)"><strong>IPrintOemPS::ResetPDEV</strong></a></p></td>
<td><p>Allows a rendering plug-in to reset its PDEV structure.</p></td>
</tr>
</tbody>
</table>

 

For more information, see [Implementing Printer Driver COM Interfaces](implementing-printer-driver-com-interfaces.md).

 

 




