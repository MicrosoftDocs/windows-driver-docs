---
title: Printer Dirids
description: Printer Dirids
ms.assetid: 104af180-c739-4733-b21b-448cfe15ab71
keywords:
- INF files WDK print , dirids
- dirids WDK
- directory identifiers WDK printer
- printer dirids WDK
- identifiers WDK printer
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Printer Dirids





When specifying target directories within INF files, directory identifiers (`dirids`) should be used. For more information, see [Using Dirids](https://msdn.microsoft.com/library/windows/hardware/ff553598).

The following table lists printer-specific `dirids` and the purpose of each.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>Dirid</th>
<th>Purpose</th>
<th>Directory Contents</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>66000</p></td>
<td><p>Represents the directory path returned by the <a href="http://go.microsoft.com/fwlink/p/?linkid=124454" data-raw-source="[GetPrinterDriverDirectory](http://go.microsoft.com/fwlink/p/?linkid=124454)">GetPrinterDriverDirectory</a> function.</p></td>
<td><p>Driver files and <a href="printer-inf-file-entries.md#ddk-dependent-files-gg" data-raw-source="[dependent files](printer-inf-file-entries.md#ddk-dependent-files-gg)">dependent files</a>.</p></td>
</tr>
<tr class="even">
<td><p>66001</p></td>
<td><p>Represents the directory path returned by the <a href="http://go.microsoft.com/fwlink/p/?linkid=124455" data-raw-source="[GetPrintProcessorDirectory](http://go.microsoft.com/fwlink/p/?linkid=124455)">GetPrintProcessorDirectory</a> function.</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff556325#wdkgloss-print-processor" data-raw-source="[&lt;em&gt;Print processor&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556325#wdkgloss-print-processor)"><em>Print processor</em></a> files.</p></td>
</tr>
<tr class="odd">
<td><p>66002</p></td>
<td><p>Represents the directory path to additional files to be copied to \System32 of the local system. See the paragraph following this table.</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff556325#wdkgloss-print-monitor" data-raw-source="[&lt;em&gt;Print monitor&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556325#wdkgloss-print-monitor)"><em>Print monitor</em></a> files.</p></td>
</tr>
<tr class="even">
<td><p>66003</p></td>
<td><p>Represents the directory path returned by the <a href="http://go.microsoft.com/fwlink/p/?linkid=124456" data-raw-source="[GetColorDirectory](http://go.microsoft.com/fwlink/p/?linkid=124456)">GetColorDirectory</a> function.</p></td>
<td><p>ICM color profile files.</p></td>
</tr>
<tr class="odd">
<td><p>66004</p></td>
<td><p>Represents the directory path to which printer type-specific ASP files are copied.</p></td>
<td><p>ASP files and associated files.</p></td>
</tr>
</tbody>
</table>

 

Files in the directory assigned to `dirid` 66002 are copied to the System32 subdirectory when printer drivers for the native architecture are being installed on the local system, such as when x86 drivers are installed locally on a x86 system. Files in this directory are ignored if a driver is being installed to a remote system.

A printer driver is installed when the printer class installer calls the spooler's [AddPrinterDriverEx](http://go.microsoft.com/fwlink/p/?linkid=124457) function. This function requires all driver files to be located in the directory that is returned by the **GetPrinterDriverDirectory** function.

 

 




