---
title: Port Monitor Server DLL Functions
author: windows-driver-content
description: Port Monitor Server DLL Functions
ms.assetid: ffbcaaaa-7f9d-4b29-b939-189e10174074
keywords:
- port monitors WDK print , functions
- server DLL port monitor functions WDK
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# Port Monitor Server DLL Functions





The following table lists the functions that a port monitor server DLL must define.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Function Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>DllEntryPoint</strong></p></td>
<td><p>DLL entry point, typically called <strong>DllMain</strong>, which is described in the Microsoft Windows SDK documentation.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>ClosePort</strong>](https://msdn.microsoft.com/library/windows/hardware/ff545975)</p></td>
<td><p>Closes a port if there are no printers connected to it.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>EndDocPort</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548742)</p></td>
<td><p>Performs end-of-print-job tasks on a port.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>EnumPorts</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548754)</p></td>
<td><p>Enumerates the ports available for printing on a server.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>InitializePrintMonitor2</strong>](https://msdn.microsoft.com/library/windows/hardware/ff551605)</p></td>
<td><p>Initializes the print monitor and returns an instance handle.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>OpenPort</strong>](https://msdn.microsoft.com/library/windows/hardware/ff559593)</p></td>
<td><p>Opens a printer port.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>OpenPortEx</strong>](https://msdn.microsoft.com/library/windows/hardware/ff559596)</p></td>
<td><p>Opens a printer port. (Language monitor only)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>ReadPort</strong>](https://msdn.microsoft.com/library/windows/hardware/ff561909)</p></td>
<td><p>Reads data from a printer port.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>StartDocPort</strong>](https://msdn.microsoft.com/library/windows/hardware/ff562710)</p></td>
<td><p>Performs the tasks required to start a print job on a port.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>WritePort</strong>](https://msdn.microsoft.com/library/windows/hardware/ff563792)</p></td>
<td><p>Writes data to a printer port.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>XcvClosePort</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564254)</p></td>
<td><p>Closes a port after port management is complete. Available in Windows 2000 and later NT-based operating system versions.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>XcvDataPort</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564258)</p></td>
<td><p>Handles port management tasks. Available in Windows 2000 and later NT-based operating system versions.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>XcvOpenPort</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564259)</p></td>
<td><p>Opens a port for management purposes. Available in Windows 2000 and later NT-based operating system versions.</p></td>
</tr>
</tbody>
</table>

 

The following port monitor server DLL functions are optional.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Function Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>[<strong>GetPrinterDataFromPort</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550506)</p></td>
<td><p>Sends an I/O control code to a port driver and returns the result.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>SendRecvBidiDataFromPort</strong>](https://msdn.microsoft.com/library/windows/hardware/ff562071)</p></td>
<td><p>Supports bidirectional communication between an application and a printer or print server. Available in Windows XP and later.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>SetPortTimeOuts</strong>](https://msdn.microsoft.com/library/windows/hardware/ff562630)</p></td>
<td><p>Sets a time-out value on an open port.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>Shutdown</strong>](https://msdn.microsoft.com/library/windows/hardware/ff562646)</p></td>
<td><p>Deletes a monitor instance. This function is required for cluster support.</p></td>
</tr>
</tbody>
</table>

 

 

 




