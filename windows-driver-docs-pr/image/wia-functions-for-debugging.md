---
title: WIA Functions for Debugging
description: WIA Functions for Debugging
ms.assetid: 164eeab3-1e4a-46de-99db-28b8f63593a4
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# WIA Functions for Debugging





You can use the following function to log trace messages, warning messages, and error messages when you are developing your WIA minidriver.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Function</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff549627" data-raw-source="[&lt;strong&gt;wiauDbgDump&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549627)"><strong>wiauDbgDump</strong></a></p></td>
<td><p>Logs a message containing one or more data values.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff549633" data-raw-source="[&lt;strong&gt;wiauDbgError&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549633)"><strong>wiauDbgError</strong></a></p></td>
<td><p>Logs an error message.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff549637" data-raw-source="[&lt;strong&gt;wiauDbgErrorHr&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549637)"><strong>wiauDbgErrorHr</strong></a></p></td>
<td><p>Logs a message containing an HRESULT and its error message string.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff549643" data-raw-source="[&lt;strong&gt;wiauDbgFlags&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549643)"><strong>wiauDbgFlags</strong></a></p></td>
<td><p>Determines whether a particular debugging flag is set.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff549649" data-raw-source="[&lt;strong&gt;wiauDbgHelper&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549649)"><strong>wiauDbgHelper</strong></a></p></td>
<td><p>Formats a message and writes it to a log file or the debugger.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff549653" data-raw-source="[&lt;strong&gt;wiauDbgHelper2&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549653)"><strong>wiauDbgHelper2</strong></a></p></td>
<td><p>Writes a message to a log file, or debugger, or both.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff549660" data-raw-source="[&lt;strong&gt;wiauDbgInit&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549660)"><strong>wiauDbgInit</strong></a></p></td>
<td><p>Initializes WIA debugging.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff549667" data-raw-source="[&lt;strong&gt;wiauDbgLegacyError&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549667)"><strong>wiauDbgLegacyError</strong></a></p></td>
<td><p>Logs an error message.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff549671" data-raw-source="[&lt;strong&gt;wiauDbgLegacyError2&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549671)"><strong>wiauDbgLegacyError2</strong></a></p></td>
<td><p>Logs an error message.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff549675" data-raw-source="[&lt;strong&gt;wiauDbgLegacyHresult2&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549675)"><strong>wiauDbgLegacyHresult2</strong></a></p></td>
<td><p>Logs a default message containing an HRESULT.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff550150" data-raw-source="[&lt;strong&gt;wiauDbgLegacyTrace&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550150)"><strong>wiauDbgLegacyTrace</strong></a></p></td>
<td><p>Logs a trace message.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff550152" data-raw-source="[&lt;strong&gt;wiauDbgLegacyTrace2&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550152)"><strong>wiauDbgLegacyTrace2</strong></a></p></td>
<td><p>Logs a trace message.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff550156" data-raw-source="[&lt;strong&gt;wiauDbgLegacyWarning&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550156)"><strong>wiauDbgLegacyWarning</strong></a></p></td>
<td><p>Logs a warning message.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff550159" data-raw-source="[&lt;strong&gt;wiauDbgSetFlags&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550159)"><strong>wiauDbgSetFlags</strong></a></p></td>
<td><p>Sets debugging flags.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff550161" data-raw-source="[&lt;strong&gt;wiauDbgTrace&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550161)"><strong>wiauDbgTrace</strong></a></p></td>
<td><p>Logs a trace message.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff550163" data-raw-source="[&lt;strong&gt;wiauDbgWarning&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550163)"><strong>wiauDbgWarning</strong></a></p></td>
<td><p>Logs a warning message.</p></td>
</tr>
</tbody>
</table>

 

 

 




