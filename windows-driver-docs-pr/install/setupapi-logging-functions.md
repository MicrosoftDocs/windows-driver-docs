---
title: SetupAPI Logging Functions
description: SetupAPI Logging Functions
ms.assetid: d27bd44c-41c1-4546-b463-11ed3f5c7d84
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# SetupAPI Logging Functions


Starting with Windows Vista, Plug and Play (PnP) device installation applications, class installers, and co-installers can use the following functions to write log entries to the [SetupAPI text logs](setupapi-text-logs.md).

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
<td align="left"><p>[<strong>SetupGetThreadLogToken</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552211)</p></td>
<td align="left"><p>Retrieves the [log token](log-tokens.md) for the thread that called [<strong>SetupGetThreadLogToken</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552211).</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>SetupSetThreadLogToken</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552216)</p></td>
<td align="left"><p>Sets the log token for the thread that called [<strong>SetupSetThreadLogToken</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552216).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>SetupWriteTextLog</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552218)</p></td>
<td align="left"><p>Writes a log entry in a [SetupAPI text log](setupapi-text-logs.md).</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>SetupWriteTextLogError</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552232)</p></td>
<td align="left"><p>Writes information about a SetupAPI-specific error or a Win32 error in SetupAPI text log.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>SetupWriteTextLogInfLine</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552236)</p></td>
<td align="left"><p>Writes a log entry in a SetupAPI text log that contains the text of a specified INF file line.</p></td>
</tr>
</tbody>
</table>

 

 

 





