---
title: SetupAPI Logging Functions
description: SetupAPI Logging Functions
ms.date: 04/20/2017
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
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupgetthreadlogtoken" data-raw-source="[&lt;strong&gt;SetupGetThreadLogToken&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupgetthreadlogtoken)"><strong>SetupGetThreadLogToken</strong></a></p></td>
<td align="left"><p>Retrieves the <a href="log-tokens.md" data-raw-source="[log token](log-tokens.md)">log token</a> for the thread that called <a href="/windows/win32/api/setupapi/nf-setupapi-setupgetthreadlogtoken" data-raw-source="[&lt;strong&gt;SetupGetThreadLogToken&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupgetthreadlogtoken)"><strong>SetupGetThreadLogToken</strong></a>.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupsetthreadlogtoken" data-raw-source="[&lt;strong&gt;SetupSetThreadLogToken&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupsetthreadlogtoken)"><strong>SetupSetThreadLogToken</strong></a></p></td>
<td align="left"><p>Sets the log token for the thread that called <a href="/windows/win32/api/setupapi/nf-setupapi-setupsetthreadlogtoken" data-raw-source="[&lt;strong&gt;SetupSetThreadLogToken&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupsetthreadlogtoken)"><strong>SetupSetThreadLogToken</strong></a>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupwritetextlog" data-raw-source="[&lt;strong&gt;SetupWriteTextLog&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupwritetextlog)"><strong>SetupWriteTextLog</strong></a></p></td>
<td align="left"><p>Writes a log entry in a <a href="setupapi-text-logs.md" data-raw-source="[SetupAPI text log](setupapi-text-logs.md)">SetupAPI text log</a>.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupwritetextlogerror" data-raw-source="[&lt;strong&gt;SetupWriteTextLogError&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupwritetextlogerror)"><strong>SetupWriteTextLogError</strong></a></p></td>
<td align="left"><p>Writes information about a SetupAPI-specific error or a Win32 error in SetupAPI text log.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupwritetextloginfline" data-raw-source="[&lt;strong&gt;SetupWriteTextLogInfLine&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupwritetextloginfline)"><strong>SetupWriteTextLogInfLine</strong></a></p></td>
<td align="left"><p>Writes a log entry in a SetupAPI text log that contains the text of a specified INF file line.</p></td>
</tr>
</tbody>
</table>

 

