---
title: Stopping a Trace Session
description: Stopping a Trace Session
ms.assetid: 648bf805-4266-4db5-aef6-414c5f37d1a3
keywords: ["trace sessions WDK , stopping", "stopping trace sessions", "TraceView WDK , stopping trace"]
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Stopping%20a%20Trace%20Session%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




