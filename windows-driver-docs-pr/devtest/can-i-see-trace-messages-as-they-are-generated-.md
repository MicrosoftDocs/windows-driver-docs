---
title: Can I see trace messages as they are generated
description: Can I see trace messages as they are generated
ms.assetid: 21d8606b-5693-4f50-81f9-c5c3a65c0550
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Can%20I%20see%20trace%20messages%20as%20they%20are%20generated?%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




