---
title: What are the WPP extended format specification strings
description: What are the WPP extended format specification strings
ms.assetid: f05117c0-cb4b-483a-a141-08423555170a
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# What are the WPP extended format specification strings?


WPP includes predefined format specification strings that you can use in trace messages in addition to the standard format strings that are defined for **printf**.

You can use the **%!FLAGS!**, **%!FUNC!** and **%!LEVEL!** strings in a [trace message prefix](trace-message-prefix.md), and in any tracing function or macro, such as [**DoTraceMessage**](https://msdn.microsoft.com/library/windows/hardware/ff544918).

You can use the other extended strings in any tracing function.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Format string</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left">Software tracing</td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><p>%!FILE!</p></td>
<td align="left"><p>Displays the name of the source file from which the trace message was generated. This variable can also be used in the <a href="trace-message-prefix.md" data-raw-source="[trace message prefix](trace-message-prefix.md)">trace message prefix</a>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>%!FLAGS!</p></td>
<td align="left"><p>Displays the value of the <a href="trace-flags.md" data-raw-source="[trace flags](trace-flags.md)">trace flags</a> that enable the trace message. This variable can also be used in the <a href="trace-message-prefix.md" data-raw-source="[trace message prefix](trace-message-prefix.md)">trace message prefix</a>.</p></td>
</tr>
<tr class="even">
<td align="left"><p>%!FUNC!</p></td>
<td align="left"><p>Displays the function that generated the trace message. This variable can also be used in the <a href="trace-message-prefix.md" data-raw-source="[trace message prefix](trace-message-prefix.md)">trace message prefix</a>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>%!LEVEL!</p></td>
<td align="left"><p>Displays the name of the <a href="trace-level.md" data-raw-source="[trace level](trace-level.md)">trace level</a> that enables the trace message. This variable can also be used in the <a href="trace-message-prefix.md" data-raw-source="[trace message prefix](trace-message-prefix.md)">trace message prefix</a>.</p></td>
</tr>
<tr class="even">
<td align="left"><p>%!LINE!</p></td>
<td align="left"><p>Displays the line number of the line in the code that generated the trace prefix. This variable can also be used in the <a href="trace-message-prefix.md" data-raw-source="[trace message prefix](trace-message-prefix.md)">trace message prefix</a>.</p></td>
</tr>
<tr class="odd">
<td align="left">General use</td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><p>%!bool!</p></td>
<td align="left"><p>Displays TRUE or FALSE</p></td>
</tr>
<tr class="odd">
<td align="left"><p>%!irql!</p></td>
<td align="left"><p>Displays the name of the current IRQL.</p></td>
</tr>
<tr class="even">
<td align="left"><p>%!sid!</p></td>
<td align="left"><p>Represents a pointer to Security Identifier (pSID). Displays the SID.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>%!SRB!</p></td>
<td align="left"><p>Represents a pointer to SCSI request block. Displays the block content.</p></td>
</tr>
<tr class="even">
<td align="left"><p>%!SENSEDATA!</p></td>
<td align="left"><p>Represents a pointer to SCSI SENSE_DATA. Displays the sense data.</p></td>
</tr>
<tr class="odd">
<td align="left">GUIDs</td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><p>%!GUID!</p></td>
<td align="left"><p>Represents a pointer to a GUID (pGUID). Displays the GUID that is pointed to.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>%!CLSID!</p></td>
<td align="left"><p>Class ID. Represents a pointer to a class ID GUID. Displays the string associated with the GUID. WPP locates the string in the registry when it formats the trace messages.</p></td>
</tr>
<tr class="even">
<td align="left"><p>%!IID!</p></td>
<td align="left"><p>Interface ID. Represents a pointer to an interface ID GUID. Displays the string associated with the GUID. WPP locates the string in the registry when it formats the trace messages.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>%!LIBID!</p></td>
<td align="left"><p>Type library. Represents the GUID of a COM type library. Displays the string associated with the GUID. WPP locates the string in the registry when it formats the trace messages.</p></td>
</tr>
<tr class="even">
<td align="left">Time</td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"><p>%!delta!</p></td>
<td align="left"><p>Displays the difference between two time values, in milliseconds. It is a LONGLONG value that is displayed in <strong>day~h<span class="emoji" shortCode="m">Ⓜ️</span>s</strong> format.</p></td>
</tr>
<tr class="even">
<td align="left"><p>%!WAITTIME!</p></td>
<td align="left"><p>Displays the time that was spent waiting for something to be completed, in milliseconds. It is a LONGLONG value that is displayed in <strong>day~h<span class="emoji" shortCode="m">Ⓜ️</span>s</strong> format.</p>
<p>Designed to be used with <strong>%!due!</strong>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>%!due!</p></td>
<td align="left"><p>Displays the time that something is expected to be completed, in milliseconds. It is a LONGLONG value that is displayed in <strong>day~h<span class="emoji" shortCode="m">Ⓜ️</span>s</strong> format.</p>
<p>Designed to be used with <strong>%!WAITTIME!</strong>.</p></td>
</tr>
<tr class="even">
<td align="left"><p>%!TIMESTAMP!</p>
<p>%!datetime!</p>
<p>%!time!</p></td>
<td align="left"><p>Displays the value of system time at a particular moment. These are LARGE_INTEGER values that are displayed in SYSTEMTIME format.</p>
<p>You can use these variables to represent different time values in your program and to distinguish among them.</p></td>
</tr>
<tr class="odd">
<td align="left">Return codes</td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><p>%!STATUS!</p></td>
<td align="left"><p>Represents a status value and displays the string associated with the status code.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>%!WINERROR!</p></td>
<td align="left"><p>Represents a Windows error code and displays the string associated with the error.</p></td>
</tr>
<tr class="even">
<td align="left"><p>%!HRESULT!</p></td>
<td align="left"><p>Represents an error or warning and displays the code in HRESULT format.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>%!NTerror!</p></td>
<td align="left"><p>Represents a Windows error and displays the error message string.</p></td>
</tr>
<tr class="even">
<td align="left">Network</td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"><p>%!IPADDR!</p></td>
<td align="left"><p>Represents a pointer to an IP address. Displays the IP address.</p></td>
</tr>
<tr class="even">
<td align="left"><p>%!PORT!</p></td>
<td align="left"><p>Displays a port number.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>%!NETEVENT!</p></td>
<td align="left"><p>Displays a network event.</p></td>
</tr>
</tbody>
</table>

 

 

 





