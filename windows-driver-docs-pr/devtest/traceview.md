---
title: TraceView Tool for Trace Session Control
description: Learn how to use TraceView to configure trace sessions, control tracing, and display formatted trace messages in Windows Driver Kit (WDK).
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
ms.date: 10/23/2025
ms.topic: overview
---

# TraceView

TraceView (TraceView.exe) is a Windows Driver Kit tool that configures and controls trace sessions and displays formatted trace messages from real-time trace sessions and trace logs. Use TraceView to enable, configure, and monitor tracing in your driver development workflow.

> [!IMPORTANT]
> TraceView's command-line interface is deprecated and outdated. Use the dedicated command-line tools  [Tracepdb](tracepdb.md), [Tracelog](tracelog.md), and [Tracefmt](tracefmt.md) instead. These tools are included when you install the WDK, Visual Studio, and the Windows SDK for desktop apps. For information about downloading the kits, see [Windows Hardware Downloads](/windows-hardware/drivers/download-the-wdk).

TraceView is a [trace controller](trace-controller.md) and a [trace consumer](trace-consumer.md). You can use TraceView to enable, configure, start, update, and stop a tracing session; to display real-time or logged trace messages; to combine trace messages from different providers in a single display; to filter a trace message display; and to convert trace messages into text format.

TraceView is located in the tools \<Platform\> subdirectory of the Windows Driver Kit (WDK), where \<Platform\> represents the platform where you run the trace session, for example, x86, x64, or arm64.

This section describes the version of TraceView that ships in the Windows 10 Fall Creators Update (1709) WDK and later. Earlier versions of TraceView might lack some of the features described here.

> [!NOTE]
> TraceView runs on Microsoft Windows 7 and later.

## Related topics

- [TraceView Overview](traceview-overview.md)

- [Using TraceView](using-traceview.md)
