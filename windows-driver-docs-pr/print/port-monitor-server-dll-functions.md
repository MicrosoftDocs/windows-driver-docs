---
title: Port Monitor Server DLL Functions
description: Port Monitor Server DLL Functions
ms.assetid: ffbcaaaa-7f9d-4b29-b939-189e10174074
keywords:
- port monitors WDK print , functions
- server DLL port monitor functions WDK
ms.date: 04/20/2017
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
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff545975" data-raw-source="[&lt;strong&gt;ClosePort&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff545975)"><strong>ClosePort</strong></a></p></td>
<td><p>Closes a port if there are no printers connected to it.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff548742" data-raw-source="[&lt;strong&gt;EndDocPort&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff548742)"><strong>EndDocPort</strong></a></p></td>
<td><p>Performs end-of-print-job tasks on a port.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff548754" data-raw-source="[&lt;strong&gt;EnumPorts&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff548754)"><strong>EnumPorts</strong></a></p></td>
<td><p>Enumerates the ports available for printing on a server.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff551605" data-raw-source="[&lt;strong&gt;InitializePrintMonitor2&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff551605)"><strong>InitializePrintMonitor2</strong></a></p></td>
<td><p>Initializes the print monitor and returns an instance handle.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff559593" data-raw-source="[&lt;strong&gt;OpenPort&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff559593)"><strong>OpenPort</strong></a></p></td>
<td><p>Opens a printer port.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff559596" data-raw-source="[&lt;strong&gt;OpenPortEx&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff559596)"><strong>OpenPortEx</strong></a></p></td>
<td><p>Opens a printer port. (Language monitor only)</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff561909" data-raw-source="[&lt;strong&gt;ReadPort&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff561909)"><strong>ReadPort</strong></a></p></td>
<td><p>Reads data from a printer port.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff562710" data-raw-source="[&lt;strong&gt;StartDocPort&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff562710)"><strong>StartDocPort</strong></a></p></td>
<td><p>Performs the tasks required to start a print job on a port.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff563792" data-raw-source="[&lt;strong&gt;WritePort&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff563792)"><strong>WritePort</strong></a></p></td>
<td><p>Writes data to a printer port.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564254" data-raw-source="[&lt;strong&gt;XcvClosePort&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564254)"><strong>XcvClosePort</strong></a></p></td>
<td><p>Closes a port after port management is complete. Available in Windows 2000 and later NT-based operating system versions.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564258" data-raw-source="[&lt;strong&gt;XcvDataPort&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564258)"><strong>XcvDataPort</strong></a></p></td>
<td><p>Handles port management tasks. Available in Windows 2000 and later NT-based operating system versions.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564259" data-raw-source="[&lt;strong&gt;XcvOpenPort&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564259)"><strong>XcvOpenPort</strong></a></p></td>
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
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff550506" data-raw-source="[&lt;strong&gt;GetPrinterDataFromPort&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550506)"><strong>GetPrinterDataFromPort</strong></a></p></td>
<td><p>Sends an I/O control code to a port driver and returns the result.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff562071" data-raw-source="[&lt;strong&gt;SendRecvBidiDataFromPort&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff562071)"><strong>SendRecvBidiDataFromPort</strong></a></p></td>
<td><p>Supports bidirectional communication between an application and a printer or print server. Available in Windows XP and later.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff562630" data-raw-source="[&lt;strong&gt;SetPortTimeOuts&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff562630)"><strong>SetPortTimeOuts</strong></a></p></td>
<td><p>Sets a time-out value on an open port.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff562646" data-raw-source="[&lt;strong&gt;Shutdown&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff562646)"><strong>Shutdown</strong></a></p></td>
<td><p>Deletes a monitor instance. This function is required for cluster support.</p></td>
</tr>
</tbody>
</table>

 

 

 




