---
title: Functions Defined by Printer Interface DLLs
description: Functions Defined by Printer Interface DLLs
keywords:
- printer interface DLL WDK , functions
- functions WDK printer interface DLL
ms.date: 04/20/2017
---

# Functions Defined by Printer Interface DLLs





Printer interface DLLs export the functions listed in the following table.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Function</th>
<th>Purpose</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>DllEntryPoint</strong></p></td>
<td><p>Initial DLL entry point, typically called DLLMain (described in the Microsoft Windows SDK documentation).</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/winddiui/nf-winddiui-drvconvertdevmode" data-raw-source="[&lt;strong&gt;DrvConvertDevMode&lt;/strong&gt;](/windows-hardware/drivers/ddi/winddiui/nf-winddiui-drvconvertdevmode)"><strong>DrvConvertDevMode</strong></a></p></td>
<td><p>Converts the specified <a href="/windows/win32/api/wingdi/ns-wingdi-devmodew" data-raw-source="[&lt;strong&gt;DEVMODEW&lt;/strong&gt;](/windows/win32/api/wingdi/ns-wingdi-devmodew)"><strong>DEVMODEW</strong></a> structure from one version to another.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/winddiui/nf-winddiui-drvdevicecapabilities" data-raw-source="[&lt;strong&gt;DrvDeviceCapabilities&lt;/strong&gt;](/windows-hardware/drivers/ddi/winddiui/nf-winddiui-drvdevicecapabilities)"><strong>DrvDeviceCapabilities</strong></a></p></td>
<td><p>Returns requested information about a printer's capabilities.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/winddiui/nf-winddiui-drvdevicepropertysheets" data-raw-source="[&lt;strong&gt;DrvDevicePropertySheets&lt;/strong&gt;](/windows-hardware/drivers/ddi/winddiui/nf-winddiui-drvdevicepropertysheets)"><strong>DrvDevicePropertySheets</strong></a></p></td>
<td><p>Calls <a href="common-property-sheet-user-interface.md" data-raw-source="[CPSUI](common-property-sheet-user-interface.md)">CPSUI</a> to create property sheet pages that describe a printer's properties.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/winddiui/nf-winddiui-drvdocumentevent" data-raw-source="[&lt;strong&gt;DrvDocumentEvent&lt;/strong&gt;](/windows-hardware/drivers/ddi/winddiui/nf-winddiui-drvdocumentevent)"><strong>DrvDocumentEvent</strong></a></p></td>
<td><p>(Optional) Allows the printer interface DLL to specify which events associated with printing a document it will handle.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/winddiui/nf-winddiui-drvdriverevent" data-raw-source="[&lt;strong&gt;DrvDriverEvent&lt;/strong&gt;](/windows-hardware/drivers/ddi/winddiui/nf-winddiui-drvdriverevent)"><strong>DrvDriverEvent</strong></a></p></td>
<td><p>(Optional) Allows the printer interface DLL to respond to notifications from the spooler that certain driver-specific events have occurred.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/winddiui/nf-winddiui-drvdocumentpropertysheets" data-raw-source="[&lt;strong&gt;DrvDocumentPropertySheets&lt;/strong&gt;](/windows-hardware/drivers/ddi/winddiui/nf-winddiui-drvdocumentpropertysheets)"><strong>DrvDocumentPropertySheets</strong></a></p></td>
<td><p>Calls CPSUI to create property sheet pages that describe a print document's properties.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/winddiui/nf-winddiui-drvprinterevent" data-raw-source="[&lt;strong&gt;DrvPrinterEvent&lt;/strong&gt;](/windows-hardware/drivers/ddi/winddiui/nf-winddiui-drvprinterevent)"><strong>DrvPrinterEvent</strong></a></p></td>
<td><p>Allows the printer interface DLL to respond to notifications from the spooler that certain printer-specific events have occurred.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/winddiui/nf-winddiui-drvquerycolorprofile" data-raw-source="[&lt;strong&gt;DrvQueryColorProfile&lt;/strong&gt;](/windows-hardware/drivers/ddi/winddiui/nf-winddiui-drvquerycolorprofile)"><strong>DrvQueryColorProfile</strong></a></p></td>
<td><p>(Optional) Allows the printer interface DLL to specify an ICC profile to use for color management.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/winddiui/nf-winddiui-drvqueryjobattributes" data-raw-source="[&lt;strong&gt;DrvQueryJobAttributes&lt;/strong&gt;](/windows-hardware/drivers/ddi/winddiui/nf-winddiui-drvqueryjobattributes)"><strong>DrvQueryJobAttributes</strong></a></p></td>
<td><p>(Optional) Allows the printer interface DLL to specify support for such capabilities as printing multiple document pages on a physical page ("N-up" printing), printing multiple copies of each page, and collating pages.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/winddiui/nf-winddiui-devqueryprintex" data-raw-source="[&lt;strong&gt;DevQueryPrintEx&lt;/strong&gt;](/windows-hardware/drivers/ddi/winddiui/nf-winddiui-devqueryprintex)"><strong>DevQueryPrintEx</strong></a></p></td>
<td><p>Determines if a print job can be printed using the printer's current configuration.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/winddiui/nf-winddiui-drvspldevicecaps" data-raw-source="[&lt;strong&gt;DrvSplDeviceCaps&lt;/strong&gt;](/windows-hardware/drivers/ddi/winddiui/nf-winddiui-drvspldevicecaps)"><strong>DrvSplDeviceCaps</strong></a></p></td>
<td><p>Returns requested information about a printer's capabilities.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/winddiui/nf-winddiui-drvupgradeprinter" data-raw-source="[&lt;strong&gt;DrvUpgradePrinter&lt;/strong&gt;](/windows-hardware/drivers/ddi/winddiui/nf-winddiui-drvupgradeprinter)"><strong>DrvUpgradePrinter</strong></a></p></td>
<td><p>(Optional) Updates a printer's registry settings when a new version of the driver is added to a system.</p></td>
</tr>
</tbody>
</table>

 

