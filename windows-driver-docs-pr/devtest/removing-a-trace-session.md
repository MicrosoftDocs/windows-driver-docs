---
title: Removing a Trace Session
description: Removing a Trace Session
ms.assetid: cc40ed01-2f1b-48b3-80da-b0711036dc77
keywords:
- trace sessions WDK , removing
- removing trace sessions
- TraceView WDK , removing trace
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Removing a Trace Session


When you *remove* a trace session from the TraceView window, TraceView deletes the row that represents the trace session from the [Trace Session List](trace-session-list.md) and the associated [Trace Message List](trace-message-lists.md) from the bottom pane of the display. To remove a trace session, do the following:

1.  In the Trace Session List, right-click any cell of the row for the trace session.

2.  Click **Remove Log Session**.

### <span id="comments"></span><span id="COMMENTS"></span>Comments

You can remove a real-time trace session or a trace log session from the Trace Session List.

To remove a real-time trace session, the session must be [stopped](stopping-a-trace-session.md) (that is, all providers must be disabled). If any providers in the session are still running (that is, are enabled), the **Remove Log Session** command is dimmed.

 

 





