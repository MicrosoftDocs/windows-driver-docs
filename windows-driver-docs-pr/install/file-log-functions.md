---
title: File Log Functions
description: File Log Functions
keywords:
- SetupAPI functions WDK , log files
- log files WDK SetupAPI
ms.date: 04/20/2017
---

# File Log Functions





You can use a log file to record information about the files copied to a system during an installation. The log file can be either the system log or your own installation log file.

The following table lists the functions that can be used to manipulate log files. For more information about function descriptions, see the [Microsoft Windows SDK documentation](/documentation/).

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
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupinitializefileloga" data-raw-source="[&lt;strong&gt;SetupInitializeFileLog&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupinitializefileloga)"><strong>SetupInitializeFileLog</strong></a></p></td>
<td align="left"><p>Initializes a log file for use.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setuplogerrora" data-raw-source="[&lt;strong&gt;SetupLogError&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setuplogerrora)"><strong>SetupLogError</strong></a></p></td>
<td align="left"><p>Writes an error message to a log file. (It should be used only during the installation of the operating system.)</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setuplogfilea" data-raw-source="[&lt;strong&gt;SetupLogFile&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setuplogfilea)"><strong>SetupLogFile</strong></a></p></td>
<td align="left"><p>Adds an entry to the log file.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupqueryfileloga" data-raw-source="[&lt;strong&gt;SetupQueryFileLog&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupqueryfileloga)"><strong>SetupQueryFileLog</strong></a></p></td>
<td align="left"><p>Retrieves information from a log file.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupremovefilelogentrya" data-raw-source="[&lt;strong&gt;SetupRemoveFileLogEntry&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupremovefilelogentrya)"><strong>SetupRemoveFileLogEntry</strong></a></p></td>
<td align="left"><p>Removes an entry from a log file.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupterminatefilelog" data-raw-source="[&lt;strong&gt;SetupTerminateFileLog&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupterminatefilelog)"><strong>SetupTerminateFileLog</strong></a></p></td>
<td align="left"><p>Releases resources allocated to a log file.</p></td>
</tr>
</tbody>
</table>

