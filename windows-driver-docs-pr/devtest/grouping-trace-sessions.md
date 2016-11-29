---
title: Grouping Trace Sessions
description: Grouping Trace Sessions
ms.assetid: dd9f39ee-fb93-4bf8-ac5c-5e884e57fcaa
keywords: ["TraceView WDK , grouping sessions", "grouping trace sessions", "trace sessions WDK , groups", "multiple trace sessions WDK TraceView"]
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Grouping%20Trace%20Sessions%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




