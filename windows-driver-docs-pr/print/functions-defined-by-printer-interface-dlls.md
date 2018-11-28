---
title: Functions Defined by Printer Interface DLLs
description: Functions Defined by Printer Interface DLLs
ms.assetid: 8b0ae796-67cf-4619-a0a7-6cb6aab8c2e4
keywords:
- printer interface DLL WDK , functions
- functions WDK printer interface DLL
ms.date: 04/20/2017
ms.localizationpriority: medium
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
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff548532" data-raw-source="[&lt;strong&gt;DrvConvertDevMode&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff548532)"><strong>DrvConvertDevMode</strong></a></p></td>
<td><p>Converts the specified <a href="https://msdn.microsoft.com/library/windows/hardware/ff552837" data-raw-source="[&lt;strong&gt;DEVMODEW&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff552837)"><strong>DEVMODEW</strong></a> structure from one version to another.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff548539" data-raw-source="[&lt;strong&gt;DrvDeviceCapabilities&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff548539)"><strong>DrvDeviceCapabilities</strong></a></p></td>
<td><p>Returns requested information about a printer&#39;s capabilities.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff548542" data-raw-source="[&lt;strong&gt;DrvDevicePropertySheets&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff548542)"><strong>DrvDevicePropertySheets</strong></a></p></td>
<td><p>Calls <a href="common-property-sheet-user-interface.md" data-raw-source="[CPSUI](common-property-sheet-user-interface.md)">CPSUI</a> to create property sheet pages that describe a printer&#39;s properties.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff548544" data-raw-source="[&lt;strong&gt;DrvDocumentEvent&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff548544)"><strong>DrvDocumentEvent</strong></a></p></td>
<td><p>(Optional) Allows the printer interface DLL to specify which events associated with printing a document it will handle.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff548551" data-raw-source="[&lt;strong&gt;DrvDriverEvent&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff548551)"><strong>DrvDriverEvent</strong></a></p></td>
<td><p>(Optional) Allows the printer interface DLL to respond to notifications from the spooler that certain driver-specific events have occurred.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff548548" data-raw-source="[&lt;strong&gt;DrvDocumentPropertySheets&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff548548)"><strong>DrvDocumentPropertySheets</strong></a></p></td>
<td><p>Calls CPSUI to create property sheet pages that describe a print document&#39;s properties.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff548564" data-raw-source="[&lt;strong&gt;DrvPrinterEvent&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff548564)"><strong>DrvPrinterEvent</strong></a></p></td>
<td><p>Allows the printer interface DLL to respond to notifications from the spooler that certain printer-specific events have occurred.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff548573" data-raw-source="[&lt;strong&gt;DrvQueryColorProfile&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff548573)"><strong>DrvQueryColorProfile</strong></a></p></td>
<td><p>(Optional) Allows the printer interface DLL to specify an ICC profile to use for color management.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff548581" data-raw-source="[&lt;strong&gt;DrvQueryJobAttributes&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff548581)"><strong>DrvQueryJobAttributes</strong></a></p></td>
<td><p>(Optional) Allows the printer interface DLL to specify support for such capabilities as printing multiple document pages on a physical page (&quot;N-up&quot; printing), printing multiple copies of each page, and collating pages.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff547576" data-raw-source="[&lt;strong&gt;DevQueryPrintEx&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff547576)"><strong>DevQueryPrintEx</strong></a></p></td>
<td><p>Determines if a print job can be printed using the printer&#39;s current configuration.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff548600" data-raw-source="[&lt;strong&gt;DrvSplDeviceCaps&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff548600)"><strong>DrvSplDeviceCaps</strong></a></p></td>
<td><p>Returns requested information about a printer&#39;s capabilities.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff548648" data-raw-source="[&lt;strong&gt;DrvUpgradePrinter&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff548648)"><strong>DrvUpgradePrinter</strong></a></p></td>
<td><p>(Optional) Updates a printer&#39;s registry settings when a new version of the driver is added to a system.</p></td>
</tr>
</tbody>
</table>

 

 

 




