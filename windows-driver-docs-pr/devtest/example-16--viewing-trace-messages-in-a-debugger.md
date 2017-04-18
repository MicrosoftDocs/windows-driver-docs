---
title: Example 16 Viewing Trace Messages in a Debugger
description: Example 16 Viewing Trace Messages in a Debugger
ms.assetid: c548643c-ae0c-47e7-af0a-0d89ed78f281
keywords: ["trace message displaying WDK", "displaying trace messages"]
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Example%2016:%20Viewing%20Trace%20Messages%20in%20a%20Debugger%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




