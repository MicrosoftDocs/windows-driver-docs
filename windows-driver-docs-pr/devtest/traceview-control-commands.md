---
title: TraceView Control Commands
description: Use a Traceview control command to manage trace sessions.
keywords:
- TraceView Control Commands Driver Development Tools
topic_type:
- apiref
api_name:
- TraceView Control Commands
api_type:
- NA
ms.date: 12/17/2018
---

# TraceView Control Commands

> [!NOTE]
> The TraceView command line options are deprecated. Use tracepdb.exe and tracefmt.exe to parse PDBs into TMF files and parse .etl files into text, respectively.content

Use a Traceview control command to manage trace sessions, including starting and stopping the session, enabling and disabling providers, updating the properties of the trace session, and flushing trace buffers.

```command
    traceview {-start | -stop | -update | -enable | -disable | -flush | -q} SessionName [Parameters]
```

```command
    traceview {-enumguid | -l | -h | -x}
```

## Command Parameters

### Actions

|Action|Description|
|----|----|
|**-start**|Starts the specified trace session.|
|**-stop**|Stops the specified trace session.|
|**-update**|Updates the properties for the specified trace session.|
|**-enable**|Enables providers for the specified trace session.|
|**-disable**|Disables providers for the specified session.|
|**-flush**|Flushes the active buffers of the specified trace session. This forced flush is in addition to the automatic flushes that occur when a buffer is full and when the trace session stops.|
|**-q**|Query the status of the specified trace session.|
|**-enumguid**|Lists providers on the system that are [registered](registered-provider.md) with Event Tracing for Windows (ETW).|
|**-l**|List all trace sessions running on the computer.|
|**-x**|Stops all trace sessions.|

### <span id="parameters"></span><span id="PARAMETERS"></span>Parameters

<span id="_______SessionName______"></span><span id="_______sessionname______"></span><span id="_______SESSIONNAME______"></span> *SessionName*   
When used with **-start**, *SessionName* is a name that you select to represent the trace session. With all other commands, *SessionName* identifies the trace session.

<span id="_______-f___LogFile_"></span><span id="_______-f___logfile_"></span><span id="_______-F___LOGFILE_"></span> **-f** \[*LogFile*\]  
When used with **-start**, **-f** starts a trace log sessions. *LogFile* specifies the path (optional) and file name of the event trace log (.etl) file. The default is C:\\LogFile.etl.

When used with **-update**, **-f** sends all new trace messages only to the specified [trace log](trace-log.md). Use this parameter to convert a real-time trace session to a trace log session or to start a new trace log for an existing trace log session. To send trace messages to a real-time trace consumer and to a trace log, use both the **-rt** and **-f** parameters in the **-update** command.

<span id="_______-rt______"></span><span id="_______-RT______"></span> **-rt**   
When used with **-start**, **-rt** starts a real-time trace sessions (A trace log session (**-f**) is the default.) If you use **-rt** and **-f** in a **-start** command, the trace messages are sent to the trace consumer and to an event trace log file.

When used with **-update**, **-rt** adds real-time message delivery to a trace log session. All new trace messages are sent directly to the trace consumer (as in a real-time trace session), in addition to a [trace log](trace-log.md).

<span id="_______-guid___GUID___GUIDFile_"></span><span id="_______-guid___guid___guidfile_"></span><span id="_______-GUID___GUID___GUIDFILE_"></span> **-guid** {**\#**<em>GUID</em> | *GUIDFile*}  
Specifies one or more trace providers. Use with **-start** to enable providers for a trace session. Use with **-enable** to enable the providers or to change their **-flag** or **-level** values. Use with **-disable** to specify the providers to disable.

*GUID* can specify either one [control GUID](control-guid.md) (preceded by a number sign (**\#**)) or the path (optional) and file name of a text file, such as a control GUID (.ctl) file, that contains the control GUIDs of one or more trace providers.

If you omit the **-guid** parameter from a **-start** command, TraceView starts an [NT Kernel Logger trace session](nt-kernel-logger-trace-session.md).

TraceView passes the values of the following subparameters to the specified providers.

<table>
<thead>
<tr>
<th>Parameter</th>
<th>Description</th>
</tr>
<tbody>
<tr>
<td><em>SessionName</em></td>
<td>When used with <strong>-start</strong>, <em>SessionName</em> is a name that you select to represent the trace session. With all other commands, <em>SessionName</em> identifies the trace session.</td>
</tr>
<tr>
<td><strong>-f</strong> \[<em>LogFile</em>\]</td>
<td><p>When used with <strong>-start</strong>, <strong>-f</strong> starts a trace log sessions. <em>LogFile</em> specifies the path (optional) and file name of the event trace log (.etl) file. The default is C:\\LogFile.etl.</p>
<p>When used with <strong>-update</strong>, <strong>-f</strong> sends all new trace messages only to the specified [trace log](trace-log.md). Use this parameter to convert a real-time trace session to a trace log session or to start a new trace log for an existing trace log session. To send trace messages to a real-time trace consumer and to a trace log, use both the <strong>-rt</strong> and <strong>-f</strong> parameters in the <strong>-update</strong> command.</p>
</td>
</tr>
<tr>
<td><strong>-rt</strong></td>
<td><p>When used with <strong>-start</strong>, <strong>-rt</strong> starts a real-time trace sessions (A trace log session (<strong>-f</strong>) is the default.) If you use <strong>-rt</strong> and <strong>-f</strong> in a <strong>-start</strong> command, the trace messages are sent to the trace consumer and to an event trace log file.</p>
<p>When used with <strong>-update</strong>, <strong>-rt</strong> adds real-time message delivery to a trace log session. All new trace messages are sent directly to the trace consumer (as in a real-time trace session), in addition to a [trace log](trace-log.md).</p>
</td>
</tr>
<tr>
<td><strong>-guid</strong> {<strong>\#</strong><em>GUID</em> | <em>GUIDFile</em>}</td>
<td><p>Specifies one or more trace providers. Use with <strong>-start</strong> to enable providers for a trace session. Use with <strong>-enable</strong> to enable the providers or to change their <strong>-flag</strong> or <strong>-level</strong> values. Use with <strong>-disable</strong> to specify the providers to disable.</p>
<p><em>GUID</em> can specify either one [control GUID](control-guid.md) (preceded by a number sign (<strong>\#</strong>)) or the path (optional) and file name of a text file, such as a control GUID (.ctl) file, that contains the control GUIDs of one or more trace providers.</p>
<p>If you omit the <strong>-guid</strong> parameter from a <strong>-start</strong> command, TraceView starts an [NT Kernel Logger trace session](nt-kernel-logger-trace-session.md).</p>
</td>
</tr>
</tbody>
</table>

TraceView passes the values of the following subparameters to the specified provider:

<table>
<thead>
<tr>
<th>Subparameters of -guid</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><p><strong>-flag</strong> <em>Flag</em></p></td>

<span id="_______-b_______BufferSize______"></span><span id="_______-b_______buffersize______"></span><span id="_______-B_______BUFFERSIZE______"></span> **-b** *BufferSize*   
Specifies the size, in KB, of each buffer allocated for the trace session. Use only with **-start**.

The default value is determined by the number of processors, the amount of physical memory, and the operating system in use.

<span id="_______-min_______NumberOfBuffers______"></span><span id="_______-min_______numberofbuffers______"></span><span id="_______-MIN_______NUMBEROFBUFFERS______"></span> **-min** *NumberOfBuffers*   
Specifies the number of buffers initially allocated for storing trace messages. Use only with **-start**.

The default value is determined by the number of processors, the amount of physical memory, and the operating system in use.

<span id="_______-max_______NumberOfBuffers______"></span><span id="_______-max_______numberofbuffers______"></span><span id="_______-MAX_______NUMBEROFBUFFERS______"></span> **-max** *NumberOfBuffers*   
When used with **-start**, **-max** specifies the maximum number of buffers allocated for the trace session. The default value is determined by the number of processors, the amount of physical memory, and the operating system in use.

When used with **-update**, **-max** changes the maximum number of buffers allocated for the trace session.

<span id="_______-ft_______FlushTime______"></span><span id="_______-ft_______flushtime______"></span><span id="_______-FT_______FLUSHTIME______"></span> **-ft** *FlushTime*   
When used with **-start**, **-ft** specifies how often, in seconds, the trace message buffers are flushed. When used with **-update**, **-ft** changes the flush time to the specified time.

The minimum flush time is 1 second. The default value is 0 (no forced flush).

This forced flush is in addition to the flushes that happen automatically whenever a trace message buffer is full and when a trace session stops.

See also: **-flush**.

<span id="_______-paged______"></span><span id="_______-PAGED______"></span> **-paged**   
Uses pageable memory for the trace message buffers. By default, event tracing uses nonpageable memory for buffers. Use only with **-start**.

Do not use this parameter when the provider is a driver that might generate trace messages at an IRQL greater than DISPATCH\_LEVEL.

This parameter is not supported in Windows 2000.

<span id="_______-seq_______MaxFileSize______"></span><span id="_______-seq_______maxfilesize______"></span><span id="_______-SEQ_______MAXFILESIZE______"></span> **-seq** *MaxFileSize*   
Specifies sequential logging (at end-of-file, stop recording events) to the event trace log (.etl) file. Use only with **-start**.

*MaxFileSize* specifies the maximum size of the file in MB. Without a *MaxFileSize* value, this parameter is ignored.

Sequential logging is the default, but you can use this parameter to set the maximum file size or to use **-prealloc**. Without this parameter, there is no file size limit.

<span id="_______-cir_______MaxFileSize______"></span><span id="_______-cir_______maxfilesize______"></span><span id="_______-CIR_______MAXFILESIZE______"></span> **-cir** *MaxFileSize*   
Specifies circular logging (at end-of-file, record new messages over the oldest messages) in the event trace log (.etl) file. Use only with **-start**.

*MaxFileSize* specifies the maximum size of the file in MB. Without a *MaxFileSize* value, this parameter is ignored.

The default is sequential logging with no file size limit.

<span id="_______-prealloc______"></span><span id="_______-PREALLOC______"></span> **-prealloc**   
Reserves space for the event trace log (.etl) file before allocating it. Use only with **-start**.

This parameter requires **-seq** or **-cir** with *MaxFileSize*. It is not valid with **-newfile**.

<p><em>Flag</em> represents a flag value defined in the trace provider, in decimal or hexadecimal format. The default value is 0. Values from 0x01000000 through 0xFF000000 are reserved for future use.</p>

<p>The meaning of the flags is defined independently by each trace provider. Typically, flags represent increasingly detailed reporting levels.</p>

<p>In a <strong>-start</strong> command, the flags value applies to all trace providers in the trace session. To set different flags for each trace provider, use a separate <strong>-enable</strong> command for each trace provider.</p>
</td>
</tr>

<tr>
<td>
<p><strong>-level</strong> <em>Level</em></p>
</td>
<td>
<p>Specifies the <a href="trace-level.md" data-raw-source="[trace level](trace-level.md)">trace level</a> for the providers in the trace session. The level determines which events the trace provider generates.</p>

<p><em>Level</em> represents a level value in decimal or hexadecimal format. The default value is 0.</p>

<p>The meaning of the level value is defined independently by each trace provider. Typically, the trace level represents the severity of the event (information, warning, or error).</p>

<p>In a <strong>-start</strong> command, the level value applies to all trace providers in the trace session. To set different levels for each trace provider, use a separate <strong>-enable</strong> command for each trace provider.</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>Parameter</tr>
<tr>Description</tr>
</thead>
<tbody>
<tr>
<td><strong>-b</strong> <em>BufferSize</em></td>
<td>Specifies the size, in KB, of each buffer allocated for the trace session. Use only with <strong>-start</strong>.
<p>The default value is determined by the number of processors, the amount of physical memory, and the operating system in use.</p></td>
</tr>
<tr>
<td><strong>-min</strong> <em>NumberOfBuffers</em></td>
<td>Specifies the number of buffers initially allocated for storing trace messages. Use only with <strong>-start</strong>.
<p>The default value is determined by the number of processors, the amount of physical memory, and the operating system in use.</p></td>
</tr>
<tr>
<td><strong>-max</strong> <em>NumberOfBuffers</em></td>
<td>When used with <strong>-start</strong>, <strong>-max</strong> specifies the maximum number of buffers allocated for the trace session. The default value is determined by the number of processors, the amount of physical memory, and the operating system in use.
<p>When used with <strong>-update</strong>, <strong>-max</strong> changes the maximum number of buffers allocated for the trace session.</p></td>
</tr>
<tr>
<td><strong>-ft</strong> <em>FlushTime</em></td>
<td>When used with <strong>-start</strong>, <strong>-ft</strong> specifies how often, in seconds, the trace message buffers are flushed. When used with <strong>-update</strong>, <strong>-ft</strong> changes the flush time to the specified time.
<p>The minimum flush time is 1 second. The default value is 0 (no forced flush).</p>
<p>This forced flush is in addition to the flushes that happen automatically whenever a trace message buffer is full and when a trace session stops.</p>
<p>See also: <strong>-flush</strong>.</p></td>
</tr>
<tr>
<td><strong>-age</strong> <em>AgeLimit</em></td>
<td>When used with <strong>-start</strong>, <strong>-age<strong> specifies how long (in minutes) unused trace buffers are kept before they are freed. When used with <strong>-update<strong>, <strong>-age<strong> changes the age limit to the specified value.
<p><em>Age Limit</em> specifies how long (in minutes) unused trace buffers are kept before they are freed. The default is 15 minutes.</p>
<p>This parameter is valid only in Windows 2000.</p></td>
</tr>
<tr>
<td><strong>-paged</strong></td>
<td>Uses pageable memory for the trace message buffers. By default, event tracing uses nonpageable memory for buffers. Use only with <strong>-start</strong>.
<p>Do not use this parameter when the provider is a driver that might generate trace messages at an IRQL greater than DISPATCH\_LEVEL.</p>
<p>This parameter is not supported in Windows 2000.</p></td>
</tr>
<tr>
<td><strong>-seq</strong> <em>MaxFileSize</em></td>
<td>Specifies sequential logging (at end-of-file, stop recording events) to the event trace log (.etl) file. Use only with <strong>-start</strong>.
<p><em>MaxFileSize</em> specifies the maximum size of the file in MB. Without a <em>MaxFileSize</em> value, this parameter is ignored.</p>
<p>Sequential logging is the default, but you can use this parameter to set the maximum file size or to use <strong>-prealloc</strong>. Without this parameter, there is no file size limit.</p></td>
</tr>
<tr>
<td><strong>-cir</strong> <em>MaxFileSize</em></td>
<td>Specifies circular logging (at end-of-file, record new messages over the oldest messages) in the event trace log (.etl) file. Use only with <strong>-start</strong>.
<p><em>MaxFileSize</em> specifies the maximum size of the file in MB. Without a <em>MaxFileSize</em> value, this parameter is ignored.</p>
<p>The default is sequential logging with no file size limit.</p></td>
</tr>
<tr>
<td><strong>-prealloc</strong></td>
<td>Reserves space for the event trace log (.etl) file before allocating it. Use only with <strong>-start</strong>.
<p>This parameter requires <strong>-seq</strong> or <strong>-cir</strong> with <em>MaxFileSize</em>. It is not valid with <strong>-newfile</strong>.</p>
<p>The system creates the event trace log (.etl) file with a size equal to the <em>MaxFileSize</em> value specified by using the <strong>-seq</strong> or <strong>-cir</strong> parameters. When you stop the session, it reduces the log file to the size of its contents.</p></td>
</tr>
<tr>
<td><strong>-newfile</strong> <em>MaxFileSize</em></td>
<td>Creates a new event trace log (.etl) file whenever the existing file reaches <em>MaxFileSize</em>. Use only with <strong>-start</strong>.
<p><em>MaxFileSize</em> specifies the maximum size of each log file in MB. Without a <em>MaxFileSize</em> value, this parameter is ignored.</p>
<p>When using <strong>-newfile</strong>, you must also use the <strong>-f</strong> <em>LogFile</em> parameter, and the value of <em>LogFile</em> must be a name that includes the characters <strong>%d</strong> indicate a decimal pattern--for example, trace%d.etl. Otherwise, the command fails with ERROR\_INVALID\_NAME. Windows increments the decimal value in the file name each time it creates a new file.</p>
<p>This parameter is not valid with preallocation (<strong>-prealloc</strong> logging (<strong>-cir</strong>), with the NT Kernel Logger session, or for private trace sessions. It is not supported in Windows 2000.</p></td>
</tr>
<tr>
<td><strong>-append</strong></td>
<td>Appends the trace messages to an existing event trace log (.etl) file. The default is to create a new file. Use only with <strong>-start</strong>.
<p>This parameter is valid only on sequential files and only when <strong>-f</strong> is used and <strong>-rt</strong> is not used. It is not supported in Windows 2000.</p></td>
</tr>
<tr>
<td><strong>-kd</strong></td>
<td>Redirects the trace messages to KD or Windbg, whichever is attached. This parameter also sets the trace buffer size to 3 KB, the maximum buffer size for the debugger, and ignores any <strong>-b</strong> parameters in the command. Use only with <strong>-start</strong>.</td>
</tr>
</tbody>
</table>

### Comments

A **traceview** command with no parameters opens the TraceView window.

You can use the TraceView -start command to start a [Global Logger trace session](global-logger-trace-session.md). To do so, use the following command format. Unlike other commands, the word "GlobalLogger" in this command format is case sensitive.

```command
traceview -start GlobalLogger [parameters]
```
