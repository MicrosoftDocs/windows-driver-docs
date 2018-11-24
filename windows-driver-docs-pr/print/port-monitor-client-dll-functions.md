---
title: Port Monitor Client DLL Functions
description: Port Monitor Client DLL Functions
ms.assetid: 41efab1a-0638-4925-90a2-cf68d2306ca6
keywords:
- port monitors WDK print , functions
- client DLL port monitor functions WDK
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Port Monitor Client DLL Functions





The following table lists the functions that a port monitor UI DLL must define.

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
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff545026" data-raw-source="[&lt;strong&gt;AddPortUI&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff545026)"><strong>AddPortUI</strong></a></p></td>
<td><p>Creates a port and obtains configuration information by displaying a dialog box.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff546290" data-raw-source="[&lt;strong&gt;ConfigurePortUI&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff546290)"><strong>ConfigurePortUI</strong></a></p></td>
<td><p>Configures a previously added port.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff547432" data-raw-source="[&lt;strong&gt;DeletePortUI&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff547432)"><strong>DeletePortUI</strong></a></p></td>
<td><p>Deletes a port.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff551608" data-raw-source="[&lt;strong&gt;InitializePrintMonitorUI&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff551608)"><strong>InitializePrintMonitorUI</strong></a></p></td>
<td><p>Initializes the port monitor UI DLL.</p></td>
</tr>
</tbody>
</table>

 

 

 




