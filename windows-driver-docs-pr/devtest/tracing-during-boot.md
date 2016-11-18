---
title: Tracing During Boot
description: Tracing During Boot
ms.assetid: 79594c33-5755-4484-aaf5-ac409b05ddcc
keywords: ["software tracing WDK , during boot", "tracing WDK , during boot", "boot-time tracing WDK", "kernel-mode software tracing WDK", "boot-time tracing WDK , about boot-time tracing"]
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Tracing%20During%20Boot%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




