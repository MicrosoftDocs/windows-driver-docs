---
title: File Log Functions
description: File Log Functions
ms.assetid: 7d9fe4c9-834f-4dcc-a216-dc6a98ee2fd3
keywords:
- SetupAPI functions WDK , log files
- log files WDK SetupAPI
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# File Log Functions


## <a href="" id="ddk-file-log-functions-dg"></a>


You can use a log file to record information about the files copied to a system during an installation. The log file can be either the system log or your own installation log file.

The following table lists the functions that can be used to manipulate log files. For more information about function descriptions, see the Microsoft Windows SDK documentation on [MSDN](http://go.microsoft.com/fwlink/p/?linkid=131248).

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
<td align="left"><p>[<strong>SetupInitializeFileLog</strong>](https://msdn.microsoft.com/library/windows/desktop/aa377397)</p></td>
<td align="left"><p>Initializes a log file for use.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>SetupLogError</strong>](https://msdn.microsoft.com/library/windows/desktop/aa377405)</p></td>
<td align="left"><p>Writes an error message to a log file. (It should be used only during the installation of the operating system.)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>SetupLogFile</strong>](https://msdn.microsoft.com/library/windows/desktop/aa377406)</p></td>
<td align="left"><p>Adds an entry to the log file.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>SetupQueryFileLog</strong>](https://msdn.microsoft.com/library/windows/desktop/aa377415)</p></td>
<td align="left"><p>Retrieves information from a log file.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>SetupRemoveFileLogEntry</strong>](https://msdn.microsoft.com/library/windows/desktop/aa377429)</p></td>
<td align="left"><p>Removes an entry from a log file.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>SetupTerminateFileLog</strong>](https://msdn.microsoft.com/library/windows/desktop/aa377443)</p></td>
<td align="left"><p>Releases resources allocated to a log file.</p></td>
</tr>
</tbody>
</table>

 

 

 





