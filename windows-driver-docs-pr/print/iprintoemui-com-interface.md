---
title: IPrintOemUI COM Interface
description: IPrintOemUI COM Interface
ms.assetid: 7fd4071a-11ce-49e6-9e23-4f0643da1d98
keywords: ["IPrintOemUI"]
---

# IPrintOemUI COM Interface


## <a href="" id="ddk-iprintoemui-com-interface-gg"></a>


The `IPrintOemUI` COM interface is the means by which the [printer interface DLL](printer-interface-dll.md) for Unidrv or Pscript5 communicates with a UI plug-in. The `IPrintOemUI` interface is implemented by each UI plug-in.

The following table lists and describes all the methods that the `IPrintOemUI` interface supplies. UI plug-ins must define all listed methods. If a method is not needed, it can simply return E\_NOTIMPL.

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
<td align="left"><p>[<strong>IPrintOemUI::CommonUIProp</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554159)</p></td>
<td align="left"><p>Enables a UI plug-in to modify an existing printer property sheet page or document property sheet page.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>IPrintOemUI::DeviceCapabilities</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554162)</p></td>
<td align="left"><p>Enables a UI plug-in to specify customized device capabilities.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>IPrintOemUI::DevicePropertySheets</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554165)</p></td>
<td align="left"><p>Enables a UI plug-in to add a new page to a printer device's printer property sheet.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>IPrintOemUI::DevMode</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554167)</p></td>
<td align="left"><p>Performs operations on a UI plug-in's private [<strong>DEVMODEW</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552837) members.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>IPrintOemUI::DevQueryPrintEx</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554172)</p></td>
<td align="left"><p>Enables a UI plug-in to help determine if a print job is printable.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>IPrintOemUI::DocumentPropertySheets</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554173)</p></td>
<td align="left"><p>Enables a UI plug-in to add a new page to a printer device's document property sheet.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>IPrintOemUI::DriverEvent</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554175)</p></td>
<td align="left"><p>Called by the print spooler when processing driver-specific events that might require action by the printer driver.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>IPrintOemUI::FontInstallerDlgProc</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554176)</p></td>
<td align="left"><p>Replaces the Unidrv font installer's user interface.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>IPrintOemUI::GetInfo</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554178)</p></td>
<td align="left"><p>(Implementation required.) Returns a UI plug-in's identification information.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>IPrintOemUI::PrinterEvent</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554182)</p></td>
<td align="left"><p>Enables a UI plug-in to process printer events.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>IPrintOemUI::PublishDriverInterface</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554184)</p></td>
<td align="left"><p>(Implementation required.) Supplies a pointer to the Unidrv or Pscript5 driver's [IPrintOemDriverUI COM interface](iprintoemdriverui-com-interface.md), [IPrintCoreUI2 COM interface](iprintcoreui2-com-interface.md), [IPrintCoreHelperPS interface](https://msdn.microsoft.com/library/windows/hardware/ff552906), or [IPrintCoreHelperUni interface](https://msdn.microsoft.com/library/windows/hardware/ff552940).</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>IPrintOemUI::QueryColorProfile</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554186)</p></td>
<td align="left"><p>Enables a printer interface DLL to specify an ICC profile for color management.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>IPrintOemUI::UpdateExternalFonts</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554188)</p></td>
<td align="left"><p>Enables a printer interface DLL to update a printer's [Unidrv font format files](customized-font-management.md#ddk-unidrv-font-format-files-gg).</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>IPrintOemUI::UpgradePrinter</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554189)</p></td>
<td align="left"><p>Enables a UI plug-in to upgrade device option values that are stored in the registry.</p></td>
</tr>
</tbody>
</table>

 

For more information, see [Implementing Printer Driver COM Interfaces](implementing-printer-driver-com-interfaces.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintOemUI%20COM%20Interface%20%20RELEASE:%20%283/29/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




