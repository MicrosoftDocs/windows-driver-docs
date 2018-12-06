---
title: Setting the Event Level for a Text Log
description: Setting the Event Level for a Text Log
ms.assetid: 3dfd2df3-179e-434c-97fb-fd8329198f8a
keywords:
- event levels WDK SetupAPI logging
- text logs WDK SetupAPI , event levels
- LogLevel
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Setting the Event Level for a Text Log


[SetupAPI](setupapi.md) writes a log entry to a text log only if the event level set for a text log is greater than or equal to the event level for the log entry, and the [event category](enabling-event-categories-for-a-text-log.md) for the log entry is enabled for the text log.

The following table lists the event levels that SetupAPI supports and the manifest constants that represent these event levels. TXTLOG_ERROR is the lowest event level, followed by the next highest event level TXTLOG_WARNING, and so on. TXTLOG_VERY_VERBOSE is the highest event level.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Event level</th>
<th align="left">Event level manifest constant</th>
<th align="left">Event level manifest value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Write errors only.</p></td>
<td align="left"><p>TXTLOG_ERROR</p></td>
<td align="left"><p>1</p></td>
</tr>
<tr class="even">
<td align="left"><p>Write errors and warnings of potential problems.</p></td>
<td align="left"><p>TXTLOG_WARNING</p></td>
<td align="left"><p>2</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Write errors, warnings, and system state changes.</p></td>
<td align="left"><p>TXTLOG_SYSTEM_STATE_CHANGE</p></td>
<td align="left"><p>3</p></td>
</tr>
<tr class="even">
<td align="left"><p>Write errors, warnings, system state changes, and high-level operations that are associated with state changes.</p></td>
<td align="left"><p>TXTLOG_SUMMARY</p></td>
<td align="left"><p>4</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Write errors, warnings, system state changes, high-level operations that are associated with state changes, and most operational details.</p></td>
<td align="left"><p>TXTLOG_DETAILS</p></td>
<td align="left"><p>5</p></td>
</tr>
<tr class="even">
<td align="left"><p>Write errors, warnings, system state changes, high-level operations that are associated with state changes, and all operational details.</p></td>
<td align="left"><p>TXTLOG_VERBOSE</p></td>
<td align="left"><p>6</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Write all log entries, including those that might generate a large amount of information that is frequently superfluous.</p></td>
<td align="left"><p>TXTLOG_VERY_VERBOSE</p></td>
<td align="left"><p>7</p></td>
</tr>
</tbody>
</table>

 

<a href="" id="to-set-the-event-level-for-the-setupapi-text-logs--create--or-modify--the-following-reg-dword-registry-value-"></a>To set the event level for the SetupAPI text logs, create (or modify) the following [REG_DWORD](https://docs.microsoft.com/windows/desktop/SysInfo/registry-value-types) registry value:  
**HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\Setup\\LogLevel**

If the **LogLevel** registry value does not exist or has a value of zero, SetupAPI sets the event level for the application installation and device installation text logs to the default values described in the following table:

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Text log</th>
<th align="left">Default value (Windows 7 and later versions)</th>
<th align="left">Default value (Windows Vista SP2)</th>
<th align="left">Default value (Windows Vista SP1 and previous versions)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Application installation text log (<em>SetupAPI.app.log</em>)</p></td>
<td align="left"><p>TXTLOG_SUMMARY</p></td>
<td align="left"><p>TXTLOG_WARNING</p></td>
<td align="left"><p>TXTLOG_DETAILS</p></td>
</tr>
<tr class="even">
<td align="left"><p>Device installation text log (<em>SetupAPI.dev.log</em>)</p></td>
<td align="left"><p>TXTLOG_DETAILS</p></td>
<td align="left"><p>TXTLOG_DETAILS</p></td>
<td align="left"><p>TXTLOG_DETAILS</p></td>
</tr>
</tbody>
</table>

 

For more information about these text log files, see [SetupAPI Text Logs](setupapi-text-logs.md).

The **LogLevel** registry value is formatted as 0x*UUUUGHVW,* where:

-   The low-order eight bits, represented by the mask 0x000000*VW*, specify whether logging is turned on for the application installation log and specify the event level for the application log.

-   The next highest eight bits, represented by the mask 0x0000*GH*00, specify whether logging is turned on for the device installation text log and specify the event level for the device installation text log.

-   The highest-level bits, represented by the mask 0x*UUUU*0000, are not used.

The value of the 0x*VW* bits controls logging for the application installation log as shown in the following table.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left"><em>0xVW</em> value</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Zero (default)</p></td>
<td align="left"><p>Logging is turned on and the event level is set to the default value as described previously.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x01 through 0x0F</p></td>
<td align="left"><p>Turns logging off.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x10 through 0x7F</p></td>
<td align="left"><p>Turns logging on and sets the event level to 0xV.</p></td>
</tr>
</tbody>
</table>

 

The value of the 0x*GH* bits controls logging for the device installation text log as shown in the following table.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left"><em>0xGH</em> value</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Zero (default)</p></td>
<td align="left"><p>Logging is turned on and the event level is set to the default value as described previously.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x01 through 0x0F</p></td>
<td align="left"><p>Turns logging off.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x10 through 0x7F</p></td>
<td align="left"><p>Turns logging on and sets the event level to 0xG.</p></td>
</tr>
</tbody>
</table>

 

The following table provides examples of typical **LogLevel** values.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">LogLevel value</th>
<th align="left">Event levels set for the text logs</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>0x00000000</p></td>
<td align="left"><p>By default, turns logging on for the application installation log and the device installation log. Sets the logging level to the default values for both logs.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x00000101</p></td>
<td align="left"><p>Turns logging off for both the application installation log and the device installation log.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x00001010</p></td>
<td align="left"><p>Turns logging on for the application installation log and the device installation log. Sets the logging level to TXTLOG_ERROR for both logs.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x00002020</p></td>
<td align="left"><p>Turns logging on for the application installation log and the device installation log. Sets the logging level to TXTLOG_WARNING for both logs.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x00005050</p></td>
<td align="left"><p>Turns logging on for the application installation log and the device installation log. Sets the logging level to TXTLOG_DETAILS for both logs.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x00006060</p></td>
<td align="left"><p>Turns logging on for the application installation log and the device installation log. Sets the logging level to TXTLOG_VERBOSE for both logs.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x00007070</p></td>
<td align="left"><p>Turns logging on for the application installation log and the device installation log. Sets the logging level to TXTLOG_VERY_VERBOSE for both logs.</p></td>
</tr>
</tbody>
</table>

 

 

 





