---
title: Example 10 Starting a Real-Time Trace Session
description: Example 10 Starting a Real-Time Trace Session
ms.assetid: 1dfa8cf1-dd51-4415-b6d4-84241db2aa03
keywords:
- trace sessions WDK , real-time
- real-time trace sessions WDK
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Example 10: Starting a Real-Time Trace Session


## <span id="ddk_starting_a_real_time_trace_session_tools"></span><span id="DDK_STARTING_A_REAL_TIME_TRACE_SESSION_TOOLS"></span>


The following command starts a real-time trace session--a session in which trace messages are sent directly to a trace consumer instead of being sent to a log file.

```
tracelog -start MyTrace guid MyProvider.guid -rt
```

You can use the same parameters to customize a real-time trace session that you would use for a trace log session, except for those parameters that affect the log file. This includes real-time tracing of special trace sessions and private trace sessions. However, because Tracelog is a [trace controller](trace-controller.md), not a [trace consumer](trace-consumer.md), you cannot use Tracelog to view the trace messages generated during a real-time trace session. Instead, use a trace consumer such as [Tracefmt](tracefmt.md), or use [TraceView](traceview.md), which is both a trace controller and a trace consumer.

The following command uses Tracefmt to format the trace messages from the MyTrace real-time trace session, display them in a Command Prompt window, and save them to a text file for later examination. For detailed information about the command syntax, see [Tracefmt](tracefmt.md).

```
tracefmt -rt MyTrace -p c:\tracing -o mytrace.txt
```

 

 





