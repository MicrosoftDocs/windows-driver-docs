---
title: How do I send trace messages to a kernel debugger
description: How do I send trace messages to a kernel debugger
ms.assetid: 867791a7-30a5-4539-be85-61f1716c279a
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20How%20do%20I%20send%20trace%20messages%20to%20a%20kernel%20debugger?%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




