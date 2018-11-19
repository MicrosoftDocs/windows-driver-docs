---
title: Stopping a Trace Session
description: Stopping a Trace Session
ms.assetid: 648bf805-4266-4db5-aef6-414c5f37d1a3
keywords:
- trace sessions WDK , stopping
- stopping trace sessions
- TraceView WDK , stopping trace
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Stopping a Trace Session


When you *stop* a trace session, TraceView disables the trace providers, flushes any unsent trace messages from the buffers into the TraceView display and trace logs, and then stops the trace session. To stop a trace session, do the following:

1.  In the [Trace Session List](trace-session-list.md), right-click any cell of the row for the trace session.

2.  Click **Stop Trace**.

After a brief pause, the value of the **State** column changes from **RUNNING** to **STOPPING** and then to **STOPPED**. When the trace session stops, you can [remove it from the display](removing-a-trace-session.md).

### <span id="comments"></span><span id="COMMENTS"></span>Comments

TraceView can stop only the trace sessions that it started. To stop other trace sessions, use a **traceview -stop***SessionName* command. For more information about this command, see [**TraceView Control Commands**](traceview-control-commands.md).

Stopping a trace session does not remove the session from the display or delete any trace logs.

TraceView uses the **EnableTrace** function to stop the trace session. For more information about this function, see the Microsoft Windows SDK documentation.

 

 





