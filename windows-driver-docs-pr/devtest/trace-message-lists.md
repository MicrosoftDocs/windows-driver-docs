---
title: Trace Message Lists
description: Trace Message Lists
ms.assetid: 32dcd09d-1046-4785-91bc-ccdd79452c7d
keywords: ["TraceView WDK , window", "Trace Message Lists WDK"]
---

# Trace Message Lists


TraceView displays one *Trace Message List* for each trace session or trace log in the [Trace Session List](trace-session-list.md). The Trace Message List might be empty, such as when a trace session first begins, or it might contain numerous trace messages.

The following screen shot shows a Trace Session List that displays two existing logs: one for Tracedrv, which is a sample trace-instrumented driver that is included in the WDK, and one for the [NT Kernel Logger trace session](nt-kernel-logger-trace-session.md). There is one Trace Message List for each trace session.

![screen shot of a trace session list displaying a tracedrv and an nt kernel logger trace session log](images/traceview-multilog.png)

The session IDs on the left border of each Trace Message List help you associate the Trace Message List with the trace session. In this example, the top Trace Message List, which is named "ID 0," corresponds to session 0, which is *LogSession0*; the session that displays the Tracedrv.etl log in the Trace Session List.

The bottom Trace Message List, which is named "ID 1," corresponds to session 1, which is LogSession1; the session that displays the NTKernelLogger.etl log in the Trace Session List.

The following topics describe the contents and features of the Trace Message List:

[Trace Message List Columns](trace-message-list-columns.md)

[Trace Message List Features](trace-message-list-features.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Trace%20Message%20Lists%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




