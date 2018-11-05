---
title: How do I send trace messages to a kernel debugger
description: How do I send trace messages to a kernel debugger
ms.assetid: 867791a7-30a5-4539-be85-61f1716c279a
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# How do I send trace messages to a kernel debugger?


You can use several methods to redirect trace messages to a kernel-mode debugger. A few are discussed here.

You can redirect trace messages to KD or to Windbg, whichever is attached. The debugger must be attached through a COM port with a debug (null modem) cable or through the 1394 ("firewire") port with a IEEE 1394 cable. You cannot redirect trace messages to other kernel debuggers, such as NTSD.

To display trace messages in a debugger, wmitrace.dll and traceprt.dll must be in the debugger's search path on the host computer. These DLLs are included in [Debugging Tools for Windows](http://go.microsoft.com/fwlink/p/?linkid=8708) Also, to enable the debugger to find the [trace message format (.tmf) files](trace-message-format-file.md) for the trace messages, the TMF files must be in the debugger's search path on the host computer. To set the debugger's search path, use the !wmitrace.searchpath specialized debugger extension or set the value of the %TRACE\_FORMAT\_SEARCH\_PATH% environment variable.

For more information, search for **!wmitrace** in *Debugging Tools for Windows*.

### <span id="logman"></span><span id="LOGMAN"></span>Logman

Use the following Logman command to redirect trace messages to a kernel-mode debugger:

```
logman start TraceSession -ets -mode KernelFilter -bs 3
```

The **-ets** parameter starts an event trace session that is not controlled by the Performance Logs and Alerts service. The **-mode** parameter activates advanced options, including the **KernelFilter** option.

The **-bs** parameter sets the buffer size for the trace session to 3 KB, the maximum buffer size for the debugger. If you omit this parameter, the debugger session will not operate properly.

Logman is included in Windows XP and later versions of Windows.

### <span id="tracelog"></span><span id="TRACELOG"></span>Tracelog

Use the following [Tracelog](tracelog.md) command redirect trace messages to a kernel-mode debugger:

```
tracelog -start MyTrace -guid MyProvider.ctl -rt -kd
```

The **-guid** parameter specifies the [trace provider](trace-provider.md). The **-rt** parameter specifies a real-time trace session. The **-kd** parameter redirects the trace messages to the kernel debugger and sets the maximum buffer size to 3 KB, the maximum for the debugger.

For an example, see [Example 16: Viewing Trace Messages in a Debugger](example-16--viewing-trace-messages-in-a-debugger.md).

Tracelog is located in the tools\\tracing\\*&lt;Platform&gt;* subdirectory of the WDK, where *&lt;Platform&gt;* is either i386, amd64, or ia64.

### <span id="traceview"></span><span id="TRACEVIEW"></span>TraceView

[TraceView](traceview.md) has a graphical user interface.

You can redirect trace messages to a kernel debugger when creating a trace session. On the **Log Session Options** page, click **Advanced Log Session Options**, click the **Log Session Parameter Options** tab, and then change the value of the **Windbg** option to **TRUE**. You cannot change this option while the trace session is running.

TraceView is located in the tools\\tracing\\*&lt;Platform&gt;* subdirectory of the WDK, where *&lt;Platform&gt;* is either i386, amd64, or ia64.

 

 





