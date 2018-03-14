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
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 





