---
title: Language Monitor Functions
description: Language Monitor Functions
keywords:
- language monitors WDK print , functions
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Language Monitor Functions





The following table lists the functions that a language monitor must define.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Function name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>DllEntryPoint</strong></p></td>
<td><p>A DLL entry point, typically called <strong>DllMain</strong>, which is described in the Microsoft Windows SDK documentation.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/winsplp/nf-winsplp-closeport" data-raw-source="[&lt;strong&gt;ClosePort&lt;/strong&gt;](/windows-hardware/drivers/ddi/winsplp/nf-winsplp-closeport)"><strong>ClosePort</strong></a></p></td>
<td><p>Closes a port when there are no printers connected to it.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/previous-versions/ff548742(v=vs.85)" data-raw-source="[&lt;strong&gt;EndDocPort&lt;/strong&gt;](/previous-versions/ff548742(v=vs.85))"><strong>EndDocPort</strong></a></p></td>
<td><p>Performs end-of-print-job tasks on a port.</p></td>
</tr>
<tr class="even">
<td><p><a href="/previous-versions/ff550506(v=vs.85)" data-raw-source="[&lt;strong&gt;GetPrinterDataFromPort&lt;/strong&gt;](/previous-versions/ff550506(v=vs.85))"><strong>GetPrinterDataFromPort</strong></a></p></td>
<td><p>Optional. Polls a port for values that are stored in the registry.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/winsplp/nf-winsplp-initializeprintmonitor2" data-raw-source="[&lt;strong&gt;InitializePrintMonitor2&lt;/strong&gt;](/windows-hardware/drivers/ddi/winsplp/nf-winsplp-initializeprintmonitor2)"><strong>InitializePrintMonitor2</strong></a></p></td>
<td><p>Initializes the print monitor and returns an instance handle.</p></td>
</tr>
<tr class="even">
<td><p><a href="/previous-versions/ff559596(v=vs.85)" data-raw-source="[&lt;strong&gt;OpenPortEx&lt;/strong&gt;](/previous-versions/ff559596(v=vs.85))"><strong>OpenPortEx</strong></a></p></td>
<td><p>Opens a port for a newly connected printer.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/winsplp/nf-winsplp-readport" data-raw-source="[&lt;strong&gt;ReadPort&lt;/strong&gt;](/windows-hardware/drivers/ddi/winsplp/nf-winsplp-readport)"><strong>ReadPort</strong></a></p></td>
<td><p>Reads data from a printer port.</p></td>
</tr>
<tr class="even">
<td><p><a href="/previous-versions/ff562071(v=vs.85)" data-raw-source="[&lt;strong&gt;SendRecvBidiDataFromPort&lt;/strong&gt;](/previous-versions/ff562071(v=vs.85))"><strong>SendRecvBidiDataFromPort</strong></a></p></td>
<td><p>Optional. Supports bidirectional communication between an application and a printer or print server.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/previous-versions/ff562646(v=vs.85)" data-raw-source="[&lt;strong&gt;Shutdown&lt;/strong&gt;](/previous-versions/ff562646(v=vs.85))"><strong>Shutdown</strong></a></p></td>
<td><p>Optional. Deletes a monitor instance. This function is required for cluster support.</p></td>
</tr>
<tr class="even">
<td><p><a href="/previous-versions/ff562710(v=vs.85)" data-raw-source="[&lt;strong&gt;StartDocPort&lt;/strong&gt;](/previous-versions/ff562710(v=vs.85))"><strong>StartDocPort</strong></a></p></td>
<td><p>Performs the tasks required to start a print job on a port.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/winsplp/nf-winsplp-writeport" data-raw-source="[&lt;strong&gt;WritePort&lt;/strong&gt;](/windows-hardware/drivers/ddi/winsplp/nf-winsplp-writeport)"><strong>WritePort</strong></a></p></td>
<td><p>Writes data to a printer port.</p></td>
</tr>
</tbody>
</table>

 

