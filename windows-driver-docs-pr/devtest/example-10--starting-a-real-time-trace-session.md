---
title: Example 10 Starting a Real-Time Trace Session
description: Example 10 Starting a Real-Time Trace Session
ms.assetid: 1dfa8cf1-dd51-4415-b6d4-84241db2aa03
keywords: ["trace sessions WDK , real-time", "real-time trace sessions WDK"]
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Example%2010:%20Starting%20a%20Real-Time%20Trace%20Session%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




