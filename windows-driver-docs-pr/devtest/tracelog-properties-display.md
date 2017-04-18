---
title: Tracelog Properties Display
description: Tracelog Properties Display
ms.assetid: 9adfb4d5-5a0b-4e79-9aa8-ae81e2e1df3e
keywords: ["Tracelog WDK , properties", "tracing WDK , properties", "properties WDK tracing"]
---

# Tracelog Properties Display


## <span id="ddk_tracelog_display_tools"></span><span id="DDK_TRACELOG_DISPLAY_TOOLS"></span>


Tracelog displays the properties of a trace session when you start, stop, update, or query the session.

The data comes from the EVENT\_TRACE\_PROPERTIES structure for the log session. The following table describes the fields in the display.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Field</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Operation Status</strong></p></td>
<td align="left"><p>The status returned by the system. For a list of status messages and system error codes, see the Microsoft Windows SDK documentation.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Logger Name</strong></p></td>
<td align="left"><p>The name of the trace session.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Logger ID</strong></p></td>
<td align="left"><p>Identifies the trace session.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Logger Thread ID</strong></p></td>
<td align="left"><p>Identifies the thread that runs the trace session.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Buffer Size</strong></p></td>
<td align="left"><p>The size of each buffer in KB.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Maximum Buffers</strong></p></td>
<td align="left"><p>The maximum number of buffers being used at one time. Use the <strong>-max</strong> parameter to change this value.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Minimum Buffers</strong></p></td>
<td align="left"><p>The minimum number of buffers allocated for the session. Use the <strong>-min</strong> parameter to set this value.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Number of Buffers</strong></p></td>
<td align="left"><p>The actual number of buffers allocated for the session.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Free Buffers</strong></p></td>
<td align="left"><p>Buffers that are allocated, but not currently in use.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Buffers Written</strong></p></td>
<td align="left"><p>The total number of buffers written during the trace session. This includes buffers written, flushed, and then rewritten, so it can exceed the value of <strong>Maximum Buffers</strong>.</p>
<p>To estimate the size of a sequential log file, multiply <strong>Buffers Written</strong> by <strong>Buffer Size</strong>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Events Lost</strong></p></td>
<td align="left"><p>The number of events that were generated but not recorded, usually because all allocated buffers were full.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Log Buffers Lost</strong></p></td>
<td align="left"><p>The number of buffers whose content could not be written to a log. Typically, this occurs only when there is not enough disk space to hold the log contents.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Real Time Buffers Lost</strong></p></td>
<td align="left"><p>The number of buffers whose content could not be delivered. Typically, this occurs when system resources are insufficient.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>AgeLimit</strong></p></td>
<td align="left"><p>The time delay before unused buffers are freed. To change this value, use <strong>-age</strong>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><em>Mode</em></p>
<p>(Real Time mode enabled, Log File mode, Buffering mode only)</p></td>
<td align="left"><p>The logging modes that are enabled for this session. For a complete list of logging mode constants, see the Windows SDK documentation.</p>
<div class="alert">
<strong>Note</strong>  
<p>The <strong>Log File Mode</strong> entry appears even when a log file is not being written. It displays the log file format.</p>
</div>
<div>
 
</div></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Enabled tracing</strong></p></td>
<td align="left"><p>The NT Kernel Logger events that are being traced. This field appears only when tracing the NT Kernel Logger session.</p>
<div class="alert">
<strong>Note</strong>  
<p>DPC, ISR, and context switch events do not appear in this field, even when they are being traced.</p>
</div>
<div>
 
</div></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Log Filename</strong></p></td>
<td align="left"><p>The log file used for the session. For real-time and buffered trace sessions, the field value is blank.</p>
<p>To change this value, use <strong>-f</strong>.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Local/Global Sequence numbers in use.</strong></p></td>
<td align="left"><p>Appears only when local or global sequence numbers are used.</p>
<p>To change this property, use <strong>-ls</strong> or <strong>-gs</strong>.</p></td>
</tr>
</tbody>
</table>

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Tracelog%20Properties%20Display%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




