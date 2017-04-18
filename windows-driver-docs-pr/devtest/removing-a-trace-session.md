---
title: Removing a Trace Session
description: Removing a Trace Session
ms.assetid: cc40ed01-2f1b-48b3-80da-b0711036dc77
keywords: ["trace sessions WDK , removing", "removing trace sessions", "TraceView WDK , removing trace"]
---

# Removing a Trace Session


When you *remove* a trace session from the TraceView window, TraceView deletes the row that represents the trace session from the [Trace Session List](trace-session-list.md) and the associated [Trace Message List](trace-message-lists.md) from the bottom pane of the display. To remove a trace session, do the following:

1.  In the Trace Session List, right-click any cell of the row for the trace session.

2.  Click **Remove Log Session**.

### <span id="comments"></span><span id="COMMENTS"></span>Comments

You can remove a real-time trace session or a trace log session from the Trace Session List.

To remove a real-time trace session, the session must be [stopped](stopping-a-trace-session.md) (that is, all providers must be disabled). If any providers in the session are still running (that is, are enabled), the **Remove Log Session** command is dimmed.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Removing%20a%20Trace%20Session%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




