---
title: wmitrace.logdump
description: The wmitrace.logdump extension displays the contents of the trace buffers for a trace session. You can limit the display to trace messages from specified providers.
ms.assetid: 073338c6-68c4-4ae0-b69e-392256277236
keywords: ["wmitrace.logdump Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- wmitrace.logdump
api_type:
- NA
ms.localizationpriority: medium
---

# !wmitrace.logdump


The **!wmitrace.logdump** extension displays the contents of the trace buffers for a trace session. You can limit the display to trace messages from specified providers.

```dbgcmd
!wmitrace.logdump [-t Count] [{LoggerID|LoggerName} [GUIDFile]] 
```

## <span id="ddk__wmitrace_logdump_dbg"></span><span id="DDK__WMITRACE_LOGDUMP_DBG"></span>Parameters


<span id="_______-t_______Count______"></span><span id="_______-t_______count______"></span><span id="_______-T_______COUNT______"></span> **-t** *Count*   
Limits the output to the most recent messages. *Count* specifies the number of messages to display.

<span id="_______LoggerID______"></span><span id="_______loggerid______"></span><span id="_______LOGGERID______"></span> *LoggerID*   
Specifies the trace session. *LoggerID* is an ordinal number that the system assigns to each trace session on the computer. If no parameter is specified, the trace session with ID equal to 1 is used.

<span id="_______LoggerName______"></span><span id="_______loggername______"></span><span id="_______LOGGERNAME______"></span> *LoggerName*   
Specifies the trace session. *LoggerName* is the text name that was specified when the trace session was started.

<span id="_______GUIDFile______"></span><span id="_______guidfile______"></span><span id="_______GUIDFILE______"></span> *GUIDFile*   
Displays only trace messages from providers specified in the *GUIDFile* file. *GUIDFile* represents the path (optional) and file name of a text file that contains the control GUIDs of one or more trace providers, such as a .guid or .ctl file.

### <span id="DLL"></span><span id="dll"></span>DLL

This extension is exported by Wmitrace.dll.

This extension is available in Windows 2000 and later versions of Windows. If you want to use this extension with Windows 2000, you must first copy the Wmitrace.dll file from the winxp subdirectory of the Debugging Tools for Windows installation directory to the w2kfre subdirectory.

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For a conceptual overview of event tracing, see the Microsoft Windows SDK. For information about Tracelog, see "Tracelog" in the Windows Driver Kit (WDK).

Remarks
-------

During Windows software trace preprocessor (WPP) software tracing, trace session buffers are used to store trace messages until they are flushed to a log file or to a trace consumer for a real-time display. The **!wmitrace.logdump** extension displays the contents of the buffers that are in physical memory. The display appears in the Debugger Command window.

This extension is especially useful to recover the most recent traces when a crash occurs, and to display the traces stored in a crash dump file.

Before you use this extension, use [**!wmitrace.searchpath**](-wmitrace-searchpath.md) or [**!wmitrace.tmffile**](-wmitrace-tmffile.md) to specify the trace message format files. The system uses the trace message format files to format the binary trace messages in the buffers so that they can be displayed as human-readable text.

**Note**  If your driver uses UMDF version 1.11 or later, you do not need to use [**!wmitrace.searchpath**](-wmitrace-searchpath.md) or [**!wmitrace.tmffile**](-wmitrace-tmffile.md).

 

When you use Tracelog to start a trace session with circular buffering (-buffering), use this extension to display the buffer contents.

To find the logger ID of a trace session, use the [**!wmitrace.strdump**](-wmitrace-strdump.md) extension. Alternatively, you can use the Tracelog command tracelog -l to list the trace sessions and their basic properties, including the logger ID.

This extension is only useful during WPP software tracing, and earlier (legacy) methods of Event Tracing for Windows. Trace events that are produced by other manifested providers do not use trace message format (TMF) files, and therefore this extension does not display their contents.

This extension is similar to the [**!wmitrace.eventlogdump**](-wmitrace-eventlogdump.md) extension, except that the output of **!wmitrace.logdump** is formatted in WPP style, and the output of **!wmitrace.eventlogdump** is formatted in event log style. You should choose the extension whose format is appropriate for the data you want to display.

For information about how to view the UMDF trace log, see [Using WPP Software Tracing in UMDF-based Drivers](https://msdn.microsoft.com/library/windows/hardware/ff561391#viewing-the-umdf-trace-log).

 

 





