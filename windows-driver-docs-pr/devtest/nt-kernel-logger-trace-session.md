---
title: NT Kernel Logger Trace Session
description: NT Kernel Logger Trace Session
ms.assetid: d805ae15-8946-4bb6-83b6-d5d31aacd456
keywords:
- trace sessions WDK , NT Kernel Logger
- NT Kernel Logger trace sessions WDK
- Windows Kernel Trace provider WDK
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 





