---
title: TraceView
description: TraceView
ms.assetid: f64ddf90-56b8-4341-8d59-f4d7e3eeddaf
keywords: ["software tracing WDK , TraceView", "tracing WDK , TraceView", "TraceView WDK", "displaying trace messages", "trace message displaying WDK", "trace sessions WDK , TraceView", "trace sessions WDK , controlling", "trace consumers WDK", "trace controllers WDK"]
---

# TraceView


## <span id="ddk_traceview_tools"></span><span id="DDK_TRACEVIEW_TOOLS"></span>


TraceView (TraceView.exe) configures and controls [trace sessions](trace-session.md) and displays formatted trace messages from real-time trace sessions and [trace logs](trace-log.md). It has a flexible graphic user interface and a command-line interface for batch processing and scripting.

TraceView is a [trace controller](trace-controller.md) and a [trace consumer](trace-consumer.md). You can use TraceView to enable, configure, start, update, and stop a tracing session; to display real-time or logged trace messages; to combine trace message from different providers in a single display; to filter a trace message display; and to convert trace messages into text format.

TraceView is located in the tools\\tracing\\&lt;*Platform*&gt; subdirectory of the Windows Driver Kit (WDK), where &lt;*Platform*&gt; is either i386, amd64, or ia64.

**Note**  TraceView runs on Microsoft Windows 2000 and later versions of Windows, although some features are restricted on Windows 2000. For more information about these restrictions, see [TraceView Limitations](traceview-limitations.md).

 

TraceView performs many of the functions of [Tracepdb](tracepdb.md), [Tracelog](tracelog.md), and [Tracefmt](tracefmt.md), the command-line tracing tools that are included in the WDK.

This section describes TraceView 2.0.15. It includes the following topics:

[TraceView Overview](traceview-overview.md)

[Using TraceView](using-traceview.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20TraceView%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




