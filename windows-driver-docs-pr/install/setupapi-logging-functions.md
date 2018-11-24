---
title: SetupAPI Logging Functions
description: SetupAPI Logging Functions
ms.assetid: d27bd44c-41c1-4546-b463-11ed3f5c7d84
ms.date: 04/20/2017
ms.localizationpriority: medium
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
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff552211" data-raw-source="[&lt;strong&gt;SetupGetThreadLogToken&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff552211)"><strong>SetupGetThreadLogToken</strong></a></p></td>
<td align="left"><p>Retrieves the <a href="log-tokens.md" data-raw-source="[log token](log-tokens.md)">log token</a> for the thread that called <a href="https://msdn.microsoft.com/library/windows/hardware/ff552211" data-raw-source="[&lt;strong&gt;SetupGetThreadLogToken&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff552211)"><strong>SetupGetThreadLogToken</strong></a>.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff552216" data-raw-source="[&lt;strong&gt;SetupSetThreadLogToken&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff552216)"><strong>SetupSetThreadLogToken</strong></a></p></td>
<td align="left"><p>Sets the log token for the thread that called <a href="https://msdn.microsoft.com/library/windows/hardware/ff552216" data-raw-source="[&lt;strong&gt;SetupSetThreadLogToken&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff552216)"><strong>SetupSetThreadLogToken</strong></a>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff552218" data-raw-source="[&lt;strong&gt;SetupWriteTextLog&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff552218)"><strong>SetupWriteTextLog</strong></a></p></td>
<td align="left"><p>Writes a log entry in a <a href="setupapi-text-logs.md" data-raw-source="[SetupAPI text log](setupapi-text-logs.md)">SetupAPI text log</a>.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff552232" data-raw-source="[&lt;strong&gt;SetupWriteTextLogError&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff552232)"><strong>SetupWriteTextLogError</strong></a></p></td>
<td align="left"><p>Writes information about a SetupAPI-specific error or a Win32 error in SetupAPI text log.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff552236" data-raw-source="[&lt;strong&gt;SetupWriteTextLogInfLine&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff552236)"><strong>SetupWriteTextLogInfLine</strong></a></p></td>
<td align="left"><p>Writes a log entry in a SetupAPI text log that contains the text of a specified INF file line.</p></td>
</tr>
</tbody>
</table>

 

 

 





