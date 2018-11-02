---
title: TraceView
description: TraceView
ms.assetid: f64ddf90-56b8-4341-8d59-f4d7e3eeddaf
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
ms.author: eliotgra
ms.date: 09/12/2018
ms.localizationpriority: medium
---

# TraceView


## <span id="ddk_traceview_tools"></span><span id="DDK_TRACEVIEW_TOOLS"></span>


TraceView (TraceView.exe) configures and controls [trace sessions](trace-session.md) and displays formatted trace messages from real-time trace sessions and [trace logs](trace-log.md). It has a flexible graphic user interface and a command-line interface for batch processing and scripting.

TraceView is a [trace controller](trace-controller.md) and a [trace consumer](trace-consumer.md). You can use TraceView to enable, configure, start, update, and stop a tracing session; to display real-time or logged trace messages; to combine trace message from different providers in a single display; to filter a trace message display; and to convert trace messages into text format.

TraceView is located in the tools\\&lt;*Platform*&gt; subdirectory of the Windows Driver Kit (WDK), where &lt;*Platform*&gt; represents the platform you are running the trace session on, for example, x86, x64, or arm64.

TraceView performs many of the functions of [Tracepdb](tracepdb.md), [Tracelog](tracelog.md), and [Tracefmt](tracefmt.md), the command-line tracing tools that are included in the WDK.

This section describes TraceView 2.0.15. It includes the following sections:

* [TraceView Overview](traceview-overview.md)

* [Using TraceView](using-traceview.md)

See [TraceView Limitations](traceview-limitations.md) for a description of the limitations you may face when running TraceView. 

 





