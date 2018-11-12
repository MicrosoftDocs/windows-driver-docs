---
title: Restarting a Trace Session
description: Restarting a Trace Session
ms.assetid: 2fd0dc74-d6dd-4057-b1d0-1c0c0ff23d48
keywords:
- trace sessions WDK , restarting
- restarting trace sessions
- TraceView WDK , restarting trace
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Restarting a Trace Session


When you create a trace session, TraceView automatically enables the trace providers and starts the trace session. You can use the **Start Trace** option to restart only a trace session that you [stopped](stopping-a-trace-session.md). To restart a stopped trace session, do the following:

1.  In the [Trace Session List](trace-session-list.md), right-click any cell of the row for the trace session.

2.  Click **Start Trace**.

After a brief pause, the value of the **State** column changes from **STOPPED** to **RUNNING**.

### <span id="comments"></span><span id="COMMENTS"></span>Comments

TraceView uses the **EnableTrace** function to restart the trace session. **EnableTrace** is described in the Microsoft Windows SDK documentation.

 

 





