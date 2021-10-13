---
title: TraceView
description: TraceView
keywords:
- software tracing WDK , TraceView
- tracing WDK , TraceView
- TraceView WDK
- displaying trace messages
- trace message displaying WDK
- trace sessions WDK , TraceView
- trace sessions WDK , controlling
- trace consumers WDK
- trace controllers WDK
ms.date: 09/12/2018
ms.localizationpriority: medium
---

# TraceView

## <span id="ddk_traceview_tools"></span><span id="DDK_TRACEVIEW_TOOLS"></span>

TraceView (TraceView.exe) configures and controls [trace sessions](trace-session.md) and displays formatted trace messages from real-time trace sessions and [trace logs](trace-log.md).

> [!IMPORTANT]
> TraceView's command-line interface is deprecated and outdated. You should prefer the dedicated command-line tools that are included in the SDK and WDK:  [Tracepdb](tracepdb.md), [Tracelog](tracelog.md), and [Tracefmt](tracefmt.md).

TraceView is a [trace controller](trace-controller.md) and a [trace consumer](trace-consumer.md). You can use TraceView to enable, configure, start, update, and stop a tracing session; to display real-time or logged trace messages; to combine trace message from different providers in a single display; to filter a trace message display; and to convert trace messages into text format.

TraceView is located in the tools\\&lt;*Platform*&gt; subdirectory of the Windows Driver Kit (WDK), where &lt;*Platform*&gt; represents the platform you are running the trace session on, for example, x86, x64, or arm64.

This section describes the version of TraceView that ships in the Windows 10 Fall Creator's Update (1709) WDK and later. Earlier versions of Traceview may lack many of the features described here.

> [!NOTE]
> TraceView runs on Microsoft Windows 7 and later versions of Windows.

* [TraceView Overview](traceview-overview.md)

[Using TraceView](using-traceview.md)
