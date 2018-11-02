---
title: wmitrace.logsave
description: The wmitrace.logsave extension writes the current contents of the trace buffers for a trace session to a file.
ms.assetid: 713fea09-d405-4142-b2e8-29c813a4c3b6
keywords: ["wmitrace.logsave Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- wmitrace.logsave
api_type:
- NA
ms.localizationpriority: medium
---

# !wmitrace.logsave


The **!wmitrace.logsave** extension writes the current contents of the trace buffers for a trace session to a file.

```dbgcmd
!wmitrace.logsave {LoggerID|LoggerName} Filename 
```

## <span id="ddk__wmitrace_logsave_dbg"></span><span id="DDK__WMITRACE_LOGSAVE_DBG"></span>Parameters


<span id="_______LoggerID______"></span><span id="_______loggerid______"></span><span id="_______LOGGERID______"></span> *LoggerID*   
Specifies the trace session. *LoggerID* is an ordinal number that the system assigns to each trace session on the computer.

<span id="_______LoggerName______"></span><span id="_______loggername______"></span><span id="_______LOGGERNAME______"></span> *LoggerName*   
Specifies the trace session. *LoggerName* is the text name that was specified when the trace session was started.

<span id="_______Filename______"></span><span id="_______filename______"></span><span id="_______FILENAME______"></span> *Filename*   
Specifies a path (optional) and file name for the output file.

### <span id="DLL"></span><span id="dll"></span>DLL

This extension is exported by Wmitrace.dll.

This extension is available in Windows 2000 and later versions of Windows. If you want to use this extension with Windows 2000, you must first copy the Wmitrace.dll file from the winxp subdirectory of the Debugging Tools for Windows installation directory to the w2kfre subdirectory.

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For a conceptual overview of event tracing, see the Microsoft Windows SDK. For information about Tracelog, see "Tracelog" in the Windows Driver Kit (WDK).

Remarks
-------

This extension displays only the traces that are in memory at the time. It does not display trace messages that have been flushed from the buffers and delivered to an event trace log file or to a trace consumer.

Trace session buffers store trace messages until they are flushed to a log file or to a trace consumer for a real-time display. This extension saves the contents of the buffers that are in physical memory to the specified file.

The output is written in binary format. Typically, these files use the .etl (event trace log) filename extension.

When you use Tracelog to start a trace session with circular buffering (-buffering), you can use this extension to save the current buffer contents.

To find the logger ID of a trace session, use the [**!wmitrace.strdump**](-wmitrace-strdump.md) extension. Alternatively, you can use the Tracelog command tracelog -l to list the trace sessions and their basic properties, including the logger ID.

 

 





