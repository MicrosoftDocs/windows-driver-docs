---
title: Limitations of Grouping
description: Limitations of Grouping
ms.assetid: 2cc49522-a504-43d7-b36b-297cd6c3f307
keywords: ["grouping trace sessions", "trace sessions WDK , groups"]
---

# Limitations of Grouping


This topic explains the limitations of the grouping feature in TraceView.

### <span id="grouping_real_time_trace_sessions"></span><span id="GROUPING_REAL_TIME_TRACE_SESSIONS"></span>Grouping Real-Time Trace Sessions

Grouping of existing log file displays is supported on Windows 2000 and later systems. Grouping of running (real-time) trace sessions is supported only on Windows Server 2003 and later operating systems. It is not supported on any version of Windows XP.

### <span id="workspaces_and_groups"></span><span id="WORKSPACES_AND_GROUPS"></span>Workspaces and Groups

You cannot save a trace session group in a workspace. If you try, TraceView displays a "Cannot save workspace settings for grouped sessions." error message..

### <span id="removing_trace_session_groups"></span><span id="REMOVING_TRACE_SESSION_GROUPS"></span>Removing Trace Session Groups

You cannot remove a trace session group from the [Trace Session List](trace-session-list.md), even if all sessions in the group are stopped. Before removing the group, you must ungroup the trace sessions.

### <span id="trace_message_order_in_a_group"></span><span id="TRACE_MESSAGE_ORDER_IN_A_GROUP"></span>Trace Message Order in a Group

Because the arrival of trace messages in the Trace Session List is affected by the message rate, the buffer size, and the flush timer for each trace session, trace messages from different sessions that arrive at the same time might actually have occurred at quite different times. For a more accurate view, combine the output files for each trace session and sort them by the **System Time** column.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Limitations%20of%20Grouping%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




