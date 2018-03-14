---
title: Language Monitor Functions
author: windows-driver-content
description: Language Monitor Functions
ms.assetid: ffe1a52f-69cc-4346-945f-3f1bc0a1a91e
keywords:
- language monitors WDK print , functions
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Language Monitor Functions


## <a href="" id="ddk-language-monitor-functions-gg"></a>


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
<td><p>[<strong>ClosePort</strong>](https://msdn.microsoft.com/library/windows/hardware/ff545975)</p></td>
<td><p>Closes a port when there are no printers connected to it.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>EndDocPort</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548742)</p></td>
<td><p>Performs end-of-print-job tasks on a port.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>GetPrinterDataFromPort</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550506)</p></td>
<td><p>Optional. Polls a port for values that are stored in the registry.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>InitializePrintMonitor2</strong>](https://msdn.microsoft.com/library/windows/hardware/ff551605)</p></td>
<td><p>Initializes the print monitor and returns an instance handle.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>OpenPortEx</strong>](https://msdn.microsoft.com/library/windows/hardware/ff559596)</p></td>
<td><p>Opens a port for a newly connected printer.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>ReadPort</strong>](https://msdn.microsoft.com/library/windows/hardware/ff561909)</p></td>
<td><p>Reads data from a printer port.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>SendRecvBidiDataFromPort</strong>](https://msdn.microsoft.com/library/windows/hardware/ff562071)</p></td>
<td><p>Optional. Supports bidirectional communication between an application and a printer or print server.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>Shutdown</strong>](https://msdn.microsoft.com/library/windows/hardware/ff562646)</p></td>
<td><p>Optional. Deletes a monitor instance. This function is required for cluster support.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>StartDocPort</strong>](https://msdn.microsoft.com/library/windows/hardware/ff562710)</p></td>
<td><p>Performs the tasks required to start a print job on a port.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>WritePort</strong>](https://msdn.microsoft.com/library/windows/hardware/ff563792)</p></td>
<td><p>Writes data to a printer port.</p></td>
</tr>
</tbody>
</table>

 

 

 




