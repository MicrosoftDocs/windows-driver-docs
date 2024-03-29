---
title: Global Logger Trace Session
description: Global Logger Trace Session
keywords:
- trace sessions WDK , Global Logger
- Global Logger trace session WDK , about Global Logger sessions
- Global Logger trace session WDK , registry entries
ms.date: 04/20/2017
---

# Global Logger Trace Session

A *Global Logger trace session* records events that occur during the boot process before the system is fully operational, such as events generated by device drivers. It is a reserved trace session that is built into Windows.

Global Logger trace sessions always write messages to a trace log. Global Logger does not support real-time trace sessions or buffered trace sessions.

Because Global Logger must be available early in the operating system boot process, it is started and configured by using registry entries (in the **HKLM\\SYSTEM\\CurrentControlSet\\Control\\WMI\\GlobalLogger** subkey), instead of function calls. After starting, the Global Logger behaves like a regular event tracing session.

The Global Logger trace session uses a reserved session name, "GlobalLogger." The [control GUID](control-guid.md) is represented by the constant, **GlobalLoggerGuid**. You create a Global Logger trace session, and then restart the computer to start the trace session. Only one Global Logger trace session can run on the computer at a time.

To create a Global Logger trace session, use [Tracelog](tracelog.md). It automatically creates the registry subkey and entries that store trace session options. The Global Logger trace session starts when you restart the computer. For more information, see [**Tracelog Command Syntax**](tracelog-command-syntax.md).

To format the trace messages from a Global Logger trace session, use [Tracefmt](tracefmt.md) with system.tmf, a [trace message format file](trace-message-format-file.md) included in the WDK.

Because the Global Logger session is triggered by registry entries, it runs every time that the entries appear in the registry. To prevent the Global Logger session from starting every time the system starts, set the value of the **Start** entry to 0 or delete all of the registry entries.

You can convert a Global Logger trace session to an NT Kernel Logger trace session, thereby tracing the kernel during the boot process. For information, see [Boot-time Global Logger Session](boot-time-global-logger-session.md)

[Trace providers](trace-provider.md), such as kernel-mode drivers and user-mode applications, can log to the Global Logger trace session. This enables you to trace a driver or other trace provider during system boot. For information, see [Logging to the Global Logger Session](logging-to-the-global-logger-session.md)

## Limitations of the Global Logger Trace Session

The Global Logger trace session is very useful, but it's important to be aware of its limitations:

You can run only one Global Logger session at a time.

The Global Logger session does not send enable notification to providers.

The Global Logger registry entries remain in the registry and are effective until you reset or delete them manually, or use the **tracelog -remove** command. Until you reset them, the Global Logger session starts every time you start the system.

The Windows ACPI logger is permanently enabled for the Global Logger trace session. The trace messages from this logger appear in the trace log.

If a standard trace session starts while a driver is logging to the Global Logger session, the driver switches and starts logging to the standard trace session.

## Global Logger Registry Entries

The following table shows the registry entries that configure the Global Logger session. These entries are in the **HKLM\\SYSTEM\\CurrentControlSet\\Control\\WMI\\GlobalLogger** subkey. Only the **Start** entry is required.

In addition to the registry entries in this table, you can also add a **ControlGUID** subkey under the **GlobalLogger** subkey to represent a trace provider, such as a driver, that logs to the Global Logger trace session. For information, see [Logging to the Global Logger Session](logging-to-the-global-logger-session.md).

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Entry</th>
<th align="left">Data type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Start</strong></p></td>
<td align="left"><p>REG_DWORD</p></td>
<td align="left"><p>When set to <strong>1</strong> (on), the Global Logger session starts the next time the system starts.</p>
<p><strong>0</strong> = off, <strong>1</strong>=on</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>BufferSize</strong></p></td>
<td align="left"><p>REG_DWORD</p></td>
<td align="left"><p>Specifies the size of each buffer (in KB). The default value is 0x40 (64 KB).</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>ClockType</strong></p></td>
<td align="left"><p>REG_DWORD</p></td>
<td align="left"><p>Specifies the timer used for trace message time stamps.</p>
<p>Beginning with Windows Vista, the default value is <strong>1</strong>. On operating systems prior to Windows Vista, the default value is <strong>2</strong>.</p>
<p><strong>1</strong> = Performance counter value (high resolution)</p>
<p><strong>2</strong> = System timer</p>
<p><strong>3</strong> = CPU cycle clock</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>EnableKernelFlags</strong></p></td>
<td align="left"><p>REG_BINARY</p></td>
<td align="left"><p>Converts the Global Logger session to an NT Kernel Logger trace session and specifies the events included in the kernel trace.</p>
<p>For information, see <a href="boot-time-global-logger-session.md" data-raw-source="[Boot-time Global Logger Session](boot-time-global-logger-session.md)">Boot-time Global Logger Session</a>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>FileCounter</strong></p></td>
<td align="left"><p>REG_DWORD</p></td>
<td align="left"><p>Stores the number of event trace log files generated by Global Logger sessions.</p>
<p>The system increments this value until it reaches the value of <strong>FileMax</strong>. Then, it resets the value to 0.</p>
<p>This counter prevents the system from overwriting a Global Logger trace log file.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>FileMax</strong></p></td>
<td align="left"><p>REG_DWORD</p></td>
<td align="left"><p>Specifies the maximum number of event trace log files permitted on the system.</p>
<p>When the number of trace logs reaches the specified maximum, the system begins to overwrite the logs, beginning with the oldest.</p>
<p>The default value is 0, meaning that there is no maximum.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>FileName</strong></p></td>
<td align="left"><p>REG_SZ</p></td>
<td align="left"><p>Path (optional) and file name of the event trace log file. The default is %SystemRoot%\System32\LogFiles\WMI\trace.log.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>FlushTimer</strong></p></td>
<td align="left"><p>REG_DWORD</p></td>
<td align="left"><p>Specifies how often (in seconds) the trace buffers are forcibly flushed. This forced flush is in addition to the automatic flush that occurs whenever a buffer is full and when the trace session stops.</p>
<p>The default value is 0. By default, buffers are flushed only when they are full.</p>
<p>The minimum flush time is 1 second.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>LogFileMode</strong></p></td>
<td align="left"><p>REG_DWORD</p></td>
<td align="left"><p>Specifies log session options.</p>
<p>Supported only in Windows Vista and later versions of Windows.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>MaximumBuffers</strong></p></td>
<td align="left"><p>REG_DWORD</p></td>
<td align="left"><p>Specifies the maximum number of buffers that can be allocated for the session. The default value is 0x19 (25).</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>MaximumFileSize</strong></p></td>
<td align="left"><p>REG_DWORD</p></td>
<td align="left"><p>Specifies the maximum size of the event trace log file. By default, there is no maximum file size.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>MinimumBuffers</strong></p></td>
<td align="left"><p>REG_DWORD</p></td>
<td align="left"><p>Specifies the number of buffers allocated when the session starts. The default value is 0x3.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Status</strong></p></td>
<td align="left"><p>REG_DWORD</p></td>
<td align="left"><p>Stores the return code from the attempt to start a Global Logger trace session.</p>
<p>If the session failed to start, the value of this entry is a Win32 error code. If the session started, the value of this entry is ERROR_SUCCESS.</p></td>
</tr>
</tbody>
</table>

 

These registry entries that you create remain in the registry and are effective until you delete them or change their values. Therefore, after the Global Logger session has run, use the **tracelog -remove GlobalLogger** command to set the value of the **Start** entry to 0 and delete the other Global Logger registry entries. Otherwise, the Global Logger session runs every time that you restart the computer, and the resulting log file can grow very large.

## Logging Mode Constants

The following table displays the valid values for the **LogFileMode** registry entry in the **HKLM\\System\\CurrentControlSet\\Control\\WMI\\GlobalLogger** subkey. This entry is used to set options for a Global Logger trace session, including those for real-time trace sessions, private trace sessions, circular logging, and buffering (no log). This registry entry is supported only in Windows Vista and later versions of Windows.

This registry entry corresponds to the **LogFileMode** member of the EVENT\_TRACE\_PROPERTIES structure. Its values correspond to the Logging Mode Constants. The EVENT\_TRACE\_PROPERTIES structure and the Logging Mode Constants are described in the Microsoft Windows SDK documentation.

This table is displayed here to show the hexadecimal values of the constants. Use these values or a sum of these values to represent the constant in the **LogFileMode** registry entry.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Value</th>
<th align="left">Constant</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>0x0</p></td>
<td align="left"><p>EVENT_TRACE_FILE_MODE_NONE</p></td>
<td align="left"><p>No event trace log files are created.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x1</p></td>
<td align="left"><p>EVENT_TRACE_FILE_MODE_SEQUENTIAL</p></td>
<td align="left"><p>Event trace log files are sequential.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x2</p></td>
<td align="left"><p>EVENT_TRACE_FILE_MODE_CIRCULAR</p></td>
<td align="left"><p>Event trace log files are circular.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x4</p></td>
<td align="left"><p>EVENT_TRACE_FILE_MODE_APPEND</p></td>
<td align="left"><p>Append trace messages to an existing log file. This mode is valid only with sequential files.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x8</p></td>
<td align="left"><p>EVENT_TRACE_FILE_MODE_NEWFILE</p></td>
<td align="left"><p>Create a new event trace log file whenever the existing file reaches the value of the <strong>MaximumFileSize</strong> entry (see the table above).</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x20</p></td>
<td align="left"><p>EVENT_TRACE_FILE_MODE_PREALLOCATE</p></td>
<td align="left"><p>Reserves space for the event trace log file.</p>
<p>Valid only with EVENT_TRACE_FILE_MODE_SEQUENTIAL or EVENT_TRACE_FILE_MODE_CIRCULAR, and not valid with EVENT_TRACE_FILE_MODE_NEWFILE.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x40</p></td>
<td align="left"><p>EVENT_TRACE_NONSTOPPABLE_MODE</p></td>
<td align="left"><p>A call to <strong>StopTrace</strong> does not stop the trace session.</p>
<p>This feature prevents users from stopping trace sessions that the system requires for diagnosis and tuning.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x100</p></td>
<td align="left"><p>EVENT_TRACE_REAL_TIME_MODE</p></td>
<td align="left"><p>Specifies a real-time trace session.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x200</p></td>
<td align="left"><p>EVENT_TRACE_DELAY_OPEN_FILE_MODE</p></td>
<td align="left"><p>For internal use only.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x400</p></td>
<td align="left"><p>EVENT_TRACE_BUFFERING_MODE</p></td>
<td align="left"><p>Events are retained in the buffers. They are never written to a log file or delivered to a trace consumer.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x800</p></td>
<td align="left"><p>EVENT_TRACE_PRIVATE_LOGGER_MODE</p></td>
<td align="left"><p>Specifies a private trace session. This flag is not valid for a Global Logger trace session.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x1000</p></td>
<td align="left"><p>EVENT_TRACE_ADD_HEADER_MODE</p></td>
<td align="left"><p>For internal use only.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x2000</p></td>
<td align="left"><p>EVENT_TRACE_USE_KBYTES_FOR_SIZE</p></td>
<td align="left"><p>Interpret the value of <strong>MaximumFileSize</strong> in KB, instead of MB.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x4000</p></td>
<td align="left"><p>EVENT_TRACE_USE_GLOBAL_SEQUENCE</p></td>
<td align="left"><p>Generates global sequence numbers for trace messages. These numbers are unique for all trace sessions on the computer.</p>
<p>By default, trace messages do not have any sequence numbers.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x8000</p></td>
<td align="left"><p>EVENT_TRACE_USE_LOCAL_SEQUENCE</p></td>
<td align="left"><p>Generates local sequence numbers for trace messages. These numbers are unique within the trace session.</p>
<p>By default, trace messages do not have any sequence numbers.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x10000</p></td>
<td align="left"><p>EVENT_TRACE_RELOG_MODE</p></td>
<td align="left"><p>For internal use only.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x80000</p></td>
<td align="left"><p>EVENT_TRACE_KD_FILTER_MODE</p></td>
<td align="left"><p>Redirects the trace messages to the kernel debugger and sets the trace buffer size to 3 KB, the maximum buffer size for the debugger.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x1000000</p></td>
<td align="left"><p>EVENT_TRACE_MODE_RESERVED</p></td>
<td align="left"><p>Not valid for a Global Logger trace session.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x01000000</p></td>
<td align="left"><p>EVENT_TRACE_USE_PAGED_MEMORY</p></td>
<td align="left"><p>Allocate trace session buffers from pageable memory. By default, the buffers are allocated from nonpageable memory.</p></td>
</tr>
</tbody>
</table>
 





