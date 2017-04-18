---
title: Trace Level
description: Trace Level
ms.assetid: 7ad3f6ee-61a4-4a0e-ab76-d839ae97a2b3
keywords: ["trace levels WDK", "levels WDK software tracing"]
---

# Trace Level


Trace levels are properties of a [trace provider](trace-provider.md), such as a kernel-mode driver or user-mode application. Trace levels determine which events the trace provider generates. Typically, the trace level represents the severity of the event (information, warning, or error), but trace providers can define them to represent any condition for generating the trace message.

Unlike [trace flags](trace-flags.md), which are defined by the trace provider in the [WPP\_CONTROL\_GUIDS](https://msdn.microsoft.com/library/windows/hardware/ff556186) structure, trace levels are defined in Evntrace.h, a public header file. However, the trace provider interprets the level and determines its effect

[Trace consumers](trace-consumer.md) such as [Tracelog](tracelog.md) and [TraceView](traceview.md), pass a trace level to the provider in the *EnableLevel* parameter of the **EnableTrace** function. For information about **EnableTrace**, see the Microsoft Windows SDK documentation.

Developers of trace providers can also write customized tracing functions (alternatives to [**DoTraceMessage**](https://msdn.microsoft.com/library/windows/hardware/ff544918)) that include the trace level as a condition for generating the trace message. For instructions, see [Can I customize DoTraceMessage?](can-i-customize-dotracemessage-.md)

When running a trace session, users can use the trace level to determine which messages will be generated during the session. [Trace consumers](trace-consumer.md), such as [Tracelog](tracelog.md) and [TraceView](traceview.md), let users set parameters and options to select the trace flags and trace level for each provider in a trace session.

Like trace flags, users can change the trace level while a trace session is running by reenabling the trace provider.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Trace%20Level%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




