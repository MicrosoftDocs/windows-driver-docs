---
title: Can I see trace messages as they are generated
description: Can I see trace messages as they are generated
ms.assetid: 21d8606b-5693-4f50-81f9-c5c3a65c0550
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Can I see trace messages as they are generated?


Yes. To view trace messages as they are generated, use the real-time trace session options in [TraceView](traceview.md), [Tracelog](tracelog.md), or [Tracefmt](tracefmt.md). These tools are included in the tools\\tracing\\&lt;*Platform*&gt; subdirectory of the Microsoft Windows Driver Kit (WDK), where &lt;*Platform*&gt; is either i386, amd64, or ia64.

[Trace providers](trace-provider.md) do not have to include any special code to support real-time tracing.

### <span id="traceview"></span><span id="TRACEVIEW"></span>TraceView

[TraceView](traceview.md) can start a real-time trace session that displays the trace messages as they are generated. To use TraceView for real-time monitoring:

1.  Start TraceView.

2.  On the **File** menu, click **Create New Log Session**.

3.  Click **Add Provider**.

4.  Select the **CTL (Control GUID) File** option. Then click the ellipsis button (**...**) to locate a [control GUID file](control-guid-file.md) for the provider.

5.  Click **Select TMF Files**.

6.  Click **Add**, locate a [trace message format (.tmf) file](trace-message-format-file.md) for the provider, click **Open**, and then click **Done**.

7.  Click **Next**.

8.  On the **Log Session Options** page, verify that the **Real Time Display** check box is selected (checked).

    You can select other options to specify [trace flags](trace-flags.md) and the [trace level](trace-level.md), or to customize the trace session.

9.  Click **Finish**.

For detailed information, in TraceView, on the **Help** menu, click **Help Topics**.

### <span id="tracelog"></span><span id="TRACELOG"></span>Tracelog

Tracelog can start, stop, and update a real-time trace session.

To start a real-time trace session by using Tracelog, use the **-rt** (real time) parameter in the command to start a trace session.

The following command starts a trace session called "My Trace" with providers whose control GUIDs are listed in the MyProvider.ctl[control GUID file](control-guid-file.md). The **-rt** parameter specifies a real-time trace session.

```
tracelog -start MyTrace -guid MyProvider.ctl -rt
```

For a detailed example, see [Example 10: Starting a Real-Time Trace Session](example-10--starting-a-real-time-trace-session.md).

To view the trace messages from a real-time trace session, use [Tracefmt](tracefmt.md).

### <span id="tracefmt"></span><span id="TRACEFMT"></span>Tracefmt

[Tracefmt](tracefmt.md) can display trace messages from a real-time trace session. In real-time mode, Tracefmt formats and displays the messages as they are written to the file.

The following command displays the trace messages from the "MyTrace" real-time trace session. The **-rt** parameter specifies a real-time session. The **-p** parameter indicates the path of the [trace message format (.tmf) file](trace-message-format-file.md) for the trace messages. The **-display** parameter directs Tracefmt to display the trace messages as they arrive from the buffer. The **-o** parameter specifies the location of the output file.

```
tracefmt -rt MyTrace -p c:\tracing -display -o mytrace.txt
```

For a detailed example, see [Example 5: Formatting Real-Time Trace Sessions](example-5--formatting-real-time-trace-sessions.md).

 

 





