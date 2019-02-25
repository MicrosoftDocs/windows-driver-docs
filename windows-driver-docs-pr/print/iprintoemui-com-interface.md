---
title: IPrintOemUI COM Interface
description: IPrintOemUI COM Interface
ms.assetid: 7fd4071a-11ce-49e6-9e23-4f0643da1d98
keywords:
- IPrintOemUI
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# IPrintOemUI COM Interface





The `IPrintOemUI` COM interface is the means by which the [printer interface DLL](printer-interface-dll.md) for Unidrv or Pscript5 communicates with a UI plug-in. The `IPrintOemUI` interface is implemented by each UI plug-in.

The following table lists and describes all the methods that the `IPrintOemUI` interface supplies. UI plug-ins must define all listed methods. If a method is not needed, it can simply return E\_NOTIMPL.

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
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554159" data-raw-source="[&lt;strong&gt;IPrintOemUI::CommonUIProp&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554159)"><strong>IPrintOemUI::CommonUIProp</strong></a></p></td>
<td><p>Enables a UI plug-in to modify an existing printer property sheet page or document property sheet page.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554162" data-raw-source="[&lt;strong&gt;IPrintOemUI::DeviceCapabilities&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554162)"><strong>IPrintOemUI::DeviceCapabilities</strong></a></p></td>
<td><p>Enables a UI plug-in to specify customized device capabilities.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554165" data-raw-source="[&lt;strong&gt;IPrintOemUI::DevicePropertySheets&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554165)"><strong>IPrintOemUI::DevicePropertySheets</strong></a></p></td>
<td><p>Enables a UI plug-in to add a new page to a printer device&#39;s printer property sheet.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554167" data-raw-source="[&lt;strong&gt;IPrintOemUI::DevMode&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554167)"><strong>IPrintOemUI::DevMode</strong></a></p></td>
<td><p>Performs operations on a UI plug-in&#39;s private <a href="https://msdn.microsoft.com/library/windows/hardware/ff552837" data-raw-source="[&lt;strong&gt;DEVMODEW&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff552837)"><strong>DEVMODEW</strong></a> members.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554172" data-raw-source="[&lt;strong&gt;IPrintOemUI::DevQueryPrintEx&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554172)"><strong>IPrintOemUI::DevQueryPrintEx</strong></a></p></td>
<td><p>Enables a UI plug-in to help determine if a print job is printable.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554173" data-raw-source="[&lt;strong&gt;IPrintOemUI::DocumentPropertySheets&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554173)"><strong>IPrintOemUI::DocumentPropertySheets</strong></a></p></td>
<td><p>Enables a UI plug-in to add a new page to a printer device&#39;s document property sheet.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554175" data-raw-source="[&lt;strong&gt;IPrintOemUI::DriverEvent&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554175)"><strong>IPrintOemUI::DriverEvent</strong></a></p></td>
<td><p>Called by the print spooler when processing driver-specific events that might require action by the printer driver.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554176" data-raw-source="[&lt;strong&gt;IPrintOemUI::FontInstallerDlgProc&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554176)"><strong>IPrintOemUI::FontInstallerDlgProc</strong></a></p></td>
<td><p>Replaces the Unidrv font installer&#39;s user interface.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554178" data-raw-source="[&lt;strong&gt;IPrintOemUI::GetInfo&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554178)"><strong>IPrintOemUI::GetInfo</strong></a></p></td>
<td><p>(Implementation required.) Returns a UI plug-in&#39;s identification information.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554182" data-raw-source="[&lt;strong&gt;IPrintOemUI::PrinterEvent&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554182)"><strong>IPrintOemUI::PrinterEvent</strong></a></p></td>
<td><p>Enables a UI plug-in to process printer events.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554184" data-raw-source="[&lt;strong&gt;IPrintOemUI::PublishDriverInterface&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554184)"><strong>IPrintOemUI::PublishDriverInterface</strong></a></p></td>
<td><p>(Implementation required.) Supplies a pointer to the Unidrv or Pscript5 driver&#39;s <a href="iprintoemdriverui-com-interface.md" data-raw-source="[IPrintOemDriverUI COM interface](iprintoemdriverui-com-interface.md)">IPrintOemDriverUI COM interface</a>, <a href="iprintcoreui2-com-interface.md" data-raw-source="[IPrintCoreUI2 COM interface](iprintcoreui2-com-interface.md)">IPrintCoreUI2 COM interface</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff552906" data-raw-source="[IPrintCoreHelperPS interface](https://msdn.microsoft.com/library/windows/hardware/ff552906)">IPrintCoreHelperPS interface</a>, or <a href="https://msdn.microsoft.com/library/windows/hardware/ff552940" data-raw-source="[IPrintCoreHelperUni interface](https://msdn.microsoft.com/library/windows/hardware/ff552940)">IPrintCoreHelperUni interface</a>.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554186" data-raw-source="[&lt;strong&gt;IPrintOemUI::QueryColorProfile&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554186)"><strong>IPrintOemUI::QueryColorProfile</strong></a></p></td>
<td><p>Enables a printer interface DLL to specify an ICC profile for color management.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554188" data-raw-source="[&lt;strong&gt;IPrintOemUI::UpdateExternalFonts&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554188)"><strong>IPrintOemUI::UpdateExternalFonts</strong></a></p></td>
<td><p>Enables a printer interface DLL to update a printer&#39;s <a href="customized-font-management.md#ddk-unidrv-font-format-files-gg" data-raw-source="[Unidrv font format files](customized-font-management.md#ddk-unidrv-font-format-files-gg)">Unidrv font format files</a>.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554189" data-raw-source="[&lt;strong&gt;IPrintOemUI::UpgradePrinter&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554189)"><strong>IPrintOemUI::UpgradePrinter</strong></a></p></td>
<td><p>Enables a UI plug-in to upgrade device option values that are stored in the registry.</p></td>
</tr>
</tbody>
</table>

 

For more information, see [Implementing Printer Driver COM Interfaces](implementing-printer-driver-com-interfaces.md).

 

 




