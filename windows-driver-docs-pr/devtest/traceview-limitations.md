---
title: TraceView Limitations
description: TraceView Limitations
ms.assetid: 946d7c69-7c6a-4bab-8fa5-fc21dcf85ddb
keywords: ["TraceView WDK , limitations"]
---

# TraceView Limitations


This topic describes the limitations of TraceView.

### <span id="traceview_window_limitations"></span><span id="TRACEVIEW_WINDOW_LIMITATIONS"></span>TraceView Window Limitations

The TraceView window can display and control only trace sessions that are started by using the window. To list and control all trace sessions on the system, use the [TraceView command-line interface](traceview-command-line-interface.md).

When you exit TraceView, it stops all running (or *real-time*) trace sessions that you started by using TraceView. To start trace sessions that run independently of the TraceView window, use the TraceView command-line interface.

You can use the [TraceView command-line interface](traceview-command-line-interface.md) and other software tracing tools, such as [Tracelog](tracelog.md), to control a trace session that TraceView started. However, if you use these other tools to change the properties of a running trace session, TraceView stops the trace session, even if you change properties that can be changed while a trace session is running. When you use TraceView to restart (or *join*) the trace session, it updates the properties.

### <span id="traceview_command_line_limitations"></span><span id="TRACEVIEW_COMMAND_LINE_LIMITATIONS"></span>TraceView Command-Line Limitations

When you submit a TraceView command in a Command Prompt window, TraceView opens a new Command Prompt window to display its output. You cannot suppress these additional windows.

### <span id="etw_limitations"></span><span id="ETW_LIMITATIONS"></span>ETW Limitations

TraceView and other tracing tools based on Event Tracing for Windows (ETW) can create only one trace session or display one trace log for each trace provider. If you try to create a trace session or display a trace log with a provider that is already enabled in TraceView, TraceView displays an error message. For more information about this error message, see [Resolving TraceView Errors](resolving-traceview-errors.md).

### <span id="global_logger_trace_sessions"></span><span id="GLOBAL_LOGGER_TRACE_SESSIONS"></span>Global Logger Trace Sessions

The TraceView window does not have an option for starting a [Global Logger trace session](global-logger-trace-session.md). However, you can use the window to start a Global Logger trace session by entering the Global Logger [control GUID](control-guid.md), e8908abc-aa84-11d2-9a93-00805f85d7c6, or by saving the control GUID in a [control GUID file](control-guid-file.md). For more information about these procedures, see [Creating a trace session with a Control GUID](creating-a-trace-session-with-a-control-guid.md) and [Creating a trace session with a CTL file](creating-a-trace-session-with-a-ctl-file.md).

You can also use the [TraceView command-line interface](traceview-command-line-interface.md) to start a Global Logger trace session. Use the following command to start a Global Logger trace session. The word "GlobalLogger" in this command is case-sensitive.

```
traceview -start GlobalLogger [parameters]
```

For more information about TraceView commands, see [**TraceView Control Commands**](traceview-control-commands.md).

### <span id="enabling_trace_providers"></span><span id="ENABLING_TRACE_PROVIDERS"></span>Enabling Trace Providers

TraceView automatically enables the trace providers that you add to the trace session. However, after you create a trace session, you cannot use the TraceView window to enable additional trace providers for the trace session or to selectively disable the trace providers that you added to the trace session.

To enable or disable providers, use a **traceview -enable** command. For more information about this command, see [**TraceView Control Commands**](traceview-control-commands.md).

### <span id="windows_xp_limitation"></span><span id="WINDOWS_XP_LIMITATION"></span>Windows XP Limitation

On Windows XP, you cannot include a real-time trace session in a trace session group. This limitation is not affected by service packs.

### <span id="windows_2000_limitations"></span><span id="WINDOWS_2000_LIMITATIONS"></span>Windows 2000 Limitations

The following limitations apply only to Windows 2000:

-   Only one trace session can be active at a time.

-   The provider must be running before TraceView starts the trace session.

-   You cannot change the properties of a trace session (or of its trace providers) while the session is running.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20TraceView%20Limitations%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




