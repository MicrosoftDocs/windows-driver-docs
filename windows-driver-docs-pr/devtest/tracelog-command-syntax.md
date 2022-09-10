---
title: Tracelog Command Syntax
description: Tracelog has commands (or actions) that start, stop, and control a trace session.
keywords:
- Tracelog Command Syntax Driver Development Tools
topic_type:
- apiref
api_name:
- Tracelog Command Syntax
api_type:
- NA
ms.date: 04/20/2017
---

# Tracelog Command Syntax


Tracelog has commands (or actions) that start, stop, and control a [trace session](trace-session.md).

> [!NOTE]
> To control a trace session you must be a member of the Performance Log Users group or the Administrators group on the computer (**Run as administrator**).

```
    tracelog [actions] [options] | [-h | -help | -?] 
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters

For information about the Tracelog parameters, see \[[*actions*](#actions)\] \[[*options*](#options)\].

### \[*actions*\]

<span id="_______-addautologger__LoggerName_"></span><span id="_______-addautologger__loggername_"></span><span id="_______-ADDAUTOLOGGER__LOGGERNAME_"></span> **-addautologger** \[*LoggerName*\]  
Configures the registry entries for an autologger session. An autologger session is the preferred method for tracing the activity of a driver or other trace provider during system boot. You must specify the session GUID using the **-sessionguid** option. The **tracelog -addautologger** command takes the same options as the **Tracelog -start** command.

<span id="_______-capturestate__LoggerName_"></span><span id="_______-capturestate__loggername_"></span><span id="_______-CAPTURESTATE__LOGGERNAME_"></span> **-capturestate** \[*LoggerName*\]  
Requests all providers enabled to *LoggerName* to log state information. The keywords enabled help determine the kind of information that is logged.

<span id="_______-disable__LoggerName_"></span><span id="_______-disable__loggername_"></span><span id="_______-DISABLE__LOGGERNAME_"></span> **-disable** \[*LoggerName*\]  
Disables the specified trace providers. When a provider is disabled, it continues to run, but it stops generating trace messages.

The **tracelog -stop** command disables the trace providers before stopping the session. You do not need to disable providers before stopping a trace session. However, you can use the **tracelog -disable** command to disable selected providers without stopping a trace session.

Disabling stops the trace provider from sending trace messages to the trace session buffers, but it does not flush the buffers or stop the trace session. Use a **tracelog -flush** command to flush the buffers and a **tracelog -stop** or **tracelog -x** (stop all) command to stop the trace session.

Tracelog uses the **EnableTrace** function to implement a **tracelog -disable** command. For more information about this function, see the Microsoft Windows SDK documentation.

<span id="_______-enable__LoggerName_"></span><span id="_______-enable__loggername_"></span><span id="_______-ENABLE__LOGGERNAME_"></span> **-enable** \[*LoggerName*\]  
Enables one or more trace providers for the *LoggerName* trace session.

When you enable a provider, the provider generates trace messages and sends them to the buffers of a trace session. If the provider is not running (or is not loaded) when you enable it, the system *pre-registers* the provider, that is, it reserves space for the provider in the ETW registration database and saves the enable command. When the provider starts and actually registers, it receives the saved enable command and begins sending trace messages to the session.

The **tracelog -start** command enables any providers specified by the optional **-guid** parameter in the **tracelog -start** command. You do not need to submit a separate **tracelog -enable** command.

You can use a **tracelog -enable** command to add a provider to a running trace session, to change the flags and level for a provider while it is tracing, or to re-enable a provider that you disabled by using a **tracelog -disable** command.

When using the **tracelog -enable** command, first submit a **tracelog -start** command to start the trace session, and then submit the **tracelog -enable** command to enable the providers.

You can enable a running provider repeatedly without disabling it. (You might do this to change the flags and levels.)

The trace flags and trace level that you specify with the **-flag** and **-level** parameters are passed to all trace providers represented by the **-guid** parameter. To specify different flags and levels for each trace provider, submit a separate **tracelog -enable** command for each provider, with its own flag and level settings.

If you enable any of the NT Kernel Logger flags (such as **-noprocess**, **-nothread**, **-fio**, or **-cm**) while a Global Logger trace session is running, the Global Logger session is converted to an NT Kernel Logger trace session. This feature is designed to trace kernel events during the boot process.

<span id="_______-enableex__LoggerName_"></span><span id="_______-enableex__loggername_"></span><span id="_______-ENABLEEX__LOGGERNAME_"></span> **-enableex** \[*LoggerName*\]  
Identical to **-enable**. This option may be removed in future versions of Tracelog.

<span id="_______-enumguid______"></span><span id="_______-ENUMGUID______"></span> **-enumguid**   
Enumerates (or lists) providers on the system that are [registered](registered-provider.md) with Event Tracing for Windows (ETW). For a description of the Enumguid display, see [Tracelog Enumguid Display](tracelog-enumguid-display.md).

Tracelog uses the **EnumerateTraceGuids** function to implement a **tracelog -enumguid** command. For more information about this function, see the Microsoft Windows SDK documentation.

<span id="_______-enumguidex___guid_"></span><span id="_______-ENUMGUIDEX___GUID_"></span> **-enumguidex** \[**\#**<em>guid</em>\]  
Enumerates (or lists) providers on the system that are [registered](registered-provider.md) with Event Tracing for Windows (ETW). For a description of the EnumguidEx display, see [Tracelog Enumguid Display](tracelog-enumguid-display.md).

Tracelog uses the **EnumerateTraceGuidsEx** function to implement a **tracelog -enumguidex** command. For more information about this function, see the Microsoft Windows SDK documentation.

<span id="_______-flush___LoggerName__"></span><span id="_______-flush___loggername__"></span><span id="_______-FLUSH___LOGGERNAME__"></span> **-flush** \[*LoggerName*\]   
Flushes the active buffers of the *LoggerName* trace session. If *LoggerName* is not specified, Tracelog flushes the buffers of the [NT Kernel Logger trace session](nt-kernel-logger-trace-session.md).

This forced flush is in addition to the flushes that occur automatically whenever a trace message buffer is full and when the trace session stops, and in addition to the flushes that are activated by the flush timer (**-ft**).

When you flush the buffers of a trace session, the events in the buffers are delivered to the trace log or trace consumer immediately.

Flushing does not disable the trace provider or redirect the trace messages. After the buffers are flushed, the trace provider continues writing events to the buffers.

Tracelog uses the **FlushTrace** function to implement a **tracelog -flush** command. For more information about this function, see the Microsoft Windows SDK documentation.

You can use the **tracelog -flush** command with the **-f** *Logfile* option to flush the trace messages that are currently in the buffer to the specified [trace log](trace-log.md) (.etl) file. This parameter is valid only for buffered trace sessions (**-buffering**); for other trace session types, the **-f** parameter is ignored.

This flush affects only the current contents of the buffer. It does not redirect future trace messages to the trace log.

<span id="_______-l______"></span><span id="_______-L______"></span> **-l** \[*-lp*\]  
Lists the properties of all trace sessions running on the computer.

If you pass the **-lp** option, Tracelog will also list all the providers enabled to each session.

<span id="_______-q___LoggerName_"></span><span id="_______-q___loggername_"></span><span id="_______-Q___LOGGERNAME_"></span> **-q** \[*LoggerName*\] \[*-lp*\]  
Lists (queries) the properties of the specified trace session. If you do not specify *LoggerName*, Tracelog queries the [NT Kernel Logger trace session](nt-kernel-logger-trace-session.md).

If you pass the **-lp** option, Tracelog will also list all the providers enabled to the session.

<span id="_______-remove_GlobalLogger______"></span><span id="_______-remove_globallogger______"></span><span id="_______-REMOVE_GLOBALLOGGER______"></span> **-remove GlobalLogger**   
Removes and reinitializes the registry values for a Global Logger trace session. It sets the value of the Start entry to 0 (do not start) and deletes the other registry entries. The **tracelog -remove** command works only for Global Logger trace sessions. All other session name values are invalid.

The **tracelog -remove** command is not required. However, if you do not set the value of the **Start** entry to 0, a Global Logger session starts every time you reboot the system.

If you do not use a **tracelog -remove** command, the options from the previous session are still in the registry, and they will be used for the new session unless you submit a **tracelog -start** command with different values for the same options.

<span id="_______-start__LoggerName_"></span><span id="_______-start__loggername_"></span><span id="_______-START__LOGGERNAME_"></span> **-start** \[*LoggerName*\]  
Starts a trace session using the *LoggerName* that you select to represent the trace session.

Use **GlobalLogger** as the *LoggerName* to specify a [Global Logger Trace Session](global-logger-trace-session.md). The session starts when you restart the computer.

The *LoggerName* can be any name that meets Windows naming guidelines, up to 1,024 characters. If the name includes spaces, enclose the name in quotation marks. Tracelog is not case-sensitive.

The default is **"NT Kernel Logger"**. If you omit this parameter, Tracelog starts an [NT Kernel Logger trace session](nt-kernel-logger-trace-session.md) and declares an error if you use the **-guid** parameter to specify a different trace provider.

<span id="_______-stop__LoggerName_"></span><span id="_______-stop__loggername_"></span><span id="_______-STOP__LOGGERNAME_"></span> **-stop** \[*LoggerName*\]  
Disables the providers in the specified trace session and then terminates the session.

The **tracelog -stop** command both disables the trace providers and stops the trace session. A **tracelog -disable** command only disables the trace providers.

If you start a [Boot-Time Global Logger session](boot-time-global-logger-session.md) which traces kernel events, you need to use the command **tracelog -stop "NT Kernel Logger"** or **tracelog -stop GlobalLogger** to stop it. When you use either of commands to stop a [Global Logger trace session](global-logger-trace-session.md) trace session, Tracelog stops the provider, but it does not reset the values of the registry entries. To reset the values of the Global Logger registry entries, use **tracelog -remove**.

<span id="-systemrundown__LoggerName_"></span><span id="-systemrundown__loggername_"></span><span id="-SYSTEMRUNDOWN__LOGGERNAME_"></span>**-systemrundown** \[*LoggerName*\]  
Requests the SystemTraceProvider to log rundown events directed at *LoggerName* session. See [Configuring and Starting a SystemTraceProvider Session](/windows/desktop/ETW/configuring-and-starting-a-systemtraceprovider-session) for information about starting a trace session.

This command is only available on Windows 8 and later versions of Windows.

<span id="_______-timeout_______value______"></span><span id="_______-TIMEOUT_______VALUE______"></span> **-timeout** *value*   
Specifies the timeout value, in milliseconds (ms), to use when enabling providers with the **tracelog -enable** command. The default timeout is 0.

If the timeout value is 0, the Tracelog will call each provider's enable callback and return immediately, without waiting for the callback to complete.

To enable providers synchronously, specify a timeout value. If you specify a timeout value, Tracelog will wait until each provider's enable callback exits or the timeout expires.

When enabling multiple providers at once, the timeout is applied to each one sequentially.

<span id="_______-update_____LoggerName__"></span><span id="_______-update_____loggername__"></span><span id="_______-UPDATE_____LOGGERNAME__"></span> **-update** \[*LoggerName*\]   
The **tracelog -update** command changes the properties of a trace session while it is running.

In a **tracelog -update** command, the -**guid** parameter is valid only when updating a private trace session (**-um**).To add or remove providers from a standard trace session while the session is running, use the **tracelog -enable** and **tracelog -disable** commands.

If you start a trace log session (**-f**), you can update to a real-time session (**-rt**), but messages continue to be sent to the trace log in addition to the trace consumer. You cannot eliminate the log from the session by updating. However, before you can add real-time message delivery to a trace log session, you must first use the **tracelog -flush** command to flush the buffers.

If you start a real-time session (**-rt**) and then update to a trace log session (**-f**), new trace messages are no longer sent directly to the trace consumer; they are sent only to the trace log. To add a trace log to a real-time trace session, use both **-rt** and **-f** in the **tracelog -update** command. Before you can add real-time message delivery to a trace log session, you must first use the **tracelog -flush** command to flush the buffers.

You cannot update a [Global Logger trace session](global-logger-trace-session.md).

For a private (user-mode) trace session, you can update only the log file name (**-f**) and the flush timer value (**-ft**).

To update the flags and levels, use the **tracelog -enable** command to re-enable the provider with new flags or levels.

Tracelog uses the **ControlTrace** function to implement a **tracelog -update** command. For more information about this function, see the Microsoft Windows SDK documentation.

### \[*options*\]

<span id="_-addtotriagedump_______"></span><span id="_-ADDTOTRIAGEDUMP_______"></span> **-addtotriagedump**   
> [!NOTE]
> This option should not be used except when you might need to view events from a kernel dump using the debugger.

Specifies that any active buffers for the session are available to be added to a triage memory dump. Triage dumps are limited in size, and if the session's buffers cause the dump to exceed its maximum size, the buffers will be left out.

<span id="_______-append______"></span><span id="_______-APPEND______"></span> **-append**   
Appends the trace messages to the event trace log (.etl) file specified by the **-f** parameter. The default is to create a new file.

This parameter is valid only in commands that include **-f** and do not include **-rt** or **-cir**.

<span id="_______-b_______BufferSize______"></span><span id="_______-b_______buffersize______"></span><span id="_______-B_______BUFFERSIZE______"></span> **-b** *BufferSize*   
Specifies the size, in KB, of each buffer allocated for the trace session. The default value is determined by the number of processors, the amount of physical memory, and the operating system in use.

<span id="-bt_n"></span><span id="-BT_N"></span>**-bt** *n*  
Specifies the number (*n*) of buffers to fill before starting to flush them. This option is available starting in Windows 8.1.

<span id="_______-buffering______"></span><span id="_______-BUFFERING______"></span> **-buffering**   
Starts a buffered trace session.

In a buffered trace session, the trace messages are retained in the trace buffers. They are not sent to a trace consumer or recorded in a trace log.

<span id="_______-cir_______MaxFileSize______"></span><span id="_______-cir_______maxfilesize______"></span><span id="_______-CIR_______MAXFILESIZE______"></span> **-cir** *MaxFileSize*   
Specifies circular logging (at end-of-file, record new messages over the oldest messages) in the event trace log (.etl) file. *MaxFileSize* specifies the maximum size of the file in MB. Without a *MaxFileSize* value, this parameter is ignored.

The default is sequential logging with no file size limit.

<span id="_______-cm______"></span><span id="_______-CM______"></span> **-cm**   
Enables tracing of registry (Configuration Manager) access. This parameter is valid only for an NT Kernel Logger trace session.

<span id="_______-critsec______"></span><span id="_______-CRITSEC______"></span> **-critsec**   
Traces critical section events for a process in a private trace session. You can start a critical section process logger on any user-mode process, even one that is not instrumented for tracing.

Use **-pids** to specify the process. Do not use **-guid** with **-critsec**. The system defines a custom GUID (CritSecGuid) for critical section traces. You cannot use **-heap** and **-critsec** in the same command.

<span id="_______-dpcisr______"></span><span id="_______-DPCISR______"></span> **-dpcisr**   
Enables tracing of deferred procedure calls (DPCs), interrupt service requests (ISRs), image load events (**-img**), and context switches in the kernel. This parameter is valid only for an NT Kernel Logger trace session.

This option is supported only in the version of Tracelog included in the Windows Driver Kit for Windows Vista and later versions of the WDK. The **–dpcisr** option cannot be used with the **-eflag** option.

Use the **-UsePerfCounter** parameter with **-dpcisr**. This parameter, which provides a unique time stamp for each event, is required by Tracerpt, a tool used to format and interpret DPC/ISR events. For information about interpreting and formatting these events, see "Comments", below.

<span id="_______-eflag________n_________flag..._"></span><span id="_______-EFLAG________N_________FLAG..._"></span> **-eflag** *n* \[*flag*...\]  
Enables kernel events using additional flags for [NT Kernel Logger trace sessions](nt-kernel-logger-trace-session.md), most notably, the flags to enable tracing of DPC, ISR, and context switch events. The **-eflag** option cannot be used with the **–dpcisr** option.

<span id="_______-enableproperty________n______"></span><span id="_______-ENABLEPROPERTY________N______"></span> **-enableproperty** *n*   
See the description of *EnabledProperties* in the *EnableParameters* struct passed as a parameter to [EnableTraceEx2](/windows/win32/api/evntrace/nf-evntrace-enabletraceex2) for descriptions and supported values.

<span id="-EventIdFilter_____-in-out_n_id1_id2_..."></span><span id="-eventidfilter_____-in-out_n_id1_id2_..."></span><span id="-EVENTIDFILTER_____-IN-OUT_N_ID1_ID2_..."></span>**-EventIdFilter** {**-in**|**-out**} **** *n* **** *id1 id2 ...*  
Specifies an event id filter with *n* event ids (maximum 64 event ids allowed). This option is available starting in Windows 8.1.

<span id="___-ExeFilter____Executable_file____Executable_file_...__"></span><span id="___-exefilter____executable_file____executable_file_...__"></span><span id="___-EXEFILTER____EXECUTABLE_FILE____EXECUTABLE_FILE_...__"></span> **-ExeFilter** *Executable\_file* \[**;** *Executable\_file* ...\]   
Specifies the names of executable files to filter. You can specify a list of files. Separate the names of the files using semi-colons. Files not listed are excluded. This option is available starting in Windows 8.1.

<span id="_______-f___LogFile_"></span><span id="_______-f___logfile_"></span><span id="_______-F___LOGFILE_"></span> **-f** \[*LogFile*\]  
Starts a trace log session. *LogFile* specifies the path (optional) and file name of the event trace log (.etl) file. The default is C:\\LogFile.etl. To place the file on a remote computer, include the computer name or IP address in the path.

If you use **-rt** with **-f**, the trace messages are sent to the consumer and to an event trace log file. You cannot use **-rt** or **-f** with **-buffering**.

<span id="_______-fio______"></span><span id="_______-FIO______"></span> **-fio**   
Enables tracing of file I/O events. This parameter is valid only for an NT Kernel Logger trace session.

<span id="_______-flag_______Flag______"></span><span id="_______-flag_______flag______"></span><span id="_______-FLAG_______FLAG______"></span> **-flag** *Flag*   
> [!NOTE]
> Flags have been superseded by keywords. Use **-matchanykw** unless you are enabling a WPP provider.

Specifies the [trace flags](trace-flags.md) for the [providers](trace-provider.md) in the trace session. The flag value determines which events the trace provider generates.

*Flag* represents a flag value defined in the trace provider, in decimal or hexadecimal format. The default value is 0. Values from 0x01000000 through 0xFF000000 are reserved for future use.

The meaning of the flag value is defined independently by each trace provider. Typically, flags represent increasingly detailed reporting levels.

The flag value specified in a **tracelog -start** command applies to all trace providers in the trace session. To set different flags for each trace provider, use **tracelog -enable**.

<span id="_______-ft_______FlushTime______"></span><span id="_______-ft_______flushtime______"></span><span id="_______-FT_______FLUSHTIME______"></span> **-ft** *FlushTime*   
Specifies how often, in seconds, the trace message buffers are flushed. The minimum flush time is 1 second. The default value is 0 (no forced flush).

This forced flush is in addition to the flushes that happen automatically whenever a trace message buffer is full and when a trace session stops.

See the **tracelog -flush command**.

<span id="_______-guid___GUID___GUIDFile_"></span><span id="_______-guid___guid___guidfile_"></span><span id="_______-GUID___GUID___GUIDFILE_"></span> **-guid** {*\#GUID* | *file* | *\*name*}  
Enables the specified trace providers.

If a file is specified, Tracelog will enable tracing for all the providers specified in the file. The file must be formatted as:

```text
; comment line
guid1;matchanykeyword;level
guid2;matchanykeyword;level
```

If a provider GUID is specified, the GUID must be preceeded by a number sign (*\#*).

If a provider name is specified, the name must be preceeded by an asterisk (*\**). The name will then be converted into a GUID using the same algorithm as .NET's Event Source. This GUID will then be used to enable the provider.

If you omit this parameter, no trace providers will send messages to the trace session. However, after starting the trace session, you can use a **tracelog -enable** command to enable one or more trace providers for the session.

<span id="_______-gs______"></span><span id="_______-GS______"></span> **-gs**   
Generates a global sequence number for each trace message.

Global sequence numbers are unique for all trace sessions on the computer. By default, there are no sequence numbers.

This parameter is not valid with the NT Kernel Logger trace session.

<span id="_______-heap______"></span><span id="_______-HEAP______"></span> **-heap**   
Traces heap memory events for a user-mode process. You can start a heap process logger on any user-mode process, even one that is not instrumented for tracing.

Use **-pids** to specify the process. Do not use **-guid** with **-heap**. The system defines a custom GUID (HeapGuid) for heap memory traces. You cannot use **-heap** and **-critsec** in the same command.

<span id="_______-hf______"></span><span id="_______-HF______"></span> **-hf**   
Enables tracing of hard page faults (page faults that require disk access to resolve). This parameter is valid only for an NT Kernel Logger trace session.

<span id="-hybridshutdown_stoppersist"></span><span id="-HYBRIDSHUTDOWN_STOPPERSIST"></span>**-hybridshutdown** {**stop**|**persist**}  
Controls hybrid shutdown logger behavior. This option is available starting in Windows 8.

*stop* will cause the session to stop when the system performs a hybrid shutdown.
*persist* will cause the session to continue after the system starts up again from a hybrid shutdown.

<span id="_______-img______"></span><span id="_______-IMG______"></span> **-img**   
Enables tracing of image load events. This parameter is valid only for an NT Kernel Logger trace session.

<span id="___-independent___"></span><span id="___-INDEPENDENT___"></span> **-independent**   
> [!NOTE]
> Independent mode should be enabled on every trace session.

Enables independent mode on the trace session. Independent mode allows the session to collect events that other non-independent-mode sessions have dropped. This option is available starting in Windows 8.1.

<span id="_______-kb______"></span><span id="_______-KB______"></span> **-kb**   
Use kilobytes (KB) for log file size. The default is megabytes (MB).

<span id="_______-kd______"></span><span id="_______-KD______"></span> **-kd**   
Redirects the trace messages to KD or Windbg, whichever is attached. This parameter also sets the trace buffer size to 3 KB, the maximum buffer size for the debugger, and ignores any **-b** parameters in the command.

The debugger must be running when you submit a Tracelog command with **-kd**. Otherwise, Tracelog stops responding.

For information about displaying trace messages in a kernel debugger, see Comments.

**-Lbr** *EventName\[**+**EventName+...\]:Filter\[**,**Filter,...\]*  
Configure LBR tracing on kernel events.

Use **-eflag Help** for a list of kernel events.

<span id="_______-level________n______"></span><span id="_______-LEVEL________N______"></span> **-level** *n*   
Specifies the [trace level](trace-level.md) for the providers in the trace session. The level determines which events the trace provider generates.

*Level* represents a level value in decimal or hexadecimal format. The default value is 0.

The meaning of the level value is defined independently by each trace provider. Typically, the trace level represents the severity of the event (information, warning, or error).

The level value specified in a **tracelog -start** command applies to all trace providers in the trace session. To set different levels for each trace provider, use **tracelog -enable**.

<span id="_______-lowcapacity______"></span><span id="_______-LOWCAPACITY______"></span> **-lowcapacity**   
> [!NOTE]
> This option should not be used unless necessary to reduce memory costs. Using this option makes each event slower to log.

Uses a single buffer at a time to gather events generated on multiple processors. This option selects the EVENT\_TRACE\_NO\_PER\_PROCESSOR\_BUFFERING logging mode. For more information, see the Windows SDK.

<span id="_______-ls______"></span><span id="_______-LS______"></span> **-ls**   
Generates a local sequence number for each trace message.

Local sequence numbers are unique within a trace session. By default, there are no sequence numbers.

This parameter is not valid with the NT Kernel Logger trace session.

<span id="_______-max_______NumberOfBuffers______"></span><span id="_______-max_______numberofbuffers______"></span><span id="_______-MAX_______NUMBEROFBUFFERS______"></span> **-max** *NumberOfBuffers*   
Specifies the maximum number of buffers that Tracelog allocates for the trace session. The default value is determined by the number of processors, the amount of physical memory, and the operating system in use.

<span id="_______-matchallkw________n______"></span><span id="_______-MATCHALLKW________N______"></span> **-matchallkw** *n*   
Specifies the *MatchAllKeyWord* bitmask that restricts the category of events the provider writes and is used in conjunction with the **-matchanykw** option.

This bitmask is optional. If the event's keyword meets the condition specified in the -**matchanykw** option, the provider will write the event only if all of the bits in this mask exist in the event's keyword. This mask is not used if **-matchanykw** is zero.

Tracelog passes the value *n* in the *MatchAllKeyWord* parameter of the [EnableTraceEx2](/windows/win32/api/evntrace/nf-evntrace-enabletraceex2) function call. See the Windows SDK for more information.

<span id="_______-matchanykw________n______"></span><span id="_______-MATCHANYKW________N______"></span> **-matchanykw** *n*   
Specifies the *MatchAnyKeyword* bitmask that determines the category of events the provider writes.

The provider writes the event if any of the event's keyword bits match any of the bits set in this mask. Tracelog passes the value *n* in the *MatchAnyKeyWord* parameter of the [EnableTraceEx2](/windows/win32/api/evntrace/nf-evntrace-enabletraceex2) function call. See the Windows SDK for more information.

<span id="_______-min_______NumberOfBuffers______"></span><span id="_______-min_______numberofbuffers______"></span><span id="_______-MIN_______NUMBEROFBUFFERS______"></span> **-min** *NumberOfBuffers*   
Specifies the number of buffers initially allocated for storing trace messages. When the buffers are full, Tracelog allocates more buffers until it reaches the maximum. The default value is determined by the number of processors, the amount of physical memory, and the operating system in use.

<span id="_______-newfile_______MaxFileSize______"></span><span id="_______-newfile_______maxfilesize______"></span><span id="_______-NEWFILE_______MAXFILESIZE______"></span> **-newfile** *MaxFileSize*   
Creates a new event trace log (.etl) file whenever the existing file reaches *MaxFileSize*. *MaxFileSize* specifies the maximum size of each log file in MB. Without a *MaxFileSize* value, this parameter is ignored.

When using **-newfile**, you must also use the **-f** *LogFile* parameter, and the value of *LogFile* must be a name that includes the characters **%d** to indicate a decimal pattern--for example, trace%d.etl. Otherwise, the command fails with ERROR\_INVALID\_NAME. Windows increments the decimal value in the file name each time it creates a new file.

This parameter is not valid with preallocation (**-prealloc**), circular logging (**-cir**), with the NT Kernel Logger session, or for private trace sessions.

<span id="_______-nodisk______"></span><span id="_______-NODISK______"></span> **-nodisk**   
Disables tracing of physical disk I/O events. This parameter is valid only for an NT Kernel Logger trace session.

<span id="_______-nonet______"></span><span id="_______-NONET______"></span> **-nonet**   
Disables tracing of TCP/IP and User Datagram Protocol (UDP) events. This parameter is valid only for an NT Kernel Logger trace session.

<span id="_______-noprocess______"></span><span id="_______-NOPROCESS______"></span> **-noprocess**   
Disables tracing of the start and end of each process. This parameter is valid only for an NT Kernel Logger trace session.

<span id="_______-nothread______"></span><span id="_______-NOTHREAD______"></span> **-nothread**   
Disables tracing of the start and end of each thread. This parameter is valid only for an NT Kernel Logger trace session.

<span id="_______-paged______"></span><span id="_______-PAGED______"></span> **-paged**   
Uses pageable memory for the trace message buffers. By default, event tracing uses nonpageable memory for buffers.

Providers that require nonpageable memory will not be able to log events to a session that uses pageable memory.

<span id="_______-pids________PIDs_PID__PID..._"></span><span id="_______-pids________pids_pid__pid..._"></span><span id="_______-PIDS________PIDS_PID__PID..._"></span> **-pids** *\#PIDs PID* \[*PID*...\]  
Specifies the user-mode processes in which a heap memory or critical section trace session runs. Valid only with **-heap** or **-critsec**.

*\#PIDs* specifies the number of process IDs listed with this parameter. *PID* represents a process identifier. You can specify up to ten PIDs with this parameter.

List multiple PIDs when the provider runs in more than one process, such as when a single program creates multiple processes.

<span id="___-PidFilter____n_pid1_pid2_..."></span><span id="___-pidfilter____n_pid1_pid2_..."></span><span id="___-PIDFILTER____N_PID1_PID2_..."></span> **-PidFilter** *n* *pid1 pid2 ...*  
Specifies a Pid filter with *n* Pids (maximum 8 allowed). This option is available starting in Windows 8.1.

<span id="_______-pf______"></span><span id="_______-PF______"></span> **-pf**   
Enables tracing of all page faults. This parameter is valid only for an NT Kernel Logger trace session.

<span id="___________________-PkgIdFilter____Package_Full_Name____Package_Full_Name..._"></span><span id="___________________-pkgidfilter____package_full_name____package_full_name..._"></span><span id="___________________-PKGIDFILTER____PACKAGE_FULL_NAME____PACKAGE_FULL_NAME..._"></span> **-PkgIdFilter** *Package Full Name* \[ **;***Package Full Name*...\]  
Specifies a package ID filter. You can specify a list of package files. Separate the names of the files using semi-colons.

<span id="___-PkgAppIdFilter_____PRAID____PRAID..._"></span><span id="___-pkgappidfilter_____praid____praid..._"></span><span id="___-PKGAPPIDFILTER_____PRAID____PRAID..._"></span> **-PkgAppIdFilter** *PRAID* \[**;***PRAID*...\]  
Specifies a package-relative app identifier (PRAID) filter. The PRAID is the unique identifier of the application within the package. You can specify more than one *PRAID*. Separate the IDs using semi-colons. This option is available for UWP apps starting in Windows 8.1.

<span id="-Pmc_Ctrs_Events"></span><span id="-pmc_ctrs_events"></span><span id="-PMC_CTRS_EVENTS"></span>**-Pmc** *Ctr1,Ctr2,...:Name+Name+...*  
Configures performance monitor counter (PMC) sampling on the specified kernel events. This option is available starting in Windows 8.

Use **-ProfileSource Help** for a list of counters.
Use **-eflag Help** for a list of kernel events.

<span id="_______-prealloc______"></span><span id="_______-PREALLOC______"></span> **-prealloc**   
Reserves space for the .etl file before starting the session.

This parameter requires **-seq** or **-cir** with *MaxFileSize*. It is not valid with **-newfile**.

<span id="-ProfileSource_src"></span><span id="-profilesource_src"></span><span id="-PROFILESOURCE_SRC"></span>**-ProfileSource** *src*  
Configure profiling source to use. For list of sources, use the command **tracelog -ProfileSource Help**. This option is available starting in Windows 8.

This option is only available on Windows 8 and later versions of Windows.

<span id="_______-rt______"></span><span id="_______-RT______"></span> **-rt**   
Starts a real-time trace session. (A trace log session (**-f**) is the default.)

If you use **-rt** and **-f**, the trace messages are sent to the trace consumer and to an event trace log file. You cannot use **-rt** or **-f** with **-buffering**. For more information, see [Trace Session](trace-session.md).

<span id="_______-secure______"></span><span id="_______-SECURE______"></span> **-secure**   
Enables tracing in secure mode. This option selects the EVENT\_TRACE\_SECURE\_MODE logging mode. Restricts who can log events to the session to those with TRACELOG\_LOG\_EVENT permission.

<span id="_______-sessionguid______"></span><span id="_______-SESSIONGUID______"></span> **-sessionguid**   
Specifies the autologger session GUID registry value.

<span id="-SetProfInt_n_src"></span><span id="-setprofint_n_src"></span><span id="-SETPROFINT_N_SRC"></span>**-SetProfInt** *n* **** *src*  
> [!IMPORTANT]
> Changing the profiling interval is not recommended.

Configure the profiling interval (*n*) for the specified source, where *n* is in units of 100ns. The default is 10000 (which is equivalent to 1ms). This option is available starting in Windows 8.

<span id="_______-seq_______MaxFileSize______"></span><span id="_______-seq_______maxfilesize______"></span><span id="_______-SEQ_______MAXFILESIZE______"></span> **-seq** *MaxFileSize*   
Specifies sequential logging (at end-of-file, stop recording events) to the event trace log (.etl) file. *MaxFileSize* specifies the maximum size of the file in MB. Without a *MaxFileSize* value, this parameter is ignored.

Sequential logging is the default, but you can use this parameter to set the maximum file size or to use **-prealloc**. Without this parameter, there is no file size limit.

<span id="_______-sourceguid________SourceGuid______"></span><span id="_______-sourceguid________sourceguid______"></span><span id="_______-SOURCEGUID________SOURCEGUID______"></span> **-sourceguid** *SourceGuid*   
Specifies the GUID passed as the *SourceId* parameter to the [EnableTraceEx](/windows/win32/api/evntrace/nf-evntrace-enabletraceex) or [EnableTraceEx2](/windows/win32/api/evntrace/nf-evntrace-enabletraceex2) functions. The *SourceId* identifies the session that enabled the provider.

**-stackwalk** \[*Events*\]  
Specifies kernel events to collect stacks on. Use **-eflag Help** for a list of kernel events. This parameter is valid only for the NT Kernel Logger or system logger trace sessions.

<span id="________________-StackWalkFilter_-in-outnid1_id2_..."></span><span id="________________-stackwalkfilter_-in-outnid1_id2_..."></span><span id="________________-STACKWALKFILTER_-IN-OUTNID1_ID2_..."></span> **-StackWalkFilter** {**-in**|**-out**}*nid1 id2 ...*  
Specifies an event ID filter with *n* event IDs (maximum 64 event IDs allowed). This option is available starting in Windows 8.1.

<span id="-systemlogger"></span><span id="-SYSTEMLOGGER"></span>**-systemlogger**  
Logger can receive SystemTraceProvider events. See [Configuring and Starting a SystemTraceProvider Session](/windows/desktop/ETW/configuring-and-starting-a-systemtraceprovider-session). This option is available starting in Windows 8.

<span id="_______-um______"></span><span id="_______-UM______"></span> **-um**   
Specifies a private trace session This parameter is required for a private trace session.

<span id="_______-UseCPUCycle______"></span><span id="_______-usecpucycle______"></span><span id="_______-USECPUCYCLE______"></span> **-UseCPUCycle**   
Uses the processor frequency (also called "CPU ticks") to measure the time of each trace message.

This timer provides the highest possible resolution, but it is so sensitive that it is prone to error, especially on power-managed systems and multiprocessor computers. For example, if you specify this timer on computer that has an Arm processor, it might result in out-of-order events. Instead, **-UsePerfCounter** is recommended for high-resolution tracing.

**-UsePerfCounter** is the default timer for event tracing.

<span id="_______-UsePerfCounter______"></span><span id="_______-useperfcounter______"></span><span id="_______-USEPERFCOUNTER______"></span> **-UsePerfCounter**   
Records the value of the high-resolution performance counter clock, rather than lower-resolution system time, with each trace message.

Because the performance counter clock counts in approximately 100-nanosecond units, it provides a unique time stamp for each event.

**-UsePerfCounter** is the default timer for event tracing.

<span id="_______-UseSystemTime______"></span><span id="_______-usesystemtime______"></span><span id="_______-USESYSTEMTIME______"></span> **-UseSystemTime**   
Records the system time, rather than the high-resolution performance counter clock time, with each trace message. Because the system timer has a resolution of 10 milliseconds (compared to 100 nanoseconds for the performance counter clock), multiple events can have the same system time.

**-UsePerfCounter** is the default timer for event tracing.

<span id="_______-_____help___-_______"></span><span id="_______-_____HELP___-_______"></span> **-? | help | -?**   
Displays usage information.

### <span id="comments"></span><span id="COMMENTS"></span>Comments

The following comments apply to several of the Tracelog commands.

### <span id="syntax_errors"></span><span id="SYNTAX_ERRORS"></span>Syntax Errors

Tracelog does not display errors for all incorrect syntax combinations, such as when you try to update a setting that cannot be changed. Instead, it ignores the invalid parts of the command and displays a success message.

### <span id="system_loggers"></span><span id="SYSTEM_LOGGERS"></span>System Loggers

Windows uses trace sessions for many purposes, some of which are critical for proper operation. Do not stop any trace sessions that you did not start.

### <span id="enumguid"></span><span id="ENUMGUID"></span>Enumguid

To determine whether a **tracelog -start** or **tracelog -enable** command was successful, use a **tracelog -enumguid** command to determine whether the providers were enabled, and then use a **tracelog -l (List)** command to examine the properties of the trace session.

### <span id="real_time_and_log_sessions"></span><span id="REAL_TIME_AND_LOG_SESSIONS"></span>Real-time and log sessions

A trace session can be both a real-time trace session and a trace log session. If you include the **-rt** (real-time) and **-f** (log session) parameters in the same command, the system sends the buffer contents both to the log and to a trace consumer. However, before you can add real-time message delivery to a trace log session, the buffers must be flushed by using the **tracelog -flush** command.

If you start a real-time session (**-rt**) and then update to a log session (**-f**), any new trace messages are sent only to the log file. To add a log file to a real-time session, use both **-rt** and **-f** in the **tracelog -update** command.

If you start a log session (**-f**), you can update to a real-time session (**-rt**), but messages continue to be sent to the log in addition to the trace consumer. You cannot eliminate the log from the session by updating.

To display or save trace messages from a real-time-only session, you can also use a trace consumer, such as [Tracefmt](tracefmt.md), or use [TraceView](traceview.md), which is both a trace controller (like Tracelog) and a trace consumer. When using Tracefmt, be sure to include the **-rt** parameter in the Tracefmt command.

### <span id="flags_and_levels"></span><span id="FLAGS_AND_LEVELS"></span>Flags and levels

Most trace providers do not generate any trace messages unless the flag or level is set to a particular value. The providers use flags or levels to control what is being traced. If the event trace log file is empty, review the flags and levels in the trace provider.

To ensure that trace messages are always generated, complete the following steps:

1.  Set the **flags** parameter to 0xFFFFFFFF to enable all flag settings.

2.  Set the **levels** parameter to 255 to enable all level settings.

### <span id="the__eflag_parameter"></span><span id="THE__EFLAG_PARAMETER"></span>The -eflag parameter

Tracelog has an **-eflag** (extended flags) parameter that was designed to enable additional flags for the [NT Kernel Logger trace session](nt-kernel-logger-trace-session.md)--most notably, the flags to enable tracing of DPC, ISR, and context switch events. Because the **tracelog -start** command now includes the **-dpcisr** parameter, use of the **-eflag** parameter is no longer necessary and is not recommended.

### <span id="outdated_parameters"></span><span id="OUTDATED_PARAMETERS"></span>Outdated parameters

In previous versions of Tracelog, the **tracelog -start** command supported the **-rt b** parameter combination. This combination has been replaced by the **-buffering** parameter and it is no longer valid.

The **-x** parameter has been removed because stopping all trace sessions can cause system instability.

The **-disableex** parameter has been removed. Use **-disable** instead.

### <span id="nt_kernel_logger"></span><span id="NT_KERNEL_LOGGER"></span>NT Kernel Logger

To start a trace session with the NT Kernel Logger, omit the session name from the **tracelog -start** command and do not use the **-guid** parameter to specify a provider GUID file. **"NT Kernel Logger"** is the default session name.

If the session name is omitted or is **"NT Kernel Logger"**, the system starts an NT Kernel Logger trace session, even if you use a **-guid** parameter to specify a GUID other than **SystemTraceControlGUID**, the control GUID for the NT Kernel Logger trace session. If you specify a different GUID, the system returns an error, ("System Logger does not accept application guids"), but still starts an NT Kernel Logger trace session.

By default, when Tracelog starts an NT Kernel Logger trace session, it enables traces of process, thread, physical disk I/O, and TCP/IP events, but you can use the parameters to disable tracing of these events and enable tracing of other events.

### <span id="dpc_isr_events"></span><span id="DPC_ISR_EVENTS"></span>DPC/ISR events

Because Tracerpt expects a system performance counter clock time as the time stamp, use the Tracelog **-UsePerfCounter** parameter when you start the trace session.

Because DPC and ISR events are collected by special instrumentation, they do not appear in the **Enabled tracing** row of the table that Tracelog displays to confirm a command.

For more information, see [Example 15: Measuring DPC/ISR Time](example-15--measuring-dpc-isr-time.md).
