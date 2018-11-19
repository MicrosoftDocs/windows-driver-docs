---
title: File Log Functions
description: File Log Functions
ms.assetid: 7d9fe4c9-834f-4dcc-a216-dc6a98ee2fd3
keywords:
- SetupAPI functions WDK , log files
- log files WDK SetupAPI
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# File Log Functions





You can use a log file to record information about the files copied to a system during an installation. The log file can be either the system log or your own installation log file.

The following table lists the functions that can be used to manipulate log files. For more information about function descriptions, see the [Microsoft Windows SDK documentation](http://go.microsoft.com/fwlink/p/?linkid=131248).

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Function</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/desktop/aa377397" data-raw-source="[&lt;strong&gt;SetupInitializeFileLog&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/desktop/aa377397)"><strong>SetupInitializeFileLog</strong></a></p></td>
<td align="left"><p>Initializes a log file for use.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/desktop/aa377405" data-raw-source="[&lt;strong&gt;SetupLogError&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/desktop/aa377405)"><strong>SetupLogError</strong></a></p></td>
<td align="left"><p>Writes an error message to a log file. (It should be used only during the installation of the operating system.)</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/desktop/aa377406" data-raw-source="[&lt;strong&gt;SetupLogFile&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/desktop/aa377406)"><strong>SetupLogFile</strong></a></p></td>
<td align="left"><p>Adds an entry to the log file.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/desktop/aa377415" data-raw-source="[&lt;strong&gt;SetupQueryFileLog&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/desktop/aa377415)"><strong>SetupQueryFileLog</strong></a></p></td>
<td align="left"><p>Retrieves information from a log file.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/desktop/aa377429" data-raw-source="[&lt;strong&gt;SetupRemoveFileLogEntry&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/desktop/aa377429)"><strong>SetupRemoveFileLogEntry</strong></a></p></td>
<td align="left"><p>Removes an entry from a log file.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/desktop/aa377443" data-raw-source="[&lt;strong&gt;SetupTerminateFileLog&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/desktop/aa377443)"><strong>SetupTerminateFileLog</strong></a></p></td>
<td align="left"><p>Releases resources allocated to a log file.</p></td>
</tr>
</tbody>
</table>

 

 

 





