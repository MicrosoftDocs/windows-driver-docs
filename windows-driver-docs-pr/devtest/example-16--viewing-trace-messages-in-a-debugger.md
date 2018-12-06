---
title: Example 16 Viewing Trace Messages in a Debugger
description: Example 16 Viewing Trace Messages in a Debugger
ms.assetid: c548643c-ae0c-47e7-af0a-0d89ed78f281
keywords:
- trace message displaying WDK
- displaying trace messages
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Example 16: Viewing Trace Messages in a Debugger


## <span id="ddk_viewing_trace_messages_in_a_debugger_tools"></span><span id="DDK_VIEWING_TRACE_MESSAGES_IN_A_DEBUGGER_TOOLS"></span>


This example shows how to redirect trace messages to KD or to WinDbg.

Before starting the trace session, verify that Wmitrace.dll and Traceprt.dll are in the debugger's search path on the host computer. These DLLs are included in [Debugging Tools for Windows](http://go.microsoft.com/fwlink/p/?linkid=8708) in the \\Program Files\\Debugging Tools for Windows\\winxp directory. (Despite the directory name, the files work in Windows 2000 and later versions of Windows.)

Also, verify that the [trace message format files](trace-message-format-file.md) (TMF) for the trace provider are in the debugger's search path.

To set the debugger's search path, use the !wmitrace.searchpath specialized debugger extension or set the value of the %TRACE\_FORMAT\_SEARCH\_PATH% environment variable. For example:

```
set TRACE_FORMAT_SEARCH_PATH=c:\tracing
```

Then, start the debugger. If you submit a Tracelog command with the **-kd** parameter, and a debugger is not running, Tracelog stops responding ("hangs").

The following command starts a trace session and sends the trace messages to KD or to Windbg, whichever is attached.

```
tracelog -start MyTrace -guid MyProvider.ctl -rt -kd
```

The **tracelog -start** command includes a session name to start the trace session. It uses the **-guid** parameter to identify the provider file. It also uses the **-rt** parameter to start a real-time trace session, so that the trace messages are sent to the debugger and not to a log file.

In response, Tracelog reports that it has started the session. When the trace provider generates messages, the messages appear in the debugger.

To view the messages in the debugger, use the WMI Tracing Extensions. For information, see [Debugging Tools for Windows](http://go.microsoft.com/fwlink/p/?linkid=8708).

 

 





