---
title: TraceView Limitations
description: TraceView Limitations
ms.assetid: 946d7c69-7c6a-4bab-8fa5-fc21dcf85ddb
keywords:
- TraceView WDK , limitations
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
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

TraceView and other tracing tools based on Event Tracing for Windows (ETW) can create only one trace session or display one trace log for each WPP or classic trace provider. If you create a trace session or display a trace log with a WPP provider that is already enabled in another trace session, it will be disabled in the other session.

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
