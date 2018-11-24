---
title: Trace Session List Columns
description: Trace Session List Columns
ms.assetid: 2e9d7636-3cff-459c-827a-719062bb778c
keywords:
- Trace Session List WDK
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Trace Session List Columns


The columns in the [Trace Session List](trace-session-list.md) represent properties of the trace session and its trace providers. You can set most of these properties in the [Log Session Parameter Options](log-session-parameter-options.md) tab of the **Advanced Log Session Options** dialog box when you create a trace session. For more information about the options in the **Log Session Parameter Options** tab, see [Setting Advanced Trace Session Options](setting-advanced-trace-session-options.md).

Properties that can be changed while a trace session is running appear in black text to show that they are available. Properties that can be changed only when the trace session is stopped appear dimmed. The properties of trace messages in trace logs cannot be changed. For more information, see [Changing the Properties of a Trace Session](changing-the-properties-of-a-trace-session.md).

The following list describes all of the columns in the Trace Session List, including those that are hidden by default. To learn how to display hidden columns, see "Hiding and Displaying Columns" in [Trace Session List Features](trace-session-list-features.md).

<span id="Group_ID___Session_Name"></span><span id="group_id___session_name"></span><span id="GROUP_ID___SESSION_NAME"></span>**Group ID / Session Name**  
Displays the group ID and the session name. You cannot hide this column.

**Group ID** is an identifier that TraceView assigns to trace sessions. When you combine trace sessions in a trace session group, TraceView reassigns a single identifier to the group. The value of **Group ID** also appears in the window frame of each [Trace Message List](trace-message-lists.md) for the session to help you associate the trace session with its trace messages.

**Session Name** is the name that you assigned to the trace session when you created it. For trace logs, because the name of the trace session is not saved in the log, TraceView displays a default session name. You cannot hide this column

<span id="State"></span><span id="state"></span><span id="STATE"></span>**State**  
Displays the status of the trace session. Valid values for this column are RUNNING, EXISTING, STOPPING, STOPPED, GROUPING, GROUPED, and UNGROUPING.

<span id="Event_Count"></span><span id="event_count"></span><span id="EVENT_COUNT"></span>**Event Count**  
For real-time trace sessions, this column displays the number of trace messages that TraceView received since the session started. For trace logs, this column displays the number of trace messages in the log.

<span id="Lost_Events"></span><span id="lost_events"></span><span id="LOST_EVENTS"></span>**Lost Events**  
Displays the number of events that were lost since the session started. Typically, events are lost because the trace session ran out of space in its buffers.

<span id="Buffers_Read"></span><span id="buffers_read"></span><span id="BUFFERS_READ"></span>**Buffers Read**  
Specifies the number of buffers from which TraceView received trace messages. For an existing trace log, this column displays the number of buffers that were used in the trace session.

<span id="Flags"></span><span id="flags"></span><span id="FLAGS"></span>**Flags**  
Specifies the [trace flags](trace-flags.md) for the trace provider. Trace flags determine which trace messages the provider generates. The meaning of the flags are determined independently by each provider.

If TraceView can find a [trace message control (.tmc) file](trace-message-control-file.md) for the provider, you can select flags and a level from a list that is displayed in the **Tracing Flags and Level Selection** dialog box. To open this dialog box, click the **SET** value of the **Flags** or **Level** column in the Tracing Session List.

<span id="Flush_Time"></span><span id="flush_time"></span><span id="FLUSH_TIME"></span>**Flush Time**  
Specifies how often (in seconds) the trace session buffers are flushed (sent to a trace log or the TraceView display). The default value is 1 (second).

These forced flushes occur in addition to the flushes that happen automatically when a buffer is full and when the trace session stops. A value of 0 in this column indicates that no forced flushes are performed.

You can change this value while the trace session is running.

<span id="Max_Buf"></span><span id="max_buf"></span><span id="MAX_BUF"></span>**Max Buf**  
Specifies the maximum number of buffers that are allocated for the trace session

The default value is determined by the number of processors, the amount of physical memory, and the operating system in use. You can change this value while the trace session is running.

<span id="Min_Buf"></span><span id="min_buf"></span><span id="MIN_BUF"></span>**Min Buf**  
Specifies the number of buffers that are initially allocated for storing trace messages.

When the buffers are full, more buffers are allocated until it reaches the value that is specified in the **Max Buf** column. The default value for **Min Buf** is determined by the number of processors, the amount of physical memory, and the operating system in use. You cannot change this value while the trace session is running.

<span id="Buf_Size"></span><span id="buf_size"></span><span id="BUF_SIZE"></span>**Buf Size**  
Specifies the size, in kilobytes (KB), of each buffer that is allocated for the trace session. The default value is determined by the number of processors, the amount of physical memory, and the operating system in use. You cannot change this value while the trace session is running.

<span id="Age"></span><span id="age"></span><span id="AGE"></span>**Age**  
Specifies how long (in minutes) unused trace buffers are kept before they are freed. The default value is 15 minutes. This value is set in the **Decay Time** field of the [Log Session Parameter Options](log-session-parameter-options.md) tab in the **Advanced Log Session Options** dialog box.

This value is used only on Windows 2000. You cannot change this value while the trace session is running.

<span id="Circular"></span><span id="circular"></span><span id="CIRCULAR"></span>**Circular**  
Specifies that the trace buffers be circular and specifies the maximum size (in MB) of each buffer.

When a circular buffer is full, new trace message are written to the beginning of the buffer, overwriting the oldest trace messages. By default, trace buffers are sequential, not circular.

You cannot change this value while the trace session is running.

<span id="Sequential"></span><span id="sequential"></span><span id="SEQUENTIAL"></span>**Sequential**  
Specifies that the trace buffers be sequential and specifies the maximum size (in MB) of each buffer.

When a sequential buffer is full, trace messages are written to another buffer or are lost. By default, trace buffers are sequential, not circular, and are 200 MB each.

You cannot change this value while the trace session is running.

<span id="New_File"></span><span id="new_file"></span><span id="NEW_FILE"></span>**New File**  
Creates a new trace log (.etl) whenever the existing log reaches the specified value. The value specifies the maximum size of each log file in megabytes (MB). This value is set in the **Start New File After Buffer Size** field of the [Log Session Parameter Options](log-session-parameter-options.md) tab in the **Advanced Log Session Options** dialog box.

This value is effective only when the provider is generating trace logs, that is, when you have selected the [Log Trace Event Data to File option](basic-trace-session-options.md) on the **Log Session Options** page. This option has no effect on circular buffers or on logs from an [NT Kernel Logger trace session](nt-kernel-logger-trace-session.md). It is not supported on Windows 2000.

<span id="Global_Seq"></span><span id="global_seq"></span><span id="GLOBAL_SEQ"></span>**Global Seq**  
Generates a global sequence number for each trace message.

Global sequence numbers are unique for all trace sessions on the computer. The default value is **FALSE**.

This parameter is not supported on Windows 2000 and has no effect on logs from an [NT Kernel Logger trace session](nt-kernel-logger-trace-session.md).

<span id="Local_Seq"></span><span id="local_seq"></span><span id="LOCAL_SEQ"></span>**Local Seq**  
Generates a local sequence number for each trace message. The default value is **TRUE**.

Local sequence numbers are unique within a trace session.

This parameter is not supported on Windows 2000 and has no effect on logs from an [NT Kernel Logger trace session](nt-kernel-logger-trace-session.md).

<span id="Level"></span><span id="level"></span><span id="LEVEL"></span>**Level**  
Specifies the [trace level](trace-level.md) for the trace provider. The trace level determines which trace messages the provider generates. The meaning of the level value is determined independently by each provider. Typically, it represents increasing levels of detail.

If TraceView can find a [trace message control (.tmc) file](trace-message-control-file.md) for the provider, you can select flags and a level from a list that is displayed in the **Tracing Flags and Level Selection** dialog box. To open this dialog box, click the **SET** value of the **Flags** or **Level** column in the Trace Session List.

For more information about trace levels, see the description of the *EnableLevel* parameter of the **EnableTrace** function in the Microsoft Windows SDK documentation.

<span id="WinDbg"></span><span id="windbg"></span><span id="WINDBG"></span>**WinDbg**  
Redirects trace messages to KD or WinDbg, whichever is enabled, in addition to displaying them in the TraceView window. This option also sets the buffer size to 3 KB, the maximum size that is permitted by WinDbg. The value that is displayed in the **Buf Size** column is ignored.

To display trace messages in any debugger, wmitrace.dll and traceprt.dll must be in the debugger's search path on the host computer. Also, to enable the debugger to find the trace message format files for the trace messages, you must use the **!wmitrace.searthpath** specialized debugger extension or set the value of the %TRACE\_FORMAT\_SEARCH\_PATH% environment variable. For information about WinDbg and WMI Tracing Extensions, see Debugging Tools for Windows.

<span id="Ignore_Traceview"></span><span id="ignore_traceview"></span><span id="IGNORE_TRACEVIEW"></span>**Ignore Traceview**  
Suppresses trace messages that are related to TraceView actions.

<span id="Max_Trace_Records"></span><span id="max_trace_records"></span><span id="MAX_TRACE_RECORDS"></span>**Max Trace Records**  
Indicates the maximum number of trace messages that TraceView stores before it begins overwriting the oldest messages to make room for newer messages.

A value of **0** means that there is no maximum value and that TraceView retains all messages and never overwrites them. The default value is **65536**, the value that is recommended for most systems. Larger values might cause significant delays.

This value is set in the **Virtual File Size** field of the [Log Session Parameter Options](log-session-parameter-options.md) tab in the **Advanced Log Session Options** dialog box.

<span id="Log_File_Name"></span><span id="log_file_name"></span><span id="LOG_FILE_NAME"></span>**Log File Name**  
Displays the name and location of the event trace log (.etl) file. For a real-time trace session, this column displays the name of the trace log to which trace messages are being written. For an existing log file, it displays the name of the trace log from which messages are being read.

<span id="Save_As_Default"></span><span id="save_as_default"></span><span id="SAVE_AS_DEFAULT"></span>**Save As Default**  
This option is not a column name. It is a command that saves the currently displayed column configuration as the default for future trace sessions. For more information, see "Saving the Column Configuration" in [Trace Session List Features](trace-session-list-features.md).

 

 





