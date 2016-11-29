---
title: NT Kernel Logger Trace Session
description: NT Kernel Logger Trace Session
ms.assetid: d805ae15-8946-4bb6-83b6-d5d31aacd456
keywords: ["trace sessions WDK , NT Kernel Logger", "NT Kernel Logger trace sessions WDK", "Windows Kernel Trace provider WDK"]
---

# NT Kernel Logger Trace Session


The NT Kernel Logger trace session generates a trace of Windows kernel events. It is a reserved trace session that is built into Windows. You can run this trace session separately, or run it while tracing a driver to reveal the actions of Windows while the driver is running. [Trace providers](trace-provider.md), such as kernel-mode drivers or user-mode applications, cannot log directly to this trace session.

This trace session uses a reserved session name, "NT Kernel Logger," and the provider GUID is represented by the constant, **SystemTraceControlGuid**.

To create an NT Kernel Logger session, use [Tracelog](tracelog.md) or [TraceView](traceview.md).

The types of events traced during an NT Kernel Logger trace session are controlled by the value of the EnableFlags **member** of the EVENT\_TRACE\_PROPERTIES structure. This structure is described in the Microsoft Windows SDK documentation.

By default, when Tracelog starts an NT Kernel Logger session, it enables tracing of process, thread, physical disk I/O, and TCP/IP events. However, you can enable or disable tracing of specific events in the following ways:

-   By using Tracelog command-line parameters. For more information, see [**Tracelog Command Syntax**](tracelog-command-syntax.md).

-   By setting check boxes in the [TraceView](traceview.md) GUI.

The NT Kernel Logger provider cannot log to other trace sessions, and other [trace providers](trace-provider.md) cannot log to the NT Kernel Logger trace session. You cannot use the **-guid** parameter when starting an NT Kernel Logger trace session, and you cannot use the GUID of the NT Kernel Logger trace session in the **-guid** parameter for a standard trace session.

To format trace messages from the NT Kernel Logger trace session, use Tracefmt with the system.tmf file. This file is included in the WDK.

To trace kernel events during system boot, convert a Global Logger trace session, which traces during system boot, to an NT Kernel Logger trace session. For information, see [Boot-time Global Logger Session](boot-time-global-logger-session.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20NT%20Kernel%20Logger%20Trace%20Session%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




