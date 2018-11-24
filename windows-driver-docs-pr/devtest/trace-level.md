---
title: Trace Level
description: Trace Level
ms.assetid: 7ad3f6ee-61a4-4a0e-ab76-d839ae97a2b3
keywords:
- trace levels WDK
- levels WDK software tracing
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Trace Level


Trace levels are properties of a [trace provider](trace-provider.md), such as a kernel-mode driver or user-mode application. Trace levels determine which events the trace provider generates. Typically, the trace level represents the severity of the event (information, warning, or error), but trace providers can define them to represent any condition for generating the trace message.

Unlike [trace flags](trace-flags.md), which are defined by the trace provider in the [WPP\_CONTROL\_GUIDS](https://msdn.microsoft.com/library/windows/hardware/ff556186) structure, trace levels are defined in Evntrace.h, a public header file. However, the trace provider interprets the level and determines its effect

[Trace consumers](trace-consumer.md) such as [Tracelog](tracelog.md) and [TraceView](traceview.md), pass a trace level to the provider in the *EnableLevel* parameter of the **EnableTrace** function. For information about **EnableTrace**, see the Microsoft Windows SDK documentation.

Developers of trace providers can also write customized tracing functions (alternatives to [**DoTraceMessage**](https://msdn.microsoft.com/library/windows/hardware/ff544918)) that include the trace level as a condition for generating the trace message. For instructions, see [Can I customize DoTraceMessage?](can-i-customize-dotracemessage-.md)

When running a trace session, users can use the trace level to determine which messages will be generated during the session. [Trace consumers](trace-consumer.md), such as [Tracelog](tracelog.md) and [TraceView](traceview.md), let users set parameters and options to select the trace flags and trace level for each provider in a trace session.

Like trace flags, users can change the trace level while a trace session is running by reenabling the trace provider.

 

 





