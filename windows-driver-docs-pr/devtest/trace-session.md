---
title: Trace Session
description: Trace Session
ms.assetid: 50a8cc64-5127-4abe-a6a8-514ca5db63ab
keywords:
- trace sessions WDK
- trace sessions WDK , about trace sessions
- sessions WDK software tracing
- private trace sessions WDK
- buffered trace sessions WDK
- real-time trace sessions WDK
- trace log sessions WDK
- user-mode trace sessions WDK
- process trace sessions WDK
- reserved trace sessions WDK
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Trace Session


## <span id="ddk_trace_session_tools"></span><span id="DDK_TRACE_SESSION_TOOLS"></span>


A *trace session* is a period during which a [trace provider](trace-provider.md) is generating trace messages. The system maintains a set of buffers for the trace session to store trace messages until they are delivered ("flushed") to a [trace log](trace-log.md) or a [trace consumer](trace-consumer.md).

There are three basic types of trace sessions: trace log sessions, real-time trace sessions, and buffered trace sessions. A single trace session can be a trace log session, a real-time trace session, or both. Buffered trace sessions are exclusive.

In addition, there are private trace sessions and reserved trace sessions, such as the [NT Kernel Logger trace session](nt-kernel-logger-trace-session.md) and [Global Logger trace session](global-logger-trace-session.md), which can be run as log sessions or real-time sessions. You can use the standard tools to control these sessions and display the resulting trace messages.

### <span id="ddk_trace_log_sessions_tools"></span><span id="DDK_TRACE_LOG_SESSIONS_TOOLS"></span>Trace Log Sessions

In a *trace log session*, trace messages are written from the trace buffers to a log file in binary format. This is the standard, default type of trace session.

### <span id="ddk_real_time_trace_sessions_tools"></span><span id="DDK_REAL_TIME_TRACE_SESSIONS_TOOLS"></span>Real-Time Trace Sessions

In a *real-time trace session*, the trace messages are delivered directly to a trace consumer, such as [TraceView](traceview.md) or [Tracefmt](tracefmt.md), instead of or, in addition to, being sent to a log file.

### <span id="ddk_buffered_trace_sessions_tools"></span><span id="DDK_BUFFERED_TRACE_SESSIONS_TOOLS"></span>Buffered Trace Sessions

In a *buffered trace session*, the trace messages remain in the trace buffer; they are not written to a [trace log](trace-log.md) or delivered to a [trace consumer](trace-consumer.md). The buffer is maintained like a circular file. When it is full, the newest trace messages overwrite the oldest trace messages in the buffer.

Buffered trace sessions are supported only on Windows Vista and later versions of Windows.

Although software tracing, in general, causes very little overhead, buffered trace sessions have the least overhead of all trace session types. You can trace for long periods of time, and then, if something interesting occurs, you can use a debugger to examine the current buffer content, or save the current buffer content in a trace log.

To see the trace messages in a trace buffer, use the **!wmitrace** specialized debugger extension. For information about this extension, see *Debugging Tools for Windows*.

To flush the buffer content to a [trace log](trace-log.md), use the **-f** parameter of the **tracelog -flush** command.

To start a buffered trace session, use the **-buffering** parameter of the **tracelog -start** command. For more information, see [**Tracelog Command Syntax**](tracelog-command-syntax.md).

### <span id="ddk_private_trace_sessions_tools"></span><span id="DDK_PRIVATE_TRACE_SESSIONS_TOOLS"></span>Private Trace Sessions

A *private trace session* is a trace session that runs in user mode as part of the user-mode process that it traces. (Standard tracing sessions run in the kernel.) Private trace sessions are also known as *user-mode trace sessions* or *process trace sessions*.

You can run more than one private trace session at a time, but you can run only one private trace session in each process.

You cannot perform real-time tracing of a private trace session. The trace messages must be written to a log.

The buffers used in private trace sessions are always pageable. You cannot specify paged or nonpaged memory for these buffers.

You cannot send the trace messages from a private trace session to the debugger. The WMI Tracing Extension (**!wmitrace**) does not support private trace sessions.

For more information about private event tracing sessions, see the Microsoft Windows SDK documentation.

 

 





