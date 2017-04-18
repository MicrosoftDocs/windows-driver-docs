---
title: What are the WPP extended format specification strings
description: What are the WPP extended format specification strings
ms.assetid: f05117c0-cb4b-483a-a141-08423555170a
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
<td align="left"><p>Displays the name of the source file from which the trace message was generated. This variable can also be used in the [trace message prefix](trace-message-prefix.md).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>%!FLAGS!</p></td>
<td align="left"><p>Displays the value of the [trace flags](trace-flags.md) that enable the trace message. This variable can also be used in the [trace message prefix](trace-message-prefix.md).</p></td>
</tr>
<tr class="even">
<td align="left"><p>%!FUNC!</p></td>
<td align="left"><p>Displays the function that generated the trace message. This variable can also be used in the [trace message prefix](trace-message-prefix.md).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>%!LEVEL!</p></td>
<td align="left"><p>Displays the name of the [trace level](trace-level.md) that enables the trace message. This variable can also be used in the [trace message prefix](trace-message-prefix.md).</p></td>
</tr>
<tr class="even">
<td align="left"><p>%!LINE!</p></td>
<td align="left"><p>Displays the line number of the line in the code that generated the trace prefix. This variable can also be used in the [trace message prefix](trace-message-prefix.md).</p></td>
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
<td align="left"><p>Displays the difference between two time values, in milliseconds. It is a LONGLONG value that is displayed in <strong>day~h:m:s</strong> format.</p></td>
</tr>
<tr class="even">
<td align="left"><p>%!WAITTIME!</p></td>
<td align="left"><p>Displays the time that was spent waiting for something to be completed, in milliseconds. It is a LONGLONG value that is displayed in <strong>day~h:m:s</strong> format.</p>
<p>Designed to be used with <strong>%!due!</strong>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>%!due!</p></td>
<td align="left"><p>Displays the time that something is expected to be completed, in milliseconds. It is a LONGLONG value that is displayed in <strong>day~h:m:s</strong> format.</p>
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

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20What%20are%20the%20WPP%20extended%20format%20specification%20strings?%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




