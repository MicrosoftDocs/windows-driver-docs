---
title: Grouping Trace Sessions
description: Grouping Trace Sessions
ms.assetid: dd9f39ee-fb93-4bf8-ac5c-5e884e57fcaa
keywords:
- TraceView WDK , grouping sessions
- grouping trace sessions
- trace sessions WDK , groups
- multiple trace sessions WDK TraceView
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Grouping Trace Sessions


You can combine multiple running trace sessions or multiple existing trace log displays into a trace session group. When you do, the trace messages from the grouped sessions or logs appear together in a single [Trace Message List](trace-message-lists.md) pane.

Trace session groups are managed as a single session. For example, if you stop a trace session that is part of a group, TraceView stops all trace sessions in the group. Similarly, if you [filter the trace messages](filtering-trace-messages.md), the filter applies to all trace messages in the group. However, you can still change the properties of a single trace session or its providers while it is part of a group.

The grouping of trace sessions does not affect the [event trace log (.etl) files](trace-log.md), the TraceView listing (.out) files, or the TraceView summary (.sum) files for the trace sessions. Those files record data from each session as though the sessions were not grouped.

This section includes:

[Creating Trace Session Groups](creating-trace-session-groups.md)

[Ungrouping Trace Sessions](ungrouping-trace-sessions.md)

[Saving a Group Log](saving-a-group-log.md)

[Limitations of Grouping](limitations-of-grouping.md)

 

 





