---
title: Limitations of Grouping
description: Limitations of Grouping
keywords:
- grouping trace sessions
- trace sessions WDK , groups
ms.date: 04/20/2017
---

# Limitations of Grouping

This topic explains the limitations of the grouping feature in TraceView.

### <span id="workspaces_and_groups"></span><span id="WORKSPACES_AND_GROUPS"></span>Workspaces and Groups

You cannot save a trace session group in a workspace. If you try, TraceView displays a "Cannot save workspace settings for grouped sessions." error message..

### <span id="removing_trace_session_groups"></span><span id="REMOVING_TRACE_SESSION_GROUPS"></span>Removing Trace Session Groups

You cannot remove a trace session group from the [Trace Session List](trace-session-list.md), even if all sessions in the group are stopped. Before removing the group, you must ungroup the trace sessions.

### <span id="trace_message_order_in_a_group"></span><span id="TRACE_MESSAGE_ORDER_IN_A_GROUP"></span>Trace Message Order in a Group

Because the arrival of trace messages in the Trace Session List is affected by the message rate, the buffer size, and the flush timer for each trace session, trace messages from different sessions that arrive at the same time might actually have occurred at quite different times. For a more accurate view, combine the output files for each trace session and sort them by the **System Time** column.
