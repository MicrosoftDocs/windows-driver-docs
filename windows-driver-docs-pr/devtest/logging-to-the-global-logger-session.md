---
title: Logging to the Global Logger Session
description: Logging to the Global Logger Session
ms.assetid: 48dfe101-b083-4d70-b85f-2e115f7e1dfa
keywords: ["tracing during boot WDK , Global Logger trace session", "boot-time tracing WDK , Global Logger trace session", "Global Logger trace session WDK , logging", "boot-time Global Logger trace session WDK , logging", "logs WDK tracing during boot"]
---

# Logging to the Global Logger Session


You can trace the actions of a driver or other trace provider during system boot by configuring the driver to log to the [Global Logger trace session](global-logger-trace-session.md), a trace session that runs during system boot. The driver must be instrumented for software tracing.

Although the Global Logger trace session does not send enable notification to providers, the method described in this section adds code to the driver that lets the driver determine when it is enabled for tracing to the Global Logger session.

This method is supported in Windows 2000 and later versions of Windows. However, in Windows Vista and later versions of Windows, the preferred method of boot tracing is to use an AutoLogger a new feature specifically designed for boot tracing. For information about tracing the activity of a driver with the AutoLogger, see [Configuring and Starting an AutoLogger Session](http://go.microsoft.com/fwlink/p/?linkid=89723).

This section includes:

[How to Log to the Global Logger Session](how-to-log-to-the-global-logger-session.md)

[Example: Global Logger Provider](example--global-logger-provider.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Logging%20to%20the%20Global%20Logger%20Session%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




