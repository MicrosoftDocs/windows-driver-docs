---
title: WIA Functions for Debugging
author: windows-driver-content
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
<td><p>[<strong>wiauDbgDump</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549627)</p></td>
<td><p>Logs a message containing one or more data values.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>wiauDbgError</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549633)</p></td>
<td><p>Logs an error message.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>wiauDbgErrorHr</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549637)</p></td>
<td><p>Logs a message containing an HRESULT and its error message string.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>wiauDbgFlags</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549643)</p></td>
<td><p>Determines whether a particular debugging flag is set.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>wiauDbgHelper</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549649)</p></td>
<td><p>Formats a message and writes it to a log file or the debugger.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>wiauDbgHelper2</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549653)</p></td>
<td><p>Writes a message to a log file, or debugger, or both.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>wiauDbgInit</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549660)</p></td>
<td><p>Initializes WIA debugging.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>wiauDbgLegacyError</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549667)</p></td>
<td><p>Logs an error message.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>wiauDbgLegacyError2</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549671)</p></td>
<td><p>Logs an error message.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>wiauDbgLegacyHresult2</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549675)</p></td>
<td><p>Logs a default message containing an HRESULT.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>wiauDbgLegacyTrace</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550150)</p></td>
<td><p>Logs a trace message.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>wiauDbgLegacyTrace2</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550152)</p></td>
<td><p>Logs a trace message.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>wiauDbgLegacyWarning</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550156)</p></td>
<td><p>Logs a warning message.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>wiauDbgSetFlags</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550159)</p></td>
<td><p>Sets debugging flags.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>wiauDbgTrace</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550161)</p></td>
<td><p>Logs a trace message.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>wiauDbgWarning</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550163)</p></td>
<td><p>Logs a warning message.</p></td>
</tr>
</tbody>
</table>

 

 

 




