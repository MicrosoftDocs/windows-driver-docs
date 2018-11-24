---
title: Log Session Parameter Options
description: Log Session Parameter Options
ms.assetid: 5398dfa7-abeb-443b-ab64-73b6599c8e73
keywords:
- trace sessions WDK , advanced options
- trace sessions WDK , log session parameter options
- log session parameter options WDK
- trace flags WDK
- flags WDK software tracing
- flush time WDK software tracing
- buffers WDK software tracing
- decay time WDK software tracing
- circular buffers WDK software tracing
- global sequence numbers WDK software tracing
- trace levels WDK
- levels WDK software tracing
- WinDbg WDK software tracing
- virtual files WDK software tracing
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Log Session Parameter Options


In the **Log Session Parameter Options** tab, you can specify the values of variable features of a trace session.

You can set and change the values of the following options while creating a trace session. Several options can be changed while a trace session is running. The options that you cannot change appear dimmed ("greyed out") in the **Log Session Parameter Options** dialog box.

<span id="Flags"></span><span id="flags"></span><span id="FLAGS"></span>**Flags**  
Specifies the [trace flags](trace-flags.md) for the trace provider. Trace flags determine which trace messages the provider generates. The meaning of the flags are determined independently by each provider.

If TraceView can find a [trace message control (.tmc) file](trace-message-control-file.md) for the provider, you can select flags and a level from a list displayed in the **Tracing Flags and Level Selection** dialog box. To open the **Tracing Flags and Level Selection** dialog box, click the **SET** value of the **Flags** or **Level** option in the **Log Session Parameter Options** dialog box.

<span id="Flush_Time__S_"></span><span id="flush_time__s_"></span><span id="FLUSH_TIME__S_"></span>**Flush Time (S)**  
Specifies how often (in seconds) the trace session buffers are flushed to a trace log or the TraceView display. The default is 1 (second).

These forced flushes occur in addition to the flushes that happen automatically when a buffer is full. A value of 0 means no forced flushes.

To flush more frequently than once per second, use the **Buffer Size** option to reduce the size of each buffer.

You can change the **Flush Time** value while the trace session is running.

<span id="Maximum_Buffers"></span><span id="maximum_buffers"></span><span id="MAXIMUM_BUFFERS"></span>**Maximum Buffers**  
Specifies the maximum number of buffers that are allocated for the trace session.

The default value is determined by the number of processors, the amount of physical memory, and the operating system that you are using. You can change this value while the trace session is running.

<span id="Minimum_Buffers"></span><span id="minimum_buffers"></span><span id="MINIMUM_BUFFERS"></span>**Minimum Buffers**  
Specifies the number of buffers that are initially allocated for storing trace messages.

When the buffers are full, more buffers are allocated until the number of buffers reaches the value specified in the **Maximum Buffers** option. The default value is determined by the number of processors, the amount of physical memory, and the operating system in use. You cannot change this value while the trace session is running.

<span id="Buffer_Size"></span><span id="buffer_size"></span><span id="BUFFER_SIZE"></span>**Buffer Size**  
Specifies the size, in kilobytes (KB), of each buffer that is allocated for the trace session. The default value is determined by the number of processors, the amount of physical memory, and the operating system in use. You cannot change this value while the trace session is running.

<span id="Decay_Time__Minutes_"></span><span id="decay_time__minutes_"></span><span id="DECAY_TIME__MINUTES_"></span>**Decay Time (Minutes)**  
Specifies how long (in minutes) unused trace buffers are kept before they are freed. The default value is 15. The value of this option is displayed in the **Age** column of the [Trace Session List](trace-session-list.md).

This parameter is valid only on Windows 2000. You cannot change this value while the trace session is running.

<span id="Circular_Buffer_Size__MB_"></span><span id="circular_buffer_size__mb_"></span><span id="CIRCULAR_BUFFER_SIZE__MB_"></span>**Circular Buffer Size (MB)**  
Specifies that the trace buffers be circular and specifies the maximum size (in MB) of each buffer.

When a circular buffer is full, new trace messages are written to the beginning of the buffer, overwriting the oldest trace messages. By default, trace buffers are sequential, not circular.

You cannot change this value while the trace session is running.

<span id="Sequential_Buffer_Size__MB_"></span><span id="sequential_buffer_size__mb_"></span><span id="SEQUENTIAL_BUFFER_SIZE__MB_"></span>**Sequential Buffer Size (MB)**  
Specifies whether the trace buffers are sequential and specifies the maximum size (in MB) of each buffer.

When a sequential buffer is full, trace messages are written to another buffer or are lost. By default, trace buffers are sequential, not circular, and are 200 MB each.

You cannot change this value while the trace session is running.

<span id="Start_New_File_After_Buffer_Size__MB_"></span><span id="start_new_file_after_buffer_size__mb_"></span><span id="START_NEW_FILE_AFTER_BUFFER_SIZE__MB_"></span>**Start New File After Buffer Size (MB)**  
Creates a new trace log file (.etl) whenever the existing log reaches the specified value. The value specifies the maximum size of each log file in MB.

The value of this option is displayed in the **New File** column of the [Trace Session List](trace-session-list.md).

This option is effective only when the provider is generating trace logs, that is, when you have selected the [Log Trace Event Data to File option](basic-trace-session-options.md) on the **Log Session Options** page. This option has no effect on circular buffers or on logs from an [NT Kernel Logger trace session](nt-kernel-logger-trace-session.md). It is not supported on Windows 2000.

<span id="Use_Global_Sequence_Numbers"></span><span id="use_global_sequence_numbers"></span><span id="USE_GLOBAL_SEQUENCE_NUMBERS"></span>**Use Global Sequence Numbers**  
Generates a global sequence number for each trace message.

Global sequence numbers are unique for all trace sessions on the computer. The default value of this option is **FALSE**.

This option is not supported on Windows 2000 and has no effect on logs from an [NT Kernel Logger trace session](nt-kernel-logger-trace-session.md).

<span id="Use_Local_Sequence_Number"></span><span id="use_local_sequence_number"></span><span id="USE_LOCAL_SEQUENCE_NUMBER"></span>**Use Local Sequence Number**  
Generates a local sequence number for each trace message. The default value is **TRUE**.

Local sequence numbers are unique within a trace session.

This option is not supported on Windows 2000 and has no effect on logs from an [NT Kernel Logger trace session](nt-kernel-logger-trace-session.md).

<span id="Level"></span><span id="level"></span><span id="LEVEL"></span>**Level**  
Specifies a [trace level](trace-level.md) for the trace provider. The trace level determines which trace messages the provider generates. The meaning of the level value is determined independently by each provider. Typically, it represents increasing levels of detail.

If TraceView can find a [trace message control (.tmc) file](trace-message-control-file.md) for the provider, you can select flags and a level from a list displayed in the **Tracing Flags and Level Selection** dialog box. To open the **Tracing Flags and Level Selection** dialog box, click the **SET** value of the **Flags** or **Level** option in the **Log Session Parameter Options** dialog box.

For more information about trace levels, see the description of the *EnableLevel* parameter of the **EnableTrace** function in the Microsoft Windows SDK.

<span id="WinDbg"></span><span id="windbg"></span><span id="WINDBG"></span>**WinDbg**  
Redirects trace messages to KD or WinDbg, whichever is enabled, in addition to displaying them in the TraceView window. This option also sets the buffer size to 3 KB, the maximum size that is permitted by WinDbg. The value that is displayed for the **Buffer Size** option is ignored.

To display trace messages in a debugger, wmitrace.dll and traceprt.dll must be in the debugger's search path on the host computer. These DLLs are included in [Debugging Tools for Windows](http://go.microsoft.com/fwlink/p/?linkid=8708) Also, to enable the debugger to find the [trace message format (.tmf) files](trace-message-format-file.md) for the trace messages, the TMF files must be in the debugger's search path on the host computer. To set the debugger's search path, use the !wmitrace.searchpath specialized debugger extension or set the value of the %TRACE\_FORMAT\_SEARCH\_PATH% environment variable. For information about WinDbg and WMI Tracing Extensions, see Debugging Tools for Windows.

<span id="Ignore_TraceView"></span><span id="ignore_traceview"></span><span id="IGNORE_TRACEVIEW"></span>**Ignore TraceView**  
Suppresses trace messages that result from TraceView operations.

<span id="Virtual_File_Size"></span><span id="virtual_file_size"></span><span id="VIRTUAL_FILE_SIZE"></span>**Virtual File Size**  
Indicates the maximum number of trace messages that TraceView stores before it begins overwriting the oldest messages to make room for newer messages.

A value of **0** means that there is no maximum value. TraceView retains all messages and never overwrites them. The default value of this option, **65536**, is the value recommended for most systems. Larger values might cause significant delays.

This value appears in the **Max Trace Records** column of the [Trace Session List](trace-session-list.md).

 

 





