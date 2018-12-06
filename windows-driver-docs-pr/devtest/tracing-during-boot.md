---
title: Tracing During Boot
description: Tracing During Boot
ms.assetid: 79594c33-5755-4484-aaf5-ac409b05ddcc
keywords:
- software tracing WDK , during boot
- tracing WDK , during boot
- boot-time tracing WDK
- kernel-mode software tracing WDK
- boot-time tracing WDK , about boot-time tracing
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Tracing During Boot


You can use features of the software tracing components in Microsoft Windows to trace the activity of the Windows kernel, and the activity of drivers and other trace providers, during the Windows boot process.

This section doesn't describe new tools. Instead, it describes methods for using existing software tracing tools and Event Tracing for Windows (ETW) features to perform this valuable task.

This section describes the following methods of tracing during boot:

-   [Boot-Time Global Logger Session](boot-time-global-logger-session.md)

    Traces Windows kernel activity during the boot process by converting a [Global Logger trace session](global-logger-trace-session.md) to an [NT Kernel Logger trace session](nt-kernel-logger-trace-session.md).

-   [Logging to the Global Logger Session](logging-to-the-global-logger-session.md)

    Traces the activity of a driver, or other trace provider, during boot. The provider must be instrumented for tracing. Only one Global Logger session can run at a time. This feature is available in Windows 2000 and later versions of Windows.

-   **AutoLogger**

    This is the preferred method for tracing the activity of a driver or other trace provider during boot. The provider must be instrumented for tracing. The AutoLogger provides callback notification to the driver. Multiple AutoLoggers can run concurrently. This feature is available in Windows Vista and later versions of Windows. For information about tracing the activity of a driver with the AutoLogger, see [Configuring and Starting an AutoLogger Session](http://go.microsoft.com/fwlink/p/?linkid=89723).

When using the Global Logger trace session, be sure that you are aware of its limitations. For information, see Limitations of the Global Logger trace session.

 

 





