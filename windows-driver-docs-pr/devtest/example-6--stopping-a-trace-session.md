---
title: Example 6 Stopping a Trace Session
description: Example 6 Stopping a Trace Session
ms.assetid: a8520531-bebb-4334-9dc3-d50f4a851e7e
keywords:
- trace sessions WDK , stopping
- stopping trace sessions
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Example 6: Stopping a Trace Session


## <span id="ddk_stopping_a_trace_session_tools"></span><span id="DDK_STOPPING_A_TRACE_SESSION_TOOLS"></span>


The following command stops the MyTrace trace session:

```
tracelog -stop MyTrace
```

In response, Tracelog displays the properties of the trace session.

```
Operation Status:       0L      The operation completed successfully.

Logger Name:            MyTrace
Logger Id:              2
Logger Thread Id:       000008C8
Buffer Size:            8 Kb
Maximum Buffers:        26
Minimum Buffers:        4
Number of Buffers:      6
Free Buffers:           6
Buffers Written:        1
Events Lost:            0
Log Buffers Lost:       0
Real Time Buffers Lost: 0
AgeLimit:               15
Log File Mode:          Sequential
Log Filename:           C:\Tracing\MyTrace.etl
```

To verify that the trace session is stopped, use a list (**tracelog -l**) or query (**tracelog -q**) command.

 

 





